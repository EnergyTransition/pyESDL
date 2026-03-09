import json

from esdl.version_migrations.version_migration_mappings import version_migration_mapping_rename_attribute, \
    version_migration_mapping_rename_class, version_migration_remove_and_replace_enum_value


class VersionMigration:
    def __init__(self):
        self.version_migration_mapping_rename_attribute = version_migration_mapping_rename_attribute
        self.version_migration_mapping_rename_class = version_migration_mapping_rename_class
        self.version_migration_remove_and_replace_enum_value = version_migration_remove_and_replace_enum_value

    def check_attribute_migration_mappings(self, class_name, attribute_name):
        for mapping in self.version_migration_mapping_rename_attribute:
            if class_name == mapping.class_name and attribute_name == mapping.attribute_name:
                return mapping.attribute_new_name

    def check_class_migration_mappings(self, class_name):
        for mapping in self.version_migration_mapping_rename_class:
            if class_name == mapping.class_name:
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
        for mapping in self.version_migration_remove_and_replace_enum_value:
            if mapping.enum_value_name == value:
                value = mapping.enum_value_to_reassign

        return feature, value
