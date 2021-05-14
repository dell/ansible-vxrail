# ExpansionNodeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_supplied** | [**CustomerSuppliedSpec**](CustomerSuppliedSpec.md) |  | [optional] 
**host_psnt** | **str** | PSNT of the host | [optional] 
**hostname** | **str** | Hostname of the host | 
**accounts** | [**NodeAccount**](NodeAccount.md) |  | 
**network** | [**list[HostIp]**](HostIp.md) | An array of network information for the host components | 
**maintenance_mode** | **bool** | Whether the hosts remain in maintenance mode after being added to the cluster | [optional] 
**geo_location** | [**GeoLocation**](GeoLocation.md) |  | [optional] 
**nic_mappings** | [**list[NicUplinkV2]**](NicUplinkV2.md) |  | 
**storage** | [**StorageInfo**](StorageInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

