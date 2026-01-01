# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    pass



@spine_type('ns_p:BillCostTypeType', is_value_type=False, no_attrib_name=False)
class BillCostTypeType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillCostTypeType -> UnionType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:BillCostTypeEnumType",
            "is_array": False,
            "is_optional": False,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:BillPositionTypeType', is_value_type=False, no_attrib_name=False)
class BillPositionTypeType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillPositionTypeType -> UnionType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:BillPositionTypeEnumType",
            "is_array": False,
            "is_optional": False,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:BillTypeType', is_value_type=False, no_attrib_name=False)
class BillTypeType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillTypeType -> UnionType
    _MEMBER_INFO = [
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:BillTypeEnumType",
            "is_array": False,
            "is_optional": False,
            "class_check": "str"
        },
    ]

