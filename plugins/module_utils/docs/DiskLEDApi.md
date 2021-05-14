# vxrail_ansible_utility.DiskLEDApi

All URIs are relative to *https://vxm-ip/rest/vxm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_disks_disk_sn_led_put**](DiskLEDApi.md#private_disks_disk_sn_led_put) | **PUT** /private/disks/{disk_sn}/led | change sepcific disk led status

# **private_disks_disk_sn_led_put**
> private_disks_disk_sn_led_put(body, disk_sn)

change sepcific disk led status

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
api_instance = vxrail_ansible_utility.DiskLEDApi(vxrail_ansible_utility.ApiClient(configuration))
body = '\"ON\"' # str | update led status of specific disk.
disk_sn = 'disk_sn_example' # str | The sn of disk.

try:
    # change sepcific disk led status
    api_instance.private_disks_disk_sn_led_put(body, disk_sn)
except ApiException as e:
    print("Exception when calling DiskLEDApi->private_disks_disk_sn_led_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| update led status of specific disk. | 
 **disk_sn** | **str**| The sn of disk. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

