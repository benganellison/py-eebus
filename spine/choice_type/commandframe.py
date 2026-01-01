# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.actuatorlevel import ActuatorLevelDataType
    from spine.base_type.actuatorlevel import ActuatorLevelDescriptionDataType
    from spine.base_type.actuatorswitch import ActuatorSwitchDataType
    from spine.base_type.actuatorswitch import ActuatorSwitchDescriptionDataType
    from spine.base_type.alarm import AlarmListDataType
    from spine.base_type.bill import BillConstraintsListDataType
    from spine.base_type.bill import BillDescriptionListDataType
    from spine.base_type.bill import BillListDataType
    from spine.base_type.bindingmanagement import BindingManagementDeleteCallType
    from spine.base_type.bindingmanagement import BindingManagementEntryListDataType
    from spine.base_type.bindingmanagement import BindingManagementRequestCallType
    from spine.base_type.commandframe import FilterType
    from spine.base_type.datatunneling import DataTunnelingCallType
    from spine.base_type.deviceclassification import DeviceClassificationManufacturerDataType
    from spine.base_type.deviceclassification import DeviceClassificationUserDataType
    from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueConstraintsListDataType
    from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueDescriptionListDataType
    from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueListDataType
    from spine.base_type.devicediagnosis import DeviceDiagnosisHeartbeatDataType
    from spine.base_type.devicediagnosis import DeviceDiagnosisServiceDataType
    from spine.base_type.devicediagnosis import DeviceDiagnosisStateDataType
    from spine.base_type.directcontrol import DirectControlActivityListDataType
    from spine.base_type.directcontrol import DirectControlDescriptionDataType
    from spine.base_type.electricalconnection import ElectricalConnectionCharacteristicListDataType
    from spine.base_type.electricalconnection import ElectricalConnectionDescriptionListDataType
    from spine.base_type.electricalconnection import ElectricalConnectionParameterDescriptionListDataType
    from spine.base_type.electricalconnection import ElectricalConnectionPermittedValueSetListDataType
    from spine.base_type.electricalconnection import ElectricalConnectionStateListDataType
    from spine.base_type.hvac import HvacOperationModeDescriptionListDataType
    from spine.base_type.hvac import HvacOverrunDescriptionListDataType
    from spine.base_type.hvac import HvacOverrunListDataType
    from spine.base_type.hvac import HvacSystemFunctionDescriptionListDataType
    from spine.base_type.hvac import HvacSystemFunctionListDataType
    from spine.base_type.hvac import HvacSystemFunctionOperationModeRelationListDataType
    from spine.base_type.hvac import HvacSystemFunctionPowerSequenceRelationListDataType
    from spine.base_type.hvac import HvacSystemFunctionSetpointRelationListDataType
    from spine.base_type.identification import IdentificationListDataType
    from spine.base_type.identification import SessionIdentificationListDataType
    from spine.base_type.identification import SessionMeasurementRelationListDataType
    from spine.base_type.incentivetable import IncentiveTableConstraintsDataType
    from spine.base_type.incentivetable import IncentiveTableDataType
    from spine.base_type.incentivetable import IncentiveTableDescriptionDataType
    from spine.base_type.loadcontrol import LoadControlEventListDataType
    from spine.base_type.loadcontrol import LoadControlLimitConstraintsListDataType
    from spine.base_type.loadcontrol import LoadControlLimitDescriptionListDataType
    from spine.base_type.loadcontrol import LoadControlLimitListDataType
    from spine.base_type.loadcontrol import LoadControlNodeDataType
    from spine.base_type.loadcontrol import LoadControlStateListDataType
    from spine.base_type.measurement import MeasurementConstraintsListDataType
    from spine.base_type.measurement import MeasurementDescriptionListDataType
    from spine.base_type.measurement import MeasurementListDataType
    from spine.base_type.measurement import MeasurementSeriesListDataType
    from spine.base_type.measurement import MeasurementThresholdRelationListDataType
    from spine.base_type.messaging import MessagingListDataType
    from spine.base_type.networkmanagement import NetworkManagementAbortCallType
    from spine.base_type.networkmanagement import NetworkManagementAddNodeCallType
    from spine.base_type.networkmanagement import NetworkManagementDeviceDescriptionListDataType
    from spine.base_type.networkmanagement import NetworkManagementDiscoverCallType
    from spine.base_type.networkmanagement import NetworkManagementEntityDescriptionListDataType
    from spine.base_type.networkmanagement import NetworkManagementFeatureDescriptionListDataType
    from spine.base_type.networkmanagement import NetworkManagementJoiningModeDataType
    from spine.base_type.networkmanagement import NetworkManagementModifyNodeCallType
    from spine.base_type.networkmanagement import NetworkManagementProcessStateDataType
    from spine.base_type.networkmanagement import NetworkManagementRemoveNodeCallType
    from spine.base_type.networkmanagement import NetworkManagementReportCandidateDataType
    from spine.base_type.networkmanagement import NetworkManagementScanNetworkCallType
    from spine.base_type.nodemanagement import NodeManagementBindingDataType
    from spine.base_type.nodemanagement import NodeManagementBindingDeleteCallType
    from spine.base_type.nodemanagement import NodeManagementBindingRequestCallType
    from spine.base_type.nodemanagement import NodeManagementDestinationListDataType
    from spine.base_type.nodemanagement import NodeManagementDetailedDiscoveryDataType
    from spine.base_type.nodemanagement import NodeManagementSubscriptionDataType
    from spine.base_type.nodemanagement import NodeManagementSubscriptionDeleteCallType
    from spine.base_type.nodemanagement import NodeManagementSubscriptionRequestCallType
    from spine.base_type.nodemanagement import NodeManagementUseCaseDataType
    from spine.base_type.operatingconstraints import OperatingConstraintsDurationListDataType
    from spine.base_type.operatingconstraints import OperatingConstraintsInterruptListDataType
    from spine.base_type.operatingconstraints import OperatingConstraintsPowerDescriptionListDataType
    from spine.base_type.operatingconstraints import OperatingConstraintsPowerLevelListDataType
    from spine.base_type.operatingconstraints import OperatingConstraintsPowerRangeListDataType
    from spine.base_type.operatingconstraints import OperatingConstraintsResumeImplicationListDataType
    from spine.base_type.powersequences import PowerSequenceAlternativesRelationListDataType
    from spine.base_type.powersequences import PowerSequenceDescriptionListDataType
    from spine.base_type.powersequences import PowerSequenceNodeScheduleInformationDataType
    from spine.base_type.powersequences import PowerSequencePriceCalculationRequestCallType
    from spine.base_type.powersequences import PowerSequencePriceListDataType
    from spine.base_type.powersequences import PowerSequenceScheduleConfigurationRequestCallType
    from spine.base_type.powersequences import PowerSequenceScheduleConstraintsListDataType
    from spine.base_type.powersequences import PowerSequenceScheduleListDataType
    from spine.base_type.powersequences import PowerSequenceSchedulePreferenceListDataType
    from spine.base_type.powersequences import PowerSequenceStateListDataType
    from spine.base_type.powersequences import PowerTimeSlotScheduleConstraintsListDataType
    from spine.base_type.powersequences import PowerTimeSlotScheduleListDataType
    from spine.base_type.powersequences import PowerTimeSlotValueListDataType
    from spine.base_type.result import ResultDataType
    from spine.base_type.sensing import SensingDescriptionDataType
    from spine.base_type.sensing import SensingListDataType
    from spine.base_type.setpoint import SetpointConstraintsListDataType
    from spine.base_type.setpoint import SetpointDescriptionListDataType
    from spine.base_type.setpoint import SetpointListDataType
    from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsConfigurationRequestCallType
    from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsDataType
    from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsPriceCalculationRequestCallType
    from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsPriceDataType
    from spine.base_type.stateinformation import StateInformationListDataType
    from spine.base_type.subscriptionmanagement import SubscriptionManagementDeleteCallType
    from spine.base_type.subscriptionmanagement import SubscriptionManagementEntryListDataType
    from spine.base_type.subscriptionmanagement import SubscriptionManagementRequestCallType
    from spine.base_type.supplycondition import SupplyConditionDescriptionListDataType
    from spine.base_type.supplycondition import SupplyConditionListDataType
    from spine.base_type.supplycondition import SupplyConditionThresholdRelationListDataType
    from spine.base_type.tariffinformation import CommodityListDataType
    from spine.base_type.tariffinformation import IncentiveDescriptionListDataType
    from spine.base_type.tariffinformation import IncentiveListDataType
    from spine.base_type.tariffinformation import TariffBoundaryRelationListDataType
    from spine.base_type.tariffinformation import TariffDescriptionListDataType
    from spine.base_type.tariffinformation import TariffListDataType
    from spine.base_type.tariffinformation import TariffOverallConstraintsDataType
    from spine.base_type.tariffinformation import TariffTierRelationListDataType
    from spine.base_type.tariffinformation import TierBoundaryDescriptionListDataType
    from spine.base_type.tariffinformation import TierBoundaryListDataType
    from spine.base_type.tariffinformation import TierDescriptionListDataType
    from spine.base_type.tariffinformation import TierIncentiveRelationListDataType
    from spine.base_type.tariffinformation import TierListDataType
    from spine.base_type.taskmanagement import TaskManagementJobDescriptionListDataType
    from spine.base_type.taskmanagement import TaskManagementJobListDataType
    from spine.base_type.taskmanagement import TaskManagementJobRelationListDataType
    from spine.base_type.taskmanagement import TaskManagementOverviewDataType
    from spine.base_type.threshold import ThresholdConstraintsListDataType
    from spine.base_type.threshold import ThresholdDescriptionListDataType
    from spine.base_type.threshold import ThresholdListDataType
    from spine.base_type.timeinformation import TimeDistributorDataType
    from spine.base_type.timeinformation import TimeDistributorEnquiryCallType
    from spine.base_type.timeinformation import TimeInformationDataType
    from spine.base_type.timeinformation import TimePrecisionDataType
    from spine.base_type.timeseries import TimeSeriesConstraintsListDataType
    from spine.base_type.timeseries import TimeSeriesDescriptionListDataType
    from spine.base_type.timeseries import TimeSeriesListDataType
    from spine.base_type.timetable import TimeTableConstraintsListDataType
    from spine.base_type.timetable import TimeTableDescriptionListDataType
    from spine.base_type.timetable import TimeTableListDataType
    from spine.base_type.usecaseinformation import UseCaseInformationListDataType
    from spine.base_type.version import SpecificationVersionListDataType
    from spine.union_type.commondatatypes import AbsoluteOrRelativeTimeType
    from spine.union_type.commondatatypes import FunctionType



@spine_type('ns_p:PayloadContributionGroup', is_value_type=False, no_attrib_name=False)
class PayloadContributionGroup(SpineBase): # EEBus_SPINE_TS_CommandFrame.xsd:ns_p:PayloadContributionGroup -> ChoiceType
    _MEMBER_INFO = [
        {
            "name": "function",
            "xml_name": "function",
            "type": "ns_p:FunctionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FunctionType"
        },
        {
            "name": "filter",
            "xml_name": "filter",
            "type": "ns_p:FilterType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
        {
            "name": "actuator_level_data",
            "xml_name": "actuatorLevelData",
            "type": "ns_p:ActuatorLevelDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ActuatorLevelDataType"
        },
        {
            "name": "actuator_level_description_data",
            "xml_name": "actuatorLevelDescriptionData",
            "type": "ns_p:ActuatorLevelDescriptionDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ActuatorLevelDescriptionDataType"
        },
        {
            "name": "actuator_switch_data",
            "xml_name": "actuatorSwitchData",
            "type": "ns_p:ActuatorSwitchDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ActuatorSwitchDataType"
        },
        {
            "name": "actuator_switch_description_data",
            "xml_name": "actuatorSwitchDescriptionData",
            "type": "ns_p:ActuatorSwitchDescriptionDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ActuatorSwitchDescriptionDataType"
        },
        {
            "name": "alarm_list_data",
            "xml_name": "alarmListData",
            "type": "ns_p:AlarmListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AlarmListDataType"
        },
        {
            "name": "bill_constraints_list_data",
            "xml_name": "billConstraintsListData",
            "type": "ns_p:BillConstraintsListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillConstraintsListDataType"
        },
        {
            "name": "bill_description_list_data",
            "xml_name": "billDescriptionListData",
            "type": "ns_p:BillDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillDescriptionListDataType"
        },
        {
            "name": "bill_list_data",
            "xml_name": "billListData",
            "type": "ns_p:BillListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillListDataType"
        },
        {
            "name": "binding_management_delete_call",
            "xml_name": "bindingManagementDeleteCall",
            "type": "ns_p:BindingManagementDeleteCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BindingManagementDeleteCallType"
        },
        {
            "name": "binding_management_entry_list_data",
            "xml_name": "bindingManagementEntryListData",
            "type": "ns_p:BindingManagementEntryListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BindingManagementEntryListDataType"
        },
        {
            "name": "binding_management_request_call",
            "xml_name": "bindingManagementRequestCall",
            "type": "ns_p:BindingManagementRequestCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BindingManagementRequestCallType"
        },
        {
            "name": "commodity_list_data",
            "xml_name": "commodityListData",
            "type": "ns_p:CommodityListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CommodityListDataType"
        },
        {
            "name": "data_tunneling_call",
            "xml_name": "dataTunnelingCall",
            "type": "ns_p:DataTunnelingCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DataTunnelingCallType"
        },
        {
            "name": "device_classification_manufacturer_data",
            "xml_name": "deviceClassificationManufacturerData",
            "type": "ns_p:DeviceClassificationManufacturerDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationManufacturerDataType"
        },
        {
            "name": "device_classification_user_data",
            "xml_name": "deviceClassificationUserData",
            "type": "ns_p:DeviceClassificationUserDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationUserDataType"
        },
        {
            "name": "device_configuration_key_value_constraints_list_data",
            "xml_name": "deviceConfigurationKeyValueConstraintsListData",
            "type": "ns_p:DeviceConfigurationKeyValueConstraintsListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueConstraintsListDataType"
        },
        {
            "name": "device_configuration_key_value_description_list_data",
            "xml_name": "deviceConfigurationKeyValueDescriptionListData",
            "type": "ns_p:DeviceConfigurationKeyValueDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueDescriptionListDataType"
        },
        {
            "name": "device_configuration_key_value_list_data",
            "xml_name": "deviceConfigurationKeyValueListData",
            "type": "ns_p:DeviceConfigurationKeyValueListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueListDataType"
        },
        {
            "name": "device_diagnosis_heartbeat_data",
            "xml_name": "deviceDiagnosisHeartbeatData",
            "type": "ns_p:DeviceDiagnosisHeartbeatDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceDiagnosisHeartbeatDataType"
        },
        {
            "name": "device_diagnosis_service_data",
            "xml_name": "deviceDiagnosisServiceData",
            "type": "ns_p:DeviceDiagnosisServiceDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceDiagnosisServiceDataType"
        },
        {
            "name": "device_diagnosis_state_data",
            "xml_name": "deviceDiagnosisStateData",
            "type": "ns_p:DeviceDiagnosisStateDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceDiagnosisStateDataType"
        },
        {
            "name": "direct_control_activity_list_data",
            "xml_name": "directControlActivityListData",
            "type": "ns_p:DirectControlActivityListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DirectControlActivityListDataType"
        },
        {
            "name": "direct_control_description_data",
            "xml_name": "directControlDescriptionData",
            "type": "ns_p:DirectControlDescriptionDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DirectControlDescriptionDataType"
        },
        {
            "name": "electrical_connection_characteristic_list_data",
            "xml_name": "electricalConnectionCharacteristicListData",
            "type": "ns_p:ElectricalConnectionCharacteristicListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionCharacteristicListDataType"
        },
        {
            "name": "electrical_connection_description_list_data",
            "xml_name": "electricalConnectionDescriptionListData",
            "type": "ns_p:ElectricalConnectionDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionDescriptionListDataType"
        },
        {
            "name": "electrical_connection_parameter_description_list_data",
            "xml_name": "electricalConnectionParameterDescriptionListData",
            "type": "ns_p:ElectricalConnectionParameterDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionParameterDescriptionListDataType"
        },
        {
            "name": "electrical_connection_permitted_value_set_list_data",
            "xml_name": "electricalConnectionPermittedValueSetListData",
            "type": "ns_p:ElectricalConnectionPermittedValueSetListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionPermittedValueSetListDataType"
        },
        {
            "name": "electrical_connection_state_list_data",
            "xml_name": "electricalConnectionStateListData",
            "type": "ns_p:ElectricalConnectionStateListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionStateListDataType"
        },
        {
            "name": "hvac_operation_mode_description_list_data",
            "xml_name": "hvacOperationModeDescriptionListData",
            "type": "ns_p:HvacOperationModeDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOperationModeDescriptionListDataType"
        },
        {
            "name": "hvac_overrun_description_list_data",
            "xml_name": "hvacOverrunDescriptionListData",
            "type": "ns_p:HvacOverrunDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunDescriptionListDataType"
        },
        {
            "name": "hvac_overrun_list_data",
            "xml_name": "hvacOverrunListData",
            "type": "ns_p:HvacOverrunListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunListDataType"
        },
        {
            "name": "hvac_system_function_description_list_data",
            "xml_name": "hvacSystemFunctionDescriptionListData",
            "type": "ns_p:HvacSystemFunctionDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionDescriptionListDataType"
        },
        {
            "name": "hvac_system_function_list_data",
            "xml_name": "hvacSystemFunctionListData",
            "type": "ns_p:HvacSystemFunctionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionListDataType"
        },
        {
            "name": "hvac_system_function_operation_mode_relation_list_data",
            "xml_name": "hvacSystemFunctionOperationModeRelationListData",
            "type": "ns_p:HvacSystemFunctionOperationModeRelationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionOperationModeRelationListDataType"
        },
        {
            "name": "hvac_system_function_power_sequence_relation_list_data",
            "xml_name": "hvacSystemFunctionPowerSequenceRelationListData",
            "type": "ns_p:HvacSystemFunctionPowerSequenceRelationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionPowerSequenceRelationListDataType"
        },
        {
            "name": "hvac_system_function_setpoint_relation_list_data",
            "xml_name": "hvacSystemFunctionSetpointRelationListData",
            "type": "ns_p:HvacSystemFunctionSetpointRelationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionSetpointRelationListDataType"
        },
        {
            "name": "identification_list_data",
            "xml_name": "identificationListData",
            "type": "ns_p:IdentificationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationListDataType"
        },
        {
            "name": "incentive_description_list_data",
            "xml_name": "incentiveDescriptionListData",
            "type": "ns_p:IncentiveDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveDescriptionListDataType"
        },
        {
            "name": "incentive_list_data",
            "xml_name": "incentiveListData",
            "type": "ns_p:IncentiveListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveListDataType"
        },
        {
            "name": "incentive_table_constraints_data",
            "xml_name": "incentiveTableConstraintsData",
            "type": "ns_p:IncentiveTableConstraintsDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableConstraintsDataType"
        },
        {
            "name": "incentive_table_data",
            "xml_name": "incentiveTableData",
            "type": "ns_p:IncentiveTableDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableDataType"
        },
        {
            "name": "incentive_table_description_data",
            "xml_name": "incentiveTableDescriptionData",
            "type": "ns_p:IncentiveTableDescriptionDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableDescriptionDataType"
        },
        {
            "name": "load_control_event_list_data",
            "xml_name": "loadControlEventListData",
            "type": "ns_p:LoadControlEventListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventListDataType"
        },
        {
            "name": "load_control_limit_constraints_list_data",
            "xml_name": "loadControlLimitConstraintsListData",
            "type": "ns_p:LoadControlLimitConstraintsListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitConstraintsListDataType"
        },
        {
            "name": "load_control_limit_description_list_data",
            "xml_name": "loadControlLimitDescriptionListData",
            "type": "ns_p:LoadControlLimitDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitDescriptionListDataType"
        },
        {
            "name": "load_control_limit_list_data",
            "xml_name": "loadControlLimitListData",
            "type": "ns_p:LoadControlLimitListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitListDataType"
        },
        {
            "name": "load_control_node_data",
            "xml_name": "loadControlNodeData",
            "type": "ns_p:LoadControlNodeDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlNodeDataType"
        },
        {
            "name": "load_control_state_list_data",
            "xml_name": "loadControlStateListData",
            "type": "ns_p:LoadControlStateListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlStateListDataType"
        },
        {
            "name": "measurement_constraints_list_data",
            "xml_name": "measurementConstraintsListData",
            "type": "ns_p:MeasurementConstraintsListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementConstraintsListDataType"
        },
        {
            "name": "measurement_description_list_data",
            "xml_name": "measurementDescriptionListData",
            "type": "ns_p:MeasurementDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementDescriptionListDataType"
        },
        {
            "name": "measurement_list_data",
            "xml_name": "measurementListData",
            "type": "ns_p:MeasurementListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementListDataType"
        },
        {
            "name": "measurement_series_list_data",
            "xml_name": "measurementSeriesListData",
            "type": "ns_p:MeasurementSeriesListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementSeriesListDataType"
        },
        {
            "name": "measurement_threshold_relation_list_data",
            "xml_name": "measurementThresholdRelationListData",
            "type": "ns_p:MeasurementThresholdRelationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementThresholdRelationListDataType"
        },
        {
            "name": "messaging_list_data",
            "xml_name": "messagingListData",
            "type": "ns_p:MessagingListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MessagingListDataType"
        },
        {
            "name": "network_management_abort_call",
            "xml_name": "networkManagementAbortCall",
            "type": "ns_p:NetworkManagementAbortCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementAbortCallType"
        },
        {
            "name": "network_management_add_node_call",
            "xml_name": "networkManagementAddNodeCall",
            "type": "ns_p:NetworkManagementAddNodeCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementAddNodeCallType"
        },
        {
            "name": "network_management_device_description_list_data",
            "xml_name": "networkManagementDeviceDescriptionListData",
            "type": "ns_p:NetworkManagementDeviceDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementDeviceDescriptionListDataType"
        },
        {
            "name": "network_management_discover_call",
            "xml_name": "networkManagementDiscoverCall",
            "type": "ns_p:NetworkManagementDiscoverCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementDiscoverCallType"
        },
        {
            "name": "network_management_entity_description_list_data",
            "xml_name": "networkManagementEntityDescriptionListData",
            "type": "ns_p:NetworkManagementEntityDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementEntityDescriptionListDataType"
        },
        {
            "name": "network_management_feature_description_list_data",
            "xml_name": "networkManagementFeatureDescriptionListData",
            "type": "ns_p:NetworkManagementFeatureDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementFeatureDescriptionListDataType"
        },
        {
            "name": "network_management_joining_mode_data",
            "xml_name": "networkManagementJoiningModeData",
            "type": "ns_p:NetworkManagementJoiningModeDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementJoiningModeDataType"
        },
        {
            "name": "network_management_modify_node_call",
            "xml_name": "networkManagementModifyNodeCall",
            "type": "ns_p:NetworkManagementModifyNodeCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementModifyNodeCallType"
        },
        {
            "name": "network_management_process_state_data",
            "xml_name": "networkManagementProcessStateData",
            "type": "ns_p:NetworkManagementProcessStateDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementProcessStateDataType"
        },
        {
            "name": "network_management_remove_node_call",
            "xml_name": "networkManagementRemoveNodeCall",
            "type": "ns_p:NetworkManagementRemoveNodeCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementRemoveNodeCallType"
        },
        {
            "name": "network_management_report_candidate_data",
            "xml_name": "networkManagementReportCandidateData",
            "type": "ns_p:NetworkManagementReportCandidateDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementReportCandidateDataType"
        },
        {
            "name": "network_management_scan_network_call",
            "xml_name": "networkManagementScanNetworkCall",
            "type": "ns_p:NetworkManagementScanNetworkCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementScanNetworkCallType"
        },
        {
            "name": "node_management_binding_data",
            "xml_name": "nodeManagementBindingData",
            "type": "ns_p:NodeManagementBindingDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementBindingDataType"
        },
        {
            "name": "node_management_binding_delete_call",
            "xml_name": "nodeManagementBindingDeleteCall",
            "type": "ns_p:NodeManagementBindingDeleteCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementBindingDeleteCallType"
        },
        {
            "name": "node_management_binding_request_call",
            "xml_name": "nodeManagementBindingRequestCall",
            "type": "ns_p:NodeManagementBindingRequestCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementBindingRequestCallType"
        },
        {
            "name": "node_management_destination_list_data",
            "xml_name": "nodeManagementDestinationListData",
            "type": "ns_p:NodeManagementDestinationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementDestinationListDataType"
        },
        {
            "name": "node_management_detailed_discovery_data",
            "xml_name": "nodeManagementDetailedDiscoveryData",
            "type": "ns_p:NodeManagementDetailedDiscoveryDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementDetailedDiscoveryDataType"
        },
        {
            "name": "node_management_subscription_data",
            "xml_name": "nodeManagementSubscriptionData",
            "type": "ns_p:NodeManagementSubscriptionDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementSubscriptionDataType"
        },
        {
            "name": "node_management_subscription_delete_call",
            "xml_name": "nodeManagementSubscriptionDeleteCall",
            "type": "ns_p:NodeManagementSubscriptionDeleteCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementSubscriptionDeleteCallType"
        },
        {
            "name": "node_management_subscription_request_call",
            "xml_name": "nodeManagementSubscriptionRequestCall",
            "type": "ns_p:NodeManagementSubscriptionRequestCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementSubscriptionRequestCallType"
        },
        {
            "name": "node_management_use_case_data",
            "xml_name": "nodeManagementUseCaseData",
            "type": "ns_p:NodeManagementUseCaseDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementUseCaseDataType"
        },
        {
            "name": "operating_constraints_duration_list_data",
            "xml_name": "operatingConstraintsDurationListData",
            "type": "ns_p:OperatingConstraintsDurationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsDurationListDataType"
        },
        {
            "name": "operating_constraints_interrupt_list_data",
            "xml_name": "operatingConstraintsInterruptListData",
            "type": "ns_p:OperatingConstraintsInterruptListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsInterruptListDataType"
        },
        {
            "name": "operating_constraints_power_description_list_data",
            "xml_name": "operatingConstraintsPowerDescriptionListData",
            "type": "ns_p:OperatingConstraintsPowerDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsPowerDescriptionListDataType"
        },
        {
            "name": "operating_constraints_power_level_list_data",
            "xml_name": "operatingConstraintsPowerLevelListData",
            "type": "ns_p:OperatingConstraintsPowerLevelListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsPowerLevelListDataType"
        },
        {
            "name": "operating_constraints_power_range_list_data",
            "xml_name": "operatingConstraintsPowerRangeListData",
            "type": "ns_p:OperatingConstraintsPowerRangeListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsPowerRangeListDataType"
        },
        {
            "name": "operating_constraints_resume_implication_list_data",
            "xml_name": "operatingConstraintsResumeImplicationListData",
            "type": "ns_p:OperatingConstraintsResumeImplicationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsResumeImplicationListDataType"
        },
        {
            "name": "power_sequence_alternatives_relation_list_data",
            "xml_name": "powerSequenceAlternativesRelationListData",
            "type": "ns_p:PowerSequenceAlternativesRelationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceAlternativesRelationListDataType"
        },
        {
            "name": "power_sequence_description_list_data",
            "xml_name": "powerSequenceDescriptionListData",
            "type": "ns_p:PowerSequenceDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceDescriptionListDataType"
        },
        {
            "name": "power_sequence_node_schedule_information_data",
            "xml_name": "powerSequenceNodeScheduleInformationData",
            "type": "ns_p:PowerSequenceNodeScheduleInformationDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceNodeScheduleInformationDataType"
        },
        {
            "name": "power_sequence_price_calculation_request_call",
            "xml_name": "powerSequencePriceCalculationRequestCall",
            "type": "ns_p:PowerSequencePriceCalculationRequestCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequencePriceCalculationRequestCallType"
        },
        {
            "name": "power_sequence_price_list_data",
            "xml_name": "powerSequencePriceListData",
            "type": "ns_p:PowerSequencePriceListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequencePriceListDataType"
        },
        {
            "name": "power_sequence_schedule_configuration_request_call",
            "xml_name": "powerSequenceScheduleConfigurationRequestCall",
            "type": "ns_p:PowerSequenceScheduleConfigurationRequestCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceScheduleConfigurationRequestCallType"
        },
        {
            "name": "power_sequence_schedule_constraints_list_data",
            "xml_name": "powerSequenceScheduleConstraintsListData",
            "type": "ns_p:PowerSequenceScheduleConstraintsListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceScheduleConstraintsListDataType"
        },
        {
            "name": "power_sequence_schedule_list_data",
            "xml_name": "powerSequenceScheduleListData",
            "type": "ns_p:PowerSequenceScheduleListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceScheduleListDataType"
        },
        {
            "name": "power_sequence_schedule_preference_list_data",
            "xml_name": "powerSequenceSchedulePreferenceListData",
            "type": "ns_p:PowerSequenceSchedulePreferenceListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceSchedulePreferenceListDataType"
        },
        {
            "name": "power_sequence_state_list_data",
            "xml_name": "powerSequenceStateListData",
            "type": "ns_p:PowerSequenceStateListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceStateListDataType"
        },
        {
            "name": "power_time_slot_schedule_constraints_list_data",
            "xml_name": "powerTimeSlotScheduleConstraintsListData",
            "type": "ns_p:PowerTimeSlotScheduleConstraintsListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotScheduleConstraintsListDataType"
        },
        {
            "name": "power_time_slot_schedule_list_data",
            "xml_name": "powerTimeSlotScheduleListData",
            "type": "ns_p:PowerTimeSlotScheduleListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotScheduleListDataType"
        },
        {
            "name": "power_time_slot_value_list_data",
            "xml_name": "powerTimeSlotValueListData",
            "type": "ns_p:PowerTimeSlotValueListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotValueListDataType"
        },
        {
            "name": "result_data",
            "xml_name": "resultData",
            "type": "ns_p:ResultDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ResultDataType"
        },
        {
            "name": "sensing_description_data",
            "xml_name": "sensingDescriptionData",
            "type": "ns_p:SensingDescriptionDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SensingDescriptionDataType"
        },
        {
            "name": "sensing_list_data",
            "xml_name": "sensingListData",
            "type": "ns_p:SensingListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SensingListDataType"
        },
        {
            "name": "session_identification_list_data",
            "xml_name": "sessionIdentificationListData",
            "type": "ns_p:SessionIdentificationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SessionIdentificationListDataType"
        },
        {
            "name": "session_measurement_relation_list_data",
            "xml_name": "sessionMeasurementRelationListData",
            "type": "ns_p:SessionMeasurementRelationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SessionMeasurementRelationListDataType"
        },
        {
            "name": "setpoint_constraints_list_data",
            "xml_name": "setpointConstraintsListData",
            "type": "ns_p:SetpointConstraintsListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointConstraintsListDataType"
        },
        {
            "name": "setpoint_description_list_data",
            "xml_name": "setpointDescriptionListData",
            "type": "ns_p:SetpointDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointDescriptionListDataType"
        },
        {
            "name": "setpoint_list_data",
            "xml_name": "setpointListData",
            "type": "ns_p:SetpointListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointListDataType"
        },
        {
            "name": "smart_energy_management_ps_configuration_request_call",
            "xml_name": "smartEnergyManagementPsConfigurationRequestCall",
            "type": "ns_p:SmartEnergyManagementPsConfigurationRequestCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsConfigurationRequestCallType"
        },
        {
            "name": "smart_energy_management_ps_data",
            "xml_name": "smartEnergyManagementPsData",
            "type": "ns_p:SmartEnergyManagementPsDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsDataType"
        },
        {
            "name": "smart_energy_management_ps_price_calculation_request_call",
            "xml_name": "smartEnergyManagementPsPriceCalculationRequestCall",
            "type": "ns_p:SmartEnergyManagementPsPriceCalculationRequestCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsPriceCalculationRequestCallType"
        },
        {
            "name": "smart_energy_management_ps_price_data",
            "xml_name": "smartEnergyManagementPsPriceData",
            "type": "ns_p:SmartEnergyManagementPsPriceDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsPriceDataType"
        },
        {
            "name": "specification_version_list_data",
            "xml_name": "specificationVersionListData",
            "type": "ns_p:SpecificationVersionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SpecificationVersionListDataType"
        },
        {
            "name": "state_information_list_data",
            "xml_name": "stateInformationListData",
            "type": "ns_p:StateInformationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "StateInformationListDataType"
        },
        {
            "name": "subscription_management_delete_call",
            "xml_name": "subscriptionManagementDeleteCall",
            "type": "ns_p:SubscriptionManagementDeleteCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SubscriptionManagementDeleteCallType"
        },
        {
            "name": "subscription_management_entry_list_data",
            "xml_name": "subscriptionManagementEntryListData",
            "type": "ns_p:SubscriptionManagementEntryListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SubscriptionManagementEntryListDataType"
        },
        {
            "name": "subscription_management_request_call",
            "xml_name": "subscriptionManagementRequestCall",
            "type": "ns_p:SubscriptionManagementRequestCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SubscriptionManagementRequestCallType"
        },
        {
            "name": "supply_condition_description_list_data",
            "xml_name": "supplyConditionDescriptionListData",
            "type": "ns_p:SupplyConditionDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionDescriptionListDataType"
        },
        {
            "name": "supply_condition_list_data",
            "xml_name": "supplyConditionListData",
            "type": "ns_p:SupplyConditionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionListDataType"
        },
        {
            "name": "supply_condition_threshold_relation_list_data",
            "xml_name": "supplyConditionThresholdRelationListData",
            "type": "ns_p:SupplyConditionThresholdRelationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionThresholdRelationListDataType"
        },
        {
            "name": "tariff_boundary_relation_list_data",
            "xml_name": "tariffBoundaryRelationListData",
            "type": "ns_p:TariffBoundaryRelationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffBoundaryRelationListDataType"
        },
        {
            "name": "tariff_description_list_data",
            "xml_name": "tariffDescriptionListData",
            "type": "ns_p:TariffDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffDescriptionListDataType"
        },
        {
            "name": "tariff_list_data",
            "xml_name": "tariffListData",
            "type": "ns_p:TariffListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffListDataType"
        },
        {
            "name": "tariff_overall_constraints_data",
            "xml_name": "tariffOverallConstraintsData",
            "type": "ns_p:TariffOverallConstraintsDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffOverallConstraintsDataType"
        },
        {
            "name": "tariff_tier_relation_list_data",
            "xml_name": "tariffTierRelationListData",
            "type": "ns_p:TariffTierRelationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffTierRelationListDataType"
        },
        {
            "name": "task_management_job_description_list_data",
            "xml_name": "taskManagementJobDescriptionListData",
            "type": "ns_p:TaskManagementJobDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobDescriptionListDataType"
        },
        {
            "name": "task_management_job_list_data",
            "xml_name": "taskManagementJobListData",
            "type": "ns_p:TaskManagementJobListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobListDataType"
        },
        {
            "name": "task_management_job_relation_list_data",
            "xml_name": "taskManagementJobRelationListData",
            "type": "ns_p:TaskManagementJobRelationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobRelationListDataType"
        },
        {
            "name": "task_management_overview_data",
            "xml_name": "taskManagementOverviewData",
            "type": "ns_p:TaskManagementOverviewDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementOverviewDataType"
        },
        {
            "name": "threshold_constraints_list_data",
            "xml_name": "thresholdConstraintsListData",
            "type": "ns_p:ThresholdConstraintsListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdConstraintsListDataType"
        },
        {
            "name": "threshold_description_list_data",
            "xml_name": "thresholdDescriptionListData",
            "type": "ns_p:ThresholdDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdDescriptionListDataType"
        },
        {
            "name": "threshold_list_data",
            "xml_name": "thresholdListData",
            "type": "ns_p:ThresholdListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdListDataType"
        },
        {
            "name": "tier_boundary_description_list_data",
            "xml_name": "tierBoundaryDescriptionListData",
            "type": "ns_p:TierBoundaryDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryDescriptionListDataType"
        },
        {
            "name": "tier_boundary_list_data",
            "xml_name": "tierBoundaryListData",
            "type": "ns_p:TierBoundaryListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryListDataType"
        },
        {
            "name": "tier_description_list_data",
            "xml_name": "tierDescriptionListData",
            "type": "ns_p:TierDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierDescriptionListDataType"
        },
        {
            "name": "tier_incentive_relation_list_data",
            "xml_name": "tierIncentiveRelationListData",
            "type": "ns_p:TierIncentiveRelationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIncentiveRelationListDataType"
        },
        {
            "name": "tier_list_data",
            "xml_name": "tierListData",
            "type": "ns_p:TierListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierListDataType"
        },
        {
            "name": "time_distributor_data",
            "xml_name": "timeDistributorData",
            "type": "ns_p:TimeDistributorDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeDistributorDataType"
        },
        {
            "name": "time_distributor_enquiry_call",
            "xml_name": "timeDistributorEnquiryCall",
            "type": "ns_p:TimeDistributorEnquiryCallType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeDistributorEnquiryCallType"
        },
        {
            "name": "time_information_data",
            "xml_name": "timeInformationData",
            "type": "ns_p:TimeInformationDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeInformationDataType"
        },
        {
            "name": "time_precision_data",
            "xml_name": "timePrecisionData",
            "type": "ns_p:TimePrecisionDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePrecisionDataType"
        },
        {
            "name": "time_series_constraints_list_data",
            "xml_name": "timeSeriesConstraintsListData",
            "type": "ns_p:TimeSeriesConstraintsListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesConstraintsListDataType"
        },
        {
            "name": "time_series_description_list_data",
            "xml_name": "timeSeriesDescriptionListData",
            "type": "ns_p:TimeSeriesDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesDescriptionListDataType"
        },
        {
            "name": "time_series_list_data",
            "xml_name": "timeSeriesListData",
            "type": "ns_p:TimeSeriesListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesListDataType"
        },
        {
            "name": "time_table_constraints_list_data",
            "xml_name": "timeTableConstraintsListData",
            "type": "ns_p:TimeTableConstraintsListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableConstraintsListDataType"
        },
        {
            "name": "time_table_description_list_data",
            "xml_name": "timeTableDescriptionListData",
            "type": "ns_p:TimeTableDescriptionListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableDescriptionListDataType"
        },
        {
            "name": "time_table_list_data",
            "xml_name": "timeTableListData",
            "type": "ns_p:TimeTableListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableListDataType"
        },
        {
            "name": "use_case_information_list_data",
            "xml_name": "useCaseInformationListData",
            "type": "ns_p:UseCaseInformationListDataType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UseCaseInformationListDataType"
        },
        {
            "name": "manufacturer_specific_extension",
            "xml_name": "manufacturerSpecificExtension",
            "type": "xs:hexBinary",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "last_update_at",
            "xml_name": "lastUpdateAt",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
    ]


@spine_type('ns_p:DataExtendGroup', is_value_type=False, no_attrib_name=False)
class DataExtendGroup(SpineBase): # EEBus_SPINE_TS_CommandFrame.xsd:ns_p:DataExtendGroup -> ChoiceType
    _MEMBER_INFO = [
        {
            "name": "manufacturer_specific_extension",
            "xml_name": "manufacturerSpecificExtension",
            "type": "xs:hexBinary",
            "is_array": False,
            "is_optional": True,
            "class_check": "str"
        },
        {
            "name": "last_update_at",
            "xml_name": "lastUpdateAt",
            "type": "ns_p:AbsoluteOrRelativeTimeType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AbsoluteOrRelativeTimeType"
        },
    ]


@spine_type('ns_p:CmdOptionGroup', is_value_type=False, no_attrib_name=False)
class CmdOptionGroup(SpineBase): # EEBus_SPINE_TS_CommandFrame.xsd:ns_p:CmdOptionGroup -> ChoiceType
    _MEMBER_INFO = [
        {
            "name": "function",
            "xml_name": "function",
            "type": "ns_p:FunctionType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FunctionType"
        },
        {
            "name": "filter",
            "xml_name": "filter",
            "type": "ns_p:FilterType",
            "is_array": True,
            "is_optional": True,
            "class_check": "list"
        },
    ]

