from dataclasses import dataclass
from enum import Enum
from typing import List


class MappingTypeEnum(str, Enum):
    RENAME_ATTRIBUTE = "RENAME_ATTRIBUTE"
    RENAME_CLASS = "RENAME_CLASS"
    # REMOVE_CLASS_AND_REASSIGN = "REMOVE_CLASS_AND_REASSIGN"
    REMOVE_AND_REPLACE_ENUM_VALUE = "REMOVE_AND_REPLACE_ENUM_VALUE"


@dataclass
class Mapping:
    id: str
    type: MappingTypeEnum


@dataclass
class RenameAttribute(Mapping):
    class_name: str
    attribute_name: str
    attribute_new_name: str


@dataclass
class RenameClass(Mapping):
    class_name: str
    class_new_name: str


# @dataclass
# class RemoveReasignClass(Mapping):
#     class_name: str
#     class_to_reassign: str


@dataclass
class RemoveReassignEnumValue(Mapping):
    enum_name: str
    enum_value_name: str
    enum_value_to_reassign: str


@dataclass
class MappingList:
    mappings: List[Mapping]
