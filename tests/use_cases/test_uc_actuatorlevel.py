from spine.union_type.actuatorlevel import ActuatorLevelFctType
from spine.base_type.actuatorlevel import ActuatorLevelDataType, ActuatorLevelDescriptionDataType, ActuatorLevelDataElementsType
from spine.choice_type.commandframe import PayloadContributionGroup
from spine.base_type.actuatorlevel import ActuatorLevelDescriptionDataElementsType

def test_uc_actuatorlevel():
    # Test ActuatorLevelFctType (UnionType mocked as value type)
    fct = ActuatorLevelFctType(value="set")
    assert fct.value == "set"

    # Test ActuatorLevelDataType
    actuator_data = ActuatorLevelDataType(
        function=fct
    )
    assert actuator_data.function.value == "set"

    # Test PayloadContributionGroup integration
    payload = PayloadContributionGroup(
        actuator_level_data=actuator_data
    )
    
    assert payload.actuator_level_data is not None
    assert payload.actuator_level_data.function.value == "set"

def test_uc_actuatorlevel_description():
    # Glue code coverage for Description types
    desc = ActuatorLevelDescriptionDataType()
    payload = PayloadContributionGroup(
        actuator_level_description_data=desc
    )
    assert payload.actuator_level_description_data is not None
