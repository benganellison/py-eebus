# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:ElectricalConnectionCharacteristicIdType', is_value_type=True, no_attrib_name=False)
class ElectricalConnectionCharacteristicIdType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionCharacteristicIdType -> AliasType
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


@spine_type('ns_p:ElectricalConnectionParameterIdType', is_value_type=True, no_attrib_name=False)
class ElectricalConnectionParameterIdType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionParameterIdType -> AliasType
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


@spine_type('ns_p:ElectricalConnectionIdType', is_value_type=True, no_attrib_name=False)
class ElectricalConnectionIdType(SpineBase): # EEBus_SPINE_TS_ElectricalConnection.xsd:ns_p:ElectricalConnectionIdType -> AliasType
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

