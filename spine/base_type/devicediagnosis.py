# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.simple_type.devicediagnosis import LastErrorCodeType
    from spine.simple_type.devicediagnosis import VendorStateCodeType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.devicediagnosis import DeviceDiagnosisOperatingStateType
    from spine.union_type.devicediagnosis import PowerSupplyConditionType



@spine_type('ns_p:DeviceDiagnosisServiceDataElementsType', is_value_type=False, no_attrib_name=False)
class DeviceDiagnosisServiceDataElementsType(SpineBase): # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:DeviceDiagnosisServiceDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "installation_time",
            "xml_name": "installationTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "boot_counter",
            "xml_name": "bootCounter",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "next_service",
            "xml_name": "nextService",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:DeviceDiagnosisServiceDataType', is_value_type=False, no_attrib_name=False)
class DeviceDiagnosisServiceDataType(SpineBase): # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:DeviceDiagnosisServiceDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "installation_time",
            "xml_name": "installationTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "boot_counter",
            "xml_name": "bootCounter",
            "type": "xs:unsignedLong",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "next_service",
            "xml_name": "nextService",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
    ]


@spine_type('ns_p:DeviceDiagnosisHeartbeatDataElementsType', is_value_type=False, no_attrib_name=False)
class DeviceDiagnosisHeartbeatDataElementsType(SpineBase): # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:DeviceDiagnosisHeartbeatDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "heartbeat_counter",
            "xml_name": "heartbeatCounter",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "heartbeat_timeout",
            "xml_name": "heartbeatTimeout",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:DeviceDiagnosisHeartbeatDataType', is_value_type=False, no_attrib_name=False)
class DeviceDiagnosisHeartbeatDataType(SpineBase): # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:DeviceDiagnosisHeartbeatDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "heartbeat_counter",
            "xml_name": "heartbeatCounter",
            "type": "xs:unsignedLong",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
        {
            "name": "heartbeat_timeout",
            "xml_name": "heartbeatTimeout",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:DeviceDiagnosisStateDataElementsType', is_value_type=False, no_attrib_name=False)
class DeviceDiagnosisStateDataElementsType(SpineBase): # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:DeviceDiagnosisStateDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "operating_state",
            "xml_name": "operatingState",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "vendor_state_code",
            "xml_name": "vendorStateCode",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "last_error_code",
            "xml_name": "lastErrorCode",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "up_time",
            "xml_name": "upTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "total_up_time",
            "xml_name": "totalUpTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "power_supply_condition",
            "xml_name": "powerSupplyCondition",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:DeviceDiagnosisStateDataType', is_value_type=False, no_attrib_name=False)
class DeviceDiagnosisStateDataType(SpineBase): # EEBus_SPINE_TS_DeviceDiagnosis.xsd:ns_p:DeviceDiagnosisStateDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "operating_state",
            "xml_name": "operatingState",
            "type": "ns_p:DeviceDiagnosisOperatingStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceDiagnosisOperatingStateType"
        },
        {
            "name": "vendor_state_code",
            "xml_name": "vendorStateCode",
            "type": "ns_p:VendorStateCodeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "VendorStateCodeType"
        },
        {
            "name": "last_error_code",
            "xml_name": "lastErrorCode",
            "type": "ns_p:LastErrorCodeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LastErrorCodeType"
        },
        {
            "name": "up_time",
            "xml_name": "upTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "total_up_time",
            "xml_name": "totalUpTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "power_supply_condition",
            "xml_name": "powerSupplyCondition",
            "type": "ns_p:PowerSupplyConditionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSupplyConditionType"
        },
    ]

