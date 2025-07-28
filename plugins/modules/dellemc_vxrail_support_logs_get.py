#!/usr/bin/python
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_support_logs_get

short_description: Query the support logs.

description:
- This module will query the support logs
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

  timeout:
    description:
      Time out value for getting support log information, the default value is 60 seconds
    required: false
    type: int
    default: 60
    
  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get Support Logs
    dellemc_vxrail_support_logs_get:
        vxmip: "{{ vxmip }}"     
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Support_Logs_API:
  description: Get Support Logs
  returned: always
  type: dict
  sample: >-  [
                {
                    "creation_time": 1735111863628,
                    "id": "VxRail_Support_Bundle_5280f658-e977-7319-aa88-51ad71ccf81b_2024-12-25_07_31_03",
                    "path": "/tmp/mystic/dc/VxRail_Support_Bundle_5280f658-e977-7319-aa88-51ad71ccf81b_2024-12-25_07_31_03.zip",
                    "size": 1002496,
                    "types": null
                },
                {
                    "creation_time": 1735181237152,
                    "id": "VxRail_Support_Bundle_5280f658-e977-7319-aa88-51ad71ccf81b_2024-12-26_02_47_17",
                    "path": "/tmp/mystic/dc/VxRail_Support_Bundle_5280f658-e977-7319-aa88-51ad71ccf81b_2024-12-26_02_47_17.zip",
                    "size": 1269760,
                    "types": null
                }
              ]
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

MODULE = "dellemc_vxrail_support_logs_get"
LOG_FILE_PATH = "/tmp/vxrail_log_support_logs_get.log"
LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return f"https://{self.vxm_ip}/rest/vxm"


class VxRailCluster():
    def __init__(self):
        self.vxm_ip = module.params.get("vxmip")
        self.vc_admin = module.params.get("vcadmin")
        self.vc_password = module.params.get("vcpasswd")
        self.timeout = module.params.get('timeout')
        self.api_version_number = module.params.get("api_version_number")
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
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split("v")[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path,
                                                                   LOGGER)
            
        call_string = self.api_version_string + "_support_logs_get"

        LOGGER.info("Using utility method: %s\n", call_string)
        api_support_logs_get = getattr(api_instance, call_string)
        return api_support_logs_get()

    def get_support_logs(self):
        api_instance = vxrail_ansible_utility.SupportLogsApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = self.get_versioned_response(api_instance, "Get support/logs")
        except ApiException as e:
            LOGGER.error("Exception when calling SupportLogsApi->%s_support_logs_get: %s\n",
                         self.api_version_string, e)
            return "error"
        LOGGER.info("Call %s/support/logs Get api response: %s\n", self.api_version_string, response)
        data = response
        logs_list = []
        logs = {}
        for i in range(len(data)):
            logs["id"] = data[i].id
            logs["creation_time"] = data[i].creation_time
            logs["path"] = data[i].path
            logs["size"] = data[i].size
            logs_list.append(dict(logs.items()))
        return logs_list

def main():
    """ Entry point into execution flow """
    result = ""
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(type="str", required=True),
        vcpasswd=dict(type="str", required=True, no_log=True),
        timeout=dict(type='int', default=60),        
        api_version_number=dict(type="int")
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    result = VxRailCluster().get_support_logs()
    if result == "error":
        module.fail_json(
            msg="Call Get support/logs failed, please see log file {} for more error details.".format(LOG_FILE_PATH))
    vx_facts = {"Logs_Information": result}
    vx_facts_result = dict(changed=False, Support_Logs_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
