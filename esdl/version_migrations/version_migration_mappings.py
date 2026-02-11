version_migration_mappings = [
    {
        # In ESDL release 26.2, the GeothermalSource attribute flowRate was renamed to maximumFlowRate
        # (aligned with the ATES maximumFlowRate attribute)
        "id": "1",
        "type": "RENAME_ATTRIBUTE",
        "class_name": "GeothermalSource",
        "attribute_name": "flowRate",
        "attribute_new_name": "maximumFlowRate"
    },
    {
        # Example rule to rename a Class in ESDL
        "id": "2",
        "type": "RENAME_CLASS",
        "class_name": "GeothermalSourceOld",
        "class_new_name": "GeothermalSource",
    },
    # {
    #     # Possible rule to get rid of PVPanel class instances in an ESDL model
    #     "id": "3",
    #     "type": "REMOVE_CLASS_AND_REASSIGN",
    #     "class_name": "PVPanel",
    #     "class_to_reassign": "PVInstallation"
    # },
    {
        # Correction of spelling mistake in the early days of ESDL
        "id": "4",
        "type": "REMOVE_AND_REPLACE_ENUM_VALUE",
        "enum_name": "MultiplierEnum",
        "enum_value_name": "TERRA",
        "enum_value_to_reassign": "TERA"
    }
]