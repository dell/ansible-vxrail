# vxrail_ansible_utility.SegmentEntityManagementApi

All URIs are relative to *https://vxm-ip/rest/vxm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_v1_cluster_layer3_initial_segment_network_info_get**](SegmentEntityManagementApi.md#private_v1_cluster_layer3_initial_segment_network_info_get) | **GET** /private/v1/cluster/layer3/initial-segment/network-info | Retrieves the intial rack node network configuration.
[**private_v1_cluster_layer3_segments_configured_hosts_count_get**](SegmentEntityManagementApi.md#private_v1_cluster_layer3_segments_configured_hosts_count_get) | **GET** /private/v1/cluster/layer3/segments/configured-hosts/count | Get the count of configured hosts per segment.
[**v1_cluster_layer3_segment_post**](SegmentEntityManagementApi.md#v1_cluster_layer3_segment_post) | **POST** /v1/cluster/layer3/segment | Creates a new segment.
[**v1_cluster_layer3_segment_segment_label_delete**](SegmentEntityManagementApi.md#v1_cluster_layer3_segment_segment_label_delete) | **DELETE** /v1/cluster/layer3/segment/{segment-label} | Deletes a segment.
[**v1_cluster_layer3_segment_segment_label_get**](SegmentEntityManagementApi.md#v1_cluster_layer3_segment_segment_label_get) | **GET** /v1/cluster/layer3/segment/{segment-label} | Retrieves the segment configuration for a specific segment.
[**v1_cluster_layer3_segment_segment_label_health_get**](SegmentEntityManagementApi.md#v1_cluster_layer3_segment_segment_label_health_get) | **GET** /v1/cluster/layer3/segment/{segment-label}/health | Retrieves the health status for a specific segment.
[**v1_cluster_layer3_segment_segment_label_patch**](SegmentEntityManagementApi.md#v1_cluster_layer3_segment_segment_label_patch) | **PATCH** /v1/cluster/layer3/segment/{segment-label} | Changes the segment label for the current segment.
[**v1_cluster_layer3_segment_segment_label_post**](SegmentEntityManagementApi.md#v1_cluster_layer3_segment_segment_label_post) | **POST** /v1/cluster/layer3/segment/{segment-label} | Updates the segment configuration for a specific segment.
[**v1_cluster_layer3_segments_get**](SegmentEntityManagementApi.md#v1_cluster_layer3_segments_get) | **GET** /v1/cluster/layer3/segments | Retrieves a list of layer 3 segments that are recognized by VxRail Manager.

# **private_v1_cluster_layer3_initial_segment_network_info_get**
> Layer3SegmentSpec private_v1_cluster_layer3_initial_segment_network_info_get()

Retrieves the intial rack node network configuration.

Retrieves the intial rack node network configuration.

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
api_instance = vxrail_ansible_utility.SegmentEntityManagementApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Retrieves the intial rack node network configuration.
    api_response = api_instance.private_v1_cluster_layer3_initial_segment_network_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentEntityManagementApi->private_v1_cluster_layer3_initial_segment_network_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Layer3SegmentSpec**](Layer3SegmentSpec.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_v1_cluster_layer3_segments_configured_hosts_count_get**
> list[SegmentHostStatisticsInfo] private_v1_cluster_layer3_segments_configured_hosts_count_get()

Get the count of configured hosts per segment.

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
api_instance = vxrail_ansible_utility.SegmentEntityManagementApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Get the count of configured hosts per segment.
    api_response = api_instance.private_v1_cluster_layer3_segments_configured_hosts_count_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentEntityManagementApi->private_v1_cluster_layer3_segments_configured_hosts_count_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SegmentHostStatisticsInfo]**](SegmentHostStatisticsInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_layer3_segment_post**
> list[Model200] v1_cluster_layer3_segment_post(body)

Creates a new segment.

Creates a new segment.

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
api_instance = vxrail_ansible_utility.SegmentEntityManagementApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Layer3SegmentStartSpec() # Layer3SegmentStartSpec | Information about the segment configuration, including the proxy IP, gateway, netmask, VLAN, and topology.

try:
    # Creates a new segment.
    api_response = api_instance.v1_cluster_layer3_segment_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentEntityManagementApi->v1_cluster_layer3_segment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Layer3SegmentStartSpec**](Layer3SegmentStartSpec.md)| Information about the segment configuration, including the proxy IP, gateway, netmask, VLAN, and topology. | 

### Return type

[**list[Model200]**](Model200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_layer3_segment_segment_label_delete**
> list[Model200] v1_cluster_layer3_segment_segment_label_delete(segment_label)

Deletes a segment.

Deletes a segment.

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
api_instance = vxrail_ansible_utility.SegmentEntityManagementApi(vxrail_ansible_utility.ApiClient(configuration))
segment_label = 'segment_label_example' # str | The label of the current segment to be acted upon.

try:
    # Deletes a segment.
    api_response = api_instance.v1_cluster_layer3_segment_segment_label_delete(segment_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentEntityManagementApi->v1_cluster_layer3_segment_segment_label_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_label** | **str**| The label of the current segment to be acted upon. | 

### Return type

[**list[Model200]**](Model200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_layer3_segment_segment_label_get**
> Layer3SegmentSpec v1_cluster_layer3_segment_segment_label_get(segment_label)

Retrieves the segment configuration for a specific segment.

Retrieves the segment configuration for a specific segment.

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
api_instance = vxrail_ansible_utility.SegmentEntityManagementApi(vxrail_ansible_utility.ApiClient(configuration))
segment_label = 'segment_label_example' # str | The label of the current segment to be acted upon.

try:
    # Retrieves the segment configuration for a specific segment.
    api_response = api_instance.v1_cluster_layer3_segment_segment_label_get(segment_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentEntityManagementApi->v1_cluster_layer3_segment_segment_label_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_label** | **str**| The label of the current segment to be acted upon. | 

### Return type

[**Layer3SegmentSpec**](Layer3SegmentSpec.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_layer3_segment_segment_label_health_get**
> list[SegmentStatusInfo] v1_cluster_layer3_segment_segment_label_health_get(segment_label)

Retrieves the health status for a specific segment.

Retrieves the health status for a specific segment.

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
api_instance = vxrail_ansible_utility.SegmentEntityManagementApi(vxrail_ansible_utility.ApiClient(configuration))
segment_label = 'segment_label_example' # str | The label of the segment that you want to query.

try:
    # Retrieves the health status for a specific segment.
    api_response = api_instance.v1_cluster_layer3_segment_segment_label_health_get(segment_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentEntityManagementApi->v1_cluster_layer3_segment_segment_label_health_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_label** | **str**| The label of the segment that you want to query. | 

### Return type

[**list[SegmentStatusInfo]**](SegmentStatusInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_layer3_segment_segment_label_patch**
> list[Model200] v1_cluster_layer3_segment_segment_label_patch(body, segment_label)

Changes the segment label for the current segment.

Changes the segment label for the current segment.

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
api_instance = vxrail_ansible_utility.SegmentEntityManagementApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Body1() # Body1 | The new label that you want the segment to be changed to.
segment_label = 'segment_label_example' # str | The label of the current segment to be acted upon.

try:
    # Changes the segment label for the current segment.
    api_response = api_instance.v1_cluster_layer3_segment_segment_label_patch(body, segment_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentEntityManagementApi->v1_cluster_layer3_segment_segment_label_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)| The new label that you want the segment to be changed to. | 
 **segment_label** | **str**| The label of the current segment to be acted upon. | 

### Return type

[**list[Model200]**](Model200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_layer3_segment_segment_label_post**
> list[Model200] v1_cluster_layer3_segment_segment_label_post(body, segment_label)

Updates the segment configuration for a specific segment.

Updates the segment configuration for a specific segment.

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
api_instance = vxrail_ansible_utility.SegmentEntityManagementApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Layer3SegmentStartSpec() # Layer3SegmentStartSpec | Information about the segment configuration, including the proxy IP, gateway, netmask, VLAN, and topology.
segment_label = 'segment_label_example' # str | The label of the current segment to be acted upon.

try:
    # Updates the segment configuration for a specific segment.
    api_response = api_instance.v1_cluster_layer3_segment_segment_label_post(body, segment_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentEntityManagementApi->v1_cluster_layer3_segment_segment_label_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Layer3SegmentStartSpec**](Layer3SegmentStartSpec.md)| Information about the segment configuration, including the proxy IP, gateway, netmask, VLAN, and topology. | 
 **segment_label** | **str**| The label of the current segment to be acted upon. | 

### Return type

[**list[Model200]**](Model200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_layer3_segments_get**
> list[str] v1_cluster_layer3_segments_get()

Retrieves a list of layer 3 segments that are recognized by VxRail Manager.

Retrieves a list of layer 3 segments that are recognized by VxRail Manager.

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
api_instance = vxrail_ansible_utility.SegmentEntityManagementApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Retrieves a list of layer 3 segments that are recognized by VxRail Manager.
    api_response = api_instance.v1_cluster_layer3_segments_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentEntityManagementApi->v1_cluster_layer3_segments_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

