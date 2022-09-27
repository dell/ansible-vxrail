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

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.4.0"

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
      The type of component to be updated. Values are vc and esxi.
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
      The password for the management account to be stored in VxRail Manager
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
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        # Added for auto-version detection
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute (ex: v1_system_update_credential_post)
        call_string = self.api_version_string + '_system_update_credential_post'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_system_update_credential_post = getattr(api_instance, call_string)
        credential, credential_dict = [], {}
        credential_dict['component'] = self.component
        credential_dict['hostname'] = self.hostname
        credential_dict['username'] = self.username
        credential_dict['password'] = self.password
        credential.append(credential_dict)
        return api_system_update_credential_post(credential)

    def post_system_update_credential(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemCredentialsApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # post system updated credential
            response = self.get_versioned_response(api_instance, "/system/update-credential")
        except ApiException as e:
            LOGGER.error("Exception when calling SystemCredentialsApi->%s_system_update_credential_post: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("Call %s/system/update-credential POST api response: %s\n", self.api_version_string, response)
        return response


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        component=dict(required=True),
        hostname=dict(required=True),
        username=dict(required=True),
        password=dict(required=True, no_log=True),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)

    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().post_system_update_credential()
    if result == 'error':
        module.fail_json(msg="Call POST /system/update-credential API failed,please see log file "
                             "/tmp/vxrail_ansible_system_update_credential.log for more error details.")
    vx_facts = {'msg': "The management user password is updated successfully"}
    vx_facts_result = dict(changed=True, System_Update_Credential_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
