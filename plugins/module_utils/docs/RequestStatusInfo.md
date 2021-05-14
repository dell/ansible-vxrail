# RequestStatusInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Each asynchronous (long-running) request returns a requestId which can be used to get the status of execution. | [optional] 
**owner** | **str** | The owner of the request which is typically the user who issue the original request | [optional] 
**state** | **str** | The current state of the execution | [optional] 
**error** | **str** | The error message if the execution state is ERROR | [optional] 
**progress** | **int** | The progress of the current execution, ranging from 0 to 100 | [optional] 
**start_time** | **int** | The start time of the current execution | [optional] 
**end_time** | **int** | The end time of the current execution | [optional] 
**target** | **str** | The target of the current execution | [optional] 
**step** | **str** | The current step if the original request has been separated into multiple steps | [optional] 
**detail** | **str** | The detailed status of a specific application | [optional] 
**extension** | **str** | The application-specific status information | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

