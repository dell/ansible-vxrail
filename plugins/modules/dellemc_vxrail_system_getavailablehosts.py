#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_getavailablehosts

short_description: Retrieve VxRail System Available Hosts Information

description:
- This module will retrieve information about available hosts that have not been added in the VxRail cluster.
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
      Time out value for getting system information, the default value is 60 seconds
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
  - name: Get System Available Hosts Information
    dellemc_vxrail_system_getavailablehosts:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
System_Available_Hosts_Info:
  description: system available hosts information summary
  returned: always
  type: dict
  sample: >-
    {
                    "appliance_id": "V0820050000000",
                    "bios_uuid": "d5b90842-ece9-d3c5-4ff1-857dc50c8ebe",
                    "cluster_affinity": false,
                    "discovered_date": 1649861881146,
                    "id": "V0820050000000-01-01",
                    "is_primary_node": false,
                    "model": "VxRail P570F",
                    "psnt": "V0820050000000",
                    "serial_number": "V082005",
                    "slot": 1
                }

'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_PATH = "/tmp/vxrail_ansible_system_getavailablehosts.log"
LOGGER = utils.get_logger("dellemc_vxrail_system_getavailablehosts", LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailSystemUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailSystemUrls.cluster_url.format(self.vxm_ip)


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

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        call_string = self.api_version_string + '_system_available_hosts_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_system_get = getattr(api_instance, call_string)
        return api_system_get()

    def get_system_available_hosts(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemInformationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query system available hosts api
            response = self.get_versioned_response(api_instance, "GET /system/available-hosts")
        except ApiException as e:
            LOGGER.error("Exception when calling SystemInformationApi->%s_system_available_hosts_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/system/available-hosts api response: %s\n", self.api_version_string, response)
        data = response
        available_hosts = {}
        available_hosts_list = []
        for i in range(len(data)):
            available_hosts['id'] = data[i].id
            available_hosts['slot'] = data[i].slot
            available_hosts['psnt'] = data[i].psnt
            available_hosts['model'] = data[i].model
            available_hosts['serial_number'] = data[i].serial_number
            available_hosts['appliance_id'] = data[i].appliance_id
            available_hosts['is_primary_node'] = data[i].is_primary_node
            available_hosts['cluster_affinity'] = data[i].cluster_affinity
            available_hosts['discovered_date'] = data[i].discovered_date
            available_hosts['bios_uuid'] = data[i].bios_uuid
            available_hosts_list.append(dict(available_hosts.items()))
        return available_hosts_list


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
    result = VxRailSystem().get_system_available_hosts()
    if result == 'error':
        module.fail_json(
            msg="Call /system/available-hosts API failed,please see log file /tmp/vxrail_ansible_system_getavailablehosts.log for more error details.")
    vx_facts = {'System_Available_Hosts_Info': result}
    vx_facts_result = dict(changed=False, System_Available_Hosts_Info_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
