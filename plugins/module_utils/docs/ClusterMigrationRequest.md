# ClusterMigrationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_vc** | [**ClusterMigrationSourceVcSpec**](ClusterMigrationSourceVcSpec.md) |  | 
**target_vc** | [**ClusterMigrationTargetVcSpec**](ClusterMigrationTargetVcSpec.md) |  | 
**vxm_vm_name** | **str** | name of VxM. | [optional] 
**hosts** | [**list[ClusterMigrationHostsSpec]**](ClusterMigrationHostsSpec.md) | esxi hosts spec | [optional] 
**cluster_type** | **str** | to distinguish the cluster type | 
**witness** | [**ClusterMigrationWitnessSpec**](ClusterMigrationWitnessSpec.md) |  | [optional] 
**vds_name** | [**list[ClusterMigrationNameSpec]**](ClusterMigrationNameSpec.md) | vds name changing spec for cluster migration | [optional] 
**portgroup_name** | [**list[ClusterMigrationNameSpec]**](ClusterMigrationNameSpec.md) | portgroup name changing spec for cluster migration | [optional] 
**vm_folder_name** | [**list[ClusterMigrationNameSpec]**](ClusterMigrationNameSpec.md) | vds name changing spec for cluster migration | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

