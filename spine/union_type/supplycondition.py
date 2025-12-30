# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:GridConditionType', is_value_type=False, no_attrib_name=False)
class GridConditionType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:GridConditionType -> UnionType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:SupplyConditionOriginatorType', is_value_type=False, no_attrib_name=False)
class SupplyConditionOriginatorType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionOriginatorType -> UnionType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:SupplyConditionEventTypeType', is_value_type=False, no_attrib_name=False)
class SupplyConditionEventTypeType(SpineBase): # EEBus_SPINE_TS_SupplyCondition.xsd:ns_p:SupplyConditionEventTypeType -> UnionType
    _MEMBER_INFO = [
    ]

