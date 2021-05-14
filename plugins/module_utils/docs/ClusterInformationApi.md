# vxrail_ansible_utility.ClusterInformationApi

All URIs are relative to *https://vxm-ip/rest/vxm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_cluster_network_nsxt_get**](ClusterInformationApi.md#private_cluster_network_nsxt_get) | **GET** /private/cluster/network/nsxt | Get NSX-T network information.
[**v1_cluster_get**](ClusterInformationApi.md#v1_cluster_get) | **GET** /v1/cluster | Retrieves VxRail cluster information.

# **private_cluster_network_nsxt_get**
> NsxtInfo private_cluster_network_nsxt_get()

Get NSX-T network information.

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
api_instance = vxrail_ansible_utility.ClusterInformationApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Get NSX-T network information.
    api_response = api_instance.private_cluster_network_nsxt_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterInformationApi->private_cluster_network_nsxt_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NsxtInfo**](NsxtInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_get**
> ClusterInfo v1_cluster_get()

Retrieves VxRail cluster information.

Retrieves VxRail cluster information and basic information about the appliances in the cluster.

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
api_instance = vxrail_ansible_utility.ClusterInformationApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Retrieves VxRail cluster information.
    api_response = api_instance.v1_cluster_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterInformationApi->v1_cluster_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterInfo**](ClusterInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

