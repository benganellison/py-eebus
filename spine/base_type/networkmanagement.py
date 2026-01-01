# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import DeviceAddressElementsType
    from spine.base_type.commondatatypes import DeviceAddressType
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import EntityAddressElementsType
    from spine.base_type.commondatatypes import EntityAddressType
    from spine.base_type.commondatatypes import FeatureAddressElementsType
    from spine.base_type.commondatatypes import FeatureAddressType
    from spine.base_type.commondatatypes import FunctionPropertyElementsType
    from spine.base_type.commondatatypes import FunctionPropertyType
    from spine.base_type.commondatatypes import PossibleOperationsElementsType
    from spine.base_type.commondatatypes import PossibleOperationsType
    from spine.enums.commondatatypes import RoleType
    from spine.enums.networkmanagement import NetworkManagementFeatureSetType
    from spine.enums.networkmanagement import NetworkManagementProcessStateStateType
    from spine.enums.networkmanagement import NetworkManagementStateChangeType
    from spine.simple_type.commondatatypes import AddressDeviceType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import FeatureGroupType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.commondatatypes import MaxResponseDelayType
    from spine.simple_type.networkmanagement import NetworkManagementCandidateSetupType
    from spine.simple_type.networkmanagement import NetworkManagementCommunicationsTechnologyInformationType
    from spine.simple_type.networkmanagement import NetworkManagementMinimumTrustLevelType
    from spine.simple_type.networkmanagement import NetworkManagementNativeSetupType
    from spine.simple_type.networkmanagement import NetworkManagementProcessTimeoutType
    from spine.simple_type.networkmanagement import NetworkManagementScanSetupType
    from spine.simple_type.networkmanagement import NetworkManagementSetupType
    from spine.simple_type.networkmanagement import NetworkManagementTechnologyAddressType
    from spine.union_type.commondatatypes import DeviceTypeType
    from spine.union_type.commondatatypes import EntityTypeType
    from spine.union_type.commondatatypes import FeatureSpecificUsageType
    from spine.union_type.commondatatypes import FeatureTypeType
    from spine.union_type.commondatatypes import FunctionType



@spine_type('ns_p:NetworkManagementFeatureDescriptionDataType', is_value_type=False, no_attrib_name=False)
class NetworkManagementFeatureDescriptionDataType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementFeatureDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "feature_address",
            "xml_name": "featureAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "feature_type",
            "xml_name": "featureType",
            "type": "ns_p:FeatureTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureTypeType"
        },
        {
            "name": "specific_usage",
            "xml_name": "specificUsage",
            "type": "ns_p:FeatureSpecificUsageType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "feature_group",
            "xml_name": "featureGroup",
            "type": "ns_p:FeatureGroupType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureGroupType"
        },
        {
            "name": "role",
            "xml_name": "role",
            "type": "ns_p:RoleType",
            "is_array": False,
            "is_optional": True,
            "class_check": "RoleType"
        },
        {
            "name": "supported_function",
            "xml_name": "supportedFunction",
            "type": "ns_p:FunctionPropertyType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "function",
            "xml_name": "function",
            "type": "ns_p:FunctionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FunctionType"
        },
        {
            "name": "possible_operations",
            "xml_name": "possibleOperations",
            "type": "ns_p:PossibleOperationsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PossibleOperationsType"
        },
        {
            "name": "last_state_change",
            "xml_name": "lastStateChange",
            "type": "ns_p:NetworkManagementStateChangeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementStateChangeType"
        },
        {
            "name": "minimum_trust_level",
            "xml_name": "minimumTrustLevel",
            "type": "ns_p:NetworkManagementMinimumTrustLevelType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementMinimumTrustLevelType"
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
        {
            "name": "max_response_delay",
            "xml_name": "maxResponseDelay",
            "type": "ns_p:MaxResponseDelayType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MaxResponseDelayType"
        },
    ]


@spine_type('ns_p:NetworkManagementEntityDescriptionDataType', is_value_type=False, no_attrib_name=False)
class NetworkManagementEntityDescriptionDataType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementEntityDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "entity_address",
            "xml_name": "entityAddress",
            "type": "ns_p:EntityAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EntityAddressType"
        },
        {
            "name": "entity_type",
            "xml_name": "entityType",
            "type": "ns_p:EntityTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EntityTypeType"
        },
        {
            "name": "last_state_change",
            "xml_name": "lastStateChange",
            "type": "ns_p:NetworkManagementStateChangeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementStateChangeType"
        },
        {
            "name": "minimum_trust_level",
            "xml_name": "minimumTrustLevel",
            "type": "ns_p:NetworkManagementMinimumTrustLevelType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementMinimumTrustLevelType"
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


@spine_type('ns_p:NetworkManagementDeviceDescriptionDataType', is_value_type=False, no_attrib_name=False)
class NetworkManagementDeviceDescriptionDataType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementDeviceDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device_address",
            "xml_name": "deviceAddress",
            "type": "ns_p:DeviceAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceAddressType"
        },
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:AddressDeviceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AddressDeviceType"
        },
        {
            "name": "device_type",
            "xml_name": "deviceType",
            "type": "ns_p:DeviceTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceTypeType"
        },
        {
            "name": "network_management_responsible_address",
            "xml_name": "networkManagementResponsibleAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "native_setup",
            "xml_name": "nativeSetup",
            "type": "ns_p:NetworkManagementNativeSetupType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementNativeSetupType"
        },
        {
            "name": "technology_address",
            "xml_name": "technologyAddress",
            "type": "ns_p:NetworkManagementTechnologyAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementTechnologyAddressType"
        },
        {
            "name": "communications_technology_information",
            "xml_name": "communicationsTechnologyInformation",
            "type": "ns_p:NetworkManagementCommunicationsTechnologyInformationType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementCommunicationsTechnologyInformationType"
        },
        {
            "name": "network_feature_set",
            "xml_name": "networkFeatureSet",
            "type": "ns_p:NetworkManagementFeatureSetType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementFeatureSetType"
        },
        {
            "name": "last_state_change",
            "xml_name": "lastStateChange",
            "type": "ns_p:NetworkManagementStateChangeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementStateChangeType"
        },
        {
            "name": "minimum_trust_level",
            "xml_name": "minimumTrustLevel",
            "type": "ns_p:NetworkManagementMinimumTrustLevelType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementMinimumTrustLevelType"
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


@spine_type('ns_p:NetworkManagementFeatureDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementFeatureDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementFeatureDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "feature_address",
            "xml_name": "featureAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "feature_type",
            "xml_name": "featureType",
            "type": "ns_p:FeatureTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureTypeType"
        },
    ]


@spine_type('ns_p:NetworkManagementFeatureDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class NetworkManagementFeatureDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementFeatureDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "network_management_feature_description_data",
            "xml_name": "networkManagementFeatureDescriptionData",
            "type": "ns_p:NetworkManagementFeatureDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "feature_address",
            "xml_name": "featureAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "feature_type",
            "xml_name": "featureType",
            "type": "ns_p:FeatureTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureTypeType"
        },
        {
            "name": "specific_usage",
            "xml_name": "specificUsage",
            "type": "ns_p:FeatureSpecificUsageType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "feature_group",
            "xml_name": "featureGroup",
            "type": "ns_p:FeatureGroupType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureGroupType"
        },
        {
            "name": "role",
            "xml_name": "role",
            "type": "ns_p:RoleType",
            "is_array": False,
            "is_optional": True,
            "class_check": "RoleType"
        },
        {
            "name": "supported_function",
            "xml_name": "supportedFunction",
            "type": "ns_p:FunctionPropertyType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "last_state_change",
            "xml_name": "lastStateChange",
            "type": "ns_p:NetworkManagementStateChangeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementStateChangeType"
        },
        {
            "name": "minimum_trust_level",
            "xml_name": "minimumTrustLevel",
            "type": "ns_p:NetworkManagementMinimumTrustLevelType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementMinimumTrustLevelType"
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
        {
            "name": "max_response_delay",
            "xml_name": "maxResponseDelay",
            "type": "ns_p:MaxResponseDelayType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MaxResponseDelayType"
        },
    ]


@spine_type('ns_p:NetworkManagementFeatureDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementFeatureDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementFeatureDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "feature_address",
            "xml_name": "featureAddress",
            "type": "ns_p:FeatureAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressElementsType"
        },
        {
            "name": "feature_type",
            "xml_name": "featureType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "specific_usage",
            "xml_name": "specificUsage",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "feature_group",
            "xml_name": "featureGroup",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "role",
            "xml_name": "role",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "supported_function",
            "xml_name": "supportedFunction",
            "type": "ns_p:FunctionPropertyElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FunctionPropertyElementsType"
        },
        {
            "name": "function",
            "xml_name": "function",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "possible_operations",
            "xml_name": "possibleOperations",
            "type": "ns_p:PossibleOperationsElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PossibleOperationsElementsType"
        },
        {
            "name": "last_state_change",
            "xml_name": "lastStateChange",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "minimum_trust_level",
            "xml_name": "minimumTrustLevel",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
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
        {
            "name": "max_response_delay",
            "xml_name": "maxResponseDelay",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:NetworkManagementEntityDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementEntityDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementEntityDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "entity_address",
            "xml_name": "entityAddress",
            "type": "ns_p:EntityAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EntityAddressType"
        },
        {
            "name": "entity_type",
            "xml_name": "entityType",
            "type": "ns_p:EntityTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EntityTypeType"
        },
    ]


@spine_type('ns_p:NetworkManagementEntityDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class NetworkManagementEntityDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementEntityDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "network_management_entity_description_data",
            "xml_name": "networkManagementEntityDescriptionData",
            "type": "ns_p:NetworkManagementEntityDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "entity_address",
            "xml_name": "entityAddress",
            "type": "ns_p:EntityAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EntityAddressType"
        },
        {
            "name": "entity_type",
            "xml_name": "entityType",
            "type": "ns_p:EntityTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EntityTypeType"
        },
        {
            "name": "last_state_change",
            "xml_name": "lastStateChange",
            "type": "ns_p:NetworkManagementStateChangeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementStateChangeType"
        },
        {
            "name": "minimum_trust_level",
            "xml_name": "minimumTrustLevel",
            "type": "ns_p:NetworkManagementMinimumTrustLevelType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementMinimumTrustLevelType"
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


@spine_type('ns_p:NetworkManagementEntityDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementEntityDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementEntityDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "entity_address",
            "xml_name": "entityAddress",
            "type": "ns_p:EntityAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "EntityAddressElementsType"
        },
        {
            "name": "entity_type",
            "xml_name": "entityType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "last_state_change",
            "xml_name": "lastStateChange",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "minimum_trust_level",
            "xml_name": "minimumTrustLevel",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
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


@spine_type('ns_p:NetworkManagementDeviceDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementDeviceDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementDeviceDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device_address",
            "xml_name": "deviceAddress",
            "type": "ns_p:DeviceAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceAddressType"
        },
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:AddressDeviceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AddressDeviceType"
        },
        {
            "name": "device_type",
            "xml_name": "deviceType",
            "type": "ns_p:DeviceTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceTypeType"
        },
    ]


@spine_type('ns_p:NetworkManagementDeviceDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class NetworkManagementDeviceDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementDeviceDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "network_management_device_description_data",
            "xml_name": "networkManagementDeviceDescriptionData",
            "type": "ns_p:NetworkManagementDeviceDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "device_address",
            "xml_name": "deviceAddress",
            "type": "ns_p:DeviceAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceAddressType"
        },
        {
            "name": "device_type",
            "xml_name": "deviceType",
            "type": "ns_p:DeviceTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceTypeType"
        },
        {
            "name": "network_management_responsible_address",
            "xml_name": "networkManagementResponsibleAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "native_setup",
            "xml_name": "nativeSetup",
            "type": "ns_p:NetworkManagementNativeSetupType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementNativeSetupType"
        },
        {
            "name": "technology_address",
            "xml_name": "technologyAddress",
            "type": "ns_p:NetworkManagementTechnologyAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementTechnologyAddressType"
        },
        {
            "name": "communications_technology_information",
            "xml_name": "communicationsTechnologyInformation",
            "type": "ns_p:NetworkManagementCommunicationsTechnologyInformationType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementCommunicationsTechnologyInformationType"
        },
        {
            "name": "network_feature_set",
            "xml_name": "networkFeatureSet",
            "type": "ns_p:NetworkManagementFeatureSetType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementFeatureSetType"
        },
        {
            "name": "last_state_change",
            "xml_name": "lastStateChange",
            "type": "ns_p:NetworkManagementStateChangeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementStateChangeType"
        },
        {
            "name": "minimum_trust_level",
            "xml_name": "minimumTrustLevel",
            "type": "ns_p:NetworkManagementMinimumTrustLevelType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementMinimumTrustLevelType"
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


@spine_type('ns_p:NetworkManagementDeviceDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementDeviceDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementDeviceDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device_address",
            "xml_name": "deviceAddress",
            "type": "ns_p:DeviceAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceAddressElementsType"
        },
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "device_type",
            "xml_name": "deviceType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "network_management_responsible_address",
            "xml_name": "networkManagementResponsibleAddress",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "native_setup",
            "xml_name": "nativeSetup",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "technology_address",
            "xml_name": "technologyAddress",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "communications_technology_information",
            "xml_name": "communicationsTechnologyInformation",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "network_feature_set",
            "xml_name": "networkFeatureSet",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "last_state_change",
            "xml_name": "lastStateChange",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "minimum_trust_level",
            "xml_name": "minimumTrustLevel",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
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


@spine_type('ns_p:NetworkManagementReportCandidateDataElementsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementReportCandidateDataElementsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementReportCandidateDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "candidate_setup",
            "xml_name": "candidateSetup",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "setup_usable_for_add",
            "xml_name": "setupUsableForAdd",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
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


@spine_type('ns_p:NetworkManagementReportCandidateDataType', is_value_type=False, no_attrib_name=False)
class NetworkManagementReportCandidateDataType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementReportCandidateDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "candidate_setup",
            "xml_name": "candidateSetup",
            "type": "ns_p:NetworkManagementCandidateSetupType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementCandidateSetupType"
        },
        {
            "name": "setup_usable_for_add",
            "xml_name": "setupUsableForAdd",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
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


@spine_type('ns_p:NetworkManagementJoiningModeDataElementsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementJoiningModeDataElementsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementJoiningModeDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setup",
            "xml_name": "setup",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:NetworkManagementJoiningModeDataType', is_value_type=False, no_attrib_name=False)
class NetworkManagementJoiningModeDataType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementJoiningModeDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "setup",
            "xml_name": "setup",
            "type": "ns_p:NetworkManagementSetupType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementSetupType"
        },
    ]


@spine_type('ns_p:NetworkManagementProcessStateDataElementsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementProcessStateDataElementsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementProcessStateDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "state",
            "xml_name": "state",
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


@spine_type('ns_p:NetworkManagementProcessStateDataType', is_value_type=False, no_attrib_name=False)
class NetworkManagementProcessStateDataType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementProcessStateDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "state",
            "xml_name": "state",
            "type": "ns_p:NetworkManagementProcessStateStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementProcessStateStateType"
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


@spine_type('ns_p:NetworkManagementAbortCallElementsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementAbortCallElementsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementAbortCallElementsType -> ComplexType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:NetworkManagementAbortCallType', is_value_type=False, no_attrib_name=False)
class NetworkManagementAbortCallType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementAbortCallType -> ComplexType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:NetworkManagementDiscoverCallElementsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementDiscoverCallElementsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementDiscoverCallElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "discover_address",
            "xml_name": "discoverAddress",
            "type": "ns_p:FeatureAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressElementsType"
        },
    ]


@spine_type('ns_p:NetworkManagementDiscoverCallType', is_value_type=False, no_attrib_name=False)
class NetworkManagementDiscoverCallType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementDiscoverCallType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "discover_address",
            "xml_name": "discoverAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
    ]


@spine_type('ns_p:NetworkManagementScanNetworkCallElementsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementScanNetworkCallElementsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementScanNetworkCallElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "scan_setup",
            "xml_name": "scanSetup",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "timeout",
            "xml_name": "timeout",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:NetworkManagementScanNetworkCallType', is_value_type=False, no_attrib_name=False)
class NetworkManagementScanNetworkCallType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementScanNetworkCallType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "scan_setup",
            "xml_name": "scanSetup",
            "type": "ns_p:NetworkManagementScanSetupType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementScanSetupType"
        },
        {
            "name": "timeout",
            "xml_name": "timeout",
            "type": "ns_p:NetworkManagementProcessTimeoutType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementProcessTimeoutType"
        },
    ]


@spine_type('ns_p:NetworkManagementModifyNodeCallElementsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementModifyNodeCallElementsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementModifyNodeCallElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "node_address",
            "xml_name": "nodeAddress",
            "type": "ns_p:FeatureAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressElementsType"
        },
        {
            "name": "native_setup",
            "xml_name": "nativeSetup",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "timeout",
            "xml_name": "timeout",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
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


@spine_type('ns_p:NetworkManagementModifyNodeCallType', is_value_type=False, no_attrib_name=False)
class NetworkManagementModifyNodeCallType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementModifyNodeCallType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "node_address",
            "xml_name": "nodeAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "native_setup",
            "xml_name": "nativeSetup",
            "type": "ns_p:NetworkManagementNativeSetupType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementNativeSetupType"
        },
        {
            "name": "timeout",
            "xml_name": "timeout",
            "type": "ns_p:NetworkManagementProcessTimeoutType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementProcessTimeoutType"
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


@spine_type('ns_p:NetworkManagementRemoveNodeCallElementsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementRemoveNodeCallElementsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementRemoveNodeCallElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "node_address",
            "xml_name": "nodeAddress",
            "type": "ns_p:FeatureAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressElementsType"
        },
        {
            "name": "timeout",
            "xml_name": "timeout",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:NetworkManagementRemoveNodeCallType', is_value_type=False, no_attrib_name=False)
class NetworkManagementRemoveNodeCallType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementRemoveNodeCallType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "node_address",
            "xml_name": "nodeAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "timeout",
            "xml_name": "timeout",
            "type": "ns_p:NetworkManagementProcessTimeoutType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementProcessTimeoutType"
        },
    ]


@spine_type('ns_p:NetworkManagementAddNodeCallElementsType', is_value_type=False, no_attrib_name=False)
class NetworkManagementAddNodeCallElementsType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementAddNodeCallElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "node_address",
            "xml_name": "nodeAddress",
            "type": "ns_p:FeatureAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressElementsType"
        },
        {
            "name": "native_setup",
            "xml_name": "nativeSetup",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "timeout",
            "xml_name": "timeout",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
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


@spine_type('ns_p:NetworkManagementAddNodeCallType', is_value_type=False, no_attrib_name=False)
class NetworkManagementAddNodeCallType(SpineBase): # EEBus_SPINE_TS_NetworkManagement.xsd:ns_p:NetworkManagementAddNodeCallType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "node_address",
            "xml_name": "nodeAddress",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "native_setup",
            "xml_name": "nativeSetup",
            "type": "ns_p:NetworkManagementNativeSetupType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementNativeSetupType"
        },
        {
            "name": "timeout",
            "xml_name": "timeout",
            "type": "ns_p:NetworkManagementProcessTimeoutType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementProcessTimeoutType"
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

