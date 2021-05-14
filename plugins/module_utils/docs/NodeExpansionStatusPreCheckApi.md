# vxrail_ansible_utility.NodeExpansionStatusPreCheckApi

All URIs are relative to *https://vxm-ip/rest/vxm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_cluster_expansion_layer3_precheck_post**](NodeExpansionStatusPreCheckApi.md#private_cluster_expansion_layer3_precheck_post) | **POST** /private/cluster/expansion/layer3Precheck | Start a L3 cluster expansion job based on the provided specs
[**private_cluster_expansion_precheck_post**](NodeExpansionStatusPreCheckApi.md#private_cluster_expansion_precheck_post) | **POST** /private/cluster/expansion/precheck | Start a cluster expansion job based on the provided specs

# **private_cluster_expansion_layer3_precheck_post**
> list[NodeStatusInfoL3] private_cluster_expansion_layer3_precheck_post(body)

Start a L3 cluster expansion job based on the provided specs

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
api_instance = vxrail_ansible_utility.NodeExpansionStatusPreCheckApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.NodePreCheckRequest() # NodePreCheckRequest | Specify the segment label and serial number that needs to do the pre-check

try:
    # Start a L3 cluster expansion job based on the provided specs
    api_response = api_instance.private_cluster_expansion_layer3_precheck_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeExpansionStatusPreCheckApi->private_cluster_expansion_layer3_precheck_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodePreCheckRequest**](NodePreCheckRequest.md)| Specify the segment label and serial number that needs to do the pre-check | 

### Return type

[**list[NodeStatusInfoL3]**](NodeStatusInfoL3.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_expansion_precheck_post**
> list[NodeStatusInfo] private_cluster_expansion_precheck_post(body)

Start a cluster expansion job based on the provided specs

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
api_instance = vxrail_ansible_utility.NodeExpansionStatusPreCheckApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.NodePreCheckRequest() # NodePreCheckRequest | Specify the serial number that needs to do the pre-check

try:
    # Start a cluster expansion job based on the provided specs
    api_response = api_instance.private_cluster_expansion_precheck_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeExpansionStatusPreCheckApi->private_cluster_expansion_precheck_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodePreCheckRequest**](NodePreCheckRequest.md)| Specify the serial number that needs to do the pre-check | 

### Return type

[**list[NodeStatusInfo]**](NodeStatusInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

