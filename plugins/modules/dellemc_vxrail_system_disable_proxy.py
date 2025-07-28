#!/usr/bin/python
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_disable_proxy

short_description: Disables the VxRail System's Proxy Configuration

description:
- This module will disable the VxRail System's Proxy Configuration.
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

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for disabling the proxy configuration, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Disable VxRail System Proxy Configuration
    dellemc_vxrail_system_disable_proxy:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
System_Proxy_Disable:
  description: Returns success message if disable is successful.
  returned: always
  type: dict
  sample: >-
        {
        "operation_successful": true
        }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

# Defining global variables
API = "DELETE /system/proxy"
MODULE = "dellemc_vxrail_system_disable_proxy"
LOG_FILE_PATH = "/tmp/vxrail_ansible_system_disable_proxy.log"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return f"https://{self.vxm_ip}/rest/vxm"


class VxRailCluster():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number,
                                                                   module_path,
                                                                   LOGGER)

        # Calls versioned method as attribute (ex: v1_system_proxy_delete)
        call_string = self.api_version_string + '_system_proxy_delete'
        LOGGER.info("Using utility method: %s\n", call_string)
        system_proxy_delete = getattr(api_instance, call_string)
        return system_proxy_delete()

    def disable_proxy_settings(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemProxySettingsApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # disable proxy configuration
            response = self.get_versioned_response(api_instance, "DELETE /system/proxy")
        except ApiException as e:
            LOGGER.error("Exception when calling SystemProxySettingsApi->%s_system_proxy_delete: %s\n", self.api_version_string, e)
            return 'error'
        success_msg = {"operation_successful": True}
        LOGGER.info("%s api response: %s (%s)", API, response, success_msg)
        return dict(success_msg)


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().disable_proxy_settings()
    if result == 'error':
        module.fail_json(
            msg=f"Call {API} API failed, please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts = {'System_Proxy_Disable': result}
    vx_facts_result = dict(changed=True, SYSTEM_PROXY_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
