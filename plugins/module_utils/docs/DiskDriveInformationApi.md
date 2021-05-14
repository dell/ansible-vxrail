# vxrail_ansible_utility.DiskDriveInformationApi

All URIs are relative to *https://vxm-ip/rest/vxm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_disks_disk_sn_get**](DiskDriveInformationApi.md#v1_disks_disk_sn_get) | **GET** /v1/disks/{disk_sn} | Retrieves information about a specific disk.
[**v1_disks_get**](DiskDriveInformationApi.md#v1_disks_get) | **GET** /v1/disks | Retrieves a list of disks and their associated information.

# **v1_disks_disk_sn_get**
> DiskInfo v1_disks_disk_sn_get(disk_sn)

Retrieves information about a specific disk.

Retrieves information about a specific disk drive.

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
api_instance = vxrail_ansible_utility.DiskDriveInformationApi(vxrail_ansible_utility.ApiClient(configuration))
disk_sn = 'disk_sn_example' # str | The serial number of disk that you want to query.

try:
    # Retrieves information about a specific disk.
    api_response = api_instance.v1_disks_disk_sn_get(disk_sn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiskDriveInformationApi->v1_disks_disk_sn_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk_sn** | **str**| The serial number of disk that you want to query. | 

### Return type

[**DiskInfo**](DiskInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_disks_get**
> list[DiskInfo] v1_disks_get()

Retrieves a list of disks and their associated information.

Retrieves a list of disk drives and their associated information.

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
api_instance = vxrail_ansible_utility.DiskDriveInformationApi(vxrail_ansible_utility.ApiClient(configuration))

try:
    # Retrieves a list of disks and their associated information.
    api_response = api_instance.v1_disks_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiskDriveInformationApi->v1_disks_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DiskInfo]**](DiskInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

