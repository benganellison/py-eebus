# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commandframe import CmdType
    from spine.base_type.commondatatypes import FeatureAddressType
    from spine.enums.commandframe import CmdClassifierType
    from spine.simple_type.commandframe import MsgCounterType
    from spine.simple_type.commondatatypes import SpecificationVersionType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType



@spine_type('ns_p:PayloadType', is_value_type=False, no_attrib_name=False)
class PayloadType(SpineBase): # EEBus_SPINE_TS_Datagram.xsd:ns_p:PayloadType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "cmd",
            "xml_name": "cmd",
            "type": "ns_p:CmdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:HeaderType', is_value_type=False, no_attrib_name=False)
class HeaderType(SpineBase): # EEBus_SPINE_TS_Datagram.xsd:ns_p:HeaderType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "specification_version",
            "xml_name": "specificationVersion",
            "type": "ns_p:SpecificationVersionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SpecificationVersionType"
        },
        {
            "name": "address_source",
            "xml_name": "addressSource",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "address_destination",
            "xml_name": "addressDestination",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "address_originator",
            "xml_name": "addressOriginator",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "msg_counter",
            "xml_name": "msgCounter",
            "type": "ns_p:MsgCounterType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MsgCounterType"
        },
        {
            "name": "msg_counter_reference",
            "xml_name": "msgCounterReference",
            "type": "ns_p:MsgCounterType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MsgCounterType"
        },
        {
            "name": "cmd_classifier",
            "xml_name": "cmdClassifier",
            "type": "ns_p:CmdClassifierType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CmdClassifierType"
        },
        {
            "name": "ack_request",
            "xml_name": "ackRequest",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
    ]


@spine_type('ns_p:DatagramType', is_value_type=False, no_attrib_name=False)
class DatagramType(SpineBase): # EEBus_SPINE_TS_Datagram.xsd:ns_p:DatagramType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "header",
            "xml_name": "header",
            "type": "ns_p:HeaderType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HeaderType"
        },
        {
            "name": "specification_version",
            "xml_name": "specificationVersion",
            "type": "ns_p:SpecificationVersionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SpecificationVersionType"
        },
        {
            "name": "address_source",
            "xml_name": "addressSource",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "address_destination",
            "xml_name": "addressDestination",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "address_originator",
            "xml_name": "addressOriginator",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "msg_counter",
            "xml_name": "msgCounter",
            "type": "ns_p:MsgCounterType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MsgCounterType"
        },
        {
            "name": "msg_counter_reference",
            "xml_name": "msgCounterReference",
            "type": "ns_p:MsgCounterType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MsgCounterType"
        },
        {
            "name": "cmd_classifier",
            "xml_name": "cmdClassifier",
            "type": "ns_p:CmdClassifierType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CmdClassifierType"
        },
        {
            "name": "ack_request",
            "xml_name": "ackRequest",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
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
            "name": "payload",
            "xml_name": "payload",
            "type": "ns_p:PayloadType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PayloadType"
        },
        {
            "name": "cmd",
            "xml_name": "cmd",
            "type": "ns_p:CmdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]

