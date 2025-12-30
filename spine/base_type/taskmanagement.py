# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.commondatatypes import ElementTagType
    from spine.simple_type.commondatatypes import DescriptionType
    from spine.simple_type.commondatatypes import LabelType
    from spine.simple_type.hvac import HvacOverrunIdType
    from spine.simple_type.loadcontrol import LoadControlEventIdType
    from spine.simple_type.powersequences import PowerSequenceIdType
    from spine.simple_type.taskmanagement import TaskManagementJobIdType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.taskmanagement import TaskManagementJobSourceType
    from spine.union_type.taskmanagement import TaskManagementJobStateType



@spine_type('ns_p:TaskManagementSmartEnergyManagementPsRelatedType', is_value_type=False, no_attrib_name=False)
class TaskManagementSmartEnergyManagementPsRelatedType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementSmartEnergyManagementPsRelatedType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
    ]


@spine_type('ns_p:TaskManagementPowerSequencesRelatedType', is_value_type=False, no_attrib_name=False)
class TaskManagementPowerSequencesRelatedType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementPowerSequencesRelatedType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
    ]


@spine_type('ns_p:TaskManagementLoadControlReleatedType', is_value_type=False, no_attrib_name=False)
class TaskManagementLoadControlReleatedType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementLoadControlReleatedType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "event_id",
            "xml_name": "eventId",
            "type": "ns_p:LoadControlEventIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventIdType"
        },
    ]


@spine_type('ns_p:TaskManagementHvacRelatedType', is_value_type=False, no_attrib_name=False)
class TaskManagementHvacRelatedType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementHvacRelatedType -> ComplexType
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


@spine_type('ns_p:TaskManagementDirectControlRelatedType', is_value_type=False, no_attrib_name=False)
class TaskManagementDirectControlRelatedType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementDirectControlRelatedType -> ComplexType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:TaskManagementJobDescriptionDataType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobDescriptionDataType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobDescriptionDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "job_id",
            "xml_name": "jobId",
            "type": "ns_p:TaskManagementJobIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobIdType"
        },
        {
            "name": "job_source",
            "xml_name": "jobSource",
            "type": "ns_p:TaskManagementJobSourceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobSourceType"
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


@spine_type('ns_p:TaskManagementJobRelationDataType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobRelationDataType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobRelationDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "job_id",
            "xml_name": "jobId",
            "type": "ns_p:TaskManagementJobIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobIdType"
        },
        {
            "name": "direct_control_related",
            "xml_name": "directControlRelated",
            "type": "ns_p:TaskManagementDirectControlRelatedType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementDirectControlRelatedType"
        },
        {
            "name": "hvac_related",
            "xml_name": "hvacRelated",
            "type": "ns_p:TaskManagementHvacRelatedType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementHvacRelatedType"
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
            "name": "load_control_releated",
            "xml_name": "loadControlReleated",
            "type": "ns_p:TaskManagementLoadControlReleatedType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementLoadControlReleatedType"
        },
        {
            "name": "event_id",
            "xml_name": "eventId",
            "type": "ns_p:LoadControlEventIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventIdType"
        },
        {
            "name": "power_sequences_related",
            "xml_name": "powerSequencesRelated",
            "type": "ns_p:TaskManagementPowerSequencesRelatedType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementPowerSequencesRelatedType"
        },
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:PowerSequenceIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceIdType"
        },
        {
            "name": "smart_energy_management_ps_related",
            "xml_name": "smartEnergyManagementPsRelated",
            "type": "ns_p:TaskManagementSmartEnergyManagementPsRelatedType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementSmartEnergyManagementPsRelatedType"
        },
    ]


@spine_type('ns_p:TaskManagementSmartEnergyManagementPsRelatedElementsType', is_value_type=False, no_attrib_name=False)
class TaskManagementSmartEnergyManagementPsRelatedElementsType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementSmartEnergyManagementPsRelatedElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TaskManagementPowerSequencesRelatedElementsType', is_value_type=False, no_attrib_name=False)
class TaskManagementPowerSequencesRelatedElementsType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementPowerSequencesRelatedElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TaskManagementLoadControlReleatedElementsType', is_value_type=False, no_attrib_name=False)
class TaskManagementLoadControlReleatedElementsType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementLoadControlReleatedElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "event_id",
            "xml_name": "eventId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TaskManagementHvacRelatedElementsType', is_value_type=False, no_attrib_name=False)
class TaskManagementHvacRelatedElementsType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementHvacRelatedElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "overrun_id",
            "xml_name": "overrunId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TaskManagementDirectControlRelatedElementsType', is_value_type=False, no_attrib_name=False)
class TaskManagementDirectControlRelatedElementsType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementDirectControlRelatedElementsType -> ComplexType
    _MEMBER_INFO = [
    ]


@spine_type('ns_p:TaskManagementJobDataType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobDataType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "job_id",
            "xml_name": "jobId",
            "type": "ns_p:TaskManagementJobIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobIdType"
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
            "name": "job_state",
            "xml_name": "jobState",
            "type": "ns_p:TaskManagementJobStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobStateType"
        },
        {
            "name": "elapsed_time",
            "xml_name": "elapsedTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "remaining_time",
            "xml_name": "remainingTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:TaskManagementOverviewDataElementsType', is_value_type=False, no_attrib_name=False)
class TaskManagementOverviewDataElementsType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementOverviewDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "remote_controllable",
            "xml_name": "remoteControllable",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "jobs_active",
            "xml_name": "jobsActive",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:TaskManagementOverviewDataType', is_value_type=False, no_attrib_name=False)
class TaskManagementOverviewDataType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementOverviewDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "remote_controllable",
            "xml_name": "remoteControllable",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
        {
            "name": "jobs_active",
            "xml_name": "jobsActive",
            "type": "xs:boolean",
            "is_array": False,
            "is_optional": True,
            "class_check": "bool"
        },
    ]


@spine_type('ns_p:TaskManagementJobDescriptionListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobDescriptionListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobDescriptionListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "job_id",
            "xml_name": "jobId",
            "type": "ns_p:TaskManagementJobIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobIdType"
        },
        {
            "name": "job_source",
            "xml_name": "jobSource",
            "type": "ns_p:TaskManagementJobSourceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobSourceType"
        },
    ]


@spine_type('ns_p:TaskManagementJobDescriptionListDataType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobDescriptionListDataType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobDescriptionListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "task_management_job_description_data",
            "xml_name": "taskManagementJobDescriptionData",
            "type": "ns_p:TaskManagementJobDescriptionDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "job_id",
            "xml_name": "jobId",
            "type": "ns_p:TaskManagementJobIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobIdType"
        },
        {
            "name": "job_source",
            "xml_name": "jobSource",
            "type": "ns_p:TaskManagementJobSourceType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobSourceType"
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


@spine_type('ns_p:TaskManagementJobDescriptionDataElementsType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobDescriptionDataElementsType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobDescriptionDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "job_id",
            "xml_name": "jobId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "job_source",
            "xml_name": "jobSource",
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


@spine_type('ns_p:TaskManagementJobRelationListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobRelationListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobRelationListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "job_id",
            "xml_name": "jobId",
            "type": "ns_p:TaskManagementJobIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobIdType"
        },
    ]


@spine_type('ns_p:TaskManagementJobRelationListDataType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobRelationListDataType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobRelationListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "task_management_job_relation_data",
            "xml_name": "taskManagementJobRelationData",
            "type": "ns_p:TaskManagementJobRelationDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "job_id",
            "xml_name": "jobId",
            "type": "ns_p:TaskManagementJobIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobIdType"
        },
        {
            "name": "direct_control_related",
            "xml_name": "directControlRelated",
            "type": "ns_p:TaskManagementDirectControlRelatedType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementDirectControlRelatedType"
        },
        {
            "name": "hvac_related",
            "xml_name": "hvacRelated",
            "type": "ns_p:TaskManagementHvacRelatedType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementHvacRelatedType"
        },
        {
            "name": "load_control_releated",
            "xml_name": "loadControlReleated",
            "type": "ns_p:TaskManagementLoadControlReleatedType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementLoadControlReleatedType"
        },
        {
            "name": "power_sequences_related",
            "xml_name": "powerSequencesRelated",
            "type": "ns_p:TaskManagementPowerSequencesRelatedType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementPowerSequencesRelatedType"
        },
        {
            "name": "smart_energy_management_ps_related",
            "xml_name": "smartEnergyManagementPsRelated",
            "type": "ns_p:TaskManagementSmartEnergyManagementPsRelatedType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementSmartEnergyManagementPsRelatedType"
        },
    ]


@spine_type('ns_p:TaskManagementJobRelationDataElementsType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobRelationDataElementsType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobRelationDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "job_id",
            "xml_name": "jobId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "direct_control_related",
            "xml_name": "directControlRelated",
            "type": "ns_p:TaskManagementDirectControlRelatedElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementDirectControlRelatedElementsType"
        },
        {
            "name": "hvac_related",
            "xml_name": "hvacRelated",
            "type": "ns_p:TaskManagementHvacRelatedElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementHvacRelatedElementsType"
        },
        {
            "name": "overrun_id",
            "xml_name": "overrunId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "load_control_releated",
            "xml_name": "loadControlReleated",
            "type": "ns_p:TaskManagementLoadControlReleatedElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementLoadControlReleatedElementsType"
        },
        {
            "name": "event_id",
            "xml_name": "eventId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "power_sequences_related",
            "xml_name": "powerSequencesRelated",
            "type": "ns_p:TaskManagementPowerSequencesRelatedElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementPowerSequencesRelatedElementsType"
        },
        {
            "name": "sequence_id",
            "xml_name": "sequenceId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "smart_energy_management_ps_related",
            "xml_name": "smartEnergyManagementPsRelated",
            "type": "ns_p:TaskManagementSmartEnergyManagementPsRelatedElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementSmartEnergyManagementPsRelatedElementsType"
        },
    ]


@spine_type('ns_p:TaskManagementJobListDataSelectorsType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobListDataSelectorsType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobListDataSelectorsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "job_id",
            "xml_name": "jobId",
            "type": "ns_p:TaskManagementJobIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobIdType"
        },
        {
            "name": "job_state",
            "xml_name": "jobState",
            "type": "ns_p:TaskManagementJobStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobStateType"
        },
    ]


@spine_type('ns_p:TaskManagementJobListDataType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobListDataType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobListDataType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "task_management_job_data",
            "xml_name": "taskManagementJobData",
            "type": "ns_p:TaskManagementJobDataType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "job_id",
            "xml_name": "jobId",
            "type": "ns_p:TaskManagementJobIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobIdType"
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
            "name": "job_state",
            "xml_name": "jobState",
            "type": "ns_p:TaskManagementJobStateType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobStateType"
        },
        {
            "name": "elapsed_time",
            "xml_name": "elapsedTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "remaining_time",
            "xml_name": "remainingTime",
            "type": "xs:duration",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
    ]


@spine_type('ns_p:TaskManagementJobDataElementsType', is_value_type=False, no_attrib_name=False)
class TaskManagementJobDataElementsType(SpineBase): # EEBus_SPINE_TS_TaskManagement.xsd:ns_p:TaskManagementJobDataElementsType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "job_id",
            "xml_name": "jobId",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "timestamp",
            "xml_name": "timestamp",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "job_state",
            "xml_name": "jobState",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "elapsed_time",
            "xml_name": "elapsedTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "remaining_time",
            "xml_name": "remainingTime",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]

