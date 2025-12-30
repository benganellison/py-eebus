# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:TimeSlotIdType', is_value_type=True, no_attrib_name=False)
class TimeSlotIdType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeSlotIdType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]


@spine_type('ns_p:TimeSlotCountType', is_value_type=True, no_attrib_name=False)
class TimeSlotCountType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeSlotCountType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:TimeSlotIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSlotIdType"
        },
    ]


@spine_type('ns_p:TimeTableIdType', is_value_type=True, no_attrib_name=False)
class TimeTableIdType(SpineBase): # EEBus_SPINE_TS_TimeTable.xsd:ns_p:TimeTableIdType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]

