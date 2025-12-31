from spine.simple_type.subscriptionmanagement import SubscriptionIdType
from spine.base_type.subscriptionmanagement import (
    SubscriptionManagementEntryDataType,
    SubscriptionManagementEntryListDataType
)
from spine.choice_type.commandframe import PayloadContributionGroup

# Assuming MessageCounterType is in simple_type/commondatatypes.py based on hypothesis, 
# but I will confirm with the view_file output before running this test if I was wrong.
# For now, I'll assume it's there or just omit it if not strictly needed for this specific test 
# (though PayloadContributionGroup might not need it, the previous test used it).
# I'll stick to testing the module specific types first.

def test_uc_subscriptionmanagement():
    # Test SubscriptionManagementEntryDataType
    sub_id = SubscriptionIdType(value=456)
    entry_data = SubscriptionManagementEntryDataType(
        subscription_id=sub_id
    )

    # Test SubscriptionManagementEntryListDataType
    entry_list = SubscriptionManagementEntryListDataType(
        subscription_management_entry_data=[entry_data]
    )
    
    # Test PayloadContributionGroup
    payload = PayloadContributionGroup(
        subscription_management_entry_list_data=entry_list
    )
    
    assert payload.subscription_management_entry_list_data is not None
    assert payload.subscription_management_entry_list_data.subscription_management_entry_data is not None
    assert len(payload.subscription_management_entry_list_data.subscription_management_entry_data) == 1
    assert payload.subscription_management_entry_list_data.subscription_management_entry_data[0].subscription_id.value == 456
