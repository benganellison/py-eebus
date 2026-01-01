import pytest
from spine.base_type.devicediagnosis import DeviceDiagnosisStateDataType
from spine.base_type.deviceclassification import DeviceClassificationManufacturerDataType
from spine.enums.devicediagnosis import DeviceDiagnosisOperatingStateEnumType
from spine.simple_type.deviceclassification import DeviceClassificationStringType
from spine.simple_type.commondatatypes import LabelType
from spine.union_type.devicediagnosis import DeviceDiagnosisOperatingStateType

# EVSECC Use Case Tests
# EVSE Commissioning and Configuration
# Ref: EEBus_UC_TS_EVSECommissioningAndConfiguration_V1.0.1.pdf

@pytest.mark.requirement("EVSECC-010")
def test_evsecc_device_name():
    """
    Verify Device Name support.
    Ref: [EVSECC-010]
    """
    data = DeviceClassificationManufacturerDataType(device_name=DeviceClassificationStringType(value="MyEVSE"))
    assert data.device_name.value == "MyEVSE"

@pytest.mark.requirement("EVSECC-011")
def test_evsecc_device_code():
    """
    Verify Device Code support.
    Ref: [EVSECC-011]
    """
    data = DeviceClassificationManufacturerDataType(device_code=DeviceClassificationStringType(value="EVSE-1234"))
    assert data.device_code.value == "EVSE-1234"

@pytest.mark.requirement("EVSECC-012")
def test_evsecc_vendor_name():
    """
    Verify Vendor Name support.
    Ref: [EVSECC-012]
    """
    data = DeviceClassificationManufacturerDataType(vendor_name=DeviceClassificationStringType(value="ACME Corp"))
    assert data.vendor_name.value == "ACME Corp"

@pytest.mark.requirement("EVSECC-013")
def test_evsecc_vendor_code():
    """
    Verify Vendor Code support.
    Ref: [EVSECC-013]
    """
    data = DeviceClassificationManufacturerDataType(vendor_code=DeviceClassificationStringType(value="VC-99"))
    assert data.vendor_code.value == "VC-99"

@pytest.mark.requirement("EVSECC-014")
def test_evsecc_brand_name():
    """
    Verify Brand Name support.
    Ref: [EVSECC-014]
    """
    data = DeviceClassificationManufacturerDataType(brand_name=DeviceClassificationStringType(value="SuperCharger"))
    assert data.brand_name.value == "SuperCharger"

@pytest.mark.requirement("EVSECC-015")
def test_evsecc_manufacturer_label():
    """
    Verify Manufacturer Label support.
    Ref: [EVSECC-015]
    """
    data = DeviceClassificationManufacturerDataType(manufacturer_label=LabelType(value="Wallbox"))
    assert data.manufacturer_label.value == "Wallbox"

@pytest.mark.requirement("EVSECC-020")
def test_evsecc_error_state():
    """
    Verify EVSE Error State (Scenario 2).
    Ref: [EVSECC-020]
    """
    # Indicates errors of the EVSE to the user.
    # Uses DeviceDiagnosisStateDataType
    state = DeviceDiagnosisStateDataType(
        operating_state=DeviceDiagnosisOperatingStateType(value=DeviceDiagnosisOperatingStateEnumType.failure)
    )
    assert state.operating_state.value == "failure"

@pytest.mark.requirement("EVSECC-020/1")
def test_evsecc_normal_operation():
    """
    Verify Normal Operation state.
    """
    state = DeviceDiagnosisStateDataType(
        operating_state=DeviceDiagnosisOperatingStateType(value=DeviceDiagnosisOperatingStateEnumType.normalOperation)
    )
    assert state.operating_state.value == "normalOperation"
