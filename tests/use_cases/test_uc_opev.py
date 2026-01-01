import pytest
from spine.base_type.loadcontrol import (
    LoadControlLimitDescriptionDataType,
    LoadControlLimitDataType,
)
from spine.base_type.devicediagnosis import (
    DeviceDiagnosisHeartbeatDataType,
    DeviceDiagnosisStateDataType,
)
from spine.union_type.loadcontrol import (
    LoadControlLimitTypeType,
    LoadControlCategoryType,
)
from spine.enums.loadcontrol import (
    LoadControlLimitTypeEnumType,
    LoadControlCategoryEnumType,
)
from spine.union_type.commondatatypes import (
    UnitOfMeasurementType,
    ScopeTypeType,
)
from spine.enums.commondatatypes import (
    UnitOfMeasurementEnumType,
    ScopeTypeEnumType,
)
from spine.base_type.commondatatypes import (
    ScaledNumberType,
)
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType,
)
from spine.union_type.devicediagnosis import (
    DeviceDiagnosisOperatingStateType,
)
from spine.enums.devicediagnosis import (
    DeviceDiagnosisOperatingStateEnumType,
)
from spine.simple_type.devicediagnosis import (
    LastErrorCodeType,
)

# OPEV Use Case Tests
# Overload Protection by EV Charging Current Curtailment (V1.0.1b)

@pytest.mark.requirement("OPEV-001")
def test_opev_scenario1_charging_curtailment():
    """
    Scenario 1: Energy Guard curtails charging current of EV.
    Ref: [OPEV-001]
    """
    # 1. Load Control Limit Description
    # scopeType "overloadProtection"
    # limitType "signDependentAbsValueLimit" (or maxValueLimit)
    # limitCategory "obligation"
    
    desc = LoadControlLimitDescriptionDataType(
        limit_id=None,
        limit_type=LoadControlLimitTypeType(value=LoadControlLimitTypeEnumType.signDependentAbsValueLimit),
        limit_category=LoadControlCategoryType(value=LoadControlCategoryEnumType.obligation),
        unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.A),
        scope_type=ScopeTypeType(value="overloadProtection") 
    )
    
    assert desc.limit_type.value == "signDependentAbsValueLimit"
    assert desc.limit_category.value == "obligation"
    assert desc.unit.value == "A"
    assert desc.scope_type.value == "overloadProtection"

    # 2. Load Control Limit Data
    # value (ScaledNumber)
    limit_data = LoadControlLimitDataType(
        limit_id=None,
        is_limit_active=True,
        value=ScaledNumberType(number=NumberType(value=10), scale=ScaleType(value=0)) # 10A
    )
    
    assert limit_data.is_limit_active is True
    assert limit_data.value.number.value == 10


@pytest.mark.requirement("OPEV-002")
def test_opev_scenario1_asymmetric_support():
    """
    Scenario 1: Asymmetric charging curtailment support.
    Ref: [OPEV-002]
    """
    # Verify that we can define limits per phase (conceptually).
    # This usually means multiple limit definitions or specific limit IDs.
    # Structural check for LimitDescription is consistent with OPEV-001.
    
    desc = LoadControlLimitDescriptionDataType(
        limit_id=None,
        limit_type=LoadControlLimitTypeType(value=LoadControlLimitTypeEnumType.signDependentAbsValueLimit),
        unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.A),
        scope_type=ScopeTypeType(value="overloadProtection")
    )
    assert desc.scope_type.value == "overloadProtection"


@pytest.mark.requirement("OPEV-005")
def test_opev_scenario2_heartbeat():
    """
    Scenario 2: EV checks Energy Guard availability (Heartbeat).
    Ref: [OPEV-005]
    """
    # Heartbeat check
    # heartbeatTimeout should be checked (e.g. 4 seconds)
    
    heartbeat = DeviceDiagnosisHeartbeatDataType(
        heartbeat_counter=100,
        heartbeat_timeout="PT4S"
    )
    
    assert heartbeat.heartbeat_counter == 100
    assert heartbeat.heartbeat_timeout == "PT4S"


@pytest.mark.requirement("OPEV-007")
def test_opev_scenario3_error_state():
    """
    Scenario 3: Energy Guard sends error state.
    Ref: [OPEV-007]
    """
    # Device Diagnosis State
    # operatingState should be checked
    
    state = DeviceDiagnosisStateDataType(
        timestamp=None,
        operating_state=DeviceDiagnosisOperatingStateType(value=DeviceDiagnosisOperatingStateEnumType.failure),
        last_error_code=LastErrorCodeType(value="Error 123")
    )
    
    assert state.operating_state.value == "failure"
    assert state.last_error_code.value == "Error 123"
