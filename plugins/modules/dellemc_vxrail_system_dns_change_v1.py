#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_dns_change_v1

short_description: Change VxRail DNS settings

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.3.0"

description:
- This module will change the system's dns settings.
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
      Indicates if the new DNS servers are set for VxRail Manager ("VXM") or all ("ALL"). Must be fully capitalized.
    required: True
    type: str

  servers:
    description:
      A list of DNS servers to be set for the system. Maximum of 2.
    required: True
    type: list
    elements: str

  timeout:
    description:
      Time out value for setting dns information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Changes the VxRail DNS settings
    dellemc_vxrail_system_dns_change_v1:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        components: "{{ components }}"
        servers: "{{ servers }}"
        timeout : "{{ timeout }}"
'''

RETURN = r'''
System_DNS_Change_v1:
  description: Changes the VxRail DNS settings. Returns the value that was set.
  returned: always
  type: dict
  sample: >-
    {
        "servers": [
            "172.24.1.167",
            "172.23.1.167"
        ],
        "is_internal": false
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_PATH = "/tmp/vxrail_ansible_system_dns_change_v1.log"
LOGGER = utils.get_logger("dellemc_vxrail_system_dns_change_v1", LOG_FILE_PATH, log_devel=logging.DEBUG)
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
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

    def post_v1_dns(self):
        dns_return_info = {}
        dns_change_info = {
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
            # post v1 dns information
            response = api_instance.v1_system_dns_post(dns_change_info)
        except ApiException as e:
            LOGGER.error("Exception when calling SystemInformationApi->v1_system_dns_post: %s\n",
                         e)
            return 'error'
        LOGGER.info("v1/system/dns POST api response: %s\n", response)
        data = response
        dns_return_info['servers'] = data.servers
        dns_return_info['is_internal'] = data.is_internal
        return dict(dns_return_info.items())


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        components=dict(required=True),
        servers=dict(type='list', elements='str', required=True),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().post_v1_dns()
    if result == 'error':
        module.fail_json(
            msg=f"Call POST V1/system/dns API failed,please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts = {'System_DNS_Change_v1': result}
    vx_facts_result = dict(changed=True, V1_System_DNS_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
