# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:



@spine_type('ns_p:PowerSupplyConditionType', is_value_type=False, no_attrib_name=False)
class PowerSupplyConditionType(SpineBase): # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:PowerSupplyConditionType -> UnionType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:DeviceDiagnosisOperatingStateType', is_value_type=False, no_attrib_name=False)
class DeviceDiagnosisOperatingStateType(SpineBase): # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:DeviceDiagnosisOperatingStateType -> UnionType
    _MEMBER_INFO = [
    ]

