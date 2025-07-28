#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_cluster_evc_change

short_description: Change VxRail cluster EVC mode

description:
- This module will change the VxRail cluster EVC mode.
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
  evc_mode:
    description:
      The EVC mode of VxRail cluster
    required: True
    type: str
  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int
  timeout:
    description:
      Time out value for tirggering task of rebooting hosts, the default value is 60 seconds
    required: false
    type: int
    default: 60
author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>
'''

EXAMPLES = r'''
  - name: Change VxRail cluster EVC mode
    dellemc_vxrail_cluster_evc_change:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        evc_mode: "{{ evc_mode }}"
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils


# Defining global variables
MODULE = "dellemc_vxrail_cluster_evc_change"
LOG_FILE_PATH = "/tmp/dellemc_vxrail_cluster_evc_change.log"
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
        self.evc_mode = module.params.get('evc_mode')
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    def get_versioned_response(self, api_instance, module_path, change_cluster_evc_info):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute (ex: v1_cluster_evc)
        call_string = self.api_version_string + '_cluster_evc'
        LOGGER.info("Using utility method: %s\n", call_string)
        change_cluster_evc_post = getattr(api_instance, call_string)
        return change_cluster_evc_post(change_cluster_evc_info)

    def change_cluster_evc(self):
        change_cluster_evc_info = {
            'evc_mode': self.evc_mode
        }

        # create an instance of the API class
        api_instance = vxrail_ansible_utility.ConfigureTheClusterEVCModeApi(vxrail_ansible_utility.ApiClient(self.configuration))
        LOGGER.info(change_cluster_evc_info)
        try:
            response = self.get_versioned_response(api_instance, "POST /cluster/evc", change_cluster_evc_info)
        except ApiException as e:
            LOGGER.error("Exception when calling ConfigureTheClusterEVCModeApi->%s_change_cluster_evc_info: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/cluster/evc api response: %s\n", self.api_version_string, response)
        return response


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        evc_mode=dict(type='str', required=True),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().change_cluster_evc()
    if result == 'error':
        module.fail_json(msg=f"Call POST /cluster/evc API failed. See log file {LOG_FILE_PATH} for more error details.")
    vx_facts_result = dict(changed=True, msg="Cluster EVC is updated successfully")
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
