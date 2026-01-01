# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.simple_type.stateinformation import stateInformationIdType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.stateinformation import StateInformationCategoryType
    from spine.union_type.stateinformation import StateInformationType



@spine_type('ns_p:StateInformationDataType', is_value_type=False, no_attrib_name=False)
class StateInformationDataType(SpineBase): # EEBus_SPINE_TS_StateInformation.xsd:ns_p:StateInformationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "state_information_id",
            "xml_name": "stateInformationId",
            "type": "ns_p:stateInformationIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "stateInformationIdType"
        },
        {
            "name": "state_information",
            "xml_name": "stateInformation",
            "type": "ns_p:StateInformationType",
            "is_array": False,
            "is_optional": True,
            "class_check": "StateInformationType"
        },
        {
            "name": "is_active",
            "xml_name": "isActive",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "category",
            "xml_name": "category",
            "type": "ns_p:StateInformationCategoryType",
            "is_array": False,
            "is_optional": True,
            "class_check": "StateInformationCategoryType"
        },
        {
            "name": "time_of_last_change",
            "xml_name": "timeOfLastChange",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
    ]


@spine_type('ns_p:StateInformationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class StateInformationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_StateInformation.xsd:ns_p:StateInformationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "state_information_id",
            "xml_name": "stateInformationId",
            "type": "ns_p:stateInformationIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "stateInformationIdType"
        },
        {
            "name": "state_information",
            "xml_name": "stateInformation",
            "type": "ns_p:StateInformationType",
            "is_array": False,
            "is_optional": True,
            "class_check": "StateInformationType"
        },
        {
            "name": "is_active",
            "xml_name": "isActive",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "category",
            "xml_name": "category",
            "type": "ns_p:StateInformationCategoryType",
            "is_array": False,
            "is_optional": True,
            "class_check": "StateInformationCategoryType"
        },
    ]


@spine_type('ns_p:StateInformationListDataType', is_value_type=False, no_attrib_name=False)
class StateInformationListDataType(SpineBase): # EEBus_SPINE_TS_StateInformation.xsd:ns_p:StateInformationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "state_information_data",
            "xml_name": "stateInformationData",
            "type": "ns_p:StateInformationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "state_information_id",
            "xml_name": "stateInformationId",
            "type": "ns_p:stateInformationIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "stateInformationIdType"
        },
        {
            "name": "state_information",
            "xml_name": "stateInformation",
            "type": "ns_p:StateInformationType",
            "is_array": False,
            "is_optional": True,
            "class_check": "StateInformationType"
        },
        {
            "name": "is_active",
            "xml_name": "isActive",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "category",
            "xml_name": "category",
            "type": "ns_p:StateInformationCategoryType",
            "is_array": False,
            "is_optional": True,
            "class_check": "StateInformationCategoryType"
        },
        {
            "name": "time_of_last_change",
            "xml_name": "timeOfLastChange",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
    ]


@spine_type('ns_p:StateInformationDataElementsType', is_value_type=False, no_attrib_name=False)
class StateInformationDataElementsType(SpineBase): # EEBus_SPINE_TS_StateInformation.xsd:ns_p:StateInformationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "state_information_id",
            "xml_name": "stateInformationId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "state_information",
            "xml_name": "stateInformation",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_active",
            "xml_name": "isActive",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "category",
            "xml_name": "category",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time_of_last_change",
            "xml_name": "timeOfLastChange",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]

