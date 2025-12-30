# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.hvac import HvacOperationModeIdType
    from spine.simple_type.hvac import HvacOverrunIdType
    from spine.simple_type.hvac import HvacSystemFunctionIdType
    from spine.simple_type.powersequences import PowerSequenceIdType
    from spine.simple_type.setpoint import SetpointIdType
    from spine.simple_type.timetable import TimeTableIdType
    from spine.union_type.hvac import HvacOperationModeTypeType
    from spine.union_type.hvac import HvacOverrunStatusType
    from spine.union_type.hvac import HvacOverrunTypeType
    from spine.union_type.hvac import HvacSystemFunctionTypeType



@spine_type('ns_p:HvacOverrunDescriptionDataType', is_value_type=False, no_attrib_name=False)
class HvacOverrunDescriptionDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOverrunDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "overrun_id",
            "xml_name": "overrunId",
            "type": "ns_p:HvacOverrunIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunIdType"
        },
        {
            "name": "overrun_type",
            "xml_name": "overrunType",
            "type": "ns_p:HvacOverrunTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunTypeType"
        },
        {
            "name": "affected_system_function_id",
            "xml_name": "affectedSystemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
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
    ]


@spine_type('ns_p:HvacOverrunDataType', is_value_type=False, no_attrib_name=False)
class HvacOverrunDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOverrunDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "overrun_id",
            "xml_name": "overrunId",
            "type": "ns_p:HvacOverrunIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunIdType"
        },
        {
            "name": "overrun_status",
            "xml_name": "overrunStatus",
            "type": "ns_p:HvacOverrunStatusType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunStatusType"
        },
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:TimeTableIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableIdType"
        },
        {
            "name": "is_overrun_status_changeable",
            "xml_name": "isOverrunStatusChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:HvacOperationModeDescriptionDataType', is_value_type=False, no_attrib_name=False)
class HvacOperationModeDescriptionDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOperationModeDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "operation_mode_id",
            "xml_name": "operationModeId",
            "type": "ns_p:HvacOperationModeIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOperationModeIdType"
        },
        {
            "name": "operation_mode_type",
            "xml_name": "operationModeType",
            "type": "ns_p:HvacOperationModeTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOperationModeTypeType"
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


@spine_type('ns_p:HvacSystemFunctionDescriptionDataType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionDescriptionDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
        {
            "name": "system_function_type",
            "xml_name": "systemFunctionType",
            "type": "ns_p:HvacSystemFunctionTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionTypeType"
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


@spine_type('ns_p:HvacSystemFunctionPowerSequenceRelationDataType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionPowerSequenceRelationDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionPowerSequenceRelationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionSetpointRelationDataType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionSetpointRelationDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionSetpointRelationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
        {
            "name": "operation_mode_id",
            "xml_name": "operationModeId",
            "type": "ns_p:HvacOperationModeIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOperationModeIdType"
        },
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:SetpointIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionOperationModeRelationDataType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionOperationModeRelationDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionOperationModeRelationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
        {
            "name": "operation_mode_id",
            "xml_name": "operationModeId",
            "type": "ns_p:HvacOperationModeIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionDataType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
        {
            "name": "current_operation_mode_id",
            "xml_name": "currentOperationModeId",
            "type": "ns_p:HvacOperationModeIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOperationModeIdType"
        },
        {
            "name": "is_operation_mode_id_changeable",
            "xml_name": "isOperationModeIdChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "current_setpoint_id",
            "xml_name": "currentSetpointId",
            "type": "ns_p:SetpointIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointIdType"
        },
        {
            "name": "is_setpoint_id_changeable",
            "xml_name": "isSetpointIdChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "is_overrun_active",
            "xml_name": "isOverrunActive",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:HvacOverrunDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class HvacOverrunDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOverrunDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "overrun_id",
            "xml_name": "overrunId",
            "type": "ns_p:HvacOverrunIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunIdType"
        },
    ]


@spine_type('ns_p:HvacOverrunDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class HvacOverrunDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOverrunDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "hvac_overrun_description_data",
            "xml_name": "hvacOverrunDescriptionData",
            "type": "ns_p:HvacOverrunDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "overrun_id",
            "xml_name": "overrunId",
            "type": "ns_p:HvacOverrunIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunIdType"
        },
        {
            "name": "overrun_type",
            "xml_name": "overrunType",
            "type": "ns_p:HvacOverrunTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunTypeType"
        },
        {
            "name": "affected_system_function_id",
            "xml_name": "affectedSystemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
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
    ]


@spine_type('ns_p:HvacOverrunDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class HvacOverrunDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOverrunDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "overrun_id",
            "xml_name": "overrunId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "overrun_type",
            "xml_name": "overrunType",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "affected_system_function_id",
            "xml_name": "affectedSystemFunctionId",
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


@spine_type('ns_p:HvacOverrunListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class HvacOverrunListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOverrunListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "overrun_id",
            "xml_name": "overrunId",
            "type": "ns_p:HvacOverrunIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunIdType"
        },
    ]


@spine_type('ns_p:HvacOverrunListDataType', is_value_type=False, no_attrib_name=False)
class HvacOverrunListDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOverrunListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "hvac_overrun_data",
            "xml_name": "hvacOverrunData",
            "type": "ns_p:HvacOverrunDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "overrun_id",
            "xml_name": "overrunId",
            "type": "ns_p:HvacOverrunIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunIdType"
        },
        {
            "name": "overrun_status",
            "xml_name": "overrunStatus",
            "type": "ns_p:HvacOverrunStatusType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunStatusType"
        },
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:TimeTableIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableIdType"
        },
        {
            "name": "is_overrun_status_changeable",
            "xml_name": "isOverrunStatusChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:HvacOverrunDataElementsType', is_value_type=False, no_attrib_name=False)
class HvacOverrunDataElementsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOverrunDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "overrun_id",
            "xml_name": "overrunId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "overrun_status",
            "xml_name": "overrunStatus",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "time_table_id",
            "xml_name": "timeTableId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_overrun_status_changeable",
            "xml_name": "isOverrunStatusChangeable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:HvacOperationModeDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class HvacOperationModeDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOperationModeDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "operation_mode_id",
            "xml_name": "operationModeId",
            "type": "ns_p:HvacOperationModeIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOperationModeIdType"
        },
    ]


@spine_type('ns_p:HvacOperationModeDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class HvacOperationModeDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOperationModeDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "hvac_operation_mode_description_data",
            "xml_name": "hvacOperationModeDescriptionData",
            "type": "ns_p:HvacOperationModeDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "operation_mode_id",
            "xml_name": "operationModeId",
            "type": "ns_p:HvacOperationModeIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOperationModeIdType"
        },
        {
            "name": "operation_mode_type",
            "xml_name": "operationModeType",
            "type": "ns_p:HvacOperationModeTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOperationModeTypeType"
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


@spine_type('ns_p:HvacOperationModeDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class HvacOperationModeDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacOperationModeDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "operation_mode_id",
            "xml_name": "operationModeId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "operation_mode_type",
            "xml_name": "operationModeType",
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


@spine_type('ns_p:HvacSystemFunctionDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "hvac_system_function_description_data",
            "xml_name": "hvacSystemFunctionDescriptionData",
            "type": "ns_p:HvacSystemFunctionDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
        {
            "name": "system_function_type",
            "xml_name": "systemFunctionType",
            "type": "ns_p:HvacSystemFunctionTypeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionTypeType"
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


@spine_type('ns_p:HvacSystemFunctionDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "system_function_type",
            "xml_name": "systemFunctionType",
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


@spine_type('ns_p:HvacSystemFunctionPowerSequenceRelationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionPowerSequenceRelationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionPowerSequenceRelationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionPowerSequenceRelationListDataType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionPowerSequenceRelationListDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionPowerSequenceRelationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "hvac_system_function_power_sequence_relation_data",
            "xml_name": "hvacSystemFunctionPowerSequenceRelationData",
            "type": "ns_p:HvacSystemFunctionPowerSequenceRelationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionPowerSequenceRelationDataElementsType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionPowerSequenceRelationDataElementsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionPowerSequenceRelationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionSetpointRelationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionSetpointRelationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionSetpointRelationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
        {
            "name": "operation_mode_id",
            "xml_name": "operationModeId",
            "type": "ns_p:HvacOperationModeIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOperationModeIdType"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionSetpointRelationListDataType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionSetpointRelationListDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionSetpointRelationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "hvac_system_function_setpoint_relation_data",
            "xml_name": "hvacSystemFunctionSetpointRelationData",
            "type": "ns_p:HvacSystemFunctionSetpointRelationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
        {
            "name": "operation_mode_id",
            "xml_name": "operationModeId",
            "type": "ns_p:HvacOperationModeIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOperationModeIdType"
        },
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:SetpointIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionSetpointRelationDataElementsType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionSetpointRelationDataElementsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionSetpointRelationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "operation_mode_id",
            "xml_name": "operationModeId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "setpoint_id",
            "xml_name": "setpointId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionOperationModeRelationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionOperationModeRelationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionOperationModeRelationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionOperationModeRelationListDataType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionOperationModeRelationListDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionOperationModeRelationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "hvac_system_function_operation_mode_relation_data",
            "xml_name": "hvacSystemFunctionOperationModeRelationData",
            "type": "ns_p:HvacSystemFunctionOperationModeRelationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
        {
            "name": "operation_mode_id",
            "xml_name": "operationModeId",
            "type": "ns_p:HvacOperationModeIdType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionOperationModeRelationDataElementsType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionOperationModeRelationDataElementsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionOperationModeRelationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "operation_mode_id",
            "xml_name": "operationModeId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionListDataType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionListDataType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "hvac_system_function_data",
            "xml_name": "hvacSystemFunctionData",
            "type": "ns_p:HvacSystemFunctionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:HvacSystemFunctionIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionIdType"
        },
        {
            "name": "current_operation_mode_id",
            "xml_name": "currentOperationModeId",
            "type": "ns_p:HvacOperationModeIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOperationModeIdType"
        },
        {
            "name": "is_operation_mode_id_changeable",
            "xml_name": "isOperationModeIdChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "current_setpoint_id",
            "xml_name": "currentSetpointId",
            "type": "ns_p:SetpointIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointIdType"
        },
        {
            "name": "is_setpoint_id_changeable",
            "xml_name": "isSetpointIdChangeable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "is_overrun_active",
            "xml_name": "isOverrunActive",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:HvacSystemFunctionDataElementsType', is_value_type=False, no_attrib_name=False)
class HvacSystemFunctionDataElementsType(SpineBase): # EEBus_SPINE_TS_HVAC.xsd:ns_p:HvacSystemFunctionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "system_function_id",
            "xml_name": "systemFunctionId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "current_operation_mode_id",
            "xml_name": "currentOperationModeId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_operation_mode_id_changeable",
            "xml_name": "isOperationModeIdChangeable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "current_setpoint_id",
            "xml_name": "currentSetpointId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_setpoint_id_changeable",
            "xml_name": "isSetpointIdChangeable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "is_overrun_active",
            "xml_name": "isOverrunActive",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]

