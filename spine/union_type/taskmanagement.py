# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:TaskManagementJobSourceType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobSourceType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobSourceType -> UnionType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:TaskManagementJobStateType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobStateType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobStateType -> UnionType
    _MEMBER_INFO = [
    ]

