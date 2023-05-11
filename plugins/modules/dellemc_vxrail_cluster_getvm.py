#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_cluster_getvm

short_description: Retrieves name, status and host information for system virtual machines in the VxRail cluster.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.4.0"

description:
- This module will retrieve the name, status, and host information for system virtual machines in the VxRail cluster.
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
      Time out value for getting cluster infomation, the default value is 60 seconds
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
  - name: Retrieves name, status and host information for system virtual machines in the VxRail cluster
    dellemc_vxrail_cluster_getvm:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
System_VM_Information:
  description: system VMs information summary
  returned: always
  type: dict
  sample: >-
    [
                {
                    "host": "vcluster109-esx04.vv13xapp01.local",
                    "name": "VxRail Manager",
                    "status": "POWERED_ON"
                },
                {
                    "host": "vcluster109-esx01.vv13xapp01.local",
                    "name": "VMware vCenter Server Appliance",
                    "status": "POWERED_ON"
                }
            ]

'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_NAME = "/tmp/vxrail_ansible_cluster_getvm.log"
LOGGER = utils.get_logger("dellemc_vxrail_cluster_getvm",
                          LOG_FILE_NAME, log_devel=logging.DEBUG)
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

        call_string = self.api_version_string + '_cluster_system_virtual_machines_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_system_get = getattr(api_instance, call_string)
        return api_system_get()

    def get_cluster_system_virtual_machines(self):
        response = ''
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.VirtualMachineInformationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query cluster system virtual machines information
            response = self.get_versioned_response(api_instance, "GET /cluster/system-virtual-machines")
        except ApiException as e:
            LOGGER.error("Exception when calling VirtualMachineInformationApi->%s_cluster_system_virtual_machines_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/cluster/system-virtual-machines api response: %s\n", self.api_version_string, response)
        system_vms = {}
        system_vms_list = []
        for i in range(len(response)):
            system_vms['host'] = response[i].host
            system_vms['name'] = response[i].name
            system_vms['status'] = response[i].status
            system_vms_list.append(dict(system_vms.items()))
        return system_vms_list


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
    result = VxRailCluster().get_cluster_system_virtual_machines()
    if result == 'error':
        module.fail_json(msg="API call failed, please refer /tmp/vxrail_ansible_cluster_getvm.log")
    vx_facts = {'System_VM_Information': result}
    vx_facts_result = dict(changed=False, VirtualMachineInformation_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
