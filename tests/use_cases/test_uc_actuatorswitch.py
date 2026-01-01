from spine.union_type.actuatorswitch import ActuatorSwitchFctType
from spine.base_type.actuatorswitch import ActuatorSwitchDataType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_uc_actuatorswitch():
    # Test ActuatorSwitchFctType
    fct = ActuatorSwitchFctType(value="on")
    assert fct.value == "on"

    # Test ActuatorSwitchDataType
    switch_data = ActuatorSwitchDataType(
        function=fct
    )
    assert switch_data.function.value == "on"

    # Test PayloadContributionGroup
    payload = PayloadContributionGroup(
        actuator_switch_data=switch_data
    )
    
    assert payload.actuator_switch_data is not None
    assert payload.actuator_switch_data.function.value == "on"
