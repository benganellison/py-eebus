# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    pass


@spine_type('ns_p:LoadControlCategoryType', is_value_type=True, no_attrib_name=False)
class LoadControlCategoryType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlCategoryType -> UnionType
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


@spine_type('ns_p:LoadControlLimitTypeType', is_value_type=True, no_attrib_name=False)
class LoadControlLimitTypeType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlLimitTypeType -> UnionType
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


@spine_type('ns_p:LoadControlEventStateType', is_value_type=True, no_attrib_name=False)
class LoadControlEventStateType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlEventStateType -> UnionType
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


@spine_type('ns_p:LoadControlEventActionType', is_value_type=True, no_attrib_name=False)
class LoadControlEventActionType(SpineBase): # EEBus_SPINE_TS_LoadControl.xsd:ns_p:LoadControlEventActionType -> UnionType
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

