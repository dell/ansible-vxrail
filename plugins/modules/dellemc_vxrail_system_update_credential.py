#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_update_credential

short_description: Update the management user passwords

description:
- This module will update the management user passwords that are stored in VxRail Manager for the vCenter and ESXi hosts.
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

  component:
    description:
      The type of component to be updated. Values are vc/esxi for v1/v2 API and VC/ESXI with uppercase for v3 API.
    required: True
    type: str

  hostname:
    description:
      The hostname of the vCenter or ESXi host
    required: True
    type: str

  username:
    description:
      The username for the management account
    required: True
    type: str

  password:
    description:
      The password for the management account to be stored in VxRail Manager, for v1/v2 API.
    required: True
    type: str

  current_password:
    description:
      The current password for the management account stored in VxRail Manager, only for v3 API.
    required: True
    type: str

  new_password:
    description:
      The new password for the management account to be stored in VxRail Manager, only for v3 API.
    required: True
    type: str

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for getting telemetry information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Update the management user passwords
    dellemc_vxrail_system_update_credential:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        component: "{{ component }}"
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils


LOGGER = utils.get_logger("dellemc_vxrail_system_update_credential", "/tmp/vxrail_ansible_system_update_credential.log",
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
        self.component = module.params.get('component')
        self.hostname = module.params.get('hostname')
        self.username = module.params.get('username')
        self.password = module.params.get('password')
        self.current_password = module.params.get('current_password')
        self.new_password = module.params.get('new_password')
        self.api_version_number = module.params.get('api_version_number')
        if self.api_version_number is None:
            self.api_version_number = 3
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

    def update_system_credential(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemCredentialsApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            if self.api_version_number >= 3:
                # Use PUT for v3 API
                call_string = 'v3_system_update_credential_put'
                credential_dict = {
                    'component': self.component,
                    'hostname': self.hostname,
                    'username': self.username,
                    'current_password': self.current_password,
                    'new_password': self.new_password
                }
            else:
                # Use POST for v1/v2 API
                call_string = 'v' + str(self.api_version_number) + '_system_update_credential_post'
                credential_dict = {
                    'component': self.component,
                    'hostname': self.hostname,
                    'username': self.username,
                    'password': self.password
                }
            LOGGER.info("Using utility method: %s", call_string)
            api_call = getattr(api_instance, call_string)
            response = api_call([credential_dict])
        except ApiException as e:
            LOGGER.error("Exception when calling SystemCredentialsApi->%s: %s", call_string, e)
            return 'error'
        LOGGER.info("Call %s api response: %s", call_string, response)
        return response


def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        component=dict(required=True),
        hostname=dict(required=True),
        username=dict(required=True),
        password=dict(required=False, no_log=True),
        current_password=dict(required=False, no_log=True),
        new_password=dict(required=False, no_log=True),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)

    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    api_version = module.params['api_version_number']
    if api_version >= 3:
        if not module.params['current_password'] or not module.params['new_password']:
            module.fail_json(msg="current_password and new_password are required for API version 3 and above.")
    else:
        if not module.params['password']:
            module.fail_json(msg="password is required for API versions less than 3.")
    result = VxRailCluster().update_system_credential()
    if result == 'error':
        module.fail_json(msg="Call update credential API failed, please see log file "
                             "/tmp/vxrail_ansible_system_update_credential.log for more error details.")
    vx_facts = {'msg': "The management user password is updated successfully"}
    vx_facts_result = dict(changed=True, System_Update_Credential_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
