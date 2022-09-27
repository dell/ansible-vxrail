#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_ntp_change

short_description: Change VxRail NTP settings

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.4.0"

description:
- This module will change the system's NTP settings.
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

  components:
    description:
      Indicates if the new NTP servers are set for VxRail Manager ("VXM") or all ("ALL"). Must be fully capitalized.
      Default Value is "ALL".
    required: false
    type: str
    default: ALL

  servers:
    description:
      A list of NTP servers to be set for the system.
    required: True
    type: list
    elements: str

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for setting NTP information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Changes the VxRail NTP settings
    dellemc_vxrail_system_ntp_change:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        components: "{{ components }}"
        servers: "{{ servers }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
System_NTP_Change:
  description: Changes the VxRail NTP settings. Returns the value that was set.
  returned: always
  type: dict
  sample: >-
    {
        "servers": [
            "172.24.1.167",
            "172.23.1.167"
        ]
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_PATH = "/tmp/vxrail_ansible_system_ntp_change.log"
LOGGER = utils.get_logger("dellemc_vxrail_system_ntp_change", LOG_FILE_PATH, log_devel=logging.DEBUG)
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
        self.components = module.params.get('components')
        self.servers = module.params.get('servers')
        self.api_version_number = module.params.get('api_version_number')

        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    def get_versioned_response(self, api_instance, module_path, ntp_change_info):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number,
                                                                   module_path,
                                                                   LOGGER)

        # Calls versioned method as attribute (ex: v1_system_ntp_post)
        call_string = self.api_version_string + '_system_ntp_post'
        LOGGER.info("Using utility method: %s\n", call_string)
        system_ntp_post = getattr(api_instance, call_string)
        return system_ntp_post(ntp_change_info)

    def post_ntp(self):
        ntp_return_info = {}
        ntp_change_info = {
            'components': self.components,
            'vcenter': {
                "username": self.vc_admin,
                "password": self.vc_password
            },
            'servers': self.servers
        }

        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemInformationApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # post ntp information
            response = self.get_versioned_response(api_instance, "/system/ntp", ntp_change_info)
        except ApiException as e:
            LOGGER.error("Exception when calling SystemInformationApi->%s_system_ntp_post: %s\n",
                         self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/system/ntp POST api response: %s\n", self.api_version_string, response)
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
        components=dict(default="ALL"),
        servers=dict(type='list', elements='str', required=True),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().post_ntp()
    if result == 'error':
        module.fail_json(
            msg=f"Call POST /system/ntp API failed,please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts = {'System_NTP_Change': result}
    vx_facts_result = dict(changed=True, System_NTP_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
