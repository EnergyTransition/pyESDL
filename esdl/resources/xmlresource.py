#  This work is based on original code developed and copyrighted by TNO 2023.
#  Subsequent contributions are licensed to you by the developers of such code and are
#  made available to the Project under one or several contributor license agreements.
#
#  This work is licensed to you under the Apache License, Version 2.0.
#  You may obtain a copy of the license at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Contributors:
#      TNO         - Initial implementation
#  Manager:
#      TNO
from pyecore.ecore import EClass, EDataType, EStringToStringMapEntry, EAnnotation, EProxy, EEnum

from esdl.resources.xmi import XMIResource, XMIOptions, XMI_URL, XSI_URL, XSI
from lxml.etree import QName, Element, ElementTree
import logging

from esdl.version_migrations.migration import VersionMigration

logger = logging.getLogger(__name__)

"""
Extension of pyecore's XMIResource to support the XMLResource in EMF.
It basically removes the xmi:version stuff from the serialization.
It also adds parse_information that can be inspected for errors when reading an ESDL file.
"""
class XMLResource(XMIResource):
    def __init__(self, uri=None, use_uuid=False):
        super().__init__(uri, use_uuid)
        self._later = []
        self.prefixes = {}
        self.reverse_nsmap = {}
        self.parse_information = []

        self.version_migration = VersionMigration()

    def get_parse_information(self):
        return self.parse_information

    def load(self, options=None):
        super().load(options)

    def save(self, output=None, options=None):
        self.options = options or {}
        output = self.open_out_stream(output)
        self.prefixes.clear()
        self.reverse_nsmap.clear()

        serialize_default = \
            self.options.get(XMIOptions.SERIALIZE_DEFAULT_VALUES,
                             False)
        nsmap = {XSI: XSI_URL} # remove XMI for XML serialization

        if len(self.contents) == 1:
            root = self.contents[0]
            self.register_eobject_epackage(root)
            tmp_xmi_root = self._go_across(root, serialize_default)
        else:
            # this case hasn't been verified for XML serialization
            tag = QName(XMI_URL, 'XMI')
            tmp_xmi_root = Element(tag)
            for root in self.contents:
                root_node = self._go_across(root, serialize_default)
                tmp_xmi_root.append(root_node)

        # update nsmap with prefixes register during the nodes creation
        nsmap.update(self.prefixes)
        xmi_root = Element(tmp_xmi_root.tag, nsmap=nsmap)
        xmi_root[:] = tmp_xmi_root[:]
        xmi_root.attrib.update(tmp_xmi_root.attrib)
        #xmi_version = etree.QName(XMI_URL, 'version') # remove XMI version in XML serialization
        #xmi_root.attrib[xmi_version] = '2.0'
        tree = ElementTree(xmi_root)
        tree.write(output,
                   pretty_print=True,
                   xml_declaration=True,
                   encoding=tree.docinfo.encoding)
        output.flush()
        return self.uri.close_stream()

    def _decode_node(self, parent_eobj, node):
        _, node_tag = self.extract_namespace(node.tag)
        feature_container = self._find_feature(parent_eobj.eClass, node_tag)
        if not feature_container:
            raise ValueError(f'Feature "{node_tag}" is unknown '
                             f'for {parent_eobj.eClass.name}, '
                             f'line {node.sourceline}')
        if self._is_none_node(node):
            if feature_container.many:
                parent_eobj.__getattribute__(feature_container._name) \
                           .append(None)
            else:
                parent_eobj.__setattr__(feature_container._name, None)

            return (None, None, [], [], False)
        if node.get('href'):
            ref = node.get('href')
            proxy = EProxy(path=ref, resource=self)
            return (feature_container, proxy, [], [], False)
        if self._type_attribute(node):
            prefix, _type = self._type_attribute(node).split(':')

            # Check if there is a relevant mapping for the ESDL EClass
            _type = self.version_migration.check_class_migration_mappings(_type)

            if not prefix:
                raise ValueError(f'Prefix {prefix} is not registered, '
                                 f'{node.tag} line {node.sourceline}')
            epackage = self.prefix2epackage(prefix)
            etype = epackage.getEClassifier(_type)
            if not etype:
                raise ValueError(f'Type {_type} is unknown in {epackage}, '
                                 f'{node.tag} line {node.sourceline}')
        else:
            etype = feature_container._eType
            if isinstance(etype, EProxy):
                etype.force_resolve()

        # we create the instance
        if etype is EClass or etype is EClass.eClass:
            name = node.get('name')
            eobject = etype(name)
        elif (etype is EStringToStringMapEntry
              or etype is EStringToStringMapEntry.eClass) \
                and feature_container is EAnnotation.details:
            annotation_key = node.get('key')
            annotation_value = node.get('value')
            parent_eobj.details[annotation_key] = annotation_value
            if annotation_key == 'documentation':
                container = parent_eobj.eContainer()
                if hasattr(container, 'python_class'):
                    container = container.python_class
                container.__doc__ = annotation_value
            return (None, None, (), (), False)
        elif isinstance(etype, EDataType):
            value = node.text if node.text else ''
            return (None, parent_eobj, ((feature_container, value),),
                    (), True)
        else:
            # idref = node.get(f'{{{XMI_URL}}}idref')
            # if idref:
            #     return (None, parent_eobj, [],
            #             [(feature_container, idref)], True)
            eobject = etype()

        # we sort the node feature (no containments)
        eatts = []
        erefs = []
        for key, value in node.attrib.items():
            feature = self._decode_attribute(eobject, key, value, node)
            if not feature:
                continue  # we skip the unknown features
            if etype is EClass and feature._name == 'name':
                continue  # we skip the name for metamodel import
            if feature.is_attribute:

                # Check if there is a relevant mapping for ESDL EEnums
                if isinstance(feature.eType, EEnum):
                    feature, value = self.version_migration.check_enum_migration_mappings(feature, value)

                eatts.append((feature, value))
                if feature.iD:
                    self.uuid_dict[value] = eobject
            else:
                erefs.append((feature, value))
        return (feature_container, eobject, eatts, erefs, False)

    """
    This function has been overriden XMIResource, to make it a little more robust for ESDL's that
    are 'older' and do not have a certain feature. By default XMIResource throws an exception when 
    an unknown attribute is found for a class. This version prints a warning and continues.
    """
    def _decode_attribute(self, owner, key, value, node):
        namespace, att_name = self.extract_namespace(key)
        prefix = self.reverse_nsmap[namespace] if namespace else None
        # This is a special case, we are working with uuids
        if key == self.xmiid:
            owner._internal_id = value
            self.uuid_dict[value] = owner
        elif prefix in ('xsi', 'xmi') and att_name == 'type':
            # type has already been handled
            pass
        # elif namespace:
        #     pass
        elif not namespace:
            if att_name == 'href':
                return
            feature = self._find_feature(owner.eClass, att_name)
            if not feature:
                #raise ValueError(f'Feature {att_name} does not exists for '
                #                 f'type {owner.eClass.name} '
                #                 f'({node.tag} line {node.sourceline})')

                alternative_att_name = self.version_migration.check_attribute_migration_mappings(owner.eClass.name, att_name)
                if alternative_att_name:
                    feature = self._find_feature(owner.eClass, alternative_att_name)

                    if feature:
                        s = 'Attribute \'{0}\' does not exists for type {1} and is replaced by {2} ({3} line {4}).' \
                            .format(att_name, owner.eClass.name, alternative_att_name, node.tag, node.sourceline)
                        logger.warning(s)
                        self.parse_information.append(s)
                    else:
                        s = 'Attribute \'{0}\' does not exists for type {1} and alternative {2} also not exists ({3} line {4}).' \
                            .format(att_name, owner.eClass.name, alternative_att_name, node.tag, node.sourceline)
                        logger.warning(s)
                        self.parse_information.append(s)
                else:
                    s = 'Attribute \'{0}\' does not exists for type {1} and is ignored ({2} line {3}).'\
                        .format(att_name, owner.eClass.name, node.tag, node.sourceline)
                    logger.warning(s)
                    self.parse_information.append(s)

            return feature
