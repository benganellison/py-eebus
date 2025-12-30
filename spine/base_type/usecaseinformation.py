# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import FeatureAddressElementsType
    from spine.base_type.commondatatypes import FeatureAddressType
    from spine.simple_type.commondatatypes import SpecificationVersionType
    from spine.simple_type.usecaseinformation import UseCaseScenarioSupportType
    from spine.union_type.usecaseinformation import UseCaseActorType
    from spine.union_type.usecaseinformation import UseCaseNameType



@spine_type('ns_p:UseCaseSupportType', is_value_type=False, no_attrib_name=False)
class UseCaseSupportType(SpineBase): # EEBus_SPINE_TS_UseCaseInformation.xsd:ns_p:UseCaseSupportType -> ComplexType
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


@spine_type('ns_p:UseCaseSupportSelectorsType', is_value_type=False, no_attrib_name=False)
class UseCaseSupportSelectorsType(SpineBase): # EEBus_SPINE_TS_UseCaseInformation.xsd:ns_p:UseCaseSupportSelectorsType -> ComplexType
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


@spine_type('ns_p:UseCaseInformationDataType', is_value_type=False, no_attrib_name=False)
class UseCaseInformationDataType(SpineBase): # EEBus_SPINE_TS_UseCaseInformation.xsd:ns_p:UseCaseInformationDataType -> ComplexType
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
            "type": "ns_p:UseCaseSupportType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
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


@spine_type('ns_p:UseCaseSupportElementsType', is_value_type=False, no_attrib_name=False)
class UseCaseSupportElementsType(SpineBase): # EEBus_SPINE_TS_UseCaseInformation.xsd:ns_p:UseCaseSupportElementsType -> ComplexType
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


@spine_type('ns_p:UseCaseInformationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class UseCaseInformationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_UseCaseInformation.xsd:ns_p:UseCaseInformationListDataSelectorsType -> ComplexType
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
            "type": "ns_p:UseCaseSupportSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UseCaseSupportSelectorsType"
        },
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


@spine_type('ns_p:UseCaseInformationListDataType', is_value_type=False, no_attrib_name=False)
class UseCaseInformationListDataType(SpineBase): # EEBus_SPINE_TS_UseCaseInformation.xsd:ns_p:UseCaseInformationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "use_case_information_data",
            "xml_name": "useCaseInformationData",
            "type": "ns_p:UseCaseInformationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
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
            "type": "ns_p:UseCaseSupportType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:UseCaseInformationDataElementsType', is_value_type=False, no_attrib_name=False)
class UseCaseInformationDataElementsType(SpineBase): # EEBus_SPINE_TS_UseCaseInformation.xsd:ns_p:UseCaseInformationDataElementsType -> ComplexType
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
            "type": "ns_p:UseCaseSupportElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UseCaseSupportElementsType"
        },
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

