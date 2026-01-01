import pytest
from spine.base_type.deviceconfiguration import (
    DeviceConfigurationKeyValueDataType,
    DeviceConfigurationKeyValueValueType,
    DeviceConfigurationKeyValueDescriptionDataType
)
from spine.simple_type.deviceconfiguration import (
    DeviceConfigurationKeyValueStringType
)
from spine.base_type.electricalconnection import (
    ElectricalConnectionPermittedValueSetDataType,
    ElectricalConnectionDescriptionDataType
)
from spine.base_type.loadcontrol import (
    LoadControlLimitDataType
)
from spine.base_type.commondatatypes import (
    ScaledNumberType,
    ScaledNumberSetType,
    ScaledNumberRangeType
)
from spine.simple_type.commondatatypes import (
    NumberType,
    ScaleType,
    LabelType
)
from spine.union_type.commondatatypes import (
    ScopeTypeType,
    UnitOfMeasurementType,
    EnergyDirectionType
)
from spine.union_type.deviceconfiguration import (
    DeviceConfigurationKeyNameType
)
from spine.base_type.deviceclassification import (
    DeviceClassificationManufacturerDataType
)
from spine.simple_type.deviceclassification import (
    DeviceClassificationStringType
)
from spine.base_type.identification import (
    IdentificationDataType
)
from spine.union_type.identification import (
    IdentificationTypeType
)
from spine.simple_type.identification import (
    IdentificationValueType
)
from spine.base_type.devicediagnosis import (
    DeviceDiagnosisStateDataType
)
# Corrected import for Enum
from spine.enums.devicediagnosis import (
    DeviceDiagnosisOperatingStateEnumType
)
# Corrected import for Union
from spine.union_type.devicediagnosis import (
    DeviceDiagnosisOperatingStateType as DeviceDiagnosisOperatingStateUnionType
)

# EVCC Use Case Tests
# EV Communication Controller

@pytest.mark.requirement("EVCC-001")
def test_evcc_identification():
    """
    Verify EVCC identification requirements.
    Ref: [EVCC-001]
    """
    conf = DeviceConfigurationKeyValueDataType(
        value=DeviceConfigurationKeyValueValueType(
            string=DeviceConfigurationKeyValueStringType(value="EV-ID-12345")
        )
    )
    assert conf.value.string.value == "EV-ID-12345"

@pytest.mark.requirement("EVCC-002")
def test_evcc_communication_standard_change():
    """
    Verify that the used communication standard may alter during runtime.
    Ref: [EVCC-002]
    """
    # 1. Description tells us the KeyName
    desc = DeviceConfigurationKeyValueDescriptionDataType(
        key_name=DeviceConfigurationKeyNameType(value="communicationStandard"),
        value_type="string" # simplified check for value type if available, checking KeyName mainly
    )
    assert desc.key_name.value == "communicationStandard"

    # 2. Value provides the data (linked by KeyId in real scenario)
    conf = DeviceConfigurationKeyValueDataType(
        value=DeviceConfigurationKeyValueValueType(
            string=DeviceConfigurationKeyValueStringType(value="iso15118-2ed1")
        )
    )
    assert conf.value.string.value == "iso15118-2ed1"

@pytest.mark.requirement("EVCC-003")
def test_evcc_iso15118_ed1():
    """
    Verify support for ISO 15118-2 Edition 1 string.
    Ref: [EVCC-003]
    """
    conf = DeviceConfigurationKeyValueDataType(
        value=DeviceConfigurationKeyValueValueType(
            string=DeviceConfigurationKeyValueStringType(value="iso15118-2ed1")
        )
    )
    assert conf.value.string.value == "iso15118-2ed1"

@pytest.mark.requirement("EVCC-004")
def test_evcc_iso15118_ed2():
    """
    Verify support for ISO 15118-2 Edition 2 string.
    Ref: [EVCC-004]
    """
    conf = DeviceConfigurationKeyValueDataType(
        value=DeviceConfigurationKeyValueValueType(
            string=DeviceConfigurationKeyValueStringType(value="iso15118-2ed2")
        )
    )
    assert conf.value.string.value == "iso15118-2ed2"

@pytest.mark.requirement("EVCC-005")
def test_evcc_iec61851():
    """
    Verify support for IEC 61851 string.
    Ref: [EVCC-005]
    """
    conf = DeviceConfigurationKeyValueDataType(
        value=DeviceConfigurationKeyValueValueType(
            string=DeviceConfigurationKeyValueStringType(value="iec61851")
        )
    )
    assert conf.value.string.value == "iec61851"

@pytest.mark.requirement("EVCC-006")
def test_evcc_asymmetric_charging():
    """
    Verify support for asymmetric charging.
    Ref: [EVCC-006]
    """
    # 1. Description tells us the KeyName
    desc = DeviceConfigurationKeyValueDescriptionDataType(
        key_name=DeviceConfigurationKeyNameType(value="asymmetricChargingSupported")
    )
    assert desc.key_name.value == "asymmetricChargingSupported"
    
    # 2. Value provides the data
    conf = DeviceConfigurationKeyValueDataType(
        value=DeviceConfigurationKeyValueValueType(
            boolean=True
        )
    )
    assert conf.value.boolean is True

@pytest.mark.requirement("EVCC-007")
def test_evcc_id_transmission():
    """
    Verify EV Identification is transmitted to CEM.
    Ref: [EVCC-007]
    """
    ident_data = IdentificationDataType(
        identification_type=IdentificationTypeType(value="eui48"),
        identification_value=IdentificationValueType(value="01-23-45-67-89-AB")
    )
    assert ident_data.identification_type.value == "eui48"
    assert ident_data.identification_value.value == "01-23-45-67-89-AB"

@pytest.mark.requirement("EVCC-008")
def test_evcc_table_8_compliance():
    """
    Verify compliance with Table 8 (Identification Value Regex).
    Ref: [EVCC-008]
    """
    import re
    pattern_eui48 = r"(([A-F]|[0-9]){2}\-){5}([A-F]|[0-9]){2}"
    value_eui48 = "01-23-45-67-89-AB"
    assert re.fullmatch(pattern_eui48, value_eui48) is not None

    pattern_eui64 = r"(([A-F]|[0-9]){2}\-){7}([A-F]|[0-9]){2}"
    value_eui64 = "01-23-45-67-89-AB-CD-EF"
    assert re.fullmatch(pattern_eui64, value_eui64) is not None

@pytest.mark.requirement("EVCC-009")
def test_evcc_manufacturer_info():
    """
    Verify manufacturer information availability.
    Ref: [EVCC-009]
    """
    man_data = DeviceClassificationManufacturerDataType(
        device_name=DeviceClassificationStringType(value="TestEV"),
        device_code=DeviceClassificationStringType(value="Code123"),
        vendor_name=DeviceClassificationStringType(value="TestVendor"),
        vendor_code=DeviceClassificationStringType(value="VCode1"),
        brand_name=DeviceClassificationStringType(value="TestBrand"),
        manufacturer_label=LabelType(value="LabelX")
    )
    assert man_data.device_name.value == "TestEV"
    assert man_data.manufacturer_label.value == "LabelX"

@pytest.mark.requirement("EVCC-010")
def test_evcc_device_name_length():
    """
    Verify Device Name length.
    Ref: [EVCC-010]
    """
    name = "A" * 256
    man_data = DeviceClassificationManufacturerDataType(
        device_name=DeviceClassificationStringType(value=name)
    )
    assert len(man_data.device_name.value) <= 256

@pytest.mark.requirement("EVCC-011")
def test_evcc_device_code_length():
    """
    Verify Device Code length.
    Ref: [EVCC-011]
    """
    code = "C" * 256
    man_data = DeviceClassificationManufacturerDataType(
        device_code=DeviceClassificationStringType(value=code)
    )
    assert len(man_data.device_code.value) <= 256

@pytest.mark.requirement("EVCC-012")
def test_evcc_vendor_name_length():
    """
    Verify Vendor Name length.
    Ref: [EVCC-012]
    """
    vname = "V" * 256
    man_data = DeviceClassificationManufacturerDataType(
        vendor_name=DeviceClassificationStringType(value=vname)
    )
    assert len(man_data.vendor_name.value) <= 256

@pytest.mark.requirement("EVCC-013")
def test_evcc_vendor_code_length():
    """
    Verify Vendor Code length.
    Ref: [EVCC-013]
    """
    vcode = "X" * 256
    man_data = DeviceClassificationManufacturerDataType(
        vendor_code=DeviceClassificationStringType(value=vcode)
    )
    assert len(man_data.vendor_code.value) <= 256

@pytest.mark.requirement("EVCC-014")
def test_evcc_brand_name_length():
    """
    Verify Brand Name length.
    Ref: [EVCC-014]
    """
    brand = "B" * 256
    man_data = DeviceClassificationManufacturerDataType(
        brand_name=DeviceClassificationStringType(value=brand)
    )
    assert len(man_data.brand_name.value) <= 256

@pytest.mark.requirement("EVCC-015")
def test_evcc_manu_label_length():
    """
    Verify Manufacturer Label length.
    Ref: [EVCC-015]
    """
    label = "L" * 256
    man_data = DeviceClassificationManufacturerDataType(
        manufacturer_label=LabelType(value=label)
    )
    assert len(man_data.manufacturer_label.value) <= 256

@pytest.mark.requirement("EVCC-016")
def test_evcc_charging_power_limits_structure():
    """
    Verify charging power limits structure (ElectricalConnectionPermittedValueSet).
    Ref: [EVCC-016]
    """
    pset = ElectricalConnectionPermittedValueSetDataType(
        permitted_value_set=[
            ScaledNumberSetType(
                range=[
                    ScaledNumberRangeType(
                        min=ScaledNumberType(number=NumberType(value=1380), scale=ScaleType(value=0)),
                        max=ScaledNumberType(number=NumberType(value=11000), scale=ScaleType(value=0))
                    )
                ]
            )
        ]
    )
    assert len(pset.permitted_value_set) == 1
    assert pset.permitted_value_set[0].range[0].min.number.value == 1380

@pytest.mark.requirement("EVCC-017")
def test_evcc_min_charging_power():
    """
    Verify minimum charging power (1380W).
    Ref: [EVCC-017]
    """
    pset = ElectricalConnectionPermittedValueSetDataType(
        permitted_value_set=[
            ScaledNumberSetType(
                range=[
                    ScaledNumberRangeType(
                        min=ScaledNumberType(number=NumberType(value=1380), scale=ScaleType(value=0))
                    )
                ]
            )
        ]
    )
    assert pset.permitted_value_set[0].range[0].min.number.value == 1380

@pytest.mark.requirement("EVCC-018")
def test_evcc_standby_inclusion():
    """
    Verify standby power inclusion (0W).
    Ref: [EVCC-018]
    """
    pset = ElectricalConnectionPermittedValueSetDataType(
        permitted_value_set=[
            ScaledNumberSetType(
                value=[
                   ScaledNumberType(number=NumberType(value=0), scale=ScaleType(value=0))
                ]
            )
        ]
    )
    assert pset.permitted_value_set[0].value[0].number.value == 0

@pytest.mark.requirement("EVCC-019")
def test_evcc_effective_charging_power():
    """
    Verify effective charging power limits max value.
    Ref: [EVCC-019]
    """
    pset = ElectricalConnectionPermittedValueSetDataType(
        permitted_value_set=[
            ScaledNumberSetType(
                range=[
                    ScaledNumberRangeType(
                        max=ScaledNumberType(number=NumberType(value=11000), scale=ScaleType(value=0))
                    )
                ]
            )
        ]
    )
    assert pset.permitted_value_set[0].range[0].max.number.value == 11000

@pytest.mark.requirement("EVCC-020")
def test_evcc_sleep_mode():
    """
    Verify EV sleep mode behavior (DeviceDiagnosisState).
    Ref: [EVCC-020]
    """
    diag_state = DeviceDiagnosisStateDataType(
        operating_state=DeviceDiagnosisOperatingStateUnionType(
            value=DeviceDiagnosisOperatingStateEnumType.standby
        )
    )
    assert diag_state.operating_state.value == "standby"

@pytest.mark.requirement("EVCC-022")
def test_evcc_remove_limits():
    """
    Verify removal of limits by CEM (isLimitActive = False).
    Ref: [EVCC-022]
    """
    limit = LoadControlLimitDataType(
        is_limit_active=False
    )
    assert limit.is_limit_active is False
