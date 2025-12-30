# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:SetpointTypeType', is_value_type=False, no_attrib_name=False)
class SetpointTypeType(SpineBase): # EEBus_SPINE_TS_Setpoint.xsd:ns_p:SetpointTypeType -> UnionType
    _MEMBER_INFO = [
    ]

