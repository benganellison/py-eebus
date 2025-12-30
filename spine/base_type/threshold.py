# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import ScaledNumberElementsType
    from spine.base_type.commondatatypes import ScaledNumberType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.simple_type.threshold import ThresholdIdType
    from spine.union_type.commondatatypes import ScopeTypeType
    from spine.union_type.commondatatypes import UnitOfMeasurementType
    from spine.union_type.threshold import ThresholdTypeType



@spine_type('ns_p:ThresholdDescriptionDataType', is_value_type=False, no_attrib_name=False)
class ThresholdDescriptionDataType(SpineBase): # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdIdType"
        },
        {
            "name": "threshold_type",
            "xml_name": "thresholdType",
            "type": "ns_p:ThresholdTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdTypeType"
        },
        {
            "name": "unit",
            "xml_name": "unit",
            "type": "ns_p:UnitOfMeasurementType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UnitOfMeasurementType"
        },
        {
            "name": "scope_type",
            "xml_name": "scopeType",
            "type": "ns_p:ScopeTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScopeTypeType"
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


@spine_type('ns_p:ThresholdConstraintsDataType', is_value_type=False, no_attrib_name=False)
class ThresholdConstraintsDataType(SpineBase): # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdConstraintsDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdIdType"
        },
        {
            "name": "threshold_range_min",
            "xml_name": "thresholdRangeMin",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "number",
            "xml_name": "number",
            "type": "ns_p:NumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NumberType"
        },
        {
            "name": "scale",
            "xml_name": "scale",
            "type": "ns_p:ScaleType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaleType"
        },
        {
            "name": "threshold_range_max",
            "xml_name": "thresholdRangeMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "threshold_step_size",
            "xml_name": "thresholdStepSize",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:ThresholdDataType', is_value_type=False, no_attrib_name=False)
class ThresholdDataType(SpineBase): # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdIdType"
        },
        {
            "name": "threshold_value",
            "xml_name": "thresholdValue",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "number",
            "xml_name": "number",
            "type": "ns_p:NumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NumberType"
        },
        {
            "name": "scale",
            "xml_name": "scale",
            "type": "ns_p:ScaleType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaleType"
        },
    ]


@spine_type('ns_p:ThresholdDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class ThresholdDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdIdType"
        },
        {
            "name": "scope_type",
            "xml_name": "scopeType",
            "type": "ns_p:ScopeTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScopeTypeType"
        },
    ]


@spine_type('ns_p:ThresholdDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class ThresholdDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "threshold_description_data",
            "xml_name": "thresholdDescriptionData",
            "type": "ns_p:ThresholdDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdIdType"
        },
        {
            "name": "threshold_type",
            "xml_name": "thresholdType",
            "type": "ns_p:ThresholdTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdTypeType"
        },
        {
            "name": "unit",
            "xml_name": "unit",
            "type": "ns_p:UnitOfMeasurementType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UnitOfMeasurementType"
        },
        {
            "name": "scope_type",
            "xml_name": "scopeType",
            "type": "ns_p:ScopeTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScopeTypeType"
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


@spine_type('ns_p:ThresholdDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class ThresholdDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "threshold_type",
            "xml_name": "thresholdType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "unit",
            "xml_name": "unit",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "scope_type",
            "xml_name": "scopeType",
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


@spine_type('ns_p:ThresholdConstraintsListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class ThresholdConstraintsListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdConstraintsListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdIdType"
        },
    ]


@spine_type('ns_p:ThresholdConstraintsListDataType', is_value_type=False, no_attrib_name=False)
class ThresholdConstraintsListDataType(SpineBase): # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdConstraintsListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "threshold_constraints_data",
            "xml_name": "thresholdConstraintsData",
            "type": "ns_p:ThresholdConstraintsDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdIdType"
        },
        {
            "name": "threshold_range_min",
            "xml_name": "thresholdRangeMin",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "threshold_range_max",
            "xml_name": "thresholdRangeMax",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "threshold_step_size",
            "xml_name": "thresholdStepSize",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:ThresholdConstraintsDataElementsType', is_value_type=False, no_attrib_name=False)
class ThresholdConstraintsDataElementsType(SpineBase): # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdConstraintsDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "threshold_range_min",
            "xml_name": "thresholdRangeMin",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "number",
            "xml_name": "number",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "scale",
            "xml_name": "scale",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "threshold_range_max",
            "xml_name": "thresholdRangeMax",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "threshold_step_size",
            "xml_name": "thresholdStepSize",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:ThresholdListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class ThresholdListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdIdType"
        },
    ]


@spine_type('ns_p:ThresholdListDataType', is_value_type=False, no_attrib_name=False)
class ThresholdListDataType(SpineBase): # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "threshold_data",
            "xml_name": "thresholdData",
            "type": "ns_p:ThresholdDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ThresholdIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdIdType"
        },
        {
            "name": "threshold_value",
            "xml_name": "thresholdValue",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:ThresholdDataElementsType', is_value_type=False, no_attrib_name=False)
class ThresholdDataElementsType(SpineBase): # EEBus_SPINE_TS_Threshold.xsd:ns_p:ThresholdDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "threshold_id",
            "xml_name": "thresholdId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "threshold_value",
            "xml_name": "thresholdValue",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "number",
            "xml_name": "number",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "scale",
            "xml_name": "scale",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]

