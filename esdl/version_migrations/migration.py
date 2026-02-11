import json
from esdl.version_migrations.mapping import MappingList, RenameAttribute, RenameClass, RemoveReassignEnumValue, \
    MappingTypeEnum
from esdl.version_migrations.version_migration_mappings import version_migration_mappings


class VersionMigration:

    def __init__(self):
        self.class_mappings = dict()         # EClass --> list[Mapping]
        self.attribute_mappings = dict()     # EClass --> list[Mapping]
        self.enum_mappings = dict()          # Enum --> list[Mapping]

        self.mappings = version_migration_mappings
        self.process_mappings()

    def append_or_add(self, dictionary, key, value):
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]

    def process_mappings(self):
        for mapping in self.mappings:
            if mapping["type"] == MappingTypeEnum.RENAME_ATTRIBUTE:
                m = RenameAttribute(**mapping)
                self.append_or_add(self.attribute_mappings, mapping["class_name"], m)
            elif mapping["type"] == MappingTypeEnum.RENAME_CLASS:
                m = RenameClass(**mapping)
                self.append_or_add(self.class_mappings, mapping["class_name"], m)
            # elif mapping["type"] == MappingTypeEnum.REMOVE_CLASS_AND_REASSIGN:
            #     m = RemoveReasignClass(**mapping)
            #     self.append_or_add(self.class_mappings, mapping["class_name"], m)
            elif mapping["type"] == MappingTypeEnum.REMOVE_AND_REPLACE_ENUM_VALUE:
                m = RemoveReassignEnumValue(**mapping)
                self.append_or_add(self.enum_mappings, mapping["enum_name"], m)

    def check_attribute_migration_mappings(self, class_name, attribute_name):
        if class_name in self.attribute_mappings:
            for mapping in self.attribute_mappings[class_name]:
                if isinstance(mapping, RenameAttribute) and \
                        class_name == mapping.class_name and \
                        attribute_name == mapping.attribute_name:
                    return mapping.attribute_new_name

    def check_class_migration_mappings(self, class_name):
        if class_name in self.class_mappings:
            for mapping in self.class_mappings[class_name]:
                if isinstance(mapping, RenameClass) and \
                        class_name == mapping.class_name:
                    return mapping.class_new_name
        return class_name

    # def get_removed_reassined_class_name(self, class_name):
    #     if class_name in self.class_mappings:
    #         for mapping in self.class_mappings[class_name]:
    #             if isinstance(mapping, RemoveReasignClass) and \
    #                     class_name == mapping.class_name:
    #                 return mapping.class_to_reassign
    #     return class_name

    def check_enum_migration_mappings(self, feature, value):
        if feature.eType.name in self.enum_mappings:
            for mapping in self.enum_mappings[feature.eType.name]:
                if isinstance(mapping, RemoveReassignEnumValue) and mapping.enum_value_name == value:
                    value = mapping.enum_value_to_reassign

        return feature, value
