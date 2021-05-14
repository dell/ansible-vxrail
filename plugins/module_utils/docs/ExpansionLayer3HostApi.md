# vxrail_ansible_utility.ExpansionLayer3HostApi

All URIs are relative to *https://vxm-ip/rest/vxm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_cluster_layer3_add_host_post**](ExpansionLayer3HostApi.md#private_cluster_layer3_add_host_post) | **POST** /private/cluster/layer3/add-host | Start a cluster expansion job based on the provided specs
[**private_cluster_layer3_add_proxy_post**](ExpansionLayer3HostApi.md#private_cluster_layer3_add_proxy_post) | **POST** /private/cluster/layer3/add-proxy | Add a proxy node to the VxRail cluster. The proxy node represents a L3 segment.
[**private_cluster_layer3_network_topology_get**](ExpansionLayer3HostApi.md#private_cluster_layer3_network_topology_get) | **GET** /private/cluster/layer3/network/topology | Get the network type (DIFF_SUBNET, SAME_SUBNET or UNDECIDED) for different traffics (management, vSAN, vMotion).
[**private_cluster_layer3_network_topology_put**](ExpansionLayer3HostApi.md#private_cluster_layer3_network_topology_put) | **PUT** /private/cluster/layer3/network/topology | Change the network type (DIFF_SUBNET, SAME_SUBNET or UNDECIDED) for different traffics (management, vSAN, vMotion).
[**private_cluster_layer3_proxy_node_segment_label_network_get**](ExpansionLayer3HostApi.md#private_cluster_layer3_proxy_node_segment_label_network_get) | **GET** /private/cluster/layer3/proxy-node/{segment-label}/network | Get network info of an unconfigured host by ip, insist of netmask, vlanId, gateway and network type topology.
[**private_cluster_layer3_segment_label_post**](ExpansionLayer3HostApi.md#private_cluster_layer3_segment_label_post) | **POST** /private/cluster/layer3/segment-label | Generate a default segment label for the newly added segment.
[**private_cluster_layer3_segments_get**](ExpansionLayer3HostApi.md#private_cluster_layer3_segments_get) | **GET** /private/cluster/layer3/segments | Get a list of Layer 3 segments that are recognized by VxRail Manager. This information is from VxM DB.
[**private_cluster_layer3_segments_initial_segment_get**](ExpansionLayer3HostApi.md#private_cluster_layer3_segments_initial_segment_get) | **GET** /private/cluster/layer3/segments/initial-segment | Information about if initial segment information is needed.
[**private_cluster_layer3_segments_initial_segment_post**](ExpansionLayer3HostApi.md#private_cluster_layer3_segments_initial_segment_post) | **POST** /private/cluster/layer3/segments/initial-segment | Provide netmask and gateway for vSAN and vMotion traffic of segment one.
[**private_cluster_layer3_segments_segment_label_available_hosts_get**](ExpansionLayer3HostApi.md#private_cluster_layer3_segments_segment_label_available_hosts_get) | **GET** /private/cluster/layer3/segments/{segment-label}/available-hosts | Get a list of unconfigured hosts from a specific L3 segment.
[**private_cluster_layer3_segments_segment_label_network_get**](ExpansionLayer3HostApi.md#private_cluster_layer3_segments_segment_label_network_get) | **GET** /private/cluster/layer3/segments/{segment-label}/network | Get the existing network configutration for selected L3 segment. Network information like ip pools, subnet mask, gateway, etc. will be given for different traffic types.
[**private_cluster_layer3_segments_segment_label_network_management_post**](ExpansionLayer3HostApi.md#private_cluster_layer3_segments_segment_label_network_management_post) | **POST** /private/cluster/layer3/segments/{segment-label}/network/management | Provide network information for management network of the new L3 segment
[**private_cluster_layer3_segments_segment_label_network_management_preview_post**](ExpansionLayer3HostApi.md#private_cluster_layer3_segments_segment_label_network_management_preview_post) | **POST** /private/cluster/layer3/segments/{segment-label}/network/management/preview | Provide management network information for preview.
[**private_cluster_layer3_segments_segment_label_network_vsan_vmotion_preview_post**](ExpansionLayer3HostApi.md#private_cluster_layer3_segments_segment_label_network_vsan_vmotion_preview_post) | **POST** /private/cluster/layer3/segments/{segment-label}/network/vsan_vmotion/preview | Provide vsan/vmotion network information for preview.
[**private_cluster_layer3_segments_segment_label_put**](ExpansionLayer3HostApi.md#private_cluster_layer3_segments_segment_label_put) | **PUT** /private/cluster/layer3/segments/{segment-label} | Change the segment label for the current segment.
[**private_cluster_layer3_validate_post**](ExpansionLayer3HostApi.md#private_cluster_layer3_validate_post) | **POST** /private/cluster/layer3/validate | Validate data for Layer 3 cluster expansion
[**private_v2_cluster_layer3_add_host_post**](ExpansionLayer3HostApi.md#private_v2_cluster_layer3_add_host_post) | **POST** /private/v2/cluster/layer3/add-host | Start a cluster expansion job based on the provided specs to support two vds
[**private_v2_cluster_layer3_validate_post**](ExpansionLayer3HostApi.md#private_v2_cluster_layer3_validate_post) | **POST** /private/v2/cluster/layer3/validate | Validate data for Layer 3 cluster expansion

# **private_cluster_layer3_add_host_post**
> RequestInfo private_cluster_layer3_add_host_post(body)

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Layer3ExpansionStartSpec() # Layer3ExpansionStartSpec | The specs for layer 3 cluster expansion

try:
    # Start a cluster expansion job based on the provided specs
    api_response = api_instance.private_cluster_layer3_add_host_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_add_host_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Layer3ExpansionStartSpec**](Layer3ExpansionStartSpec.md)| The specs for layer 3 cluster expansion | 

### Return type

[**RequestInfo**](RequestInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_add_proxy_post**
> list[Model200] private_cluster_layer3_add_proxy_post(body)

Add a proxy node to the VxRail cluster. The proxy node represents a L3 segment.

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Body3() # Body3 | The management IP that user manually configures on the proxy node.

try:
    # Add a proxy node to the VxRail cluster. The proxy node represents a L3 segment.
    api_response = api_instance.private_cluster_layer3_add_proxy_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_add_proxy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)| The management IP that user manually configures on the proxy node. | 

### Return type

[**list[Model200]**](Model200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_network_topology_get**
> Layer3TrafficNetworkTypes private_cluster_layer3_network_topology_get()

Get the network type (DIFF_SUBNET, SAME_SUBNET or UNDECIDED) for different traffics (management, vSAN, vMotion).

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Get the network type (DIFF_SUBNET, SAME_SUBNET or UNDECIDED) for different traffics (management, vSAN, vMotion).
    api_response = api_instance.private_cluster_layer3_network_topology_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_network_topology_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Layer3TrafficNetworkTypes**](Layer3TrafficNetworkTypes.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_network_topology_put**
> Model200 private_cluster_layer3_network_topology_put(body)

Change the network type (DIFF_SUBNET, SAME_SUBNET or UNDECIDED) for different traffics (management, vSAN, vMotion).

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.ClusterNetworkTypeSpec() # ClusterNetworkTypeSpec | Netmask and gateway for vSAN and vMotion traffic of segment one.

try:
    # Change the network type (DIFF_SUBNET, SAME_SUBNET or UNDECIDED) for different traffics (management, vSAN, vMotion).
    api_response = api_instance.private_cluster_layer3_network_topology_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_network_topology_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterNetworkTypeSpec**](ClusterNetworkTypeSpec.md)| Netmask and gateway for vSAN and vMotion traffic of segment one. | 

### Return type

[**Model200**](Model200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_proxy_node_segment_label_network_get**
> ProxyNodeNetworkInfo private_cluster_layer3_proxy_node_segment_label_network_get(segment_label)

Get network info of an unconfigured host by ip, insist of netmask, vlanId, gateway and network type topology.

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
segment_label = 'segment_label_example' # str | The Ip of the proxy node that the user is filling on add-proxy web.

try:
    # Get network info of an unconfigured host by ip, insist of netmask, vlanId, gateway and network type topology.
    api_response = api_instance.private_cluster_layer3_proxy_node_segment_label_network_get(segment_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_proxy_node_segment_label_network_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_label** | **str**| The Ip of the proxy node that the user is filling on add-proxy web. | 

### Return type

[**ProxyNodeNetworkInfo**](ProxyNodeNetworkInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_segment_label_post**
> list[Model200] private_cluster_layer3_segment_label_post(body)

Generate a default segment label for the newly added segment.

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Body2() # Body2 | The management IP of the proxy node.

try:
    # Generate a default segment label for the newly added segment.
    api_response = api_instance.private_cluster_layer3_segment_label_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_segment_label_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)| The management IP of the proxy node. | 

### Return type

[**list[Model200]**](Model200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_segments_get**
> list[str] private_cluster_layer3_segments_get()

Get a list of Layer 3 segments that are recognized by VxRail Manager. This information is from VxM DB.

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Get a list of Layer 3 segments that are recognized by VxRail Manager. This information is from VxM DB.
    api_response = api_instance.private_cluster_layer3_segments_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_segments_get: %s\n" % e)
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

# **private_cluster_layer3_segments_initial_segment_get**
> Layer3SegmentOneInfoSpec private_cluster_layer3_segments_initial_segment_get()

Information about if initial segment information is needed.

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Information about if initial segment information is needed.
    api_response = api_instance.private_cluster_layer3_segments_initial_segment_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_segments_initial_segment_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Layer3SegmentOneInfoSpec**](Layer3SegmentOneInfoSpec.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_segments_initial_segment_post**
> Model200 private_cluster_layer3_segments_initial_segment_post(body)

Provide netmask and gateway for vSAN and vMotion traffic of segment one.

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Layer3SegmentOneSpec() # Layer3SegmentOneSpec | Netmask and gateway for vSAN and vMotion traffic of segment one.

try:
    # Provide netmask and gateway for vSAN and vMotion traffic of segment one.
    api_response = api_instance.private_cluster_layer3_segments_initial_segment_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_segments_initial_segment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Layer3SegmentOneSpec**](Layer3SegmentOneSpec.md)| Netmask and gateway for vSAN and vMotion traffic of segment one. | 

### Return type

[**Model200**](Model200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_segments_segment_label_available_hosts_get**
> list[Layer3VxRailHostSpec] private_cluster_layer3_segments_segment_label_available_hosts_get(segment_label)

Get a list of unconfigured hosts from a specific L3 segment.

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
segment_label = 'segment_label_example' # str | The label of the L3 segment that the user chooses.

try:
    # Get a list of unconfigured hosts from a specific L3 segment.
    api_response = api_instance.private_cluster_layer3_segments_segment_label_available_hosts_get(segment_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_segments_segment_label_available_hosts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_label** | **str**| The label of the L3 segment that the user chooses. | 

### Return type

[**list[Layer3VxRailHostSpec]**](Layer3VxRailHostSpec.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_segments_segment_label_network_get**
> Layer3NetworkInformationMap private_cluster_layer3_segments_segment_label_network_get(segment_label)

Get the existing network configutration for selected L3 segment. Network information like ip pools, subnet mask, gateway, etc. will be given for different traffic types.

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
segment_label = 'segment_label_example' # str | The label of the L3 segment that user chooses.

try:
    # Get the existing network configutration for selected L3 segment. Network information like ip pools, subnet mask, gateway, etc. will be given for different traffic types.
    api_response = api_instance.private_cluster_layer3_segments_segment_label_network_get(segment_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_segments_segment_label_network_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_label** | **str**| The label of the L3 segment that user chooses. | 

### Return type

[**Layer3NetworkInformationMap**](Layer3NetworkInformationMap.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_segments_segment_label_network_management_post**
> Model200 private_cluster_layer3_segments_segment_label_network_management_post(body, segment_label)

Provide network information for management network of the new L3 segment

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Layer3ManagementNetworkConfigSpec() # Layer3ManagementNetworkConfigSpec | The management network information provided
segment_label = 'segment_label_example' # str | The label of the L3 segment that this management network information is provide for

try:
    # Provide network information for management network of the new L3 segment
    api_response = api_instance.private_cluster_layer3_segments_segment_label_network_management_post(body, segment_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_segments_segment_label_network_management_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Layer3ManagementNetworkConfigSpec**](Layer3ManagementNetworkConfigSpec.md)| The management network information provided | 
 **segment_label** | **str**| The label of the L3 segment that this management network information is provide for | 

### Return type

[**Model200**](Model200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_segments_segment_label_network_management_preview_post**
> Layer3ExpansionPreviewInfo private_cluster_layer3_segments_segment_label_network_management_preview_post(body, segment_label)

Provide management network information for preview.

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Layer3ManagementNetworkPreviewSpec() # Layer3ManagementNetworkPreviewSpec | Netmask and gateway for vSAN and vMotion traffic of segment one.
segment_label = 'segment_label_example' # str | The label of the L3 segment that this management network information is provide for

try:
    # Provide management network information for preview.
    api_response = api_instance.private_cluster_layer3_segments_segment_label_network_management_preview_post(body, segment_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_segments_segment_label_network_management_preview_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Layer3ManagementNetworkPreviewSpec**](Layer3ManagementNetworkPreviewSpec.md)| Netmask and gateway for vSAN and vMotion traffic of segment one. | 
 **segment_label** | **str**| The label of the L3 segment that this management network information is provide for | 

### Return type

[**Layer3ExpansionPreviewInfo**](Layer3ExpansionPreviewInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_segments_segment_label_network_vsan_vmotion_preview_post**
> Layer3ExpansionPreviewInfo private_cluster_layer3_segments_segment_label_network_vsan_vmotion_preview_post(body, segment_label)

Provide vsan/vmotion network information for preview.

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Layer3VsanVmotionNetworkPreviewSpec() # Layer3VsanVmotionNetworkPreviewSpec | Provide vsan/vmotion network information for preview.
segment_label = 'segment_label_example' # str | The label of the L3 segment that this vsan/vmotion network information is provide for

try:
    # Provide vsan/vmotion network information for preview.
    api_response = api_instance.private_cluster_layer3_segments_segment_label_network_vsan_vmotion_preview_post(body, segment_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_segments_segment_label_network_vsan_vmotion_preview_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Layer3VsanVmotionNetworkPreviewSpec**](Layer3VsanVmotionNetworkPreviewSpec.md)| Provide vsan/vmotion network information for preview. | 
 **segment_label** | **str**| The label of the L3 segment that this vsan/vmotion network information is provide for | 

### Return type

[**Layer3ExpansionPreviewInfo**](Layer3ExpansionPreviewInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_segments_segment_label_put**
> list[Model200] private_cluster_layer3_segments_segment_label_put(body, segment_label)

Change the segment label for the current segment.

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Body4() # Body4 | The label of the current segment.
segment_label = 'segment_label_example' # str | The label of the current segment.

try:
    # Change the segment label for the current segment.
    api_response = api_instance.private_cluster_layer3_segments_segment_label_put(body, segment_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_segments_segment_label_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body4**](Body4.md)| The label of the current segment. | 
 **segment_label** | **str**| The label of the current segment. | 

### Return type

[**list[Model200]**](Model200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_layer3_validate_post**
> RequestInfo private_cluster_layer3_validate_post(body)

Validate data for Layer 3 cluster expansion

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Layer3ExpansionValidationRequest() # Layer3ExpansionValidationRequest | The specs for layer 3 cluster expansion

try:
    # Validate data for Layer 3 cluster expansion
    api_response = api_instance.private_cluster_layer3_validate_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_cluster_layer3_validate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Layer3ExpansionValidationRequest**](Layer3ExpansionValidationRequest.md)| The specs for layer 3 cluster expansion | 

### Return type

[**RequestInfo**](RequestInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_v2_cluster_layer3_add_host_post**
> RequestInfo private_v2_cluster_layer3_add_host_post(body)

Start a cluster expansion job based on the provided specs to support two vds

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Layer3ExpansionStartTwoVDSSpec() # Layer3ExpansionStartTwoVDSSpec | The specs for layer 3 cluster expansion

try:
    # Start a cluster expansion job based on the provided specs to support two vds
    api_response = api_instance.private_v2_cluster_layer3_add_host_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_v2_cluster_layer3_add_host_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Layer3ExpansionStartTwoVDSSpec**](Layer3ExpansionStartTwoVDSSpec.md)| The specs for layer 3 cluster expansion | 

### Return type

[**RequestInfo**](RequestInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_v2_cluster_layer3_validate_post**
> RequestInfo private_v2_cluster_layer3_validate_post(body)

Validate data for Layer 3 cluster expansion

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
api_instance = vxrail_ansible_utility.ExpansionLayer3HostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.Layer3ExpansionValidationTwoVDSRequest() # Layer3ExpansionValidationTwoVDSRequest | The specs for layer 3 cluster expansion

try:
    # Validate data for Layer 3 cluster expansion
    api_response = api_instance.private_v2_cluster_layer3_validate_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionLayer3HostApi->private_v2_cluster_layer3_validate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Layer3ExpansionValidationTwoVDSRequest**](Layer3ExpansionValidationTwoVDSRequest.md)| The specs for layer 3 cluster expansion | 

### Return type

[**RequestInfo**](RequestInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

