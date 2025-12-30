# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:StateInformationCategoryType', is_value_type=False, no_attrib_name=False)
class StateInformationCategoryType(SpineBase): # EEBus_SPINE_TS_StateInformation.xsd:ns_p:StateInformationCategoryType -> UnionType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:StateInformationType', is_value_type=False, no_attrib_name=False)
class StateInformationType(SpineBase): # EEBus_SPINE_TS_StateInformation.xsd:ns_p:StateInformationType -> UnionType
    _MEMBER_INFO = [
    ]

