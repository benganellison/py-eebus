# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    pass



@spine_type('ns_p:PowerSequenceStateType', is_value_type=True, no_attrib_name=False)
class PowerSequenceStateType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceStateType -> UnionType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:string",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:PowerSequenceScopeType', is_value_type=True, no_attrib_name=False)
class PowerSequenceScopeType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceScopeType -> UnionType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:string",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:PowerTimeSlotValueTypeType', is_value_type=True, no_attrib_name=False)
class PowerTimeSlotValueTypeType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotValueTypeType -> UnionType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "xs:string",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]

