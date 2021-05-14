# vxrail_ansible_utility.ClusterShutdownApi

All URIs are relative to *https://vxm-ip/rest/vxm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_cluster_shutdown_post**](ClusterShutdownApi.md#v1_cluster_shutdown_post) | **POST** /v1/cluster/shutdown | Shuts down a cluster or performs a shutdown dry run.
[**v1_requests_id_get**](ClusterShutdownApi.md#v1_requests_id_get) | **GET** /v1/requests/{id} | Gets the status and progress of cluster shutdown.

# **v1_cluster_shutdown_post**
> RequestInfo v1_cluster_shutdown_post(body=body)

Shuts down a cluster or performs a shutdown dry run.

Shuts down a cluster or performs a shutdown dry run.

### Example
```python
from __future__ import print_function
import time
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = vxrail_ansible_utility.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = vxrail_ansible_utility.ClusterShutdownApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Body() # Body | Perform an optional dry run to check whether it is safe to shut down. The default value is false. (optional)

try:
    # Shuts down a cluster or performs a shutdown dry run.
    api_response = api_instance.v1_cluster_shutdown_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterShutdownApi->v1_cluster_shutdown_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| Perform an optional dry run to check whether it is safe to shut down. The default value is false. | [optional] 

### Return type

[**RequestInfo**](RequestInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_requests_id_get**
> list[RequestStatusInfo] v1_requests_id_get(id)

Gets the status and progress of cluster shutdown.

Gets the status and progress of cluster shutdown.

### Example
```python
from __future__ import print_function
import time
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = vxrail_ansible_utility.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = vxrail_ansible_utility.ClusterShutdownApi(vxrail_ansible_utility.ApiClient(configuration))
id = 'id_example' # str | The request ID of any long running operation

try:
    # Gets the status and progress of cluster shutdown.
    api_response = api_instance.v1_requests_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterShutdownApi->v1_requests_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The request ID of any long running operation | 

### Return type

[**list[RequestStatusInfo]**](RequestStatusInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

