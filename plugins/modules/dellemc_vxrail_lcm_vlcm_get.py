#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm_vlcm_get

short_description: get vlcm info

description:
- This module will retry the LCM full upgrade or partial upgrade if started through the LCM API call.
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
      Time out value for LCM Upgrade Retry, the default value is 21600 seconds
    required: false
    type: int
    default: 21600

  api_version_number:
    description:
      Specify the API version to perform the upgrade.
    required: false
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

RETURN = r'''
VLCM_INFO:
  description: The current vlcm info
  returned: always
  type: dict
  sample: >-
        {
                "enable": true,
                "cluster_name": "VxRail-Virtual-SAN-Cluster-7f002c05-9e11-4c14-9e4b-e9799c19f7e6"
            }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_NAME = "/tmp/vxrail_ansible_lcm_vlcm.log"
LOGGER = utils.get_logger("dellemc_vxrail_lcm_vlcm", LOG_FILE_NAME, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
MAX_RETRY_COUNT = 8
CHECK_STATUS_INTERVAL = 360
MAX_CHECK_COUNT = 60


class VxrailVXMUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailVXMUrls.vxm_url.format(self.vxm_ip)


class VxRailLCMGetVLCM():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.vxm_url = VxrailVXMUrls(self.vxm_ip)
        self.api_version_number = module.params.get('api_version_number')
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.vxm_url.set_host()

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, module_path):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(api_version_string.split('v')[1])
        else:
            api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path,
                                                              LOGGER)
        return api_version_string

    def get_vlcm_info(self):
        try:
            # create an instance of the API class
            LOGGER.info("Retrieve cluster vLCM  information")
            api_instance = vxrail_ansible_utility.VLCMApi(vxrail_ansible_utility.ApiClient(self.configuration))
            api_version_string = self.get_versioned_response("GET /lcm/vlcm")
            call_string = 'vlcm_enablement_get_' + api_version_string
            LOGGER.info("Using utility method: %s\n", call_string)
            api_vlcm_get = getattr(api_instance, call_string)
            response = api_vlcm_get()

            LOGGER.info("Response: %s\n", response)
        except ApiException as e:
            LOGGER.error("Exception when calling %s %s, response: %s\n", api_version_string, e, response)
            return 'error'
        return response.to_dict()


def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module

    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        api_version_number=dict(type='int', required=False),
        timeout=dict(type='int', default=3600)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailLCMGetVLCM().get_vlcm_info()
    if result == 'error':
        module.fail_json(msg=f"Retrieve vLCM informations has failed. Please see the {LOG_FILE_NAME} for more details")

    vx_facts = result
    vx_facts_result = dict(VLCM_INFO=vx_facts, msg=f"Retrieve vLCM informations success. Please see the {LOG_FILE_NAME} for more details")
    LOGGER.info("vx_facts_result: %s\n", vx_facts_result)
    module.exit_json(**vx_facts_result)

if __name__ == '__main__':
    main()
