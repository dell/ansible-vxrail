#!/usr/bin/python
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_hosts_update

short_description: Update the geographical location of a host

description:
- This module will update the geographical location of the specified host.
options:

  vxmip:
    description:
      The IP address of the VxRail Manager System
    required: True
    type: str

  vcadmin:
    description:
      Administrative account of the vCenter Server the VxRail Manager is registered to
    required: True
    type: str

  vcpasswd:
    description:
      The password for the administrator account provided in vcadmin
    required: True
    type: str

  host_sn:
    description:
      Serial number of the host to update
    required: True
    type: str

  rack_name:
    description:
      The updated rack name to assign the host
    required: False
    type: str

  order_number:
    description:
      The updated order number to assign the host
    required: False
    type: int

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for updating host geographical information, the default value is 60 seconds
    required: false
    type: int
    default: 1800

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Update the geographical location of the specified host
    dellemc_vxrail_system_update_proxy:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        host_sn: "{{ host_sn }}"
        rack_name: "{{ rack_name }}"
        order_number: "{{ order_number }}"
        api_version_number: "{{ api_version_number }}"
        timeout: "{{ timeout }}"
'''

RETURN = r'''
Hosts_Update:
  description: Update the VxRail System Proxy settings. Returns the values that were updated.
  returned: always
  type: dict
  sample: >-
    {
            "Request_ID": "SBI_1",
            "Request_Status": "COMPLETED"
        }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

# Defining global variables
API = "PATCH /hosts/{sn}"
MODULE = "dellemc_vxrail_hosts_update"
LOG_FILE_PATH = "/tmp/vxrail_ansible_hosts_update.log"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailClusterUrls.cluster_url.format(self.vxm_ip)


class VxRailCluster():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.host_sn = module.params.get('host_sn')
        self.rack_name = module.params.get('rack_name')
        self.order_number = module.params.get('order_number')
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        # Added for auto-version detection
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute (ex: v1_hosts_sn_patch)
        call_string = self.api_version_string + '_hosts_sn_patch'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_host_update_patch = getattr(api_instance, call_string)
        host_patch_info = {}
        host_patch_spec = {}
        if self.rack_name is not None:
            host_patch_spec["rack_name"] = self.rack_name
        if self.order_number is not None:
            host_patch_spec["order_number"] = self.order_number
        host_patch_info["geo_location"] = host_patch_spec
        return api_host_update_patch(body=host_patch_info, sn=self.host_sn)

    def patch_host(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.HostInformationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # start host update
            response = self.get_versioned_response(api_instance, "PATCH /hosts/{sn}")
        except ApiException as e:
            LOGGER.error("Exception when calling HostInformationApi->%s_host_sn_patch: %s\n", self.api_version_string, e)
            return 'error'
        requestid = response.request_id
        return requestid


def main():
    ''' Entry point into execution flow '''
    result_request_id = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        host_sn=dict(required=True),
        rack_name=dict(required=False),
        order_number=dict(type='int', required=False),
        api_version_number=dict(type='int', required=False),
        timeout=dict(type='int', default=1800)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result_request_id = VxRailCluster().patch_host()
    if result_request_id == 'error':
        module.fail_json(msg=f"Call {API} API failed,please see log file {LOG_FILE_PATH} for more error details.")
    LOGGER.info('Host Update request_id: %s.', result_request_id)
    host_sn = module.params.get('host_sn')
    rack_name = module.params.get('rack_name')
    order_number = module.params.get('order_number')
    vxmip = module.params.get('vxmip')
    vcadmin = module.params.get('vcadmin')
    vcpasswd = module.params.get('vcpasswd')
    LOGGER.info('Host SN: %s', host_sn)
    LOGGER.info('Host rack name: %s.', rack_name)
    LOGGER.info('Order number: %s.', order_number)
    task_state = 0
    time_out = 0
    initial_timeout = module.params.get('timeout')
    LOGGER.info('Timeout setting: %s seconds.', initial_timeout)
    # Check call to v1/requests/{request_id}
    result_response = utils.get_request_status(vxm_ip=vxmip, vcadmin=vcadmin, vcpasswd=vcpasswd, logger=LOGGER, request_id=result_request_id)
    if result_response == 'error':
        module.fail_json(msg="Call v1/requests/request_id API failed,please see "
                             "log file /tmp/vxrail_ansible_hosts_update.log for more error details.")
    else:
        LOGGER.info('No issues found in call to v1/requests/request_id API. Begin checking status of host update operation.')
    while task_state not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        result_response = utils.get_request_status(vxm_ip=vxmip, vcadmin=vcadmin, vcpasswd=vcpasswd, logger=LOGGER, request_id=result_request_id)
        task_state = result_response.state
        LOGGER.info('Request_status: %s', task_state)
        ''' call frequently to capture 'COMPLETED' status before host update'''
        time_out = time_out + 1
        time.sleep(1)
    error_message = result_response.error
    if task_state == 'COMPLETED' and not error_message:
        LOGGER.info("Host Update Completed")
        output_msg = "Host update has completed. Please see the logs at /tmp/vxrail_ansible_hosts_update.log for more details"
        vx_facts = {'Request_ID': result_request_id, 'Request_Status': task_state}
        vx_facts_result = dict(changed=True, Hosts_Update_API=vx_facts, msg=output_msg)
    else:
        LOGGER.info("Host update has Failed")
        output_msg = "Please see the /tmp/vxrail_ansible_hosts_update.log for more details"
        vx_facts = {'Request_ID': result_request_id}
        vx_facts_result = dict(failed=True, Hosts_Update_API=vx_facts, msg=output_msg)
    LOGGER.info('Request_info: %s', result_response)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
