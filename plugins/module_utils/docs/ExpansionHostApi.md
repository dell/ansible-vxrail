# vxrail_ansible_utility.ExpansionHostApi

All URIs are relative to *https://vxm-ip/rest/vxm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_cluster_add_host_post**](ExpansionHostApi.md#private_cluster_add_host_post) | **POST** /private/cluster/add-host | Host expansion validation, starts an expansion job based on the provided ExpansionSpec And this endpoint should only be called after validation has passed on
[**private_cluster_expansion_preview_get**](ExpansionHostApi.md#private_cluster_expansion_preview_get) | **GET** /private/cluster/expansion/preview | Host expansion preview, return domain name.
[**private_v1_cluster_expansion_post**](ExpansionHostApi.md#private_v1_cluster_expansion_post) | **POST** /private/v1/cluster/expansion | Host expansion, starts an expansion job based on the provided expansion spec
[**private_v2_cluster_add_host_post**](ExpansionHostApi.md#private_v2_cluster_add_host_post) | **POST** /private/v2/cluster/add-host | Host expansion validation, starts an expansion job based on the provided ExpansionSpec And this endpoint should only be called after validation has passed on
[**private_v2_cluster_expansion_validate_post**](ExpansionHostApi.md#private_v2_cluster_expansion_validate_post) | **POST** /private/v2/cluster/expansion/validate | Host expansion validation, validate form data for expansion

# **private_cluster_add_host_post**
> RequestInfo private_cluster_add_host_post(body)

Host expansion validation, starts an expansion job based on the provided ExpansionSpec And this endpoint should only be called after validation has passed on

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
api_instance = vxrail_ansible_utility.ExpansionHostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.ExpansionAddRequest() # ExpansionAddRequest | The specification for host expansion.

try:
    # Host expansion validation, starts an expansion job based on the provided ExpansionSpec And this endpoint should only be called after validation has passed on
    api_response = api_instance.private_cluster_add_host_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionHostApi->private_cluster_add_host_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExpansionAddRequest**](ExpansionAddRequest.md)| The specification for host expansion. | 

### Return type

[**RequestInfo**](RequestInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_cluster_expansion_preview_get**
> Layer2ExpansionPreviewInfo private_cluster_expansion_preview_get()

Host expansion preview, return domain name.

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
api_instance = vxrail_ansible_utility.ExpansionHostApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Host expansion preview, return domain name.
    api_response = api_instance.private_cluster_expansion_preview_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionHostApi->private_cluster_expansion_preview_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Layer2ExpansionPreviewInfo**](Layer2ExpansionPreviewInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_v1_cluster_expansion_post**
> Layer2ExpansionNodeInfo private_v1_cluster_expansion_post(body)

Host expansion, starts an expansion job based on the provided expansion spec

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
api_instance = vxrail_ansible_utility.ExpansionHostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.ExpansionAddRequest() # ExpansionAddRequest | The specification for host expansion.

try:
    # Host expansion, starts an expansion job based on the provided expansion spec
    api_response = api_instance.private_v1_cluster_expansion_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionHostApi->private_v1_cluster_expansion_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExpansionAddRequest**](ExpansionAddRequest.md)| The specification for host expansion. | 

### Return type

[**Layer2ExpansionNodeInfo**](Layer2ExpansionNodeInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_v2_cluster_add_host_post**
> RequestInfo private_v2_cluster_add_host_post(body)

Host expansion validation, starts an expansion job based on the provided ExpansionSpec And this endpoint should only be called after validation has passed on

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
api_instance = vxrail_ansible_utility.ExpansionHostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.ExpansionAddRequest() # ExpansionAddRequest | The specification for host expansion.

try:
    # Host expansion validation, starts an expansion job based on the provided ExpansionSpec And this endpoint should only be called after validation has passed on
    api_response = api_instance.private_v2_cluster_add_host_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionHostApi->private_v2_cluster_add_host_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExpansionAddRequest**](ExpansionAddRequest.md)| The specification for host expansion. | 

### Return type

[**RequestInfo**](RequestInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_v2_cluster_expansion_validate_post**
> RequestInfo private_v2_cluster_expansion_validate_post(body)

Host expansion validation, validate form data for expansion

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
api_instance = vxrail_ansible_utility.ExpansionHostApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.ExpansionValidateSpec() # ExpansionValidateSpec | The specification for host expansion validation.

try:
    # Host expansion validation, validate form data for expansion
    api_response = api_instance.private_v2_cluster_expansion_validate_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpansionHostApi->private_v2_cluster_expansion_validate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExpansionValidateSpec**](ExpansionValidateSpec.md)| The specification for host expansion validation. | 

### Return type

[**RequestInfo**](RequestInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

