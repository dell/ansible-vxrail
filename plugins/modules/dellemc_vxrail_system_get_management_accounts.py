#!/usr/bin/python
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_get_management_accounts

short_description: Retrieve VxRail Management Account Info (VC Only)

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.6.0"

description:
- This module will retrieve the VxRail System vCenter management account information
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
      Time out value for getting management account information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Retrieve VxRail Management Account Info (VC Only)
    dellemc_vxrail_system_get_management_accounts:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        api_version_number: "{{ api_version_number }}"
        timeout : "{{ timeout }}"
'''

RETURN = r'''
Management_Accounts_Info:
  description: The retrieved VxRail system management accounts information (vCenter Only)
  returned: always
  type: dict
  sample: >-
    [
        {
            "component": "VC",
            "hostname": null,
            "username": "management@vsphere.local"
        }
    ]
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

# Defining global variables
API = "GET /system/accounts/management"
MODULE = "dellemc_vxrail_system_get_management_accounts"
LOG_FILE_PATH = "/tmp/vxrail_ansible_system_get_management_accounts.log"

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
        self.api_version_number = module.params.get('api_version_number')
        self.component = "VC"  # Current version only support VC component
        self.system_url = VxrailClusterUrls(self.vxm_ip)
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
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number,
                                                                   module_path,
                                                                   LOGGER)

        # Calls versioned method as attribute (ex: v1_system_accounts_management_get)
        call_string = self.api_version_string + '_system_accounts_management_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        system_accounts_management_get = getattr(api_instance, call_string)
        return system_accounts_management_get(component=self.component)

    def get_management_accounts(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.ManagementAccountApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query management account information
            response = self.get_versioned_response(api_instance, API)
        except ApiException as e:
            LOGGER.error("Exception when calling ManagementAccountApi->%s_system_accounts_management_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s api response: %s", API, response)
        data = response
        management_account = {}
        management_accounts_list = []
        for i in range(len(data)):
            management_account['component'] = data[i].component
            management_account['hostname'] = data[i].hostname
            management_account['username'] = data[i].username
            management_accounts_list.append(dict(management_account.items()))
        return management_accounts_list


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
    result = VxRailCluster().get_management_accounts()
    if result == 'error':
        module.fail_json(
            msg=f"Call {API} API failed, please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts = {'Management_Accounts_Info': result}
    vx_facts_result = dict(changed=False, MANAGEMENT_ACCOUNTS_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
