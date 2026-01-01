# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import FeatureAddressElementsType
    from spine.base_type.commondatatypes import FeatureAddressType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.subscriptionmanagement import SubscriptionIdType
    from spine.union_type.commondatatypes import FeatureTypeType



@spine_type('ns_p:SubscriptionManagementEntryDataType', is_value_type=False, no_attrib_name=False)
class SubscriptionManagementEntryDataType(SpineBase): # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementEntryDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "subscription_id",
            "xml_name": "subscriptionId",
            "type": "ns_p:SubscriptionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SubscriptionIdType"
        },
        {
            "name": "client_address",
            "xml_name": "clientAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "server_address",
            "xml_name": "serverAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "label",
            "xml_name": "label",
            "type": "ns_p:LabelType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LabelType"
        },
        {
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:DescriptionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DescriptionType"
        },
    ]


@spine_type('ns_p:SubscriptionManagementDeleteCallElementsType', is_value_type=False, no_attrib_name=False)
class SubscriptionManagementDeleteCallElementsType(SpineBase): # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementDeleteCallElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "subscription_id",
            "xml_name": "subscriptionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "client_address",
            "xml_name": "clientAddress",
            "type": "ns_p:FeatureAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressElementsType"
        },
        {
            "name": "server_address",
            "xml_name": "serverAddress",
            "type": "ns_p:FeatureAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressElementsType"
        },
    ]


@spine_type('ns_p:SubscriptionManagementDeleteCallType', is_value_type=False, no_attrib_name=False)
class SubscriptionManagementDeleteCallType(SpineBase): # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementDeleteCallType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "subscription_id",
            "xml_name": "subscriptionId",
            "type": "ns_p:SubscriptionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SubscriptionIdType"
        },
        {
            "name": "client_address",
            "xml_name": "clientAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "server_address",
            "xml_name": "serverAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
    ]


@spine_type('ns_p:SubscriptionManagementRequestCallElementsType', is_value_type=False, no_attrib_name=False)
class SubscriptionManagementRequestCallElementsType(SpineBase): # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementRequestCallElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "client_address",
            "xml_name": "clientAddress",
            "type": "ns_p:FeatureAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressElementsType"
        },
        {
            "name": "server_address",
            "xml_name": "serverAddress",
            "type": "ns_p:FeatureAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressElementsType"
        },
        {
            "name": "server_feature_type",
            "xml_name": "serverFeatureType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:SubscriptionManagementRequestCallType', is_value_type=False, no_attrib_name=False)
class SubscriptionManagementRequestCallType(SpineBase): # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementRequestCallType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "client_address",
            "xml_name": "clientAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "server_address",
            "xml_name": "serverAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "server_feature_type",
            "xml_name": "serverFeatureType",
            "type": "ns_p:FeatureTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureTypeType"
        },
    ]


@spine_type('ns_p:SubscriptionManagementEntryListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class SubscriptionManagementEntryListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementEntryListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "subscription_id",
            "xml_name": "subscriptionId",
            "type": "ns_p:SubscriptionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SubscriptionIdType"
        },
        {
            "name": "client_address",
            "xml_name": "clientAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "server_address",
            "xml_name": "serverAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
    ]


@spine_type('ns_p:SubscriptionManagementEntryListDataType', is_value_type=False, no_attrib_name=False)
class SubscriptionManagementEntryListDataType(SpineBase): # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementEntryListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "subscription_management_entry_data",
            "xml_name": "subscriptionManagementEntryData",
            "type": "ns_p:SubscriptionManagementEntryDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "subscription_id",
            "xml_name": "subscriptionId",
            "type": "ns_p:SubscriptionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SubscriptionIdType"
        },
        {
            "name": "client_address",
            "xml_name": "clientAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "server_address",
            "xml_name": "serverAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "label",
            "xml_name": "label",
            "type": "ns_p:LabelType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LabelType"
        },
        {
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:DescriptionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DescriptionType"
        },
    ]


@spine_type('ns_p:SubscriptionManagementEntryDataElementsType', is_value_type=False, no_attrib_name=False)
class SubscriptionManagementEntryDataElementsType(SpineBase): # EEBus_SPINE_TS_SubscriptionManagement.xsd:ns_p:SubscriptionManagementEntryDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "subscription_id",
            "xml_name": "subscriptionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "client_address",
            "xml_name": "clientAddress",
            "type": "ns_p:FeatureAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressElementsType"
        },
        {
            "name": "server_address",
            "xml_name": "serverAddress",
            "type": "ns_p:FeatureAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressElementsType"
        },
        {
            "name": "label",
            "xml_name": "label",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]

