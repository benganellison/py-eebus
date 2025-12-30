# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:UseCaseNameType', is_value_type=False, no_attrib_name=False)
class UseCaseNameType(SpineBase): # EEBus_SPINE_TS_UseCaseInformation.xsd:ns_p:UseCaseNameType -> UnionType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:UseCaseActorType', is_value_type=False, no_attrib_name=False)
class UseCaseActorType(SpineBase): # EEBus_SPINE_TS_UseCaseInformation.xsd:ns_p:UseCaseActorType -> UnionType
    _MEMBER_INFO = [
    ]

