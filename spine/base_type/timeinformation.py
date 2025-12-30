# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.enums.commondatatypes import DayOfWeekType
    from spine.simple_type.commondatatypes import CalendarWeekType



@spine_type('ns_p:TimeDistributorEnquiryCallElementsType', is_value_type=False, no_attrib_name=False)
class TimeDistributorEnquiryCallElementsType(SpineBase): # EEBus_SPINE_TS_TimeInformation.xsd:ns_p:TimeDistributorEnquiryCallElementsType -> ComplexType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:TimeDistributorEnquiryCallType', is_value_type=False, no_attrib_name=False)
class TimeDistributorEnquiryCallType(SpineBase): # EEBus_SPINE_TS_TimeInformation.xsd:ns_p:TimeDistributorEnquiryCallType -> ComplexType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:TimePrecisionDataElementsType', is_value_type=False, no_attrib_name=False)
class TimePrecisionDataElementsType(SpineBase): # EEBus_SPINE_TS_TimeInformation.xsd:ns_p:TimePrecisionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "is_synchronised",
            "xml_name": "isSynchronised",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "last_sync_at",
            "xml_name": "lastSyncAt",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "clock_drift",
            "xml_name": "clockDrift",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TimePrecisionDataType', is_value_type=False, no_attrib_name=False)
class TimePrecisionDataType(SpineBase): # EEBus_SPINE_TS_TimeInformation.xsd:ns_p:TimePrecisionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "is_synchronised",
            "xml_name": "isSynchronised",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "last_sync_at",
            "xml_name": "lastSyncAt",
            "type": "xs:dateTime",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "clock_drift",
            "xml_name": "clockDrift",
            "type": "xs:integer",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]


@spine_type('ns_p:TimeDistributorDataElementsType', is_value_type=False, no_attrib_name=False)
class TimeDistributorDataElementsType(SpineBase): # EEBus_SPINE_TS_TimeInformation.xsd:ns_p:TimeDistributorDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "is_time_distributor",
            "xml_name": "isTimeDistributor",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "distributor_priority",
            "xml_name": "distributorPriority",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TimeDistributorDataType', is_value_type=False, no_attrib_name=False)
class TimeDistributorDataType(SpineBase): # EEBus_SPINE_TS_TimeInformation.xsd:ns_p:TimeDistributorDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "is_time_distributor",
            "xml_name": "isTimeDistributor",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "distributor_priority",
            "xml_name": "distributorPriority",
            "type": "xs:unsignedInt",
            "is_array": False,
            "is_optional": True,
            "class_check": "int"
        },
    ]


@spine_type('ns_p:TimeInformationDataElementsType', is_value_type=False, no_attrib_name=False)
class TimeInformationDataElementsType(SpineBase): # EEBus_SPINE_TS_TimeInformation.xsd:ns_p:TimeInformationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "utc",
            "xml_name": "utc",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "utc_offset",
            "xml_name": "utcOffset",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "day_of_week",
            "xml_name": "dayOfWeek",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "calendar_week",
            "xml_name": "calendarWeek",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TimeInformationDataType', is_value_type=False, no_attrib_name=False)
class TimeInformationDataType(SpineBase): # EEBus_SPINE_TS_TimeInformation.xsd:ns_p:TimeInformationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "utc",
            "xml_name": "utc",
            "type": "xs:dateTime",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "utc_offset",
            "xml_name": "utcOffset",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "day_of_week",
            "xml_name": "dayOfWeek",
            "type": "ns_p:DayOfWeekType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DayOfWeekType"
        },
        {
            "name": "calendar_week",
            "xml_name": "calendarWeek",
            "type": "ns_p:CalendarWeekType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CalendarWeekType"
        },
    ]

