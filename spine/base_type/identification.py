# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import TimePeriodElementsType
    from spine.base_type.commondatatypes import TimePeriodType
    from spine.simple_type.identification import IdentificationIdType
    from spine.simple_type.identification import IdentificationValueType
    from spine.simple_type.identification import SessionIdType
    from spine.simple_type.measurement import MeasurementIdType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.identification import IdentificationTypeType



@spine_type('ns_p:SessionMeasurementRelationDataType', is_value_type=False, no_attrib_name=False)
class SessionMeasurementRelationDataType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionMeasurementRelationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "session_id",
            "xml_name": "sessionId",
            "type": "ns_p:SessionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SessionIdType"
        },
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:SessionIdentificationDataType', is_value_type=False, no_attrib_name=False)
class SessionIdentificationDataType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionIdentificationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "session_id",
            "xml_name": "sessionId",
            "type": "ns_p:SessionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SessionIdType"
        },
        {
            "name": "identification_id",
            "xml_name": "identificationId",
            "type": "ns_p:IdentificationIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationIdType"
        },
        {
            "name": "is_latest_session",
            "xml_name": "isLatestSession",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "time_period",
            "xml_name": "timePeriod",
            "type": "ns_p:TimePeriodType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePeriodType"
        },
        {
            "name": "start_time",
            "xml_name": "startTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "end_time",
            "xml_name": "endTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
    ]


@spine_type('ns_p:IdentificationDataType', is_value_type=False, no_attrib_name=False)
class IdentificationDataType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:IdentificationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "identification_id",
            "xml_name": "identificationId",
            "type": "ns_p:IdentificationIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationIdType"
        },
        {
            "name": "identification_type",
            "xml_name": "identificationType",
            "type": "ns_p:IdentificationTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationTypeType"
        },
        {
            "name": "identification_value",
            "xml_name": "identificationValue",
            "type": "ns_p:IdentificationValueType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationValueType"
        },
        {
            "name": "authorized",
            "xml_name": "authorized",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:SessionMeasurementRelationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class SessionMeasurementRelationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionMeasurementRelationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "session_id",
            "xml_name": "sessionId",
            "type": "ns_p:SessionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SessionIdType"
        },
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementIdType"
        },
    ]


@spine_type('ns_p:SessionMeasurementRelationListDataType', is_value_type=False, no_attrib_name=False)
class SessionMeasurementRelationListDataType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionMeasurementRelationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "session_measurement_relation_data",
            "xml_name": "sessionMeasurementRelationData",
            "type": "ns_p:SessionMeasurementRelationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "session_id",
            "xml_name": "sessionId",
            "type": "ns_p:SessionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SessionIdType"
        },
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:MeasurementIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:SessionMeasurementRelationDataElementsType', is_value_type=False, no_attrib_name=False)
class SessionMeasurementRelationDataElementsType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionMeasurementRelationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "session_id",
            "xml_name": "sessionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "measurement_id",
            "xml_name": "measurementId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:SessionIdentificationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class SessionIdentificationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionIdentificationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "session_id",
            "xml_name": "sessionId",
            "type": "ns_p:SessionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SessionIdType"
        },
        {
            "name": "identification_id",
            "xml_name": "identificationId",
            "type": "ns_p:IdentificationIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationIdType"
        },
        {
            "name": "is_latest_session",
            "xml_name": "isLatestSession",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "time_period",
            "xml_name": "timePeriod",
            "type": "ns_p:TimePeriodType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePeriodType"
        },
        {
            "name": "start_time",
            "xml_name": "startTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "end_time",
            "xml_name": "endTime",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
    ]


@spine_type('ns_p:SessionIdentificationListDataType', is_value_type=False, no_attrib_name=False)
class SessionIdentificationListDataType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionIdentificationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "session_identification_data",
            "xml_name": "sessionIdentificationData",
            "type": "ns_p:SessionIdentificationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "session_id",
            "xml_name": "sessionId",
            "type": "ns_p:SessionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SessionIdType"
        },
        {
            "name": "identification_id",
            "xml_name": "identificationId",
            "type": "ns_p:IdentificationIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationIdType"
        },
        {
            "name": "is_latest_session",
            "xml_name": "isLatestSession",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "time_period",
            "xml_name": "timePeriod",
            "type": "ns_p:TimePeriodType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePeriodType"
        },
    ]


@spine_type('ns_p:SessionIdentificationDataElementsType', is_value_type=False, no_attrib_name=False)
class SessionIdentificationDataElementsType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:SessionIdentificationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "session_id",
            "xml_name": "sessionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "identification_id",
            "xml_name": "identificationId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_latest_session",
            "xml_name": "isLatestSession",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time_period",
            "xml_name": "timePeriod",
            "type": "ns_p:TimePeriodElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePeriodElementsType"
        },
        {
            "name": "start_time",
            "xml_name": "startTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "end_time",
            "xml_name": "endTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:IdentificationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class IdentificationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:IdentificationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "identification_id",
            "xml_name": "identificationId",
            "type": "ns_p:IdentificationIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationIdType"
        },
        {
            "name": "identification_type",
            "xml_name": "identificationType",
            "type": "ns_p:IdentificationTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationTypeType"
        },
    ]


@spine_type('ns_p:IdentificationListDataType', is_value_type=False, no_attrib_name=False)
class IdentificationListDataType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:IdentificationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "identification_data",
            "xml_name": "identificationData",
            "type": "ns_p:IdentificationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "identification_id",
            "xml_name": "identificationId",
            "type": "ns_p:IdentificationIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationIdType"
        },
        {
            "name": "identification_type",
            "xml_name": "identificationType",
            "type": "ns_p:IdentificationTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationTypeType"
        },
        {
            "name": "identification_value",
            "xml_name": "identificationValue",
            "type": "ns_p:IdentificationValueType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationValueType"
        },
        {
            "name": "authorized",
            "xml_name": "authorized",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:IdentificationDataElementsType', is_value_type=False, no_attrib_name=False)
class IdentificationDataElementsType(SpineBase): # EEBus_SPINE_TS_Identification.xsd:ns_p:IdentificationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "identification_id",
            "xml_name": "identificationId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "identification_type",
            "xml_name": "identificationType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "identification_value",
            "xml_name": "identificationValue",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "authorized",
            "xml_name": "authorized",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]

