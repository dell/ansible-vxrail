#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_vc_getmode

short_description: Retrieve VC and PSC mode.

description:
- This module will retrieve the current vCenter mode and PSC mode.
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
      Time out value for getting telemetry information, the default value is 60 seconds
    required: false
    type: int
    default: 60

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: false
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get VC Mode Information
    dellemc_vxrail_vc_getmode:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
VC_PSC_Mode:
  description: The current VC and PSC mode
  returned: always
  type: dict
  sample: >-
        {
                "psc_mode": "EMBEDDED",
                "vc_mode": "EMBEDDED"
        }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_vc_getmode", "/tmp/vxrail_ansible_vc_mode_info.log", log_devel=logging.DEBUG)
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
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        call_string = self.api_version_string + '_vc_vc_mode_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_system_get = getattr(api_instance, call_string)
        return api_system_get()

    def get_vc_mode(self):
        VCModeInfo = {}
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.VCenterServerModeApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query VC Mode information
            response = self.get_versioned_response(api_instance, "GET /vc/mode")
        except ApiException as e:
            LOGGER.error("Exception when calling VCenterServerModeApi->%s_vc_vc_mode_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/vc/mode api response: %s\n", self.api_version_string, response)
        data = response
        VCModeInfo['vc_mode'] = data.vc_mode
        VCModeInfo['psc_mode'] = data.psc_mode
        return dict(VCModeInfo.items())


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
    result = VxRailCluster().get_vc_mode()
    if result == 'error':
        module.fail_json(msg="Call /vc/mode API failed,please see log file /tmp/vxrail_ansible_vc_mode_info.log for more error details.")
    vx_facts = {'VC_PSC_Mode': result}
    vx_facts_result = dict(changed=False, VC_Mode_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
