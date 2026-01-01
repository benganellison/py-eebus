# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.commondatatypes import ScaledNumberElementsType
    from spine.base_type.commondatatypes import ScaledNumberType
    from spine.base_type.commondatatypes import TimePeriodElementsType
    from spine.base_type.commondatatypes import TimePeriodType
    from spine.simple_type.bill import BillCostIdType
    from spine.simple_type.bill import BillIdType
    from spine.simple_type.bill import BillPositionCountType
    from spine.simple_type.bill import BillPositionIdType
    from spine.simple_type.bill import BillValueIdType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.commondatatypes import NumberType
    from spine.simple_type.commondatatypes import ScaleType
    from spine.simple_type.identification import SessionIdType
    from spine.union_type.bill import BillCostTypeType
    from spine.union_type.bill import BillPositionTypeType
    from spine.union_type.bill import BillTypeType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import CurrencyType
    from spine.union_type.commondatatypes import ScopeTypeType
    from spine.union_type.commondatatypes import UnitOfMeasurementType



@spine_type('ns_p:BillCostType', is_value_type=False, no_attrib_name=False)
class BillCostType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillCostType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "cost_id",
            "xml_name": "costId",
            "type": "ns_p:BillCostIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillCostIdType"
        },
        {
            "name": "cost_type",
            "xml_name": "costType",
            "type": "ns_p:BillCostTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillCostTypeType"
        },
        {
            "name": "value_id",
            "xml_name": "valueId",
            "type": "ns_p:BillValueIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillValueIdType"
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
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:CurrencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CurrencyType"
        },
        {
            "name": "cost",
            "xml_name": "cost",
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
            "name": "cost_percentage",
            "xml_name": "costPercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:BillValueType', is_value_type=False, no_attrib_name=False)
class BillValueType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillValueType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "value_id",
            "xml_name": "valueId",
            "type": "ns_p:BillValueIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillValueIdType"
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
            "name": "value",
            "xml_name": "value",
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
            "name": "value_percentage",
            "xml_name": "valuePercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:BillPositionType', is_value_type=False, no_attrib_name=False)
class BillPositionType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillPositionType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "position_id",
            "xml_name": "positionId",
            "type": "ns_p:BillPositionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillPositionIdType"
        },
        {
            "name": "position_type",
            "xml_name": "positionType",
            "type": "ns_p:BillPositionTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillPositionTypeType"
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
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:BillValueType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "value_id",
            "xml_name": "valueId",
            "type": "ns_p:BillValueIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillValueIdType"
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
            "name": "value_percentage",
            "xml_name": "valuePercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "cost",
            "xml_name": "cost",
            "type": "ns_p:BillCostType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "cost_id",
            "xml_name": "costId",
            "type": "ns_p:BillCostIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillCostIdType"
        },
        {
            "name": "cost_type",
            "xml_name": "costType",
            "type": "ns_p:BillCostTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillCostTypeType"
        },
        {
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:CurrencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CurrencyType"
        },
        {
            "name": "cost_percentage",
            "xml_name": "costPercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
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


@spine_type('ns_p:Anonymous_4496085936', is_value_type=False, no_attrib_name=False)
class Anonymous_4496085936(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:Anonymous_4496085936 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "cost_id",
            "xml_name": "costId",
            "type": "ns_p:BillCostIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillCostIdType"
        },
        {
            "name": "cost_type",
            "xml_name": "costType",
            "type": "ns_p:BillCostTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillCostTypeType"
        },
        {
            "name": "value_id",
            "xml_name": "valueId",
            "type": "ns_p:BillValueIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillValueIdType"
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
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:CurrencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CurrencyType"
        },
        {
            "name": "cost",
            "xml_name": "cost",
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
            "name": "cost_percentage",
            "xml_name": "costPercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:Anonymous_4495212384', is_value_type=False, no_attrib_name=False)
class Anonymous_4495212384(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:Anonymous_4495212384 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "value_id",
            "xml_name": "valueId",
            "type": "ns_p:BillValueIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillValueIdType"
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
            "name": "value",
            "xml_name": "value",
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
            "name": "value_percentage",
            "xml_name": "valuePercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:BillCostElementsType', is_value_type=False, no_attrib_name=False)
class BillCostElementsType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillCostElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "cost_id",
            "xml_name": "costId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "cost_type",
            "xml_name": "costType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value_id",
            "xml_name": "valueId",
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
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "cost",
            "xml_name": "cost",
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
            "name": "cost_percentage",
            "xml_name": "costPercentage",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:BillValueElementsType', is_value_type=False, no_attrib_name=False)
class BillValueElementsType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillValueElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "value_id",
            "xml_name": "valueId",
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
            "name": "value",
            "xml_name": "value",
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
            "name": "value_percentage",
            "xml_name": "valuePercentage",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:BillDescriptionDataType', is_value_type=False, no_attrib_name=False)
class BillDescriptionDataType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "bill_id",
            "xml_name": "billId",
            "type": "ns_p:BillIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillIdType"
        },
        {
            "name": "bill_writeable",
            "xml_name": "billWriteable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "update_required",
            "xml_name": "updateRequired",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "supported_bill_type",
            "xml_name": "supportedBillType",
            "type": "ns_p:BillTypeType",
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
    ]


@spine_type('ns_p:BillConstraintsDataType', is_value_type=False, no_attrib_name=False)
class BillConstraintsDataType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillConstraintsDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "bill_id",
            "xml_name": "billId",
            "type": "ns_p:BillIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillIdType"
        },
        {
            "name": "position_count_min",
            "xml_name": "positionCountMin",
            "type": "ns_p:BillPositionCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillPositionCountType"
        },
        {
            "name": "position_count_max",
            "xml_name": "positionCountMax",
            "type": "ns_p:BillPositionCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillPositionCountType"
        },
    ]


@spine_type('ns_p:Anonymous_4495211504', is_value_type=False, no_attrib_name=False)
class Anonymous_4495211504(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:Anonymous_4495211504 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "position_id",
            "xml_name": "positionId",
            "type": "ns_p:BillPositionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillPositionIdType"
        },
        {
            "name": "position_type",
            "xml_name": "positionType",
            "type": "ns_p:BillPositionTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillPositionTypeType"
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
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "value_id",
            "xml_name": "valueId",
            "type": "ns_p:BillValueIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillValueIdType"
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
            "name": "value_percentage",
            "xml_name": "valuePercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "cost",
            "xml_name": "cost",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "cost_id",
            "xml_name": "costId",
            "type": "ns_p:BillCostIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillCostIdType"
        },
        {
            "name": "cost_type",
            "xml_name": "costType",
            "type": "ns_p:BillCostTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillCostTypeType"
        },
        {
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:CurrencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CurrencyType"
        },
        {
            "name": "cost_percentage",
            "xml_name": "costPercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
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


@spine_type('ns_p:Anonymous_4495210448', is_value_type=False, no_attrib_name=False)
class Anonymous_4495210448(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:Anonymous_4495210448 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "position_id",
            "xml_name": "positionId",
            "type": "ns_p:BillPositionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillPositionIdType"
        },
        {
            "name": "position_type",
            "xml_name": "positionType",
            "type": "ns_p:BillPositionTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillPositionTypeType"
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
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "value_id",
            "xml_name": "valueId",
            "type": "ns_p:BillValueIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillValueIdType"
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
            "name": "value_percentage",
            "xml_name": "valuePercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "cost",
            "xml_name": "cost",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
        {
            "name": "cost_id",
            "xml_name": "costId",
            "type": "ns_p:BillCostIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillCostIdType"
        },
        {
            "name": "cost_type",
            "xml_name": "costType",
            "type": "ns_p:BillCostTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillCostTypeType"
        },
        {
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:CurrencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CurrencyType"
        },
        {
            "name": "cost_percentage",
            "xml_name": "costPercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
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


@spine_type('ns_p:BillDataType', is_value_type=False, no_attrib_name=False)
class BillDataType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "bill_id",
            "xml_name": "billId",
            "type": "ns_p:BillIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillIdType"
        },
        {
            "name": "bill_type",
            "xml_name": "billType",
            "type": "ns_p:BillTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillTypeType"
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
            "name": "time_period",
            "xml_name": "timePeriod",
            "type": "ns_p:TimePeriodType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePeriodType"
        },
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:Anonymous_4495212384",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "cost",
            "xml_name": "cost",
            "type": "ns_p:Anonymous_4496085936",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
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
            "name": "position_id",
            "xml_name": "positionId",
            "type": "ns_p:BillPositionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillPositionIdType"
        },
        {
            "name": "position_type",
            "xml_name": "positionType",
            "type": "ns_p:BillPositionTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillPositionTypeType"
        },
    ]


@spine_type('ns_p:Anonymous_4496041232', is_value_type=False, no_attrib_name=False)
class Anonymous_4496041232(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:Anonymous_4496041232 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "cost_id",
            "xml_name": "costId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "cost_type",
            "xml_name": "costType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value_id",
            "xml_name": "valueId",
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
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "cost",
            "xml_name": "cost",
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
            "name": "cost_percentage",
            "xml_name": "costPercentage",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:Anonymous_4496040176', is_value_type=False, no_attrib_name=False)
class Anonymous_4496040176(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:Anonymous_4496040176 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "value_id",
            "xml_name": "valueId",
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
            "name": "value",
            "xml_name": "value",
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
            "name": "value_percentage",
            "xml_name": "valuePercentage",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:BillDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class BillDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "bill_id",
            "xml_name": "billId",
            "type": "ns_p:BillIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillIdType"
        },
    ]


@spine_type('ns_p:BillDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class BillDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "bill_description_data",
            "xml_name": "billDescriptionData",
            "type": "ns_p:BillDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "bill_id",
            "xml_name": "billId",
            "type": "ns_p:BillIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillIdType"
        },
        {
            "name": "bill_writeable",
            "xml_name": "billWriteable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "update_required",
            "xml_name": "updateRequired",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "supported_bill_type",
            "xml_name": "supportedBillType",
            "type": "ns_p:BillTypeType",
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
    ]


@spine_type('ns_p:BillDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class BillDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "bill_id",
            "xml_name": "billId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "bill_writeable",
            "xml_name": "billWriteable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "update_required",
            "xml_name": "updateRequired",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "supported_bill_type",
            "xml_name": "supportedBillType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "session_id",
            "xml_name": "sessionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:BillConstraintsListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class BillConstraintsListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillConstraintsListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "bill_id",
            "xml_name": "billId",
            "type": "ns_p:BillIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillIdType"
        },
    ]


@spine_type('ns_p:BillConstraintsListDataType', is_value_type=False, no_attrib_name=False)
class BillConstraintsListDataType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillConstraintsListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "bill_constraints_data",
            "xml_name": "billConstraintsData",
            "type": "ns_p:BillConstraintsDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "bill_id",
            "xml_name": "billId",
            "type": "ns_p:BillIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillIdType"
        },
        {
            "name": "position_count_min",
            "xml_name": "positionCountMin",
            "type": "ns_p:BillPositionCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillPositionCountType"
        },
        {
            "name": "position_count_max",
            "xml_name": "positionCountMax",
            "type": "ns_p:BillPositionCountType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillPositionCountType"
        },
    ]


@spine_type('ns_p:BillConstraintsDataElementsType', is_value_type=False, no_attrib_name=False)
class BillConstraintsDataElementsType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillConstraintsDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "bill_id",
            "xml_name": "billId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "position_count_min",
            "xml_name": "positionCountMin",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "position_count_max",
            "xml_name": "positionCountMax",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:BillListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class BillListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "bill_id",
            "xml_name": "billId",
            "type": "ns_p:BillIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillIdType"
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


@spine_type('ns_p:BillListDataType', is_value_type=False, no_attrib_name=False)
class BillListDataType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "bill_data",
            "xml_name": "billData",
            "type": "ns_p:BillDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "bill_id",
            "xml_name": "billId",
            "type": "ns_p:BillIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillIdType"
        },
        {
            "name": "bill_type",
            "xml_name": "billType",
            "type": "ns_p:BillTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillTypeType"
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
            "name": "total",
            "xml_name": "total",
            "type": "ns_p:Anonymous_4495210448",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4495210448"
        },
        {
            "name": "position",
            "xml_name": "position",
            "type": "ns_p:Anonymous_4495211504",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:BillDataElementsType', is_value_type=False, no_attrib_name=False)
class BillDataElementsType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "bill_id",
            "xml_name": "billId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "bill_type",
            "xml_name": "billType",
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
            "name": "time_period",
            "xml_name": "timePeriod",
            "type": "ns_p:TimePeriodElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePeriodElementsType"
        },
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:Anonymous_4496040176",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4496040176"
        },
        {
            "name": "cost",
            "xml_name": "cost",
            "type": "ns_p:Anonymous_4496041232",
            "is_array": False,
            "is_optional": True,
            "class_check": "Anonymous_4496041232"
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
            "name": "position_id",
            "xml_name": "positionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "position_type",
            "xml_name": "positionType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:Anonymous_4496106944', is_value_type=False, no_attrib_name=False)
class Anonymous_4496106944(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:Anonymous_4496106944 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "cost_id",
            "xml_name": "costId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "cost_type",
            "xml_name": "costType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "value_id",
            "xml_name": "valueId",
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
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "cost",
            "xml_name": "cost",
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
            "name": "cost_percentage",
            "xml_name": "costPercentage",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:Anonymous_4496105888', is_value_type=False, no_attrib_name=False)
class Anonymous_4496105888(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:Anonymous_4496105888 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "value_id",
            "xml_name": "valueId",
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
            "name": "value",
            "xml_name": "value",
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
            "name": "value_percentage",
            "xml_name": "valuePercentage",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
    ]


@spine_type('ns_p:Anonymous_4496038896', is_value_type=False, no_attrib_name=False)
class Anonymous_4496038896(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:Anonymous_4496038896 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "cost_id",
            "xml_name": "costId",
            "type": "ns_p:BillCostIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillCostIdType"
        },
        {
            "name": "cost_type",
            "xml_name": "costType",
            "type": "ns_p:BillCostTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillCostTypeType"
        },
        {
            "name": "value_id",
            "xml_name": "valueId",
            "type": "ns_p:BillValueIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillValueIdType"
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
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:CurrencyType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CurrencyType"
        },
        {
            "name": "cost",
            "xml_name": "cost",
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
            "name": "cost_percentage",
            "xml_name": "costPercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:Anonymous_4496037840', is_value_type=False, no_attrib_name=False)
class Anonymous_4496037840(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:Anonymous_4496037840 -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "value_id",
            "xml_name": "valueId",
            "type": "ns_p:BillValueIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillValueIdType"
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
            "name": "value",
            "xml_name": "value",
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
            "name": "value_percentage",
            "xml_name": "valuePercentage",
            "type": "ns_p:ScaledNumberType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberType"
        },
    ]


@spine_type('ns_p:BillPositionElementsType', is_value_type=False, no_attrib_name=False)
class BillPositionElementsType(SpineBase): # EEBus_SPINE_TS_Bill.xsd:ns_p:BillPositionElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "position_id",
            "xml_name": "positionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "position_type",
            "xml_name": "positionType",
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
        {
            "name": "value",
            "xml_name": "value",
            "type": "ns_p:BillValueElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillValueElementsType"
        },
        {
            "name": "value_id",
            "xml_name": "valueId",
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
            "name": "value_percentage",
            "xml_name": "valuePercentage",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
        },
        {
            "name": "cost",
            "xml_name": "cost",
            "type": "ns_p:BillCostElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillCostElementsType"
        },
        {
            "name": "cost_id",
            "xml_name": "costId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "cost_type",
            "xml_name": "costType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "currency",
            "xml_name": "currency",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "cost_percentage",
            "xml_name": "costPercentage",
            "type": "ns_p:ScaledNumberElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ScaledNumberElementsType"
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

