# Jinja Template message_type.py.jinja2
from __future__ import annotations
from typing import TYPE_CHECKING
from spine.base import SpineBase, spine_type
from spine.type_registry import TypeRegistry

if TYPE_CHECKING:
    from spine.base_type.actuatorlevel import ActuatorLevelDataElementsType
    from spine.base_type.actuatorlevel import ActuatorLevelDescriptionDataElementsType
    from spine.base_type.actuatorswitch import ActuatorSwitchDataElementsType
    from spine.base_type.actuatorswitch import ActuatorSwitchDescriptionDataElementsType
    from spine.base_type.alarm import AlarmDataElementsType
    from spine.base_type.alarm import AlarmListDataSelectorsType
    from spine.base_type.bill import BillConstraintsDataElementsType
    from spine.base_type.bill import BillConstraintsListDataSelectorsType
    from spine.base_type.bill import BillDataElementsType
    from spine.base_type.bill import BillDescriptionDataElementsType
    from spine.base_type.bill import BillDescriptionListDataSelectorsType
    from spine.base_type.bill import BillListDataSelectorsType
    from spine.base_type.bindingmanagement import BindingManagementDeleteCallElementsType
    from spine.base_type.bindingmanagement import BindingManagementEntryDataElementsType
    from spine.base_type.bindingmanagement import BindingManagementEntryListDataSelectorsType
    from spine.base_type.bindingmanagement import BindingManagementRequestCallElementsType
    from spine.base_type.commondatatypes import ElementTagType
    from spine.base_type.datatunneling import DataTunnelingCallElementsType
    from spine.base_type.deviceclassification import DeviceClassificationManufacturerDataElementsType
    from spine.base_type.deviceclassification import DeviceClassificationUserDataElementsType
    from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueConstraintsDataElementsType
    from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueConstraintsListDataSelectorsType
    from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueDataElementsType
    from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueDescriptionDataElementsType
    from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueDescriptionListDataSelectorsType
    from spine.base_type.deviceconfiguration import DeviceConfigurationKeyValueListDataSelectorsType
    from spine.base_type.devicediagnosis import DeviceDiagnosisHeartbeatDataElementsType
    from spine.base_type.devicediagnosis import DeviceDiagnosisServiceDataElementsType
    from spine.base_type.devicediagnosis import DeviceDiagnosisStateDataElementsType
    from spine.base_type.directcontrol import DirectControlActivityDataElementsType
    from spine.base_type.directcontrol import DirectControlActivityListDataSelectorsType
    from spine.base_type.directcontrol import DirectControlDescriptionDataElementsType
    from spine.base_type.electricalconnection import ElectricalConnectionCharacteristicDataElementsType
    from spine.base_type.electricalconnection import ElectricalConnectionCharacteristicListDataSelectorsType
    from spine.base_type.electricalconnection import ElectricalConnectionDescriptionDataElementsType
    from spine.base_type.electricalconnection import ElectricalConnectionDescriptionListDataSelectorsType
    from spine.base_type.electricalconnection import ElectricalConnectionParameterDescriptionDataElementsType
    from spine.base_type.electricalconnection import ElectricalConnectionParameterDescriptionListDataSelectorsType
    from spine.base_type.electricalconnection import ElectricalConnectionPermittedValueSetDataElementsType
    from spine.base_type.electricalconnection import ElectricalConnectionPermittedValueSetListDataSelectorsType
    from spine.base_type.electricalconnection import ElectricalConnectionStateDataElementsType
    from spine.base_type.electricalconnection import ElectricalConnectionStateListDataSelectorsType
    from spine.base_type.hvac import HvacOperationModeDescriptionDataElementsType
    from spine.base_type.hvac import HvacOperationModeDescriptionListDataSelectorsType
    from spine.base_type.hvac import HvacOverrunDataElementsType
    from spine.base_type.hvac import HvacOverrunDescriptionDataElementsType
    from spine.base_type.hvac import HvacOverrunDescriptionListDataSelectorsType
    from spine.base_type.hvac import HvacOverrunListDataSelectorsType
    from spine.base_type.hvac import HvacSystemFunctionDataElementsType
    from spine.base_type.hvac import HvacSystemFunctionDescriptionDataElementsType
    from spine.base_type.hvac import HvacSystemFunctionDescriptionListDataSelectorsType
    from spine.base_type.hvac import HvacSystemFunctionListDataSelectorsType
    from spine.base_type.hvac import HvacSystemFunctionOperationModeRelationDataElementsType
    from spine.base_type.hvac import HvacSystemFunctionOperationModeRelationListDataSelectorsType
    from spine.base_type.hvac import HvacSystemFunctionPowerSequenceRelationDataElementsType
    from spine.base_type.hvac import HvacSystemFunctionPowerSequenceRelationListDataSelectorsType
    from spine.base_type.hvac import HvacSystemFunctionSetpointRelationDataElementsType
    from spine.base_type.hvac import HvacSystemFunctionSetpointRelationListDataSelectorsType
    from spine.base_type.identification import IdentificationDataElementsType
    from spine.base_type.identification import IdentificationListDataSelectorsType
    from spine.base_type.identification import SessionIdentificationDataElementsType
    from spine.base_type.identification import SessionIdentificationListDataSelectorsType
    from spine.base_type.identification import SessionMeasurementRelationDataElementsType
    from spine.base_type.identification import SessionMeasurementRelationListDataSelectorsType
    from spine.base_type.incentivetable import IncentiveTableConstraintsDataElementsType
    from spine.base_type.incentivetable import IncentiveTableConstraintsDataSelectorsType
    from spine.base_type.incentivetable import IncentiveTableDataElementsType
    from spine.base_type.incentivetable import IncentiveTableDataSelectorsType
    from spine.base_type.incentivetable import IncentiveTableDescriptionDataElementsType
    from spine.base_type.incentivetable import IncentiveTableDescriptionDataSelectorsType
    from spine.base_type.loadcontrol import LoadControlEventDataElementsType
    from spine.base_type.loadcontrol import LoadControlEventListDataSelectorsType
    from spine.base_type.loadcontrol import LoadControlLimitConstraintsDataElementsType
    from spine.base_type.loadcontrol import LoadControlLimitConstraintsListDataSelectorsType
    from spine.base_type.loadcontrol import LoadControlLimitDataElementsType
    from spine.base_type.loadcontrol import LoadControlLimitDescriptionDataElementsType
    from spine.base_type.loadcontrol import LoadControlLimitDescriptionListDataSelectorsType
    from spine.base_type.loadcontrol import LoadControlLimitListDataSelectorsType
    from spine.base_type.loadcontrol import LoadControlNodeDataElementsType
    from spine.base_type.loadcontrol import LoadControlStateDataElementsType
    from spine.base_type.loadcontrol import LoadControlStateListDataSelectorsType
    from spine.base_type.measurement import MeasurementConstraintsDataElementsType
    from spine.base_type.measurement import MeasurementConstraintsListDataSelectorsType
    from spine.base_type.measurement import MeasurementDataElementsType
    from spine.base_type.measurement import MeasurementDescriptionDataElementsType
    from spine.base_type.measurement import MeasurementDescriptionListDataSelectorsType
    from spine.base_type.measurement import MeasurementListDataSelectorsType
    from spine.base_type.measurement import MeasurementSeriesDataElementsType
    from spine.base_type.measurement import MeasurementSeriesListDataSelectorsType
    from spine.base_type.measurement import MeasurementThresholdRelationDataElementsType
    from spine.base_type.measurement import MeasurementThresholdRelationListDataSelectorsType
    from spine.base_type.messaging import MessagingDataElementsType
    from spine.base_type.messaging import MessagingListDataSelectorsType
    from spine.base_type.networkmanagement import NetworkManagementAbortCallElementsType
    from spine.base_type.networkmanagement import NetworkManagementAddNodeCallElementsType
    from spine.base_type.networkmanagement import NetworkManagementDeviceDescriptionDataElementsType
    from spine.base_type.networkmanagement import NetworkManagementDeviceDescriptionListDataSelectorsType
    from spine.base_type.networkmanagement import NetworkManagementDiscoverCallElementsType
    from spine.base_type.networkmanagement import NetworkManagementEntityDescriptionDataElementsType
    from spine.base_type.networkmanagement import NetworkManagementEntityDescriptionListDataSelectorsType
    from spine.base_type.networkmanagement import NetworkManagementFeatureDescriptionDataElementsType
    from spine.base_type.networkmanagement import NetworkManagementFeatureDescriptionListDataSelectorsType
    from spine.base_type.networkmanagement import NetworkManagementJoiningModeDataElementsType
    from spine.base_type.networkmanagement import NetworkManagementModifyNodeCallElementsType
    from spine.base_type.networkmanagement import NetworkManagementProcessStateDataElementsType
    from spine.base_type.networkmanagement import NetworkManagementRemoveNodeCallElementsType
    from spine.base_type.networkmanagement import NetworkManagementReportCandidateDataElementsType
    from spine.base_type.networkmanagement import NetworkManagementScanNetworkCallElementsType
    from spine.base_type.nodemanagement import NodeManagementBindingDataElementsType
    from spine.base_type.nodemanagement import NodeManagementBindingDataSelectorsType
    from spine.base_type.nodemanagement import NodeManagementBindingDeleteCallElementsType
    from spine.base_type.nodemanagement import NodeManagementBindingRequestCallElementsType
    from spine.base_type.nodemanagement import NodeManagementDestinationDataElementsType
    from spine.base_type.nodemanagement import NodeManagementDestinationListDataSelectorsType
    from spine.base_type.nodemanagement import NodeManagementDetailedDiscoveryDataElementsType
    from spine.base_type.nodemanagement import NodeManagementDetailedDiscoveryDataSelectorsType
    from spine.base_type.nodemanagement import NodeManagementSubscriptionDataElementsType
    from spine.base_type.nodemanagement import NodeManagementSubscriptionDataSelectorsType
    from spine.base_type.nodemanagement import NodeManagementSubscriptionDeleteCallElementsType
    from spine.base_type.nodemanagement import NodeManagementSubscriptionRequestCallElementsType
    from spine.base_type.nodemanagement import NodeManagementUseCaseDataElementsType
    from spine.base_type.nodemanagement import NodeManagementUseCaseDataSelectorsType
    from spine.base_type.operatingconstraints import OperatingConstraintsDurationDataElementsType
    from spine.base_type.operatingconstraints import OperatingConstraintsDurationListDataSelectorsType
    from spine.base_type.operatingconstraints import OperatingConstraintsInterruptDataElementsType
    from spine.base_type.operatingconstraints import OperatingConstraintsInterruptListDataSelectorsType
    from spine.base_type.operatingconstraints import OperatingConstraintsPowerDescriptionDataElementsType
    from spine.base_type.operatingconstraints import OperatingConstraintsPowerDescriptionListDataSelectorsType
    from spine.base_type.operatingconstraints import OperatingConstraintsPowerLevelDataElementsType
    from spine.base_type.operatingconstraints import OperatingConstraintsPowerLevelListDataSelectorsType
    from spine.base_type.operatingconstraints import OperatingConstraintsPowerRangeDataElementsType
    from spine.base_type.operatingconstraints import OperatingConstraintsPowerRangeListDataSelectorsType
    from spine.base_type.operatingconstraints import OperatingConstraintsResumeImplicationDataElementsType
    from spine.base_type.operatingconstraints import OperatingConstraintsResumeImplicationListDataSelectorsType
    from spine.base_type.powersequences import PowerSequenceAlternativesRelationDataElementsType
    from spine.base_type.powersequences import PowerSequenceAlternativesRelationListDataSelectorsType
    from spine.base_type.powersequences import PowerSequenceDescriptionDataElementsType
    from spine.base_type.powersequences import PowerSequenceDescriptionListDataSelectorsType
    from spine.base_type.powersequences import PowerSequenceNodeScheduleInformationDataElementsType
    from spine.base_type.powersequences import PowerSequencePriceCalculationRequestCallElementsType
    from spine.base_type.powersequences import PowerSequencePriceDataElementsType
    from spine.base_type.powersequences import PowerSequencePriceListDataSelectorsType
    from spine.base_type.powersequences import PowerSequenceScheduleConfigurationRequestCallElementsType
    from spine.base_type.powersequences import PowerSequenceScheduleConstraintsDataElementsType
    from spine.base_type.powersequences import PowerSequenceScheduleConstraintsListDataSelectorsType
    from spine.base_type.powersequences import PowerSequenceScheduleDataElementsType
    from spine.base_type.powersequences import PowerSequenceScheduleListDataSelectorsType
    from spine.base_type.powersequences import PowerSequenceSchedulePreferenceDataElementsType
    from spine.base_type.powersequences import PowerSequenceSchedulePreferenceListDataSelectorsType
    from spine.base_type.powersequences import PowerSequenceStateDataElementsType
    from spine.base_type.powersequences import PowerSequenceStateListDataSelectorsType
    from spine.base_type.powersequences import PowerTimeSlotScheduleConstraintsDataElementsType
    from spine.base_type.powersequences import PowerTimeSlotScheduleConstraintsListDataSelectorsType
    from spine.base_type.powersequences import PowerTimeSlotScheduleDataElementsType
    from spine.base_type.powersequences import PowerTimeSlotScheduleListDataSelectorsType
    from spine.base_type.powersequences import PowerTimeSlotValueDataElementsType
    from spine.base_type.powersequences import PowerTimeSlotValueListDataSelectorsType
    from spine.base_type.sensing import SensingDataElementsType
    from spine.base_type.sensing import SensingDescriptionDataElementsType
    from spine.base_type.sensing import SensingListDataSelectorsType
    from spine.base_type.setpoint import SetpointConstraintsDataElementsType
    from spine.base_type.setpoint import SetpointConstraintsListDataSelectorsType
    from spine.base_type.setpoint import SetpointDataElementsType
    from spine.base_type.setpoint import SetpointDescriptionDataElementsType
    from spine.base_type.setpoint import SetpointDescriptionListDataSelectorsType
    from spine.base_type.setpoint import SetpointListDataSelectorsType
    from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsConfigurationRequestCallElementsType
    from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsDataElementsType
    from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsDataSelectorsType
    from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsPriceCalculationRequestCallElementsType
    from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsPriceDataElementsType
    from spine.base_type.smartenergymanagementps import SmartEnergyManagementPsPriceDataSelectorsType
    from spine.base_type.stateinformation import StateInformationDataElementsType
    from spine.base_type.stateinformation import StateInformationListDataSelectorsType
    from spine.base_type.subscriptionmanagement import SubscriptionManagementDeleteCallElementsType
    from spine.base_type.subscriptionmanagement import SubscriptionManagementEntryDataElementsType
    from spine.base_type.subscriptionmanagement import SubscriptionManagementEntryListDataSelectorsType
    from spine.base_type.subscriptionmanagement import SubscriptionManagementRequestCallElementsType
    from spine.base_type.supplycondition import SupplyConditionDataElementsType
    from spine.base_type.supplycondition import SupplyConditionDescriptionDataElementsType
    from spine.base_type.supplycondition import SupplyConditionDescriptionListDataSelectorsType
    from spine.base_type.supplycondition import SupplyConditionListDataSelectorsType
    from spine.base_type.supplycondition import SupplyConditionThresholdRelationDataElementsType
    from spine.base_type.supplycondition import SupplyConditionThresholdRelationListDataSelectorsType
    from spine.base_type.tariffinformation import CommodityDataElementsType
    from spine.base_type.tariffinformation import CommodityListDataSelectorsType
    from spine.base_type.tariffinformation import IncentiveDataElementsType
    from spine.base_type.tariffinformation import IncentiveDescriptionDataElementsType
    from spine.base_type.tariffinformation import IncentiveDescriptionListDataSelectorsType
    from spine.base_type.tariffinformation import IncentiveListDataSelectorsType
    from spine.base_type.tariffinformation import TariffBoundaryRelationDataElementsType
    from spine.base_type.tariffinformation import TariffBoundaryRelationListDataSelectorsType
    from spine.base_type.tariffinformation import TariffDataElementsType
    from spine.base_type.tariffinformation import TariffDescriptionDataElementsType
    from spine.base_type.tariffinformation import TariffDescriptionListDataSelectorsType
    from spine.base_type.tariffinformation import TariffListDataSelectorsType
    from spine.base_type.tariffinformation import TariffOverallConstraintsDataElementsType
    from spine.base_type.tariffinformation import TariffTierRelationDataElementsType
    from spine.base_type.tariffinformation import TariffTierRelationListDataSelectorsType
    from spine.base_type.tariffinformation import TierBoundaryDataElementsType
    from spine.base_type.tariffinformation import TierBoundaryDescriptionDataElementsType
    from spine.base_type.tariffinformation import TierBoundaryDescriptionListDataSelectorsType
    from spine.base_type.tariffinformation import TierBoundaryListDataSelectorsType
    from spine.base_type.tariffinformation import TierDataElementsType
    from spine.base_type.tariffinformation import TierDescriptionDataElementsType
    from spine.base_type.tariffinformation import TierDescriptionListDataSelectorsType
    from spine.base_type.tariffinformation import TierIncentiveRelationDataElementsType
    from spine.base_type.tariffinformation import TierIncentiveRelationListDataSelectorsType
    from spine.base_type.tariffinformation import TierListDataSelectorsType
    from spine.base_type.taskmanagement import TaskManagementJobDataElementsType
    from spine.base_type.taskmanagement import TaskManagementJobDescriptionDataElementsType
    from spine.base_type.taskmanagement import TaskManagementJobDescriptionListDataSelectorsType
    from spine.base_type.taskmanagement import TaskManagementJobListDataSelectorsType
    from spine.base_type.taskmanagement import TaskManagementJobRelationDataElementsType
    from spine.base_type.taskmanagement import TaskManagementJobRelationListDataSelectorsType
    from spine.base_type.taskmanagement import TaskManagementOverviewDataElementsType
    from spine.base_type.threshold import ThresholdConstraintsDataElementsType
    from spine.base_type.threshold import ThresholdConstraintsListDataSelectorsType
    from spine.base_type.threshold import ThresholdDataElementsType
    from spine.base_type.threshold import ThresholdDescriptionDataElementsType
    from spine.base_type.threshold import ThresholdDescriptionListDataSelectorsType
    from spine.base_type.threshold import ThresholdListDataSelectorsType
    from spine.base_type.timeinformation import TimeDistributorDataElementsType
    from spine.base_type.timeinformation import TimeDistributorEnquiryCallElementsType
    from spine.base_type.timeinformation import TimeInformationDataElementsType
    from spine.base_type.timeinformation import TimePrecisionDataElementsType
    from spine.base_type.timeseries import TimeSeriesConstraintsDataElementsType
    from spine.base_type.timeseries import TimeSeriesConstraintsListDataSelectorsType
    from spine.base_type.timeseries import TimeSeriesDataElementsType
    from spine.base_type.timeseries import TimeSeriesDescriptionDataElementsType
    from spine.base_type.timeseries import TimeSeriesDescriptionListDataSelectorsType
    from spine.base_type.timeseries import TimeSeriesListDataSelectorsType
    from spine.base_type.timetable import TimeTableConstraintsDataElementsType
    from spine.base_type.timetable import TimeTableConstraintsListDataSelectorsType
    from spine.base_type.timetable import TimeTableDataElementsType
    from spine.base_type.timetable import TimeTableDescriptionDataElementsType
    from spine.base_type.timetable import TimeTableDescriptionListDataSelectorsType
    from spine.base_type.timetable import TimeTableListDataSelectorsType
    from spine.base_type.usecaseinformation import UseCaseInformationDataElementsType
    from spine.base_type.usecaseinformation import UseCaseInformationListDataSelectorsType
    from spine.base_type.version import SpecificationVersionDataElementsType
    from spine.base_type.version import SpecificationVersionListDataSelectorsType
    from spine.choice_type.commandcommondefinitions import DataElementsChoiceGroup
    from spine.choice_type.commandcommondefinitions import DataSelectorsChoiceGroup
    from spine.choice_type.commandframe import PayloadContributionGroup
    from spine.simple_type.commandframe import FilterIdType



@spine_type('ns_p:CmdControlType', is_value_type=False, no_attrib_name=False)
class CmdControlType(SpineBase): # EEBus_SPINE_TS_CommandFrame.xsd:ns_p:CmdControlType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "delete",
            "xml_name": "delete",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "partial",
            "xml_name": "partial",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
    ]


@spine_type('ns_p:CmdType', is_value_type=False, no_attrib_name=False)
class CmdType(SpineBase): # EEBus_SPINE_TS_CommandFrame.xsd:ns_p:CmdType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "payload_contribution_group",
            "xml_name": "payload_contribution_group",
            "type": "ns_p:PayloadContributionGroup",
            "is_array": False,
            "is_optional": True,
            "class_check": "PayloadContributionGroup"
        },
    ]


@spine_type('ns_p:FilterType', is_value_type=False, no_attrib_name=False)
class FilterType(SpineBase): # EEBus_SPINE_TS_CommandFrame.xsd:ns_p:FilterType -> ComplexType
    _MEMBER_INFO = [
        {
            "name": "filter_id",
            "xml_name": "filterId",
            "type": "ns_p:FilterIdType",
            "is_array": False,
            "is_optional": True,
            "class_check": "FilterIdType"
        },
        {
            "name": "cmd_control",
            "xml_name": "cmdControl",
            "type": "ns_p:CmdControlType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CmdControlType"
        },
        {
            "name": "delete",
            "xml_name": "delete",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "partial",
            "xml_name": "partial",
            "type": "ns_p:ElementTagType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElementTagType"
        },
        {
            "name": "alarm_list_data_selectors",
            "xml_name": "alarmListDataSelectors",
            "type": "ns_p:AlarmListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AlarmListDataSelectorsType"
        },
        {
            "name": "bill_constraints_list_data_selectors",
            "xml_name": "billConstraintsListDataSelectors",
            "type": "ns_p:BillConstraintsListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillConstraintsListDataSelectorsType"
        },
        {
            "name": "bill_description_list_data_selectors",
            "xml_name": "billDescriptionListDataSelectors",
            "type": "ns_p:BillDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillDescriptionListDataSelectorsType"
        },
        {
            "name": "bill_list_data_selectors",
            "xml_name": "billListDataSelectors",
            "type": "ns_p:BillListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillListDataSelectorsType"
        },
        {
            "name": "binding_management_entry_list_data_selectors",
            "xml_name": "bindingManagementEntryListDataSelectors",
            "type": "ns_p:BindingManagementEntryListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BindingManagementEntryListDataSelectorsType"
        },
        {
            "name": "commodity_list_data_selectors",
            "xml_name": "commodityListDataSelectors",
            "type": "ns_p:CommodityListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CommodityListDataSelectorsType"
        },
        {
            "name": "device_configuration_key_value_constraints_list_data_selectors",
            "xml_name": "deviceConfigurationKeyValueConstraintsListDataSelectors",
            "type": "ns_p:DeviceConfigurationKeyValueConstraintsListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueConstraintsListDataSelectorsType"
        },
        {
            "name": "device_configuration_key_value_description_list_data_selectors",
            "xml_name": "deviceConfigurationKeyValueDescriptionListDataSelectors",
            "type": "ns_p:DeviceConfigurationKeyValueDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueDescriptionListDataSelectorsType"
        },
        {
            "name": "device_configuration_key_value_list_data_selectors",
            "xml_name": "deviceConfigurationKeyValueListDataSelectors",
            "type": "ns_p:DeviceConfigurationKeyValueListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueListDataSelectorsType"
        },
        {
            "name": "direct_control_activity_list_data_selectors",
            "xml_name": "directControlActivityListDataSelectors",
            "type": "ns_p:DirectControlActivityListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DirectControlActivityListDataSelectorsType"
        },
        {
            "name": "electrical_connection_characteristic_list_data_selectors",
            "xml_name": "electricalConnectionCharacteristicListDataSelectors",
            "type": "ns_p:ElectricalConnectionCharacteristicListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionCharacteristicListDataSelectorsType"
        },
        {
            "name": "electrical_connection_description_list_data_selectors",
            "xml_name": "electricalConnectionDescriptionListDataSelectors",
            "type": "ns_p:ElectricalConnectionDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionDescriptionListDataSelectorsType"
        },
        {
            "name": "electrical_connection_parameter_description_list_data_selectors",
            "xml_name": "electricalConnectionParameterDescriptionListDataSelectors",
            "type": "ns_p:ElectricalConnectionParameterDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionParameterDescriptionListDataSelectorsType"
        },
        {
            "name": "electrical_connection_permitted_value_set_list_data_selectors",
            "xml_name": "electricalConnectionPermittedValueSetListDataSelectors",
            "type": "ns_p:ElectricalConnectionPermittedValueSetListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionPermittedValueSetListDataSelectorsType"
        },
        {
            "name": "electrical_connection_state_list_data_selectors",
            "xml_name": "electricalConnectionStateListDataSelectors",
            "type": "ns_p:ElectricalConnectionStateListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionStateListDataSelectorsType"
        },
        {
            "name": "hvac_operation_mode_description_list_data_selectors",
            "xml_name": "hvacOperationModeDescriptionListDataSelectors",
            "type": "ns_p:HvacOperationModeDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOperationModeDescriptionListDataSelectorsType"
        },
        {
            "name": "hvac_overrun_description_list_data_selectors",
            "xml_name": "hvacOverrunDescriptionListDataSelectors",
            "type": "ns_p:HvacOverrunDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunDescriptionListDataSelectorsType"
        },
        {
            "name": "hvac_overrun_list_data_selectors",
            "xml_name": "hvacOverrunListDataSelectors",
            "type": "ns_p:HvacOverrunListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunListDataSelectorsType"
        },
        {
            "name": "hvac_system_function_description_list_data_selectors",
            "xml_name": "hvacSystemFunctionDescriptionListDataSelectors",
            "type": "ns_p:HvacSystemFunctionDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionDescriptionListDataSelectorsType"
        },
        {
            "name": "hvac_system_function_list_data_selectors",
            "xml_name": "hvacSystemFunctionListDataSelectors",
            "type": "ns_p:HvacSystemFunctionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionListDataSelectorsType"
        },
        {
            "name": "hvac_system_function_operation_mode_relation_list_data_selectors",
            "xml_name": "hvacSystemFunctionOperationModeRelationListDataSelectors",
            "type": "ns_p:HvacSystemFunctionOperationModeRelationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionOperationModeRelationListDataSelectorsType"
        },
        {
            "name": "hvac_system_function_power_sequence_relation_list_data_selectors",
            "xml_name": "hvacSystemFunctionPowerSequenceRelationListDataSelectors",
            "type": "ns_p:HvacSystemFunctionPowerSequenceRelationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionPowerSequenceRelationListDataSelectorsType"
        },
        {
            "name": "hvac_system_function_setpoint_relation_list_data_selectors",
            "xml_name": "hvacSystemFunctionSetpointRelationListDataSelectors",
            "type": "ns_p:HvacSystemFunctionSetpointRelationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionSetpointRelationListDataSelectorsType"
        },
        {
            "name": "identification_list_data_selectors",
            "xml_name": "identificationListDataSelectors",
            "type": "ns_p:IdentificationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationListDataSelectorsType"
        },
        {
            "name": "incentive_description_list_data_selectors",
            "xml_name": "incentiveDescriptionListDataSelectors",
            "type": "ns_p:IncentiveDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveDescriptionListDataSelectorsType"
        },
        {
            "name": "incentive_list_data_selectors",
            "xml_name": "incentiveListDataSelectors",
            "type": "ns_p:IncentiveListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveListDataSelectorsType"
        },
        {
            "name": "incentive_table_constraints_data_selectors",
            "xml_name": "incentiveTableConstraintsDataSelectors",
            "type": "ns_p:IncentiveTableConstraintsDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableConstraintsDataSelectorsType"
        },
        {
            "name": "incentive_table_data_selectors",
            "xml_name": "incentiveTableDataSelectors",
            "type": "ns_p:IncentiveTableDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableDataSelectorsType"
        },
        {
            "name": "incentive_table_description_data_selectors",
            "xml_name": "incentiveTableDescriptionDataSelectors",
            "type": "ns_p:IncentiveTableDescriptionDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableDescriptionDataSelectorsType"
        },
        {
            "name": "load_control_event_list_data_selectors",
            "xml_name": "loadControlEventListDataSelectors",
            "type": "ns_p:LoadControlEventListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventListDataSelectorsType"
        },
        {
            "name": "load_control_limit_constraints_list_data_selectors",
            "xml_name": "loadControlLimitConstraintsListDataSelectors",
            "type": "ns_p:LoadControlLimitConstraintsListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitConstraintsListDataSelectorsType"
        },
        {
            "name": "load_control_limit_description_list_data_selectors",
            "xml_name": "loadControlLimitDescriptionListDataSelectors",
            "type": "ns_p:LoadControlLimitDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitDescriptionListDataSelectorsType"
        },
        {
            "name": "load_control_limit_list_data_selectors",
            "xml_name": "loadControlLimitListDataSelectors",
            "type": "ns_p:LoadControlLimitListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitListDataSelectorsType"
        },
        {
            "name": "load_control_state_list_data_selectors",
            "xml_name": "loadControlStateListDataSelectors",
            "type": "ns_p:LoadControlStateListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlStateListDataSelectorsType"
        },
        {
            "name": "measurement_constraints_list_data_selectors",
            "xml_name": "measurementConstraintsListDataSelectors",
            "type": "ns_p:MeasurementConstraintsListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementConstraintsListDataSelectorsType"
        },
        {
            "name": "measurement_description_list_data_selectors",
            "xml_name": "measurementDescriptionListDataSelectors",
            "type": "ns_p:MeasurementDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementDescriptionListDataSelectorsType"
        },
        {
            "name": "measurement_list_data_selectors",
            "xml_name": "measurementListDataSelectors",
            "type": "ns_p:MeasurementListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementListDataSelectorsType"
        },
        {
            "name": "measurement_series_list_data_selectors",
            "xml_name": "measurementSeriesListDataSelectors",
            "type": "ns_p:MeasurementSeriesListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementSeriesListDataSelectorsType"
        },
        {
            "name": "measurement_threshold_relation_list_data_selectors",
            "xml_name": "measurementThresholdRelationListDataSelectors",
            "type": "ns_p:MeasurementThresholdRelationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementThresholdRelationListDataSelectorsType"
        },
        {
            "name": "messaging_list_data_selectors",
            "xml_name": "messagingListDataSelectors",
            "type": "ns_p:MessagingListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MessagingListDataSelectorsType"
        },
        {
            "name": "network_management_device_description_list_data_selectors",
            "xml_name": "networkManagementDeviceDescriptionListDataSelectors",
            "type": "ns_p:NetworkManagementDeviceDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementDeviceDescriptionListDataSelectorsType"
        },
        {
            "name": "network_management_entity_description_list_data_selectors",
            "xml_name": "networkManagementEntityDescriptionListDataSelectors",
            "type": "ns_p:NetworkManagementEntityDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementEntityDescriptionListDataSelectorsType"
        },
        {
            "name": "network_management_feature_description_list_data_selectors",
            "xml_name": "networkManagementFeatureDescriptionListDataSelectors",
            "type": "ns_p:NetworkManagementFeatureDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementFeatureDescriptionListDataSelectorsType"
        },
        {
            "name": "node_management_binding_data_selectors",
            "xml_name": "nodeManagementBindingDataSelectors",
            "type": "ns_p:NodeManagementBindingDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementBindingDataSelectorsType"
        },
        {
            "name": "node_management_destination_list_data_selectors",
            "xml_name": "nodeManagementDestinationListDataSelectors",
            "type": "ns_p:NodeManagementDestinationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementDestinationListDataSelectorsType"
        },
        {
            "name": "node_management_detailed_discovery_data_selectors",
            "xml_name": "nodeManagementDetailedDiscoveryDataSelectors",
            "type": "ns_p:NodeManagementDetailedDiscoveryDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementDetailedDiscoveryDataSelectorsType"
        },
        {
            "name": "node_management_subscription_data_selectors",
            "xml_name": "nodeManagementSubscriptionDataSelectors",
            "type": "ns_p:NodeManagementSubscriptionDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementSubscriptionDataSelectorsType"
        },
        {
            "name": "node_management_use_case_data_selectors",
            "xml_name": "nodeManagementUseCaseDataSelectors",
            "type": "ns_p:NodeManagementUseCaseDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementUseCaseDataSelectorsType"
        },
        {
            "name": "operating_constraints_duration_list_data_selectors",
            "xml_name": "operatingConstraintsDurationListDataSelectors",
            "type": "ns_p:OperatingConstraintsDurationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsDurationListDataSelectorsType"
        },
        {
            "name": "operating_constraints_interrupt_list_data_selectors",
            "xml_name": "operatingConstraintsInterruptListDataSelectors",
            "type": "ns_p:OperatingConstraintsInterruptListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsInterruptListDataSelectorsType"
        },
        {
            "name": "operating_constraints_power_description_list_data_selectors",
            "xml_name": "operatingConstraintsPowerDescriptionListDataSelectors",
            "type": "ns_p:OperatingConstraintsPowerDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsPowerDescriptionListDataSelectorsType"
        },
        {
            "name": "operating_constraints_power_level_list_data_selectors",
            "xml_name": "operatingConstraintsPowerLevelListDataSelectors",
            "type": "ns_p:OperatingConstraintsPowerLevelListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsPowerLevelListDataSelectorsType"
        },
        {
            "name": "operating_constraints_power_range_list_data_selectors",
            "xml_name": "operatingConstraintsPowerRangeListDataSelectors",
            "type": "ns_p:OperatingConstraintsPowerRangeListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsPowerRangeListDataSelectorsType"
        },
        {
            "name": "operating_constraints_resume_implication_list_data_selectors",
            "xml_name": "operatingConstraintsResumeImplicationListDataSelectors",
            "type": "ns_p:OperatingConstraintsResumeImplicationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsResumeImplicationListDataSelectorsType"
        },
        {
            "name": "power_sequence_alternatives_relation_list_data_selectors",
            "xml_name": "powerSequenceAlternativesRelationListDataSelectors",
            "type": "ns_p:PowerSequenceAlternativesRelationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceAlternativesRelationListDataSelectorsType"
        },
        {
            "name": "power_sequence_description_list_data_selectors",
            "xml_name": "powerSequenceDescriptionListDataSelectors",
            "type": "ns_p:PowerSequenceDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceDescriptionListDataSelectorsType"
        },
        {
            "name": "power_sequence_price_list_data_selectors",
            "xml_name": "powerSequencePriceListDataSelectors",
            "type": "ns_p:PowerSequencePriceListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequencePriceListDataSelectorsType"
        },
        {
            "name": "power_sequence_schedule_constraints_list_data_selectors",
            "xml_name": "powerSequenceScheduleConstraintsListDataSelectors",
            "type": "ns_p:PowerSequenceScheduleConstraintsListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceScheduleConstraintsListDataSelectorsType"
        },
        {
            "name": "power_sequence_schedule_list_data_selectors",
            "xml_name": "powerSequenceScheduleListDataSelectors",
            "type": "ns_p:PowerSequenceScheduleListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceScheduleListDataSelectorsType"
        },
        {
            "name": "power_sequence_schedule_preference_list_data_selectors",
            "xml_name": "powerSequenceSchedulePreferenceListDataSelectors",
            "type": "ns_p:PowerSequenceSchedulePreferenceListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceSchedulePreferenceListDataSelectorsType"
        },
        {
            "name": "power_sequence_state_list_data_selectors",
            "xml_name": "powerSequenceStateListDataSelectors",
            "type": "ns_p:PowerSequenceStateListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceStateListDataSelectorsType"
        },
        {
            "name": "power_time_slot_schedule_constraints_list_data_selectors",
            "xml_name": "powerTimeSlotScheduleConstraintsListDataSelectors",
            "type": "ns_p:PowerTimeSlotScheduleConstraintsListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotScheduleConstraintsListDataSelectorsType"
        },
        {
            "name": "power_time_slot_schedule_list_data_selectors",
            "xml_name": "powerTimeSlotScheduleListDataSelectors",
            "type": "ns_p:PowerTimeSlotScheduleListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotScheduleListDataSelectorsType"
        },
        {
            "name": "power_time_slot_value_list_data_selectors",
            "xml_name": "powerTimeSlotValueListDataSelectors",
            "type": "ns_p:PowerTimeSlotValueListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotValueListDataSelectorsType"
        },
        {
            "name": "sensing_list_data_selectors",
            "xml_name": "sensingListDataSelectors",
            "type": "ns_p:SensingListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SensingListDataSelectorsType"
        },
        {
            "name": "session_identification_list_data_selectors",
            "xml_name": "sessionIdentificationListDataSelectors",
            "type": "ns_p:SessionIdentificationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SessionIdentificationListDataSelectorsType"
        },
        {
            "name": "session_measurement_relation_list_data_selectors",
            "xml_name": "sessionMeasurementRelationListDataSelectors",
            "type": "ns_p:SessionMeasurementRelationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SessionMeasurementRelationListDataSelectorsType"
        },
        {
            "name": "setpoint_constraints_list_data_selectors",
            "xml_name": "setpointConstraintsListDataSelectors",
            "type": "ns_p:SetpointConstraintsListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointConstraintsListDataSelectorsType"
        },
        {
            "name": "setpoint_description_list_data_selectors",
            "xml_name": "setpointDescriptionListDataSelectors",
            "type": "ns_p:SetpointDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointDescriptionListDataSelectorsType"
        },
        {
            "name": "setpoint_list_data_selectors",
            "xml_name": "setpointListDataSelectors",
            "type": "ns_p:SetpointListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointListDataSelectorsType"
        },
        {
            "name": "smart_energy_management_ps_data_selectors",
            "xml_name": "smartEnergyManagementPsDataSelectors",
            "type": "ns_p:SmartEnergyManagementPsDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsDataSelectorsType"
        },
        {
            "name": "smart_energy_management_ps_price_data_selectors",
            "xml_name": "smartEnergyManagementPsPriceDataSelectors",
            "type": "ns_p:SmartEnergyManagementPsPriceDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsPriceDataSelectorsType"
        },
        {
            "name": "specification_version_list_data_selectors",
            "xml_name": "specificationVersionListDataSelectors",
            "type": "ns_p:SpecificationVersionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SpecificationVersionListDataSelectorsType"
        },
        {
            "name": "state_information_list_data_selectors",
            "xml_name": "stateInformationListDataSelectors",
            "type": "ns_p:StateInformationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "StateInformationListDataSelectorsType"
        },
        {
            "name": "subscription_management_entry_list_data_selectors",
            "xml_name": "subscriptionManagementEntryListDataSelectors",
            "type": "ns_p:SubscriptionManagementEntryListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SubscriptionManagementEntryListDataSelectorsType"
        },
        {
            "name": "supply_condition_description_list_data_selectors",
            "xml_name": "supplyConditionDescriptionListDataSelectors",
            "type": "ns_p:SupplyConditionDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionDescriptionListDataSelectorsType"
        },
        {
            "name": "supply_condition_list_data_selectors",
            "xml_name": "supplyConditionListDataSelectors",
            "type": "ns_p:SupplyConditionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionListDataSelectorsType"
        },
        {
            "name": "supply_condition_threshold_relation_list_data_selectors",
            "xml_name": "supplyConditionThresholdRelationListDataSelectors",
            "type": "ns_p:SupplyConditionThresholdRelationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionThresholdRelationListDataSelectorsType"
        },
        {
            "name": "tariff_boundary_relation_list_data_selectors",
            "xml_name": "tariffBoundaryRelationListDataSelectors",
            "type": "ns_p:TariffBoundaryRelationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffBoundaryRelationListDataSelectorsType"
        },
        {
            "name": "tariff_description_list_data_selectors",
            "xml_name": "tariffDescriptionListDataSelectors",
            "type": "ns_p:TariffDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffDescriptionListDataSelectorsType"
        },
        {
            "name": "tariff_list_data_selectors",
            "xml_name": "tariffListDataSelectors",
            "type": "ns_p:TariffListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffListDataSelectorsType"
        },
        {
            "name": "tariff_tier_relation_list_data_selectors",
            "xml_name": "tariffTierRelationListDataSelectors",
            "type": "ns_p:TariffTierRelationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffTierRelationListDataSelectorsType"
        },
        {
            "name": "task_management_job_description_list_data_selectors",
            "xml_name": "taskManagementJobDescriptionListDataSelectors",
            "type": "ns_p:TaskManagementJobDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobDescriptionListDataSelectorsType"
        },
        {
            "name": "task_management_job_list_data_selectors",
            "xml_name": "taskManagementJobListDataSelectors",
            "type": "ns_p:TaskManagementJobListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobListDataSelectorsType"
        },
        {
            "name": "task_management_job_relation_list_data_selectors",
            "xml_name": "taskManagementJobRelationListDataSelectors",
            "type": "ns_p:TaskManagementJobRelationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobRelationListDataSelectorsType"
        },
        {
            "name": "threshold_constraints_list_data_selectors",
            "xml_name": "thresholdConstraintsListDataSelectors",
            "type": "ns_p:ThresholdConstraintsListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdConstraintsListDataSelectorsType"
        },
        {
            "name": "threshold_description_list_data_selectors",
            "xml_name": "thresholdDescriptionListDataSelectors",
            "type": "ns_p:ThresholdDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdDescriptionListDataSelectorsType"
        },
        {
            "name": "threshold_list_data_selectors",
            "xml_name": "thresholdListDataSelectors",
            "type": "ns_p:ThresholdListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdListDataSelectorsType"
        },
        {
            "name": "tier_boundary_description_list_data_selectors",
            "xml_name": "tierBoundaryDescriptionListDataSelectors",
            "type": "ns_p:TierBoundaryDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryDescriptionListDataSelectorsType"
        },
        {
            "name": "tier_boundary_list_data_selectors",
            "xml_name": "tierBoundaryListDataSelectors",
            "type": "ns_p:TierBoundaryListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryListDataSelectorsType"
        },
        {
            "name": "tier_description_list_data_selectors",
            "xml_name": "tierDescriptionListDataSelectors",
            "type": "ns_p:TierDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierDescriptionListDataSelectorsType"
        },
        {
            "name": "tier_incentive_relation_list_data_selectors",
            "xml_name": "tierIncentiveRelationListDataSelectors",
            "type": "ns_p:TierIncentiveRelationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIncentiveRelationListDataSelectorsType"
        },
        {
            "name": "tier_list_data_selectors",
            "xml_name": "tierListDataSelectors",
            "type": "ns_p:TierListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierListDataSelectorsType"
        },
        {
            "name": "time_series_constraints_list_data_selectors",
            "xml_name": "timeSeriesConstraintsListDataSelectors",
            "type": "ns_p:TimeSeriesConstraintsListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesConstraintsListDataSelectorsType"
        },
        {
            "name": "time_series_description_list_data_selectors",
            "xml_name": "timeSeriesDescriptionListDataSelectors",
            "type": "ns_p:TimeSeriesDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesDescriptionListDataSelectorsType"
        },
        {
            "name": "time_series_list_data_selectors",
            "xml_name": "timeSeriesListDataSelectors",
            "type": "ns_p:TimeSeriesListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesListDataSelectorsType"
        },
        {
            "name": "time_table_constraints_list_data_selectors",
            "xml_name": "timeTableConstraintsListDataSelectors",
            "type": "ns_p:TimeTableConstraintsListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableConstraintsListDataSelectorsType"
        },
        {
            "name": "time_table_description_list_data_selectors",
            "xml_name": "timeTableDescriptionListDataSelectors",
            "type": "ns_p:TimeTableDescriptionListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableDescriptionListDataSelectorsType"
        },
        {
            "name": "time_table_list_data_selectors",
            "xml_name": "timeTableListDataSelectors",
            "type": "ns_p:TimeTableListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableListDataSelectorsType"
        },
        {
            "name": "use_case_information_list_data_selectors",
            "xml_name": "useCaseInformationListDataSelectors",
            "type": "ns_p:UseCaseInformationListDataSelectorsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UseCaseInformationListDataSelectorsType"
        },
        {
            "name": "actuator_level_data_elements",
            "xml_name": "actuatorLevelDataElements",
            "type": "ns_p:ActuatorLevelDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ActuatorLevelDataElementsType"
        },
        {
            "name": "actuator_level_description_data_elements",
            "xml_name": "actuatorLevelDescriptionDataElements",
            "type": "ns_p:ActuatorLevelDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ActuatorLevelDescriptionDataElementsType"
        },
        {
            "name": "actuator_switch_data_elements",
            "xml_name": "actuatorSwitchDataElements",
            "type": "ns_p:ActuatorSwitchDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ActuatorSwitchDataElementsType"
        },
        {
            "name": "actuator_switch_description_data_elements",
            "xml_name": "actuatorSwitchDescriptionDataElements",
            "type": "ns_p:ActuatorSwitchDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ActuatorSwitchDescriptionDataElementsType"
        },
        {
            "name": "alarm_data_elements",
            "xml_name": "alarmDataElements",
            "type": "ns_p:AlarmDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "AlarmDataElementsType"
        },
        {
            "name": "bill_constraints_data_elements",
            "xml_name": "billConstraintsDataElements",
            "type": "ns_p:BillConstraintsDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillConstraintsDataElementsType"
        },
        {
            "name": "bill_data_elements",
            "xml_name": "billDataElements",
            "type": "ns_p:BillDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillDataElementsType"
        },
        {
            "name": "bill_description_data_elements",
            "xml_name": "billDescriptionDataElements",
            "type": "ns_p:BillDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BillDescriptionDataElementsType"
        },
        {
            "name": "binding_management_delete_call_elements",
            "xml_name": "bindingManagementDeleteCallElements",
            "type": "ns_p:BindingManagementDeleteCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BindingManagementDeleteCallElementsType"
        },
        {
            "name": "binding_management_entry_data_elements",
            "xml_name": "bindingManagementEntryDataElements",
            "type": "ns_p:BindingManagementEntryDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BindingManagementEntryDataElementsType"
        },
        {
            "name": "binding_management_request_call_elements",
            "xml_name": "bindingManagementRequestCallElements",
            "type": "ns_p:BindingManagementRequestCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "BindingManagementRequestCallElementsType"
        },
        {
            "name": "commodity_data_elements",
            "xml_name": "commodityDataElements",
            "type": "ns_p:CommodityDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "CommodityDataElementsType"
        },
        {
            "name": "data_tunneling_call_elements",
            "xml_name": "dataTunnelingCallElements",
            "type": "ns_p:DataTunnelingCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DataTunnelingCallElementsType"
        },
        {
            "name": "device_classification_manufacturer_data_elements",
            "xml_name": "deviceClassificationManufacturerDataElements",
            "type": "ns_p:DeviceClassificationManufacturerDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationManufacturerDataElementsType"
        },
        {
            "name": "device_classification_user_data_elements",
            "xml_name": "deviceClassificationUserDataElements",
            "type": "ns_p:DeviceClassificationUserDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceClassificationUserDataElementsType"
        },
        {
            "name": "device_configuration_key_value_constraints_data_elements",
            "xml_name": "deviceConfigurationKeyValueConstraintsDataElements",
            "type": "ns_p:DeviceConfigurationKeyValueConstraintsDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueConstraintsDataElementsType"
        },
        {
            "name": "device_configuration_key_value_data_elements",
            "xml_name": "deviceConfigurationKeyValueDataElements",
            "type": "ns_p:DeviceConfigurationKeyValueDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueDataElementsType"
        },
        {
            "name": "device_configuration_key_value_description_data_elements",
            "xml_name": "deviceConfigurationKeyValueDescriptionDataElements",
            "type": "ns_p:DeviceConfigurationKeyValueDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceConfigurationKeyValueDescriptionDataElementsType"
        },
        {
            "name": "device_diagnosis_heartbeat_data_elements",
            "xml_name": "deviceDiagnosisHeartbeatDataElements",
            "type": "ns_p:DeviceDiagnosisHeartbeatDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceDiagnosisHeartbeatDataElementsType"
        },
        {
            "name": "device_diagnosis_service_data_elements",
            "xml_name": "deviceDiagnosisServiceDataElements",
            "type": "ns_p:DeviceDiagnosisServiceDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceDiagnosisServiceDataElementsType"
        },
        {
            "name": "device_diagnosis_state_data_elements",
            "xml_name": "deviceDiagnosisStateDataElements",
            "type": "ns_p:DeviceDiagnosisStateDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DeviceDiagnosisStateDataElementsType"
        },
        {
            "name": "direct_control_activity_data_elements",
            "xml_name": "directControlActivityDataElements",
            "type": "ns_p:DirectControlActivityDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DirectControlActivityDataElementsType"
        },
        {
            "name": "direct_control_description_data_elements",
            "xml_name": "directControlDescriptionDataElements",
            "type": "ns_p:DirectControlDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "DirectControlDescriptionDataElementsType"
        },
        {
            "name": "electrical_connection_characteristic_data_elements",
            "xml_name": "electricalConnectionCharacteristicDataElements",
            "type": "ns_p:ElectricalConnectionCharacteristicDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionCharacteristicDataElementsType"
        },
        {
            "name": "electrical_connection_description_data_elements",
            "xml_name": "electricalConnectionDescriptionDataElements",
            "type": "ns_p:ElectricalConnectionDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionDescriptionDataElementsType"
        },
        {
            "name": "electrical_connection_parameter_description_data_elements",
            "xml_name": "electricalConnectionParameterDescriptionDataElements",
            "type": "ns_p:ElectricalConnectionParameterDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionParameterDescriptionDataElementsType"
        },
        {
            "name": "electrical_connection_permitted_value_set_data_elements",
            "xml_name": "electricalConnectionPermittedValueSetDataElements",
            "type": "ns_p:ElectricalConnectionPermittedValueSetDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionPermittedValueSetDataElementsType"
        },
        {
            "name": "electrical_connection_state_data_elements",
            "xml_name": "electricalConnectionStateDataElements",
            "type": "ns_p:ElectricalConnectionStateDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ElectricalConnectionStateDataElementsType"
        },
        {
            "name": "hvac_operation_mode_description_data_elements",
            "xml_name": "hvacOperationModeDescriptionDataElements",
            "type": "ns_p:HvacOperationModeDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOperationModeDescriptionDataElementsType"
        },
        {
            "name": "hvac_overrun_data_elements",
            "xml_name": "hvacOverrunDataElements",
            "type": "ns_p:HvacOverrunDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunDataElementsType"
        },
        {
            "name": "hvac_overrun_description_data_elements",
            "xml_name": "hvacOverrunDescriptionDataElements",
            "type": "ns_p:HvacOverrunDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacOverrunDescriptionDataElementsType"
        },
        {
            "name": "hvac_system_function_data_elements",
            "xml_name": "hvacSystemFunctionDataElements",
            "type": "ns_p:HvacSystemFunctionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionDataElementsType"
        },
        {
            "name": "hvac_system_function_description_data_elements",
            "xml_name": "hvacSystemFunctionDescriptionDataElements",
            "type": "ns_p:HvacSystemFunctionDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionDescriptionDataElementsType"
        },
        {
            "name": "hvac_system_function_operation_mode_relation_data_elements",
            "xml_name": "hvacSystemFunctionOperationModeRelationDataElements",
            "type": "ns_p:HvacSystemFunctionOperationModeRelationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionOperationModeRelationDataElementsType"
        },
        {
            "name": "hvac_system_function_power_sequence_relation_data_elements",
            "xml_name": "hvacSystemFunctionPowerSequenceRelationDataElements",
            "type": "ns_p:HvacSystemFunctionPowerSequenceRelationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionPowerSequenceRelationDataElementsType"
        },
        {
            "name": "hvac_system_function_setpoint_relation_data_elements",
            "xml_name": "hvacSystemFunctionSetpointRelationDataElements",
            "type": "ns_p:HvacSystemFunctionSetpointRelationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "HvacSystemFunctionSetpointRelationDataElementsType"
        },
        {
            "name": "identification_data_elements",
            "xml_name": "identificationDataElements",
            "type": "ns_p:IdentificationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IdentificationDataElementsType"
        },
        {
            "name": "incentive_data_elements",
            "xml_name": "incentiveDataElements",
            "type": "ns_p:IncentiveDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveDataElementsType"
        },
        {
            "name": "incentive_description_data_elements",
            "xml_name": "incentiveDescriptionDataElements",
            "type": "ns_p:IncentiveDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveDescriptionDataElementsType"
        },
        {
            "name": "incentive_table_constraints_data_elements",
            "xml_name": "incentiveTableConstraintsDataElements",
            "type": "ns_p:IncentiveTableConstraintsDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableConstraintsDataElementsType"
        },
        {
            "name": "incentive_table_data_elements",
            "xml_name": "incentiveTableDataElements",
            "type": "ns_p:IncentiveTableDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableDataElementsType"
        },
        {
            "name": "incentive_table_description_data_elements",
            "xml_name": "incentiveTableDescriptionDataElements",
            "type": "ns_p:IncentiveTableDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "IncentiveTableDescriptionDataElementsType"
        },
        {
            "name": "load_control_event_data_elements",
            "xml_name": "loadControlEventDataElements",
            "type": "ns_p:LoadControlEventDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlEventDataElementsType"
        },
        {
            "name": "load_control_limit_constraints_data_elements",
            "xml_name": "loadControlLimitConstraintsDataElements",
            "type": "ns_p:LoadControlLimitConstraintsDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitConstraintsDataElementsType"
        },
        {
            "name": "load_control_limit_data_elements",
            "xml_name": "loadControlLimitDataElements",
            "type": "ns_p:LoadControlLimitDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitDataElementsType"
        },
        {
            "name": "load_control_limit_description_data_elements",
            "xml_name": "loadControlLimitDescriptionDataElements",
            "type": "ns_p:LoadControlLimitDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlLimitDescriptionDataElementsType"
        },
        {
            "name": "load_control_node_data_elements",
            "xml_name": "loadControlNodeDataElements",
            "type": "ns_p:LoadControlNodeDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlNodeDataElementsType"
        },
        {
            "name": "load_control_state_data_elements",
            "xml_name": "loadControlStateDataElements",
            "type": "ns_p:LoadControlStateDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "LoadControlStateDataElementsType"
        },
        {
            "name": "measurement_constraints_data_elements",
            "xml_name": "measurementConstraintsDataElements",
            "type": "ns_p:MeasurementConstraintsDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementConstraintsDataElementsType"
        },
        {
            "name": "measurement_data_elements",
            "xml_name": "measurementDataElements",
            "type": "ns_p:MeasurementDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementDataElementsType"
        },
        {
            "name": "measurement_description_data_elements",
            "xml_name": "measurementDescriptionDataElements",
            "type": "ns_p:MeasurementDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementDescriptionDataElementsType"
        },
        {
            "name": "measurement_series_data_elements",
            "xml_name": "measurementSeriesDataElements",
            "type": "ns_p:MeasurementSeriesDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementSeriesDataElementsType"
        },
        {
            "name": "measurement_threshold_relation_data_elements",
            "xml_name": "measurementThresholdRelationDataElements",
            "type": "ns_p:MeasurementThresholdRelationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MeasurementThresholdRelationDataElementsType"
        },
        {
            "name": "messaging_data_elements",
            "xml_name": "messagingDataElements",
            "type": "ns_p:MessagingDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "MessagingDataElementsType"
        },
        {
            "name": "network_management_abort_call_elements",
            "xml_name": "networkManagementAbortCallElements",
            "type": "ns_p:NetworkManagementAbortCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementAbortCallElementsType"
        },
        {
            "name": "network_management_add_node_call_elements",
            "xml_name": "networkManagementAddNodeCallElements",
            "type": "ns_p:NetworkManagementAddNodeCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementAddNodeCallElementsType"
        },
        {
            "name": "network_management_device_description_data_elements",
            "xml_name": "networkManagementDeviceDescriptionDataElements",
            "type": "ns_p:NetworkManagementDeviceDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementDeviceDescriptionDataElementsType"
        },
        {
            "name": "network_management_discover_call_elements",
            "xml_name": "networkManagementDiscoverCallElements",
            "type": "ns_p:NetworkManagementDiscoverCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementDiscoverCallElementsType"
        },
        {
            "name": "network_management_entity_description_data_elements",
            "xml_name": "networkManagementEntityDescriptionDataElements",
            "type": "ns_p:NetworkManagementEntityDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementEntityDescriptionDataElementsType"
        },
        {
            "name": "network_management_feature_description_data_elements",
            "xml_name": "networkManagementFeatureDescriptionDataElements",
            "type": "ns_p:NetworkManagementFeatureDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementFeatureDescriptionDataElementsType"
        },
        {
            "name": "network_management_joining_mode_data_elements",
            "xml_name": "networkManagementJoiningModeDataElements",
            "type": "ns_p:NetworkManagementJoiningModeDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementJoiningModeDataElementsType"
        },
        {
            "name": "network_management_modify_node_call_elements",
            "xml_name": "networkManagementModifyNodeCallElements",
            "type": "ns_p:NetworkManagementModifyNodeCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementModifyNodeCallElementsType"
        },
        {
            "name": "network_management_process_state_data_elements",
            "xml_name": "networkManagementProcessStateDataElements",
            "type": "ns_p:NetworkManagementProcessStateDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementProcessStateDataElementsType"
        },
        {
            "name": "network_management_remove_node_call_elements",
            "xml_name": "networkManagementRemoveNodeCallElements",
            "type": "ns_p:NetworkManagementRemoveNodeCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementRemoveNodeCallElementsType"
        },
        {
            "name": "network_management_report_candidate_data_elements",
            "xml_name": "networkManagementReportCandidateDataElements",
            "type": "ns_p:NetworkManagementReportCandidateDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementReportCandidateDataElementsType"
        },
        {
            "name": "network_management_scan_network_call_elements",
            "xml_name": "networkManagementScanNetworkCallElements",
            "type": "ns_p:NetworkManagementScanNetworkCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NetworkManagementScanNetworkCallElementsType"
        },
        {
            "name": "node_management_binding_data_elements",
            "xml_name": "nodeManagementBindingDataElements",
            "type": "ns_p:NodeManagementBindingDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementBindingDataElementsType"
        },
        {
            "name": "node_management_binding_delete_call_elements",
            "xml_name": "nodeManagementBindingDeleteCallElements",
            "type": "ns_p:NodeManagementBindingDeleteCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementBindingDeleteCallElementsType"
        },
        {
            "name": "node_management_binding_request_call_elements",
            "xml_name": "nodeManagementBindingRequestCallElements",
            "type": "ns_p:NodeManagementBindingRequestCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementBindingRequestCallElementsType"
        },
        {
            "name": "node_management_destination_data_elements",
            "xml_name": "nodeManagementDestinationDataElements",
            "type": "ns_p:NodeManagementDestinationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementDestinationDataElementsType"
        },
        {
            "name": "node_management_detailed_discovery_data_elements",
            "xml_name": "nodeManagementDetailedDiscoveryDataElements",
            "type": "ns_p:NodeManagementDetailedDiscoveryDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementDetailedDiscoveryDataElementsType"
        },
        {
            "name": "node_management_subscription_data_elements",
            "xml_name": "nodeManagementSubscriptionDataElements",
            "type": "ns_p:NodeManagementSubscriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementSubscriptionDataElementsType"
        },
        {
            "name": "node_management_subscription_delete_call_elements",
            "xml_name": "nodeManagementSubscriptionDeleteCallElements",
            "type": "ns_p:NodeManagementSubscriptionDeleteCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementSubscriptionDeleteCallElementsType"
        },
        {
            "name": "node_management_subscription_request_call_elements",
            "xml_name": "nodeManagementSubscriptionRequestCallElements",
            "type": "ns_p:NodeManagementSubscriptionRequestCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementSubscriptionRequestCallElementsType"
        },
        {
            "name": "node_management_use_case_data_elements",
            "xml_name": "nodeManagementUseCaseDataElements",
            "type": "ns_p:NodeManagementUseCaseDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "NodeManagementUseCaseDataElementsType"
        },
        {
            "name": "operating_constraints_duration_data_elements",
            "xml_name": "operatingConstraintsDurationDataElements",
            "type": "ns_p:OperatingConstraintsDurationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsDurationDataElementsType"
        },
        {
            "name": "operating_constraints_interrupt_data_elements",
            "xml_name": "operatingConstraintsInterruptDataElements",
            "type": "ns_p:OperatingConstraintsInterruptDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsInterruptDataElementsType"
        },
        {
            "name": "operating_constraints_power_description_data_elements",
            "xml_name": "operatingConstraintsPowerDescriptionDataElements",
            "type": "ns_p:OperatingConstraintsPowerDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsPowerDescriptionDataElementsType"
        },
        {
            "name": "operating_constraints_power_level_data_elements",
            "xml_name": "operatingConstraintsPowerLevelDataElements",
            "type": "ns_p:OperatingConstraintsPowerLevelDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsPowerLevelDataElementsType"
        },
        {
            "name": "operating_constraints_power_range_data_elements",
            "xml_name": "operatingConstraintsPowerRangeDataElements",
            "type": "ns_p:OperatingConstraintsPowerRangeDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsPowerRangeDataElementsType"
        },
        {
            "name": "operating_constraints_resume_implication_data_elements",
            "xml_name": "operatingConstraintsResumeImplicationDataElements",
            "type": "ns_p:OperatingConstraintsResumeImplicationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "OperatingConstraintsResumeImplicationDataElementsType"
        },
        {
            "name": "power_sequence_alternatives_relation_data_elements",
            "xml_name": "powerSequenceAlternativesRelationDataElements",
            "type": "ns_p:PowerSequenceAlternativesRelationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceAlternativesRelationDataElementsType"
        },
        {
            "name": "power_sequence_description_data_elements",
            "xml_name": "powerSequenceDescriptionDataElements",
            "type": "ns_p:PowerSequenceDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceDescriptionDataElementsType"
        },
        {
            "name": "power_sequence_node_schedule_information_data_elements",
            "xml_name": "powerSequenceNodeScheduleInformationDataElements",
            "type": "ns_p:PowerSequenceNodeScheduleInformationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceNodeScheduleInformationDataElementsType"
        },
        {
            "name": "power_sequence_price_calculation_request_call_elements",
            "xml_name": "powerSequencePriceCalculationRequestCallElements",
            "type": "ns_p:PowerSequencePriceCalculationRequestCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequencePriceCalculationRequestCallElementsType"
        },
        {
            "name": "power_sequence_price_data_elements",
            "xml_name": "powerSequencePriceDataElements",
            "type": "ns_p:PowerSequencePriceDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequencePriceDataElementsType"
        },
        {
            "name": "power_sequence_schedule_configuration_request_call_elements",
            "xml_name": "powerSequenceScheduleConfigurationRequestCallElements",
            "type": "ns_p:PowerSequenceScheduleConfigurationRequestCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceScheduleConfigurationRequestCallElementsType"
        },
        {
            "name": "power_sequence_schedule_constraints_data_elements",
            "xml_name": "powerSequenceScheduleConstraintsDataElements",
            "type": "ns_p:PowerSequenceScheduleConstraintsDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceScheduleConstraintsDataElementsType"
        },
        {
            "name": "power_sequence_schedule_data_elements",
            "xml_name": "powerSequenceScheduleDataElements",
            "type": "ns_p:PowerSequenceScheduleDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceScheduleDataElementsType"
        },
        {
            "name": "power_sequence_schedule_preference_data_elements",
            "xml_name": "powerSequenceSchedulePreferenceDataElements",
            "type": "ns_p:PowerSequenceSchedulePreferenceDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceSchedulePreferenceDataElementsType"
        },
        {
            "name": "power_sequence_state_data_elements",
            "xml_name": "powerSequenceStateDataElements",
            "type": "ns_p:PowerSequenceStateDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerSequenceStateDataElementsType"
        },
        {
            "name": "power_time_slot_schedule_constraints_data_elements",
            "xml_name": "powerTimeSlotScheduleConstraintsDataElements",
            "type": "ns_p:PowerTimeSlotScheduleConstraintsDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotScheduleConstraintsDataElementsType"
        },
        {
            "name": "power_time_slot_schedule_data_elements",
            "xml_name": "powerTimeSlotScheduleDataElements",
            "type": "ns_p:PowerTimeSlotScheduleDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotScheduleDataElementsType"
        },
        {
            "name": "power_time_slot_value_data_elements",
            "xml_name": "powerTimeSlotValueDataElements",
            "type": "ns_p:PowerTimeSlotValueDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "PowerTimeSlotValueDataElementsType"
        },
        {
            "name": "sensing_data_elements",
            "xml_name": "sensingDataElements",
            "type": "ns_p:SensingDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SensingDataElementsType"
        },
        {
            "name": "sensing_description_data_elements",
            "xml_name": "sensingDescriptionDataElements",
            "type": "ns_p:SensingDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SensingDescriptionDataElementsType"
        },
        {
            "name": "session_identification_data_elements",
            "xml_name": "sessionIdentificationDataElements",
            "type": "ns_p:SessionIdentificationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SessionIdentificationDataElementsType"
        },
        {
            "name": "session_measurement_relation_data_elements",
            "xml_name": "sessionMeasurementRelationDataElements",
            "type": "ns_p:SessionMeasurementRelationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SessionMeasurementRelationDataElementsType"
        },
        {
            "name": "setpoint_constraints_data_elements",
            "xml_name": "setpointConstraintsDataElements",
            "type": "ns_p:SetpointConstraintsDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointConstraintsDataElementsType"
        },
        {
            "name": "setpoint_data_elements",
            "xml_name": "setpointDataElements",
            "type": "ns_p:SetpointDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointDataElementsType"
        },
        {
            "name": "setpoint_description_data_elements",
            "xml_name": "setpointDescriptionDataElements",
            "type": "ns_p:SetpointDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SetpointDescriptionDataElementsType"
        },
        {
            "name": "smart_energy_management_ps_configuration_request_call_elements",
            "xml_name": "smartEnergyManagementPsConfigurationRequestCallElements",
            "type": "ns_p:SmartEnergyManagementPsConfigurationRequestCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsConfigurationRequestCallElementsType"
        },
        {
            "name": "smart_energy_management_ps_data_elements",
            "xml_name": "smartEnergyManagementPsDataElements",
            "type": "ns_p:SmartEnergyManagementPsDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsDataElementsType"
        },
        {
            "name": "smart_energy_management_ps_price_calculation_request_call_elements",
            "xml_name": "smartEnergyManagementPsPriceCalculationRequestCallElements",
            "type": "ns_p:SmartEnergyManagementPsPriceCalculationRequestCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsPriceCalculationRequestCallElementsType"
        },
        {
            "name": "smart_energy_management_ps_price_data_elements",
            "xml_name": "smartEnergyManagementPsPriceDataElements",
            "type": "ns_p:SmartEnergyManagementPsPriceDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SmartEnergyManagementPsPriceDataElementsType"
        },
        {
            "name": "specification_version_data_elements",
            "xml_name": "specificationVersionDataElements",
            "type": "ns_p:SpecificationVersionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SpecificationVersionDataElementsType"
        },
        {
            "name": "state_information_data_elements",
            "xml_name": "stateInformationDataElements",
            "type": "ns_p:StateInformationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "StateInformationDataElementsType"
        },
        {
            "name": "subscription_management_delete_call_elements",
            "xml_name": "subscriptionManagementDeleteCallElements",
            "type": "ns_p:SubscriptionManagementDeleteCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SubscriptionManagementDeleteCallElementsType"
        },
        {
            "name": "subscription_management_entry_data_elements",
            "xml_name": "subscriptionManagementEntryDataElements",
            "type": "ns_p:SubscriptionManagementEntryDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SubscriptionManagementEntryDataElementsType"
        },
        {
            "name": "subscription_management_request_call_elements",
            "xml_name": "subscriptionManagementRequestCallElements",
            "type": "ns_p:SubscriptionManagementRequestCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SubscriptionManagementRequestCallElementsType"
        },
        {
            "name": "supply_condition_data_elements",
            "xml_name": "supplyConditionDataElements",
            "type": "ns_p:SupplyConditionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionDataElementsType"
        },
        {
            "name": "supply_condition_description_data_elements",
            "xml_name": "supplyConditionDescriptionDataElements",
            "type": "ns_p:SupplyConditionDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionDescriptionDataElementsType"
        },
        {
            "name": "supply_condition_threshold_relation_data_elements",
            "xml_name": "supplyConditionThresholdRelationDataElements",
            "type": "ns_p:SupplyConditionThresholdRelationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "SupplyConditionThresholdRelationDataElementsType"
        },
        {
            "name": "tariff_boundary_relation_data_elements",
            "xml_name": "tariffBoundaryRelationDataElements",
            "type": "ns_p:TariffBoundaryRelationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffBoundaryRelationDataElementsType"
        },
        {
            "name": "tariff_data_elements",
            "xml_name": "tariffDataElements",
            "type": "ns_p:TariffDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffDataElementsType"
        },
        {
            "name": "tariff_description_data_elements",
            "xml_name": "tariffDescriptionDataElements",
            "type": "ns_p:TariffDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffDescriptionDataElementsType"
        },
        {
            "name": "tariff_overall_constraints_data_elements",
            "xml_name": "tariffOverallConstraintsDataElements",
            "type": "ns_p:TariffOverallConstraintsDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffOverallConstraintsDataElementsType"
        },
        {
            "name": "tariff_tier_relation_data_elements",
            "xml_name": "tariffTierRelationDataElements",
            "type": "ns_p:TariffTierRelationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TariffTierRelationDataElementsType"
        },
        {
            "name": "task_management_job_data_elements",
            "xml_name": "taskManagementJobDataElements",
            "type": "ns_p:TaskManagementJobDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobDataElementsType"
        },
        {
            "name": "task_management_job_description_data_elements",
            "xml_name": "taskManagementJobDescriptionDataElements",
            "type": "ns_p:TaskManagementJobDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobDescriptionDataElementsType"
        },
        {
            "name": "task_management_job_relation_data_elements",
            "xml_name": "taskManagementJobRelationDataElements",
            "type": "ns_p:TaskManagementJobRelationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementJobRelationDataElementsType"
        },
        {
            "name": "task_management_overview_data_elements",
            "xml_name": "taskManagementOverviewDataElements",
            "type": "ns_p:TaskManagementOverviewDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TaskManagementOverviewDataElementsType"
        },
        {
            "name": "threshold_constraints_data_elements",
            "xml_name": "thresholdConstraintsDataElements",
            "type": "ns_p:ThresholdConstraintsDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdConstraintsDataElementsType"
        },
        {
            "name": "threshold_data_elements",
            "xml_name": "thresholdDataElements",
            "type": "ns_p:ThresholdDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdDataElementsType"
        },
        {
            "name": "threshold_description_data_elements",
            "xml_name": "thresholdDescriptionDataElements",
            "type": "ns_p:ThresholdDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "ThresholdDescriptionDataElementsType"
        },
        {
            "name": "tier_boundary_data_elements",
            "xml_name": "tierBoundaryDataElements",
            "type": "ns_p:TierBoundaryDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryDataElementsType"
        },
        {
            "name": "tier_boundary_description_data_elements",
            "xml_name": "tierBoundaryDescriptionDataElements",
            "type": "ns_p:TierBoundaryDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierBoundaryDescriptionDataElementsType"
        },
        {
            "name": "tier_data_elements",
            "xml_name": "tierDataElements",
            "type": "ns_p:TierDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierDataElementsType"
        },
        {
            "name": "tier_description_data_elements",
            "xml_name": "tierDescriptionDataElements",
            "type": "ns_p:TierDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierDescriptionDataElementsType"
        },
        {
            "name": "tier_incentive_relation_data_elements",
            "xml_name": "tierIncentiveRelationDataElements",
            "type": "ns_p:TierIncentiveRelationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TierIncentiveRelationDataElementsType"
        },
        {
            "name": "time_distributor_data_elements",
            "xml_name": "timeDistributorDataElements",
            "type": "ns_p:TimeDistributorDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeDistributorDataElementsType"
        },
        {
            "name": "time_distributor_enquiry_call_elements",
            "xml_name": "timeDistributorEnquiryCallElements",
            "type": "ns_p:TimeDistributorEnquiryCallElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeDistributorEnquiryCallElementsType"
        },
        {
            "name": "time_information_data_elements",
            "xml_name": "timeInformationDataElements",
            "type": "ns_p:TimeInformationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeInformationDataElementsType"
        },
        {
            "name": "time_precision_data_elements",
            "xml_name": "timePrecisionDataElements",
            "type": "ns_p:TimePrecisionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimePrecisionDataElementsType"
        },
        {
            "name": "time_series_constraints_data_elements",
            "xml_name": "timeSeriesConstraintsDataElements",
            "type": "ns_p:TimeSeriesConstraintsDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesConstraintsDataElementsType"
        },
        {
            "name": "time_series_data_elements",
            "xml_name": "timeSeriesDataElements",
            "type": "ns_p:TimeSeriesDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesDataElementsType"
        },
        {
            "name": "time_series_description_data_elements",
            "xml_name": "timeSeriesDescriptionDataElements",
            "type": "ns_p:TimeSeriesDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeSeriesDescriptionDataElementsType"
        },
        {
            "name": "time_table_constraints_data_elements",
            "xml_name": "timeTableConstraintsDataElements",
            "type": "ns_p:TimeTableConstraintsDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableConstraintsDataElementsType"
        },
        {
            "name": "time_table_data_elements",
            "xml_name": "timeTableDataElements",
            "type": "ns_p:TimeTableDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableDataElementsType"
        },
        {
            "name": "time_table_description_data_elements",
            "xml_name": "timeTableDescriptionDataElements",
            "type": "ns_p:TimeTableDescriptionDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "TimeTableDescriptionDataElementsType"
        },
        {
            "name": "use_case_information_data_elements",
            "xml_name": "useCaseInformationDataElements",
            "type": "ns_p:UseCaseInformationDataElementsType",
            "is_array": False,
            "is_optional": True,
            "class_check": "UseCaseInformationDataElementsType"
        },
        {
            "name": "data_selectors_choice_group",
            "xml_name": "data_selectors_choice_group",
            "type": "ns_p:DataSelectorsChoiceGroup",
            "is_array": False,
            "is_optional": True,
            "class_check": "DataSelectorsChoiceGroup"
        },
        {
            "name": "data_elements_choice_group",
            "xml_name": "data_elements_choice_group",
            "type": "ns_p:DataElementsChoiceGroup",
            "is_array": False,
            "is_optional": True,
            "class_check": "DataElementsChoiceGroup"
        },
    ]

