#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_get_ntp

short_description: Retrieve information about the NTP servers for the cluster.

description:
- This module will retrieve information about the NTP servers for the cluster.
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
      Time out value for getting system information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get System NTP Information
    dellemc_vxrail_system_get_ntp:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
System_NTP_Info:
  description: System NTP information summary
  returned: always
  type: dict
  sample: >-
    {
        "servers": [
            "172.23.1.167",
            "172.24.1.167"
        ]
    }

'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

# Defining global variables
API = "/system/ntp"
MODULE = "dellemc_vxrail_system_get_ntp"
LOG_FILE_PATH = "/tmp/vxrail_ansible_system_get_ntp.log"
RESULT = "System_NTP_Info"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailSystemUrls():

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return f"https://{self.vxm_ip}/rest/vxm"


class VxRailSystem():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.api_version_number = module.params.get('api_version_number')

        self.system_url = VxrailSystemUrls(self.vxm_ip)
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
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path,
                                                                   LOGGER)

        # Calls versioned method as attribute (ex: v1_system_ntp_get)
        call_string = self.api_version_string + '_system_ntp_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        system_ntp_get = getattr(api_instance, call_string)
        return system_ntp_get()

    def get_api_response(self):
        ntp_return_info = {}

        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemInformationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query API
            response = self.get_versioned_response(api_instance, "GET /system/ntp")
        except ApiException as e:
            LOGGER.error("Exception when calling SystemInformationApi->%s_system_ntp_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s%s api response: %s\n", self.api_version_string, API, response)
        data = response
        ntp_return_info['servers'] = data.servers
        return dict(ntp_return_info.items())


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
    result = VxRailSystem().get_api_response()
    if result == 'error':
        module.fail_json(
            msg=f"Call {API} API failed,please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts = {RESULT: result}
    vx_facts_result = dict(changed=False, System_NTP_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
