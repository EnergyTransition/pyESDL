from dataclasses import dataclass
from typing import List


@dataclass
class ESDLVesionMapping:
    id: str


@dataclass
class RenameAttribute(ESDLVesionMapping):
    class_name: str
    attribute_name: str
    attribute_new_name: str


@dataclass
class RenameClass(ESDLVesionMapping):
    class_name: str
    class_new_name: str


# @dataclass
# class RemoveReasignClass(Mapping):
#     class_name: str
#     class_to_reassign: str


@dataclass
class RemoveReassignEnumValue(ESDLVesionMapping):
    enum_name: str
    enum_value_name: str
    enum_value_to_reassign: str


@dataclass
class MappingList:
    mappings: List[ESDLVesionMapping]
