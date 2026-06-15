from typing import List

from esdl.version_migrations.mapping import RenameAttribute, RenameClass, RemoveReassignEnumValue


version_migration_mapping_rename_attribute: List[RenameAttribute] = [
    RenameAttribute(
        # In ESDL release 26.2, the GeothermalSource attribute flowRate was renamed to maximumFlowRate
        # (aligned with the ATES maximumFlowRate attribute)
        id="1",
        class_name="GeothermalSource",
        attribute_name="flowRate",
        attribute_new_name="maximumFlowRate"
    ),
]

version_migration_mapping_rename_class: List[RenameClass] = [
    RenameClass(
        # In ESDL release 26.5, the BiomassHeater class was replaced by the Heater class
        id="1",
        class_name="BiomassHeater",
        class_new_name="Heater",
    ),
]

    # {
    #     # Possible rule to get rid of PVPanel class instances in an ESDL model
    #     "id": "1",
    #     "type": "REMOVE_CLASS_AND_REASSIGN",
    #     "class_name": "PVPanel",
    #     "class_to_reassign": "PVInstallation"
    # },

version_migration_remove_and_replace_enum_value: List[RemoveReassignEnumValue] = [
    RemoveReassignEnumValue(
        # Correction of spelling mistake in the early days of ESDL
        id="1",
        enum_name="MultiplierEnum",
        enum_value_name="TERRA",
        enum_value_to_reassign="TERA"
    )
]