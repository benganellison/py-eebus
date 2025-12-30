# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:SensingTypeType', is_value_type=False, no_attrib_name=False)
class SensingTypeType(SpineBase): # EEBus_SPINE_TS_Sensing.xsd:ns_p:SensingTypeType -> UnionType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:SensingStateType', is_value_type=False, no_attrib_name=False)
class SensingStateType(SpineBase): # EEBus_SPINE_TS_Sensing.xsd:ns_p:SensingStateType -> UnionType
    _MEMBER_INFO = [
    ]

