#!/usr/bin/python
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_support_logs

short_description: vxrail support logs

description:
- This module will collect the support logs with the specified types.
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
  
  types:
    description:
      The types of the log to collect. Include: vxm, vcenter, esxi, idrac, ptagent, connectivity. Connectivity is supported starting from VxRail 8.0.330. User can enter one or more types, and use comma "," to seperate the types. e.g. esxi,vxm
    required: True
    type: str

  nodes:
    description:
      The service tags of the log to collect. If "types" contains "esxi" or "idrac" or "ptagent", parameter "nodes" must be supplied. Use comma "," to seperate the nodes. e.g. node1,node2
    required: False
    type: str

  autoclean:
    description:
      If disk space is not enough, auto clean the existing log files.
    required: False
    type: str

  timeout:
    description:
      Time out value for creating support log, the default value is 60 seconds
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
  - name: Create Support Log
    dellemc_vxrail_support_logs:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        types: "{{ types }}"
        nodes: "{{ nodes }}"
        autoclean: "{{ autoclean }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"       
'''

RETURN = r'''
Support_Logs_API:
  description: Create Support Log
  returned: always
  type: dict
  sample: >-
    {
      "request_id": "5ffe7062-a590-45b8-a172-8d2cf119562e"
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

MODULE = "dellemc_vxrail_support_logs"
LOG_FILE_PATH = "/tmp/vxrail_support_logs.log"
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
        self.types = module.params.get("types")
        self.nodes = module.params.get("nodes")
        self.autoclean = module.params.get("autoclean")
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
        call_string = self.api_version_string + "_support_logs_post"

        LOGGER.info("Using utility method: %s\n", call_string)
        api_support_logs_post = getattr(api_instance, call_string)
        log_collection_info = self.create_support_logs_json()
        return api_support_logs_post(log_collection_info)

    def create_support_logs_json(self):
        support_logs_request = {}

        support_logs_request["types"] = self.types.split(",")

        if self.nodes and len(self.nodes.split(",")) != 0:
            support_logs_request["nodes"] = self.nodes.split(",")
        support_logs_request["autoclean"] = self.autoclean
        
        return support_logs_request

    def collect_logs(self):
        api_instance = vxrail_ansible_utility.SupportLogsApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = self.get_versioned_response(api_instance, "Post support/logs")
        except ApiException as e:
            LOGGER.error("Exception when calling SupportLogsApi->%s_collect_logs_post: %s\n",
                         self.api_version_string, e)
            return "error"
        LOGGER.info("Call %s/support/logs POST api response: %s\n", self.api_version_string, response)
        return response.to_dict()


def main():
    """ Entry point into execution flow """
    result = ""
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(type="str", required=True),
        vcpasswd=dict(type="str", required=True, no_log=True),
        types=dict(type="str", required=True),
        nodes=dict(type="str", required=False),
        autoclean=dict(type="bool", required=False, default=False),
        timeout=dict(type='int', default=60),
        api_version_number=dict(type="int")
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().collect_logs()
    if result == "error":
        module.fail_json(
            msg="Call Post support/logs API failed, please see log file {} for more error details.".format(LOG_FILE_PATH))
    vx_facts = {"Logs_Information": result}
    vx_facts_result = dict(changed=False, Support_Logs_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
