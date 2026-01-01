import pytest
from spine.base_type.loadcontrol import (
    LoadControlLimitDescriptionDataType,
    LoadControlLimitDataType,
)
from spine.base_type.devicediagnosis import (
    DeviceDiagnosisHeartbeatDataType,
    DeviceDiagnosisStateDataType,
)
from spine.base_type.electricalconnection import (
    ElectricalConnectionParameterDescriptionDataType,
)
from spine.base_type.commondatatypes import (
    ScaledNumberType,
)
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType,
)
from spine.union_type.loadcontrol import (
    LoadControlLimitTypeType,
    LoadControlCategoryType,
)
from spine.union_type.commondatatypes import (
    UnitOfMeasurementType,
    ScopeTypeType,
)
from spine.union_type.devicediagnosis import (
    DeviceDiagnosisOperatingStateType,
)
from spine.enums.loadcontrol import (
    LoadControlLimitTypeEnumType,
    LoadControlCategoryEnumType,
)
from spine.enums.commondatatypes import (
    UnitOfMeasurementEnumType,
    ScopeTypeEnumType,
)
from spine.enums.devicediagnosis import (
    DeviceDiagnosisOperatingStateEnumType,
)
from spine.union_type.electricalconnection import (
    ElectricalConnectionPhaseNameType,
)


@pytest.mark.requirement("OSCEV-001")
def test_oscev_self_consumption_limit():
    """
    Verify Self-Consumption Limit Description and Data (Scenario 1).
    Ref: [OSCEV-001]
    The CEM informs the EV about self-produced current.
    """
    # 1. Verify Description
    # Table 15: Content of Specialization "LoadControlLimit_SelfConsumptionOptimization"
    limit_desc = LoadControlLimitDescriptionDataType(
        limit_type=LoadControlLimitTypeType(value=LoadControlLimitTypeEnumType.maxValueLimit),
        limit_category=LoadControlCategoryType(value=LoadControlCategoryEnumType.recommendation),
        unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.A),
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.selfConsumption)
    )
    
    assert limit_desc.limit_type.value == "maxValueLimit"
    assert limit_desc.limit_category.value == "recommendation"
    assert limit_desc.unit.value == "A"
    assert limit_desc.scope_type.value == "selfConsumption"

    # 2. Verify Data (Limit Value)
    # The CEM sends the available current (e.g. 16A)
    limit_data = LoadControlLimitDataType(
        limit_id=None,
        value=ScaledNumberType(
            number=NumberType(value=16),
            scale=ScaleType(value=0)
        ),
        is_limit_active=True
    )
    
    assert limit_data.value.number.value == 16
    assert limit_data.value.scale.value == 0
    assert limit_data.is_limit_active is True


@pytest.mark.requirement("OSCEV-002")
def test_oscev_asymmetric_phases():
    """
    Verify Asymmetric Charging Support (Scenario 1).
    Ref: [OSCEV-002]
    If asymmetric charging is supported, CEM should inform EV about self-produced current of each phase.
    """
    # Table 8: ElectricalConnectionParameterDescriptionDataType
    # acMeasuredPhases can be "a", "b", "c"
    
    phases = ["a", "b", "c"]
    for phase in phases:
        param_desc = ElectricalConnectionParameterDescriptionDataType(
             ac_measured_phases=ElectricalConnectionPhaseNameType(value=phase)
        )
        assert param_desc.ac_measured_phases.value == phase


@pytest.mark.requirement("OSCEV-005")
def test_oscev_heartbeat():
    """
    Verify EV checks CEM availability (Scenario 2).
    Ref: [OSCEV-005]
    heartbeatTimeout <= 4s
    """
    # Table 13: deviceDiagnosisHeartbeatData
    # heartbeatTimeout <= 4s
    # heartbeatCounter is unsignedLong (int)
    
    heartbeat = DeviceDiagnosisHeartbeatDataType(
        heartbeat_counter=12345,
        heartbeat_timeout="PT4S"
    )
    assert heartbeat.heartbeat_timeout == "PT4S"
    assert heartbeat.heartbeat_counter == 12345


@pytest.mark.requirement("OSCEV-007")
def test_oscev_error_state():
    """
    Verify CEM sends error state (Scenario 3).
    Ref: [OSCEV-007]
    operatingState = failure
    """
    # Table 14: deviceDiagnosisStateData
    # operatingState can be "normalOperation" or "failure"
    
    failure_state = DeviceDiagnosisStateDataType(
        operating_state=DeviceDiagnosisOperatingStateType(
            value=DeviceDiagnosisOperatingStateEnumType.failure
        )
    )
    
    assert failure_state.operating_state.value == "failure"

    normal_state = DeviceDiagnosisStateDataType(
        operating_state=DeviceDiagnosisOperatingStateType(
            value=DeviceDiagnosisOperatingStateEnumType.normalOperation
        )
    )
    
    assert normal_state.operating_state.value == "normalOperation"

