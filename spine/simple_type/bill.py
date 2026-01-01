# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    pass



@spine_type('ns_p:BillPositionIdType', is_value_type=True, no_attrib_name=False)
class BillPositionIdType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillPositionIdType -> AliasType
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


@spine_type('ns_p:BillPositionCountType', is_value_type=True, no_attrib_name=False)
class BillPositionCountType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillPositionCountType -> AliasType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:BillPositionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillPositionIdType"
        },
    ]


@spine_type('ns_p:BillIdType', is_value_type=True, no_attrib_name=False)
class BillIdType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillIdType -> AliasType
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


@spine_type('ns_p:BillCostIdType', is_value_type=True, no_attrib_name=False)
class BillCostIdType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillCostIdType -> AliasType
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


@spine_type('ns_p:BillValueIdType', is_value_type=True, no_attrib_name=False)
class BillValueIdType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillValueIdType -> AliasType
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

