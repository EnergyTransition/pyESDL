import json
from esdl.version_migrations.mapping import MappingList, RenameAttribute, RenameClass, RemoveReasignClass, RemoveReassignEnumValue


class VersionMigration:

    def __init__(self):
        self.mapping_list = None

        self.class_mappings = dict()         # EClass --> list[Mapping]
        self.attribute_mappings = dict()     # EClass --> list[Mapping]
        self.enum_mappings = dict()          # Enum --> list[Mapping]

        self.load_version_migration_mappings("./version_migration_mappings.json")

    def append_or_add(self, dictionary, key, value):
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]

    def load_version_migration_mappings(self, file_path):
        self.mapping_list = MappingList(
            mappings=list()
        )

        with open(file_path, 'r') as f:
            mappings = json.load(f)

            for mapping in mappings:
                if mapping["type"] == "RENAME_ATTRIBUTE":
                    m = RenameAttribute(**mapping)
                    self.append_or_add(self.attribute_mappings, mapping["class_name"], m)
                elif mapping["type"] == "RENAME_CLASS":
                    m = RenameClass(**mapping)
                    self.append_or_add(self.class_mappings, mapping["class_name"], m)
                elif mapping["type"] == "REMOVE_CLASS_AND_REASSIGN":
                    m = RemoveReasignClass(**mapping)
                    self.append_or_add(self.class_mappings, mapping["class_name"], m)
                elif mapping["type"] == "REMOVE_AND_REPLACE_ENUM_VALUE":
                    m = RemoveReassignEnumValue(**mapping)
                    self.append_or_add(self.enum_mappings, mapping["enum_name"], m)

                self.mapping_list.mappings.append(m)

    def get_mappings(self):
        return self.mapping_list

    def get_replaced_attribute_name(self, class_name, attribute_name):
        if not self.mapping_list:
            # logger.error("No version migration mappings loaded")
            print("ERROR: No version migration mappings loaded")
        else:
            for mapping in self.mapping_list.mappings:
                if isinstance(mapping, RenameAttribute) and \
                        class_name == mapping.class_name and \
                        attribute_name == mapping.attribute_name:
                    return mapping.attribute_new_name

    def get_replaced_class_name(self, class_name):
        if class_name in self.class_mappings:
            for mapping in self.class_mappings[class_name]:
                if isinstance(mapping, RenameClass) and \
                        class_name == mapping.class_name:
                    return mapping.class_new_name

    def get_removed_reassined_class_name(self, class_name):
        if class_name in self.class_mappings:
            for mapping in self.class_mappings[class_name]:
                if isinstance(mapping, RemoveReasignClass) and \
                        class_name == mapping.class_name:
                    return mapping.class_to_reassign

    def check_enum_migration_mappings(self, feature, value):
        if feature.eType.name in self.enum_mappings:
            for mapping in self.enum_mappings[feature.eType.name]:
                if isinstance(mapping, RemoveReassignEnumValue) and mapping.enum_value_name == value:
                    value = mapping.enum_value_to_reassign

        return feature, value
