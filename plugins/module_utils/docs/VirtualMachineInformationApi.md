# vxrail_ansible_utility.VirtualMachineInformationApi

All URIs are relative to *https://vxm-ip/rest/vxm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_cluster_system_virtual_machines_get**](VirtualMachineInformationApi.md#v1_cluster_system_virtual_machines_get) | **GET** /v1/cluster/system-virtual-machines | Retrieves information about system virtual machines in the cluster.

# **v1_cluster_system_virtual_machines_get**
> list[SystemVMInfo] v1_cluster_system_virtual_machines_get()

Retrieves information about system virtual machines in the cluster.

Retrieves name, status, and host information for system virtual machines in the VxRail cluster.

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
api_instance = vxrail_ansible_utility.VirtualMachineInformationApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Retrieves information about system virtual machines in the cluster.
    api_response = api_instance.v1_cluster_system_virtual_machines_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachineInformationApi->v1_cluster_system_virtual_machines_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SystemVMInfo]**](SystemVMInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

