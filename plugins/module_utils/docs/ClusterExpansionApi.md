# vxrail_ansible_utility.ClusterExpansionApi

All URIs are relative to *https://vxm-ip/rest/vxm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_v1_hosts_host_disk_group_info_post**](ClusterExpansionApi.md#private_v1_hosts_host_disk_group_info_post) | **POST** /private/v1/hosts/host-disk-group-info | Retrieves a list of diskgroup info with available hosts.
[**v1_cluster_expansion_cancel_post**](ClusterExpansionApi.md#v1_cluster_expansion_cancel_post) | **POST** /v1/cluster/expansion/cancel | Cancels a failed cluster expansion.
[**v1_cluster_expansion_post**](ClusterExpansionApi.md#v1_cluster_expansion_post) | **POST** /v1/cluster/expansion | Performs a cluster expansion.
[**v1_cluster_expansion_validate_post**](ClusterExpansionApi.md#v1_cluster_expansion_validate_post) | **POST** /v1/cluster/expansion/validate | Validates a cluster expansion.

# **private_v1_hosts_host_disk_group_info_post**
> HostsDiskGroupInfo private_v1_hosts_host_disk_group_info_post(body)

Retrieves a list of diskgroup info with available hosts.

Retrieves a list of diskgroup info with available hosts.

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
api_instance = vxrail_ansible_utility.ClusterExpansionApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.HostDiskGroupInfoSpec() # HostDiskGroupInfoSpec | 

try:
    # Retrieves a list of diskgroup info with available hosts.
    api_response = api_instance.private_v1_hosts_host_disk_group_info_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterExpansionApi->private_v1_hosts_host_disk_group_info_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostDiskGroupInfoSpec**](HostDiskGroupInfoSpec.md)|  | 

### Return type

[**HostsDiskGroupInfo**](HostsDiskGroupInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_expansion_cancel_post**
> v1_cluster_expansion_cancel_post()

Cancels a failed cluster expansion.

Cancels a failed cluster expansion.

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
api_instance = vxrail_ansible_utility.ClusterExpansionApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Cancels a failed cluster expansion.
    api_instance.v1_cluster_expansion_cancel_post()
except ApiException as e:
    print("Exception when calling ClusterExpansionApi->v1_cluster_expansion_cancel_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_expansion_post**
> ExpansionNodeInfo v1_cluster_expansion_post(body)

Performs a cluster expansion.

Performs a cluster expansion (layer 2 or layer 3) based on the provided expansion specification.

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
api_instance = vxrail_ansible_utility.ClusterExpansionApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.ExpansionRequest() # ExpansionRequest | Parameters to perform the cluster expansion.

try:
    # Performs a cluster expansion.
    api_response = api_instance.v1_cluster_expansion_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterExpansionApi->v1_cluster_expansion_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExpansionRequest**](ExpansionRequest.md)| Parameters to perform the cluster expansion. | 

### Return type

[**ExpansionNodeInfo**](ExpansionNodeInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_expansion_validate_post**
> ExpansionNodeInfo v1_cluster_expansion_validate_post(body)

Validates a cluster expansion.

Validates a cluster expansion (layer 2 or layer 3) based on the provided expansion specification.

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
api_instance = vxrail_ansible_utility.ClusterExpansionApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.ExpansionRequest() # ExpansionRequest | Parameters to validate the cluster expansion.

try:
    # Validates a cluster expansion.
    api_response = api_instance.v1_cluster_expansion_validate_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterExpansionApi->v1_cluster_expansion_validate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExpansionRequest**](ExpansionRequest.md)| Parameters to validate the cluster expansion. | 

### Return type

[**ExpansionNodeInfo**](ExpansionNodeInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

