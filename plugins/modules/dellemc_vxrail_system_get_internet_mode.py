#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_get_internet_mode

short_description: Retrieve VxRail Internet Mode

description:
- This module will retrieve the system's Internet Mode Information.
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
      Time out value for getting internet mode information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get Internet Mode Information
    dellemc_vxrail_system_get_internet_mode:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Internet_Mode:
  description: The currently-set Internet Mode
  returned: always
  type: dict
  sample: >-
        {
            "is_dark_site": false
        }

'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_system_get_internet_mode",
                          "/tmp/vxrail_ansible_system_get_internet_mode.log",
                          log_devel=logging.DEBUG)
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
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        self.api_version_number = module.params.get('api_version_number')

        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number,
                                                                   module_path,
                                                                   LOGGER)

        # Calls versioned method as attribute (ex: v1_system_internet_mode_get)
        call_string = self.api_version_string + '_system_internet_mode_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        system_internet_mode_get = getattr(api_instance, call_string)
        return system_internet_mode_get()

    def get_internet_mode(self):
        internet_mode_info = {}
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemNetworkApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query internet mode information
            response = self.get_versioned_response(api_instance, "GET /system/internet-mode")
        except ApiException as e:
            LOGGER.error("Exception when calling SystemNetworkApi->%s_system_internet_mode_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/system/internet-mode api response: %s\n", self.api_version_string, response)
        data = response
        internet_mode_info['is_dark_site'] = data.is_dark_site
        return dict(internet_mode_info.items())


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        timeout=dict(type='int', default=60),
        api_version_number=dict(type='int')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().get_internet_mode()
    if result == 'error':
        module.fail_json(msg="Call /system/internet-mode API failed,"
                             "please see log file /tmp/dellemc_vxrail_system_get_internet_mode.log for more error details.")
    vx_facts = {'Internet_Mode': result}
    vx_facts_result = dict(changed=False, System_Internet_Mode_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
