# Layer3ExpansionHostSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sn** | **str** | sn of the host | [optional] 
**customer_supplied** | [**CustomerSuppliedSpec**](CustomerSuppliedSpec.md) |  | [optional] 
**hostname** | **str** |  | 
**network** | [**list[HostIp]**](HostIp.md) |  | 
**accounts** | [**NodeAccount**](NodeAccount.md) |  | 
**geo_location** | [**GeoLocation**](GeoLocation.md) |  | [optional] 
**root_password** | **str** | Root password of host. | [optional] 
**is_maintenance_mode** | [**Object**](Object.md) | whether to put the host in maintenance mode or not | [optional] 
**nic_mappings** | [**list[NicUplinkV2]**](NicUplinkV2.md) |  | 
**storage** | [**StroageInfoPrivate**](StroageInfoPrivate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

