# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:HvacOverrunStatusType', is_value_type=False, no_attrib_name=False)
class HvacOverrunStatusType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOverrunStatusType -> UnionType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:HvacOverrunTypeType', is_value_type=False, no_attrib_name=False)
class HvacOverrunTypeType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOverrunTypeType -> UnionType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:HvacOperationModeTypeType', is_value_type=False, no_attrib_name=False)
class HvacOperationModeTypeType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOperationModeTypeType -> UnionType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:HvacSystemFunctionTypeType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionTypeType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionTypeType -> UnionType
    _MEMBER_INFO = [
    ]

