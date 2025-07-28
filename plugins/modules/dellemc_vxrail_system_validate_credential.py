#!/usr/bin/python
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_validate_credential

short_description: Validate VxRail System Credential

description:
- This module will validate the username and password for the specified software components.
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

  vc_root_account:
    description:
      Root account of the vCenter Server the VxRail Manager is registered to
    required: False
    type: str

  vc_root_passwd:
    description:
      The password for the rFalseoot account provided in vcroot
    required: False
    type: str

  psc_root_account:
    description:
      Root account of the PSC the VxRail Manager is registered to
    required: False
    type: str

  psc_root_passwd:
    description:
      The password for the root account provided in PSC
    required: False
    type: str

  host_sn:
    description:
      The SN of the host
    required: False
    type: str

  host_root_account:
    description:
      Root account of the host
    required: False
    type: str

  host_root_passwd:
    description:
      The password for the root account provided in host
    required: False
    type: str

  timeout:
    description:
      Time out value for updating proxy information, the default value is 60 seconds
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
  - name: Validate VxRail System Credential
    dellemc_vxrail_system_validate_credential:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
        psc_root_account: "{{ psc_root_account }}"
        psc_root_passwd: "{{ psc_root_passwd }}"
        host_sn: "{{host_sn}}"
        host_root_account: "{{ host_root_account }}"
        host_root_passwd: "{{ host_root_passwd }}"
        timeout : "{{ timeout | default(omit) }}"
        api_version_number: "{{ api_version_number | default(omit) }}"
'''

RETURN = r'''
System_Validate_Credential:
  description: Validate VxRail System Credential
  returned: always
  type: dict
  sample: >-
    {
      "message": "Credential Validation is successful."
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

MODULE = "dellemc_vxrail_system_validate_credential"
LOG_FILE_PATH = "/tmp/vxrail_ansible_system_validate_credential.log"
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
        self.vc_root_account = module.params.get('vc_root_account')
        self.vc_root_passwd = module.params.get('vc_root_passwd')
        self.psc_root_account = module.params.get('psc_root_account')
        self.psc_root_passwd = module.params.get('psc_root_passwd')
        self.host_sn = module.params.get('host_sn')
        self.host_root_account = module.params.get('host_root_account')
        self.host_root_passwd = module.params.get('host_root_passwd')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_number = module.params.get('api_version_number')

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path, credential_info):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path,
                                                                   LOGGER)
        call_string = self.api_version_string + '_system_validate_credential_post'

        LOGGER.info("Using utility method: %s\n", call_string)
        api_validate_credential_post = getattr(api_instance, call_string)
        return api_validate_credential_post(credential_info)

    def validate_credential(self):
        credential_info = {}

        # Add optional params if found

        if self.vc_admin:
            vcadmin_spec = {
                "vc_admin_user": {
                    "username": self.vc_admin,
                    "password": self.vc_password
                }
            }
        credential_info['vcenter'] = vcadmin_spec
        if self.vc_root_account:
            vcroot_spec = {
                "vcsa_root_user": {
                    "username": self.vc_root_account,
                    "password": self.vc_root_passwd
                }
            }
            if 'vcenter' in credential_info:
                credential_info['vcenter'].update(vcroot_spec)
            else:
                credential_info['vcenter'] = vcroot_spec
        if self.psc_root_account:
            pscroot_spec = {
                "psc_root_user": {
                    "username": self.psc_root_account,
                    "password": self.psc_root_passwd
                }
            }
            if 'vcenter' in credential_info:
                credential_info['vcenter'].update(pscroot_spec)
            else:
                credential_info['vcenter'] = pscroot_spec

        if self.host_sn:
            hosts_spec = [
                {
                    "sn": self.host_sn,
                    "root_user": {
                        "username": self.host_root_account,
                        "password": self.host_root_passwd
                    }
                }
            ]
            credential_info["hosts"] = hosts_spec
        api_instance = vxrail_ansible_utility.SystemCredentialsApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = self.get_versioned_response(api_instance, 'POST /system/validate-credential', credential_info)
        except ApiException as e:
            LOGGER.error("Exception when calling SystemCredentialsApi->%s_system_validate_credential_post: %s\n",
                         self.api_version_string, e)
            return 'error'
        LOGGER.info("Call %s/system/validate-credential POST api response: %s\n", self.api_version_string, response)
        return response


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(type='str', required=True),
        vcpasswd=dict(type='str', required=True),
        vc_root_account=dict(type='str', required=False),
        vc_root_passwd=dict(type='str', required=False, no_log=True),
        psc_root_account=dict(type='str', required=False),
        psc_root_passwd=dict(type='str', required=False, no_log=True),
        host_sn=dict(type='str', required=False),
        host_root_account=dict(type='str', required=False),
        host_root_passwd=dict(type='str', required=False, no_log=True),
        timeout=dict(type='int', default=60),
        api_version_number=dict(type='int')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().validate_credential()
    if result == 'error':
        module.fail_json(
            msg="Call Validate Credential API failed,please see log file /tmp/vxrail_ansible_system_validate_credential.log for more error details.")
    vx_facts = {'msg': "Credential Validation is successful"}
    vx_facts_result = dict(changed=False, System_Validate_Credential=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
