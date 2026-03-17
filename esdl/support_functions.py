#  This work is based on original code developed and copyrighted by TNO 2020.
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

"""
Support functions for managing EObjects
"""
from typing import Dict

from pyecore.ecore import EAttribute, EObject, EClass, EReference, EStructuralFeature
from pyecore.innerutils import InternalSet
from pyecore.valuecontainer import ECollection
import logging

logger = logging.getLogger(__name__)



# add support for shallow copying or cloning an object
# it copies the object's attributes (e.g. clone an object), does only shallow copying
def clone(self):
    """
    Shallow copying or cloning an object
    It only copies the object's attributes (e.g. clone an object)
    Usage object.clone() or copy.copy(object) (as __copy__() is also implemented)
    :param self:
    :return: A clone of the object
    """
    newone = type(self)()
    eclass = self.eClass
    for x in eclass.eAllStructuralFeatures():
        if isinstance(x, EAttribute):
            #logger.trace("clone: processing attribute {}".format(x.name))
            if x.many:
                eOrderedSet = newone.eGet(x.name)
                for v in self.eGet(x.name):
                    eOrderedSet.append(v)
            else:
                newone.eSet(x.name, self.eGet(x.name))
    return newone


def deepcopy(self, memo=None, uuid_dict: Dict[str, EObject]=None, target_es: EObject=None, copy_xrefs=True) -> EObject:
    """
    Deep copying an EObject.

    :param memo: is used in recursive calls to find out which object have already been cloned
    :param uuid_dict: can be passed by the user to update the uuid_dict of the resource while deepcopying
    :param target_es search for cross-references in the target_es energy system or eObject if not found in copy.
           This can be used if the source ESDL has the same IDs as the target ESDL (e.g. quantity and units,
           or carriers) to make use the cross references are also connected in the deepcopy, before adding it to the
           `target_es`
    :param copy_xrefs copy cross-references (default). Set to False to not copy cross-references, e.g. in case
           you want to avoid copying references to other ESDLs that not have them. E.g. when cutting out an asset
           from an ESDL, without references to other parts of this ESDL.
    :return a deepcopy of the object.
    """
    first_call = False
    if memo is None:
        memo = dict()
        first_call = True
    if self in memo:
        return memo[self]

    copy: EObject = self.clone()
    if uuid_dict is not None and hasattr(copy, 'id'):
        uuid_dict[copy.id] = copy
    eclass: EClass = self.eClass
    for x in eclass.eAllStructuralFeatures():
        if isinstance(x, EReference):
            ref: EReference = x
            value: EStructuralFeature = self.eGet(ref)
            if value is None:
                continue
            if ref.containment:
                if ref.many and isinstance(value, ECollection):
                    #clone all containment elements
                    eAbstractSet: ECollection = copy.eGet(ref.name)
                    for ref_value in value:
                        duplicate = ref_value.__deepcopy__(memo, uuid_dict, target_es, copy_xrefs)
                        eAbstractSet.append(duplicate)
                else:
                    copy.eSet(ref.name, value.__deepcopy__(memo, uuid_dict, target_es, copy_xrefs))
            #else:
            #    # no containment relation, but a reference
            #    # this can only be done after a full copy
            #    pass
    # now copy should a full copy, but without cross-references

    memo[self] = copy

    if first_call and copy_xrefs:
        #logger.debug("copying references")
        for k, v in memo.items():
            eclass: EClass = k.eClass
            for x in eclass.eAllStructuralFeatures():
                if isinstance(x, EReference):
                    #logger.debug("deepcopy: processing x-reference {}".format(x.name))
                    ref: EReference = x
                    orig_value: EStructuralFeature = k.eGet(ref)
                    if orig_value is None:
                        continue
                    if not ref.containment:
                        opposite = ref.eOpposite
                        if opposite and opposite.containment:
                            # do not handle eOpposite relations, they are handled automatically in pyEcore
                            continue
                        if x.many:
                            eAbstractSet = v.eGet(ref.name)
                            for orig_ref_value in orig_value:
                                copy_ref_value = None
                                try:
                                    copy_ref_value = memo[orig_ref_value]
                                except KeyError:
                                    try:
                                        if target_es:
                                            if hasattr(orig_ref_value, 'id'): # use id to find object in target_es
                                                r = target_es.eResource
                                                ref_id = orig_ref_value.id
                                                copy_ref_value = r.uuid_dict[ref_id]
                                                #logger.warning(
                                                #    f'Using reference of type {orig_ref_value.eClass.name} for reference {k.eClass.name}.{ref.name} in deepcopy memo, using {copy_ref_value}')
                                            else:
                                                logger.warning(
                                                    f'deepcopy(): No id found in target_es, cannot find reference of type {orig_ref_value.eClass.name} for reference {k.eClass.name}.{ref.name} in deepcopy memo, using original')
                                                copy_ref_value = orig_ref_value
                                        else:
                                            logger.warning(
                                                f'deepcopy(): Cannot find reference of type {orig_ref_value.eClass.name} for reference {k.eClass.name}.{ref.name} in deepcopy memo, using original')
                                            copy_ref_value = orig_ref_value
                                    except Exception:
                                        logger.warning(f'deepcopy(): Cannot find reference of type {orig_ref_value.eClass.name} for reference {k.eClass.name}.{ref.name} in deepcopy memo, using original')
                                        copy_ref_value = orig_ref_value
                                eAbstractSet.append(copy_ref_value)
                        else:
                            try:
                                copy_value = memo[orig_value]
                            except KeyError:
                                try:
                                    if target_es:
                                        if hasattr(orig_value, 'id'):  # use id to find object in target_es
                                            r = target_es.eResource
                                            ref_id = orig_value.id
                                            copy_value = r.uuid_dict[ref_id]
                                            # logger.debug(
                                            #     f'Using reference of type {orig_value.eClass.name} for reference {k.eClass.name}.{ref.name} in deepcopy memo, using {copy_value}')
                                        else:
                                            logger.warning(
                                                f'deepcopy(): Referenced object has no ID, Can\'t find reference for {orig_value.eClass.name} for reference {k.eClass.name}.{ref.name} in deepcopy memo or target_es, using original {orig_value}')
                                            copy_value = orig_value
                                    else:
                                        logger.warning(
                                            f'deepcopy(): Can\'t find reference for {orig_value.eClass.name} for reference {k.eClass.name}.{ref.name} in deepcopy memo, using original')
                                        copy_value = orig_value
                                except Exception as e:
                                    logger.warning(f'deepcopy(): {e}: Cannot find reference of type {orig_value.eClass.name} of reference {k.eClass.name}.{ref.name} in deepcopy memo, using original')
                                    copy_value = orig_value
                            v.eSet(ref.name, copy_value)
    copy._isset = InternalSet(self._isset)  # copy over the eIsSet configuration, otherwise all attributes are set due to this deepcopy
    return copy


setattr(EObject, '__copy__', clone)
setattr(EObject, 'clone', clone)
setattr(EObject, '__deepcopy__', deepcopy)
setattr(EObject, 'deepcopy', deepcopy)
