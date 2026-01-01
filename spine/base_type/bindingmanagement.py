# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import FeatureAddressElementsType
    from spine.base_type.commondatatypes import FeatureAddressType
    from spine.simple_type.bindingmanagement import BindingIdType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.union_type.commondatatypes import FeatureTypeType



@spine_type('ns_p:BindingManagementEntryDataType', is_value_type=False, no_attrib_name=False)
class BindingManagementEntryDataType(SpineBase): # EEBus_SPINE_TS_BindingManagement.xsd:ns_p:BindingManagementEntryDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "binding_id",
            "xml_name": "bindingId",
            "type": "ns_p:BindingIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BindingIdType"
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


@spine_type('ns_p:BindingManagementDeleteCallElementsType', is_value_type=False, no_attrib_name=False)
class BindingManagementDeleteCallElementsType(SpineBase): # EEBus_SPINE_TS_BindingManagement.xsd:ns_p:BindingManagementDeleteCallElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "binding_id",
            "xml_name": "bindingId",
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


@spine_type('ns_p:BindingManagementDeleteCallType', is_value_type=False, no_attrib_name=False)
class BindingManagementDeleteCallType(SpineBase): # EEBus_SPINE_TS_BindingManagement.xsd:ns_p:BindingManagementDeleteCallType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "binding_id",
            "xml_name": "bindingId",
            "type": "ns_p:BindingIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BindingIdType"
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


@spine_type('ns_p:BindingManagementRequestCallElementsType', is_value_type=False, no_attrib_name=False)
class BindingManagementRequestCallElementsType(SpineBase): # EEBus_SPINE_TS_BindingManagement.xsd:ns_p:BindingManagementRequestCallElementsType -> ComplexType
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


@spine_type('ns_p:BindingManagementRequestCallType', is_value_type=False, no_attrib_name=False)
class BindingManagementRequestCallType(SpineBase): # EEBus_SPINE_TS_BindingManagement.xsd:ns_p:BindingManagementRequestCallType -> ComplexType
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


@spine_type('ns_p:BindingManagementEntryListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class BindingManagementEntryListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_BindingManagement.xsd:ns_p:BindingManagementEntryListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "binding_id",
            "xml_name": "bindingId",
            "type": "ns_p:BindingIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BindingIdType"
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


@spine_type('ns_p:BindingManagementEntryListDataType', is_value_type=False, no_attrib_name=False)
class BindingManagementEntryListDataType(SpineBase): # EEBus_SPINE_TS_BindingManagement.xsd:ns_p:BindingManagementEntryListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "binding_management_entry_data",
            "xml_name": "bindingManagementEntryData",
            "type": "ns_p:BindingManagementEntryDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "binding_id",
            "xml_name": "bindingId",
            "type": "ns_p:BindingIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BindingIdType"
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


@spine_type('ns_p:BindingManagementEntryDataElementsType', is_value_type=False, no_attrib_name=False)
class BindingManagementEntryDataElementsType(SpineBase): # EEBus_SPINE_TS_BindingManagement.xsd:ns_p:BindingManagementEntryDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "binding_id",
            "xml_name": "bindingId",
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

