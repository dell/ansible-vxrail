# vxrail_ansible_utility.ClusterMigrationApi

All URIs are relative to *https://vxm-ip/rest/vxm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_cluster_migration_post**](ClusterMigrationApi.md#v1_cluster_migration_post) | **POST** /v1/cluster/migration | Start a cluster migration job based on input body.
[**v1_cluster_migration_validation_post**](ClusterMigrationApi.md#v1_cluster_migration_validation_post) | **POST** /v1/cluster/migration/validation | Start a cluster migration validation job based on input body.

# **v1_cluster_migration_post**
> RequestInfo v1_cluster_migration_post(body)

Start a cluster migration job based on input body.

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
api_instance = vxrail_ansible_utility.ClusterMigrationApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.ClusterMigrationRequest() # ClusterMigrationRequest | 

try:
    # Start a cluster migration job based on input body.
    api_response = api_instance.v1_cluster_migration_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterMigrationApi->v1_cluster_migration_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterMigrationRequest**](ClusterMigrationRequest.md)|  | 

### Return type

[**RequestInfo**](RequestInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_migration_validation_post**
> RequestInfo v1_cluster_migration_validation_post(body)

Start a cluster migration validation job based on input body.

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
api_instance = vxrail_ansible_utility.ClusterMigrationApi(vxrail_ansible_utility.ApiClient(configuration))
body = vxrail_ansible_utility.ClusterMigrationRequest() # ClusterMigrationRequest | 

try:
    # Start a cluster migration validation job based on input body.
    api_response = api_instance.v1_cluster_migration_validation_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterMigrationApi->v1_cluster_migration_validation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterMigrationRequest**](ClusterMigrationRequest.md)|  | 

### Return type

[**RequestInfo**](RequestInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

