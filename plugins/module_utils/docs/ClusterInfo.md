# ClusterInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The UUID of the VxRail cluster | [optional] 
**product_type** | **str** | Product type of the host | [optional] 
**device_type** | **str** | Device type of the host | [optional] 
**vc_connected** | **bool** | Whether the vCenter is connected | [optional] 
**health** | **str** | Status of the health of the cluster. Supported values are Critical, Error, Warning, and Healthy. | [optional] 
**operational_status** | **str** | Operational status information | [optional] 
**chassis** | [**list[ChassisBasicInfo]**](ChassisBasicInfo.md) |  | [optional] 
**suppressed** | **bool** | Whether under suppression mode or not | [optional] 
**last_time** | **int** | The last time the cluster was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

