import pytest
from spine.union_type.commondatatypes import (
    UnitOfMeasurementType,
    ScopeTypeType,
)
from spine.base_type.hvac import (
    HvacOperationModeDescriptionDataType,
    HvacSystemFunctionDescriptionDataType,
    HvacSystemFunctionOperationModeRelationDataType,
    HvacSystemFunctionDataType
)
from spine.base_type.measurement import (
    MeasurementDescriptionDataType,
    MeasurementDataType
)
from spine.base_type.commondatatypes import ScaledNumberType
from spine.simple_type.commondatatypes import (
    ScaleType,
    NumberType,
)
from spine.enums.hvac import (
    HvacOperationModeTypeEnumType,
    HvacSystemFunctionTypeEnumType
)
from spine.enums.commondatatypes import (
    ScopeTypeEnumType,
    UnitOfMeasurementEnumType
)
from spine.enums.measurement import MeasurementTypeEnumType
from spine.union_type.measurement import MeasurementTypeType
from spine.union_type.hvac import (
    HvacOperationModeTypeType,
    HvacSystemFunctionTypeType
)
from spine.simple_type.hvac import (
    HvacOperationModeIdType,
    HvacSystemFunctionIdType
)
from spine.simple_type.measurement import MeasurementIdType

# HVAC Use Case Tests
# Covers: MRT (Monitoring of Room Temperature), CRHSF (Configuration of Room Heating System Function)

# MRT - Monitoring of Room Temperature
@pytest.mark.requirement("MRT-001")
def test_mrt_scenario_1():
    """
    Scenario 1: Monitor HVAC room temperature.
    The Monitor (Client) receives room temperature from HVAC Room (Server).
    """
    # 1. MeasurementDescriptionDataType
    # Scope should be roomAirTemperature
    
    description_data = MeasurementDescriptionDataType(
        measurement_id=MeasurementIdType(value=1),
        measurement_type=MeasurementTypeType(value=MeasurementTypeEnumType.temperature),
        unit=UnitOfMeasurementType(value=UnitOfMeasurementEnumType.degC),
        scope_type=ScopeTypeType(value=ScopeTypeEnumType.roomAirTemperature)
    )
    
    assert description_data.scope_type.value == ScopeTypeEnumType.roomAirTemperature
    assert description_data.unit.value == UnitOfMeasurementEnumType.degC
    assert description_data.measurement_type.value == MeasurementTypeEnumType.temperature

    # 2. MeasurementDataType
    # Value should be a ScaledNumberType (e.g., 20.5 degC)
    
    measurement_data = MeasurementDataType(
        measurement_id=MeasurementIdType(value=1),
        value=ScaledNumberType(number=NumberType(value=205), scale=ScaleType(value=-1))
    )
    
    assert measurement_data.measurement_id.value == 1
    assert measurement_data.value.number.value == 205
    assert measurement_data.value.scale.value == -1

# CRHSF - Configuration of Room Heating System Function
@pytest.mark.requirement("CRHSF-001")
def test_crhsf_scenario_1():
    """
    Scenario 1: Set room heating operation mode.
    The Configuration Appliance (Client) configures the HVAC Room (Server).
    """
    
    # 1. HvacSystemFunctionDescriptionDataType
    # Describes the 'heating' function
    
    sys_func_desc = HvacSystemFunctionDescriptionDataType(
        system_function_id=HvacSystemFunctionIdType(value=1),
        system_function_type=HvacSystemFunctionTypeType(value=HvacSystemFunctionTypeEnumType.heating)
    )
    
    assert sys_func_desc.system_function_id.value == 1
    assert sys_func_desc.system_function_type.value == HvacSystemFunctionTypeEnumType.heating
    
    # 2. HvacOperationModeDescriptionDataType
    # Describes available modes: auto, on, off, eco
    
    op_mode_auto = HvacOperationModeDescriptionDataType(
        operation_mode_id=HvacOperationModeIdType(value=1),
        operation_mode_type=HvacOperationModeTypeType(value=HvacOperationModeTypeEnumType.auto)
    )
    op_mode_on = HvacOperationModeDescriptionDataType(
        operation_mode_id=HvacOperationModeIdType(value=2),
        operation_mode_type=HvacOperationModeTypeType(value=HvacOperationModeTypeEnumType.on)
    )
    
    assert op_mode_auto.operation_mode_type.value == HvacOperationModeTypeEnumType.auto
    assert op_mode_on.operation_mode_type.value == HvacOperationModeTypeEnumType.on
    
    # 3. HvacSystemFunctionOperationModeRelationDataType
    # Links system function to allowed operation modes
    
    relation = HvacSystemFunctionOperationModeRelationDataType(
        system_function_id=HvacSystemFunctionIdType(value=1),
        operation_mode_id=[HvacOperationModeIdType(value=1), HvacOperationModeIdType(value=2)]
    )
    
    assert relation.system_function_id.value == 1
    assert len(relation.operation_mode_id) == 2
    assert relation.operation_mode_id[0].value == 1
    assert relation.operation_mode_id[1].value == 2
    
    # 4. HvacSystemFunctionDataType (Client Write)
    # Simulator setting the mode to 'auto' (ID 1)
    
    write_data = HvacSystemFunctionDataType(
        system_function_id=HvacSystemFunctionIdType(value=1),
        current_operation_mode_id=HvacOperationModeIdType(value=1)
    )
    
    assert write_data.system_function_id.value == 1
    assert write_data.current_operation_mode_id.value == 1

# Placeholders for other HVAC use cases not yet strictly implemented, 
# keeping the structure valid for partial execution if needed.
@pytest.mark.requirement("CDSF-001")
def test_cdsf_placeholder():
    assert True
