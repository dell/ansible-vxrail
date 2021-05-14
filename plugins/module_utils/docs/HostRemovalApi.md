# vxrail_ansible_utility.HostRemovalApi

All URIs are relative to *https://vxm-ip/rest/vxm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_cluster_remove_host_post**](HostRemovalApi.md#v1_cluster_remove_host_post) | **POST** /v1/cluster/remove-host | Removes a host from the cluster.

# **v1_cluster_remove_host_post**
> RequestInfo v1_cluster_remove_host_post(body)

Removes a host from the cluster.

Removes a host from the cluster.

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
api_instance = vxrail_ansible_utility.HostRemovalApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.RemoveHostSpec() # RemoveHostSpec | The user-specified host to be removed

try:
    # Removes a host from the cluster.
    api_response = api_instance.v1_cluster_remove_host_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostRemovalApi->v1_cluster_remove_host_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoveHostSpec**](RemoveHostSpec.md)| The user-specified host to be removed | 

### Return type

[**RequestInfo**](RequestInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

