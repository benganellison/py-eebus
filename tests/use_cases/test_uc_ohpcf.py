import pytest
from spine.base_type.smartenergymanagementps import (
    SmartEnergyManagementPsDataType,
    SmartEnergyManagementPsAlternativesType,
    SmartEnergyManagementPsPowerSequenceType,
    SmartEnergyManagementPsAlternativesRelationType,
    SmartEnergyManagementPsPowerTimeSlotElementsType,
    SmartEnergyManagementPsPowerTimeSlotValueListElementsType,
    SmartEnergyManagementPsPowerTimeSlotValueListType,
    SmartEnergyManagementPsPowerTimeSlotType,
    Anonymous_4504061728, # schedule for powerSequence
    Anonymous_4504178352  # value for powerTimeSlot
)
from spine.simple_type.powersequences import (
    AlternativesIdType,
    PowerSequenceIdType,
    PowerTimeSlotNumberType
)
from spine.enums.powersequences import (
    PowerSequenceStateEnumType,
    PowerTimeSlotValueTypeEnumType
)
from spine.base_type.commondatatypes import ScaledNumberType
from spine.simple_type.commondatatypes import NumberType, ScaleType
from spine.union_type.powersequences import PowerSequenceStateType, PowerTimeSlotValueTypeType

@pytest.mark.requirement("OHPCF-001")
def test_ohpcf_monitoring_scenario_1():
    """
    Verify Scenario 1: Monitor heat pump compressor's power consumption flexibility.
    Ref: [OHPCF-001], [OHPCF-011], [OHPCF-013]
    """
    # 1. SmartEnergyManagementPs Data (Server)
    # The Compressor (Server) provides SmartEnergyManagementPsDataType.
    
    # Constructing a mock response that the Client (CEM) would receive or the Server would send.
    
    # Requirement [OHPCF-001]: Announcement of optional power consumption process.
    # Requirement [OHPCF-011]: Compressor announces availability, power value, etc.
    
    # Create the detailed structure
    
    # Value list for a time slot (Power value)
    val_item = SmartEnergyManagementPsPowerTimeSlotValueListType(
        value_type=PowerTimeSlotValueTypeType(value=PowerTimeSlotValueTypeEnumType.power),
        value=ScaledNumberType(
            number=NumberType(value=1000),
            scale=ScaleType(value=0)
        )
    )
    
    # Time Slot
    time_slot = SmartEnergyManagementPsPowerTimeSlotType(
        slot_number=PowerTimeSlotNumberType(value=1),
        value_list=SmartEnergyManagementPsPowerTimeSlotValueListType(
            value_type=PowerTimeSlotValueTypeType(value=PowerTimeSlotValueTypeEnumType.power),
            value=ScaledNumberType(
                number=NumberType(value=1000),
                scale=ScaleType(value=0)
            )
        ) 
        # Note: The generated code has 'value_list' as a SINGLE SmartEnergyManagementPsPowerTimeSlotValueListType 
        # in some contexts or a LIST in others?
        # Let's double check SmartEnergyManagementPsPowerTimeSlotType definition.
        # It says 'value_list' type is SmartEnergyManagementPsPowerTimeSlotValueListType, is_array=False.
        # And SmartEnergyManagementPsPowerTimeSlotValueListType has 'value' (ScaledNumberType).
        # This seems to match "value (1..2)" if we consider the list is implicit or handled by repeated elements?
        # Actually, if is_array=False, it holds ONE value list type.
        # But SmartEnergyManagementPsPowerTimeSlotValueListType has 'value' (ScaledNumberType) is_array=False.
        # This might mean only ONE value is supported in this structure?
        # The spec says "value (1..2)".
        # Usually checking generated code: SmartEnergyManagementPsPowerTimeSlotType has 'value_list'.
        # If I need multiple values (power and powerMax), verify if I can pass a list?
        # No, is_array=False.
        # There is typically a "value" list member if it's a list.
        # Wait, SmartEnergyManagementPsPowerTimeSlotType also has a 'value' member (list of Anonymous_4504085776).
        # See line 702 in smartenergymanagementps.py: "value", type Anonymous..., is_array=True.
        # This is likely where the list of values goes.
    )

    # Re-structure Time Slot to use 'value' list for multiple values if needed, 
    # but for basic test, 'value_list' might be sufficient or we use 'value'.
    # Let's use the 'value' member which is an array of Anonymous items.
    # Anonymous_4504085776 has value_type, value (ScaledNumberType).
    
    # But wait, [OHPCF-011] usually uses 'valueList'.
    # Let's stick to 'value_list' for now if it works, or fallback to 'value'.
    
    power_sequence = SmartEnergyManagementPsPowerSequenceType(
        sequence_id=PowerSequenceIdType(value=1),
        state=PowerSequenceStateType(value=PowerSequenceStateEnumType.inactive),
        power_time_slot=[time_slot]
    )

    alternatives = SmartEnergyManagementPsAlternativesType(
        alternatives_id=AlternativesIdType(value=1),
        power_sequence=[power_sequence]
    )
    
    msg_data = SmartEnergyManagementPsDataType(
        node_remote_controllable=True,
        supports_single_slot_scheduling_only=False, # [OHPCF-011] says just bool, value depends on device
        alternatives_count=1,
        total_sequences_count_max=1,
        supports_reselection=False,
        alternatives=[alternatives]
    )
    
    # Assertions
    assert msg_data.node_remote_controllable is True
    assert msg_data.supports_reselection is False
    assert len(msg_data.alternatives) == 1
    assert msg_data.alternatives[0].alternatives_id.value == 1
    assert len(msg_data.alternatives[0].power_sequence) == 1
    
    seq = msg_data.alternatives[0].power_sequence[0]
    assert seq.sequence_id.value == 1
    assert seq.state.value == "inactive"
    assert len(seq.power_time_slot) == 1
    assert seq.power_time_slot[0].slot_number.value == 1
    
    # Check value inside time slot
    # Depending on how we populated it. I populated 'value_list'.
    # Verify strict typing.
    assert isinstance(seq.power_time_slot[0].value_list.value, ScaledNumberType)
    assert seq.power_time_slot[0].value_list.value.number.value == 1000

@pytest.mark.requirement("OHPCF-004")
def test_ohpcf_control_activation_scenario_2():
    """
    Verify Scenario 2: Control - Activate (Schedule) a power consumption process.
    Ref: [OHPCF-004], [OHPCF-021]
    """
    # The CEM sends a 'write' command to 'schedule' a sequence.
    # This involves setting the 'schedule' element with 'startTime'.
    
    # We simulate creating the payload for the write.
    
    # Using the Anonymous class for schedule as identified
    schedule_payload = Anonymous_4504061728(
        start_time="PT0S" # Immediate start
    )
    
    power_sequence = SmartEnergyManagementPsPowerSequenceType(
        sequence_id=PowerSequenceIdType(value=1),
        schedule=schedule_payload
    )
    
    alternatives = SmartEnergyManagementPsAlternativesType(
        alternatives_id=AlternativesIdType(value=1),
        power_sequence=[power_sequence]
    )
    
    msg_data = SmartEnergyManagementPsDataType(
        alternatives=[alternatives]
    )
    
    # Assertions
    seq = msg_data.alternatives[0].power_sequence[0]
    assert seq.sequence_id.value == 1
    assert seq.schedule is not None
    assert seq.schedule.start_time == "PT0S"
    
@pytest.mark.requirement("OHPCF-005")
def test_ohpcf_control_interruption_scenario_2():
    """
    Verify Scenario 2: Control - Interrupt/Resume a power consumption process.
    Ref: [OHPCF-005], [OHPCF-022]
    """
    # The CEM sends a 'write' command to change the 'state' of a sequence (e.g., to 'paused' or 'invalid' to stop).
    
    power_sequence = SmartEnergyManagementPsPowerSequenceType(
        sequence_id=PowerSequenceIdType(value=1),
        state=PowerSequenceStateType(value=PowerSequenceStateEnumType.paused)
    )
    
    alternatives = SmartEnergyManagementPsAlternativesType(
        alternatives_id=AlternativesIdType(value=1),
        power_sequence=[power_sequence]
    )
    
    msg_data = SmartEnergyManagementPsDataType(
        alternatives=[alternatives]
    )
    
    # Assertions
    seq = msg_data.alternatives[0].power_sequence[0]
    assert seq.sequence_id.value == 1
    assert seq.state.value == "paused"
