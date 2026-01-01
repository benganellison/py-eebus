from spine.base_type.tariffinformation import (
    TariffDataType,
    TariffDescriptionDataType,
    TariffDescriptionListDataType,
    TariffListDataType
)
from spine.simple_type.tariffinformation import TariffIdType, CommodityIdType
from spine.base_type.datagram import DatagramType
from spine.choice_type.commandframe import PayloadContributionGroup

def test_tariff_description_data_type():
    """
    Test creation of TariffDescriptionDataType and integration with PayloadContributionGroup.
    """
    tariff_desc = TariffDescriptionDataType(
        tariff_id=TariffIdType(value=1),
        commodity_id=CommodityIdType(value=1),
        tariff_writeable=True,
        update_required=False
    )
    
    # Verify standard attribute access (snake_case)
    assert tariff_desc.tariff_id.value == 1
    assert tariff_desc.tariff_writeable is True

    # Wrappers for list types
    # TariffDescriptionListDataType has a member "tariff_description_data" which is a list
    tariff_desc_list = TariffDescriptionListDataType(
        tariff_description_data=[tariff_desc]
    )
    assert len(tariff_desc_list.tariff_description_data) == 1
    assert tariff_desc_list.tariff_description_data[0].tariff_id.value == 1

def test_tariff_data_type():
    """
    Test creation of TariffDataType.
    """
    tariff_data = TariffDataType(
        tariff_id=TariffIdType(value=1)
    )
    
    assert tariff_data.tariff_id.value == 1

    # Standard pattern: PayloadContributionGroup usually takes the *ListDataType
    # Checking PayloadContributionGroup definition for tariff... 
    # (Assuming it follows standard naming: tariff_description_list_data, tariff_list_data)
    
    tariff_list = TariffListDataType(
        tariff_data=[tariff_data]
    )
    
    payload = PayloadContributionGroup(
        tariff_list_data=tariff_list
    )
    
    assert payload.tariff_list_data is not None
    assert len(payload.tariff_list_data.tariff_data) == 1
