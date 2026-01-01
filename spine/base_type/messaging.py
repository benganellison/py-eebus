# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import TimestampIntervalType
    from spine.simple_type.messaging import MessagingDataTextType
    from spine.simple_type.messaging import MessagingNumberType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.messaging import MessagingTypeType



@spine_type('ns_p:MessagingDataType', is_value_type=False, no_attrib_name=False)
class MessagingDataType(SpineBase): # EEBus_SPINE_TS_Messaging.xsd:ns_p:MessagingDataType -> ComplexType
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
            "name": "messaging_number",
            "xml_name": "messagingNumber",
            "type": "ns_p:MessagingNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MessagingNumberType"
        },
        {
            "name": "type",
            "xml_name": "type",
            "type": "ns_p:MessagingTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MessagingTypeType"
        },
        {
            "name": "text",
            "xml_name": "text",
            "type": "ns_p:MessagingDataTextType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MessagingDataTextType"
        },
    ]


@spine_type('ns_p:MessagingListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class MessagingListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Messaging.xsd:ns_p:MessagingListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "timestamp_interval",
            "xml_name": "timestampInterval",
            "type": "ns_p:TimestampIntervalType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimestampIntervalType"
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
        {
            "name": "messaging_number",
            "xml_name": "messagingNumber",
            "type": "ns_p:MessagingNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MessagingNumberType"
        },
    ]


@spine_type('ns_p:MessagingListDataType', is_value_type=False, no_attrib_name=False)
class MessagingListDataType(SpineBase): # EEBus_SPINE_TS_Messaging.xsd:ns_p:MessagingListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "messaging_data",
            "xml_name": "messagingData",
            "type": "ns_p:MessagingDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
        {
            "name": "messaging_number",
            "xml_name": "messagingNumber",
            "type": "ns_p:MessagingNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MessagingNumberType"
        },
        {
            "name": "type",
            "xml_name": "type",
            "type": "ns_p:MessagingTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MessagingTypeType"
        },
        {
            "name": "text",
            "xml_name": "text",
            "type": "ns_p:MessagingDataTextType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MessagingDataTextType"
        },
    ]


@spine_type('ns_p:MessagingDataElementsType', is_value_type=False, no_attrib_name=False)
class MessagingDataElementsType(SpineBase): # EEBus_SPINE_TS_Messaging.xsd:ns_p:MessagingDataElementsType -> ComplexType
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
            "name": "messaging_number",
            "xml_name": "messagingNumber",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "type",
            "xml_name": "type",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "text",
            "xml_name": "text",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]

