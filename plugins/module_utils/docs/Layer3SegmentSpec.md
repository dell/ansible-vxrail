# Layer3SegmentSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_label** | **str** | The name of the segment | 
**proxy_ip** | **str** | The IP address of the node which provides proxy service | [optional] 
**management_gateway** | **str** | The IPv4 gateway address of the management traffic for the current segment | [optional] 
**management_netmask** | **str** | The subnet mask of the management traffic for the current segment | [optional] 
**management_vlan** | **int** | The VLAN ID of the management traffic for the current segment | [optional] 
**vsan_gateway** | **str** | The IPv4 gateway address of the vSAN traffic for the current segment | [optional] 
**management_topology** | **str** | The topology type for management traffic for the VxRail cluster | [optional] 
**vsan_netmask** | **str** | The subnet mask for the vSAN traffic for the current segment | [optional] 
**vsan_vlan** | **int** | The VLAN ID for the vSAN traffic for the current segment | [optional] 
**vsan_init_gateway** | **str** | The IPv4 gateway address of the vSAN traffic for the initial segment. **Note:** When vsan_topology is set as DIFF_SUBNET, this value must be provided during the first L3 segment creation. | [optional] 
**vsan_topology** | **str** | The topology type for the vSAN traffic for the VxRail cluster | [optional] 
**vmotion_gateway** | **str** | The IPv4 gateway address of the vMotion traffic of the current segment | [optional] 
**vmotion_netmask** | **str** | The subnet mask for the vMotion traffic of the current segment | [optional] 
**vmotion_vlan** | **int** | The VLAN ID for the vMotion traffic of the current segment | [optional] 
**vmotion_init_gateway** | **str** | The IPv4 gateway address of the vMotion traffic for the initial segment. **Note:** When vmotion_topology is set as DIFF_SUBNET, this value must be provided during the first L3 segment creation. | [optional] 
**vmotion_topology** | **str** | The topology type for the vMotion traffic for the VxRail cluster | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

