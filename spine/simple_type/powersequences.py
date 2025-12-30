# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:AlternativesIdType', is_value_type=True, no_attrib_name=False)
class AlternativesIdType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:AlternativesIdType -> AliasType
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


@spine_type('ns_p:PowerTimeSlotNumberType', is_value_type=True, no_attrib_name=False)
class PowerTimeSlotNumberType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerTimeSlotNumberType -> AliasType
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


@spine_type('ns_p:PowerSequenceIdType', is_value_type=True, no_attrib_name=False)
class PowerSequenceIdType(SpineBase): # EEBus_SPINE_TS_PowerSequences.xsd:ns_p:PowerSequenceIdType -> AliasType
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

