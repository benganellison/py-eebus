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
    from spine.base_type.networkmanagement import NetworkManagementDeviceDescriptionDataElementsType
    from spine.base_type.networkmanagement import NetworkManagementDeviceDescriptionDataType
    from spine.base_type.networkmanagement import NetworkManagementEntityDescriptionDataElementsType
    from spine.base_type.networkmanagement import NetworkManagementEntityDescriptionDataType
    from spine.base_type.networkmanagement import NetworkManagementFeatureDescriptionDataElementsType
    from spine.base_type.networkmanagement import NetworkManagementFeatureDescriptionDataType
    from spine.base_type.usecaseinformation import UseCaseSupportElementsType
    from spine.base_type.usecaseinformation import UseCaseSupportSelectorsType
    from spine.base_type.usecaseinformation import UseCaseSupportType
    from spine.base_type.version import SpecificationVersionDataElementsType
    from spine.base_type.version import SpecificationVersionDataType
    from spine.enums.commondatatypes import RoleType
    from spine.enums.networkmanagement import NetworkManagementFeatureSetType
    from spine.enums.networkmanagement import NetworkManagementStateChangeType
    from spine.simple_type.bindingmanagement import BindingIdType
    from spine.simple_type.commondatatypes import AddressDeviceType
    from spine.simple_type.commondatatypes import AddressEntityType
    from spine.simple_type.commondatatypes import AddressFeatureType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import FeatureGroupType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.commondatatypes import MaxResponseDelayType
    from spine.simple_type.commondatatypes import SpecificationVersionType
    from spine.simple_type.networkmanagement import NetworkManagementCommunicationsTechnologyInformationType
    from spine.simple_type.networkmanagement import NetworkManagementMinimumTrustLevelType
    from spine.simple_type.networkmanagement import NetworkManagementNativeSetupType
    from spine.simple_type.networkmanagement import NetworkManagementTechnologyAddressType
    from spine.simple_type.subscriptionmanagement import SubscriptionIdType
    from spine.simple_type.usecaseinformation import UseCaseScenarioSupportType
    from spine.union_type.commondatatypes import DeviceTypeType
    from spine.union_type.commondatatypes import EntityTypeType
    from spine.union_type.commondatatypes import FeatureSpecificUsageType
    from spine.union_type.commondatatypes import FeatureTypeType
    from spine.union_type.commondatatypes import FunctionType
    from spine.union_type.usecaseinformation import UseCaseActorType
    from spine.union_type.usecaseinformation import UseCaseNameType



@spine_type('ns_p:Anonymous_4503667808', is_value_type=False, no_attrib_name=False)
class Anonymous_4503667808(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503667808 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "entity",
            "xml_name": "entity",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "feature",
            "xml_name": "feature",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4503652656', is_value_type=False, no_attrib_name=False)
class Anonymous_4503652656(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503652656 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "entity",
            "xml_name": "entity",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4503636624', is_value_type=False, no_attrib_name=False)
class Anonymous_4503636624(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503636624 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4503600816', is_value_type=False, no_attrib_name=False)
class Anonymous_4503600816(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503600816 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:AddressDeviceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AddressDeviceType"
        },
        {
            "name": "entity",
            "xml_name": "entity",
            "type": "ns_p:AddressEntityType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "feature",
            "xml_name": "feature",
            "type": "ns_p:AddressFeatureType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AddressFeatureType"
        },
    ]


@spine_type('ns_p:Anonymous_4503597120', is_value_type=False, no_attrib_name=False)
class Anonymous_4503597120(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503597120 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:AddressDeviceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AddressDeviceType"
        },
        {
            "name": "entity",
            "xml_name": "entity",
            "type": "ns_p:AddressEntityType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:Anonymous_4503567168', is_value_type=False, no_attrib_name=False)
class Anonymous_4503567168(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503567168 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device",
            "xml_name": "device",
            "type": "ns_p:AddressDeviceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AddressDeviceType"
        },
    ]


@spine_type('ns_p:Anonymous_4503851600', is_value_type=False, no_attrib_name=False)
class Anonymous_4503851600(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503851600 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "use_case_name",
            "xml_name": "useCaseName",
            "type": "ns_p:UseCaseNameType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UseCaseNameType"
        },
        {
            "name": "use_case_version",
            "xml_name": "useCaseVersion",
            "type": "ns_p:SpecificationVersionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SpecificationVersionType"
        },
        {
            "name": "scenario_support",
            "xml_name": "scenarioSupport",
            "type": "ns_p:UseCaseScenarioSupportType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UseCaseScenarioSupportType"
        },
    ]


@spine_type('ns_p:Anonymous_4503836096', is_value_type=False, no_attrib_name=False)
class Anonymous_4503836096(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503836096 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "use_case_name",
            "xml_name": "useCaseName",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "use_case_version",
            "xml_name": "useCaseVersion",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "use_case_available",
            "xml_name": "useCaseAvailable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "scenario_support",
            "xml_name": "scenarioSupport",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "use_case_document_sub_revision",
            "xml_name": "useCaseDocumentSubRevision",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4503815792', is_value_type=False, no_attrib_name=False)
class Anonymous_4503815792(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503815792 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "use_case_name",
            "xml_name": "useCaseName",
            "type": "ns_p:UseCaseNameType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UseCaseNameType"
        },
        {
            "name": "use_case_version",
            "xml_name": "useCaseVersion",
            "type": "ns_p:SpecificationVersionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SpecificationVersionType"
        },
        {
            "name": "use_case_available",
            "xml_name": "useCaseAvailable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "scenario_support",
            "xml_name": "scenarioSupport",
            "type": "ns_p:UseCaseScenarioSupportType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "use_case_document_sub_revision",
            "xml_name": "useCaseDocumentSubRevision",
            "type": "xs:string",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:Anonymous_4503788528', is_value_type=False, no_attrib_name=False)
class Anonymous_4503788528(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503788528 -> ComplexType
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


@spine_type('ns_p:NodeManagementDestinationDataType', is_value_type=False, no_attrib_name=False)
class NodeManagementDestinationDataType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDestinationDataType -> ComplexType
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
            "name": "label",
            "xml_name": "label",
            "type": "ns_p:LabelType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LabelType"
        },
    ]


@spine_type('ns_p:NodeManagementDetailedDiscoveryFeatureInformationElementsType', is_value_type=False, no_attrib_name=False)
class NodeManagementDetailedDiscoveryFeatureInformationElementsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryFeatureInformationElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "feature_address",
            "xml_name": "featureAddress",
            "type": "ns_p:Anonymous_4503667808",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503667808"
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


@spine_type('ns_p:NodeManagementDetailedDiscoveryEntityInformationElementsType', is_value_type=False, no_attrib_name=False)
class NodeManagementDetailedDiscoveryEntityInformationElementsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryEntityInformationElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "entity_address",
            "xml_name": "entityAddress",
            "type": "ns_p:Anonymous_4503652656",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503652656"
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


@spine_type('ns_p:Anonymous_4503635744', is_value_type=False, no_attrib_name=False)
class Anonymous_4503635744(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503635744 -> ComplexType
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


@spine_type('ns_p:NodeManagementDetailedDiscoveryDeviceInformationElementsType', is_value_type=False, no_attrib_name=False)
class NodeManagementDetailedDiscoveryDeviceInformationElementsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryDeviceInformationElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device_address",
            "xml_name": "deviceAddress",
            "type": "ns_p:Anonymous_4503636624",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503636624"
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


@spine_type('ns_p:Anonymous_4503634688', is_value_type=False, no_attrib_name=False)
class Anonymous_4503634688(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503634688 -> ComplexType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:NodeManagementSpecificationVersionListElementsType', is_value_type=False, no_attrib_name=False)
class NodeManagementSpecificationVersionListElementsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSpecificationVersionListElementsType -> ComplexType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:NodeManagementDetailedDiscoveryFeatureInformationType', is_value_type=False, no_attrib_name=False)
class NodeManagementDetailedDiscoveryFeatureInformationType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryFeatureInformationType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "feature_address",
            "xml_name": "featureAddress",
            "type": "ns_p:Anonymous_4503600816",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503600816"
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


@spine_type('ns_p:NodeManagementDetailedDiscoveryEntityInformationType', is_value_type=False, no_attrib_name=False)
class NodeManagementDetailedDiscoveryEntityInformationType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryEntityInformationType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "entity_address",
            "xml_name": "entityAddress",
            "type": "ns_p:Anonymous_4503597120",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503597120"
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


@spine_type('ns_p:Anonymous_4503566112', is_value_type=False, no_attrib_name=False)
class Anonymous_4503566112(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503566112 -> ComplexType
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


@spine_type('ns_p:NodeManagementDetailedDiscoveryDeviceInformationType', is_value_type=False, no_attrib_name=False)
class NodeManagementDetailedDiscoveryDeviceInformationType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryDeviceInformationType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device_address",
            "xml_name": "deviceAddress",
            "type": "ns_p:Anonymous_4503567168",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503567168"
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


@spine_type('ns_p:NodeManagementSpecificationVersionListType', is_value_type=False, no_attrib_name=False)
class NodeManagementSpecificationVersionListType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSpecificationVersionListType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "specification_version",
            "xml_name": "specificationVersion",
            "type": "ns_p:SpecificationVersionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:NodeManagementUseCaseDataSelectorsType', is_value_type=False, no_attrib_name=False)
class NodeManagementUseCaseDataSelectorsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementUseCaseDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "address",
            "xml_name": "address",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "actor",
            "xml_name": "actor",
            "type": "ns_p:UseCaseActorType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UseCaseActorType"
        },
        {
            "name": "use_case_support",
            "xml_name": "useCaseSupport",
            "type": "ns_p:Anonymous_4503851600",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503851600"
        },
    ]


@spine_type('ns_p:NodeManagementUseCaseDataElementsType', is_value_type=False, no_attrib_name=False)
class NodeManagementUseCaseDataElementsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementUseCaseDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "address",
            "xml_name": "address",
            "type": "ns_p:FeatureAddressElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressElementsType"
        },
        {
            "name": "actor",
            "xml_name": "actor",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "use_case_support",
            "xml_name": "useCaseSupport",
            "type": "ns_p:Anonymous_4503836096",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503836096"
        },
    ]


@spine_type('ns_p:NodeManagementUseCaseDataType', is_value_type=False, no_attrib_name=False)
class NodeManagementUseCaseDataType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementUseCaseDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "address",
            "xml_name": "address",
            "type": "ns_p:FeatureAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FeatureAddressType"
        },
        {
            "name": "actor",
            "xml_name": "actor",
            "type": "ns_p:UseCaseActorType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UseCaseActorType"
        },
        {
            "name": "use_case_support",
            "xml_name": "useCaseSupport",
            "type": "ns_p:Anonymous_4503815792",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:NodeManagementDestinationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class NodeManagementDestinationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDestinationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "device_address",
            "xml_name": "deviceAddress",
            "type": "ns_p:DeviceAddressType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceAddressType"
        },
    ]


@spine_type('ns_p:NodeManagementDestinationListDataType', is_value_type=False, no_attrib_name=False)
class NodeManagementDestinationListDataType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDestinationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "node_management_destination_data",
            "xml_name": "nodeManagementDestinationData",
            "type": "ns_p:NodeManagementDestinationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "device_description",
            "xml_name": "deviceDescription",
            "type": "ns_p:Anonymous_4503788528",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503788528"
        },
    ]


@spine_type('ns_p:NodeManagementDestinationDataElementsType', is_value_type=False, no_attrib_name=False)
class NodeManagementDestinationDataElementsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDestinationDataElementsType -> ComplexType
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
            "name": "label",
            "xml_name": "label",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:NodeManagementSubscriptionDeleteCallElementsType', is_value_type=False, no_attrib_name=False)
class NodeManagementSubscriptionDeleteCallElementsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionDeleteCallElementsType -> ComplexType
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


@spine_type('ns_p:NodeManagementSubscriptionDeleteCallType', is_value_type=False, no_attrib_name=False)
class NodeManagementSubscriptionDeleteCallType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionDeleteCallType -> ComplexType
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


@spine_type('ns_p:NodeManagementSubscriptionRequestCallElementsType', is_value_type=False, no_attrib_name=False)
class NodeManagementSubscriptionRequestCallElementsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionRequestCallElementsType -> ComplexType
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


@spine_type('ns_p:NodeManagementSubscriptionRequestCallType', is_value_type=False, no_attrib_name=False)
class NodeManagementSubscriptionRequestCallType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionRequestCallType -> ComplexType
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


@spine_type('ns_p:NodeManagementSubscriptionDataSelectorsType', is_value_type=False, no_attrib_name=False)
class NodeManagementSubscriptionDataSelectorsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionDataSelectorsType -> ComplexType
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


@spine_type('ns_p:NodeManagementSubscriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class NodeManagementSubscriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionDataElementsType -> ComplexType
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


@spine_type('ns_p:NodeManagementSubscriptionDataType', is_value_type=False, no_attrib_name=False)
class NodeManagementSubscriptionDataType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementSubscriptionDataType -> ComplexType
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


@spine_type('ns_p:NodeManagementBindingDeleteCallElementsType', is_value_type=False, no_attrib_name=False)
class NodeManagementBindingDeleteCallElementsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingDeleteCallElementsType -> ComplexType
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


@spine_type('ns_p:NodeManagementBindingDeleteCallType', is_value_type=False, no_attrib_name=False)
class NodeManagementBindingDeleteCallType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingDeleteCallType -> ComplexType
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


@spine_type('ns_p:NodeManagementBindingRequestCallElementsType', is_value_type=False, no_attrib_name=False)
class NodeManagementBindingRequestCallElementsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingRequestCallElementsType -> ComplexType
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


@spine_type('ns_p:NodeManagementBindingRequestCallType', is_value_type=False, no_attrib_name=False)
class NodeManagementBindingRequestCallType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingRequestCallType -> ComplexType
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


@spine_type('ns_p:NodeManagementBindingDataSelectorsType', is_value_type=False, no_attrib_name=False)
class NodeManagementBindingDataSelectorsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:NodeManagementBindingDataElementsType', is_value_type=False, no_attrib_name=False)
class NodeManagementBindingDataElementsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingDataElementsType -> ComplexType
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


@spine_type('ns_p:NodeManagementBindingDataType', is_value_type=False, no_attrib_name=False)
class NodeManagementBindingDataType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementBindingDataType -> ComplexType
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


@spine_type('ns_p:NodeManagementDetailedDiscoveryDataSelectorsType', is_value_type=False, no_attrib_name=False)
class NodeManagementDetailedDiscoveryDataSelectorsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryDataSelectorsType -> ComplexType
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
            "name": "device_type",
            "xml_name": "deviceType",
            "type": "ns_p:DeviceTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceTypeType"
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


@spine_type('ns_p:NodeManagementDetailedDiscoveryDataElementsType', is_value_type=False, no_attrib_name=False)
class NodeManagementDetailedDiscoveryDataElementsType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "specification_version_list",
            "xml_name": "specificationVersionList",
            "type": "ns_p:NodeManagementSpecificationVersionListElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementSpecificationVersionListElementsType"
        },
        {
            "name": "specification_version",
            "xml_name": "specificationVersion",
            "type": "ns_p:Anonymous_4503634688",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503634688"
        },
        {
            "name": "device_information",
            "xml_name": "deviceInformation",
            "type": "ns_p:NodeManagementDetailedDiscoveryDeviceInformationElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementDetailedDiscoveryDeviceInformationElementsType"
        },
        {
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:Anonymous_4503635744",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503635744"
        },
        {
            "name": "entity_information",
            "xml_name": "entityInformation",
            "type": "ns_p:NodeManagementDetailedDiscoveryEntityInformationElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementDetailedDiscoveryEntityInformationElementsType"
        },
        {
            "name": "feature_information",
            "xml_name": "featureInformation",
            "type": "ns_p:NodeManagementDetailedDiscoveryFeatureInformationElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementDetailedDiscoveryFeatureInformationElementsType"
        },
    ]


@spine_type('ns_p:Anonymous_4503666752', is_value_type=False, no_attrib_name=False)
class Anonymous_4503666752(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503666752 -> ComplexType
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
        {
            "name": "entity",
            "xml_name": "entity",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "feature",
            "xml_name": "feature",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4503651600', is_value_type=False, no_attrib_name=False)
class Anonymous_4503651600(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503651600 -> ComplexType
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
        {
            "name": "entity",
            "xml_name": "entity",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:NodeManagementDetailedDiscoveryDataType', is_value_type=False, no_attrib_name=False)
class NodeManagementDetailedDiscoveryDataType(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:NodeManagementDetailedDiscoveryDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "specification_version_list",
            "xml_name": "specificationVersionList",
            "type": "ns_p:NodeManagementSpecificationVersionListType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementSpecificationVersionListType"
        },
        {
            "name": "specification_version",
            "xml_name": "specificationVersion",
            "type": "ns_p:SpecificationVersionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "device_information",
            "xml_name": "deviceInformation",
            "type": "ns_p:NodeManagementDetailedDiscoveryDeviceInformationType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementDetailedDiscoveryDeviceInformationType"
        },
        {
            "name": "description",
            "xml_name": "description",
            "type": "ns_p:Anonymous_4503566112",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4503566112"
        },
        {
            "name": "entity_information",
            "xml_name": "entityInformation",
            "type": "ns_p:NodeManagementDetailedDiscoveryEntityInformationType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "feature_information",
            "xml_name": "featureInformation",
            "type": "ns_p:NodeManagementDetailedDiscoveryFeatureInformationType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:Anonymous_4503599760', is_value_type=False, no_attrib_name=False)
class Anonymous_4503599760(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503599760 -> ComplexType
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


@spine_type('ns_p:Anonymous_4503587824', is_value_type=False, no_attrib_name=False)
class Anonymous_4503587824(SpineBase): # EEBus_SPINE_TS_NodeManagement.xsd:ns_p:Anonymous_4503587824 -> ComplexType
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

