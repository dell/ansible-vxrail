#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_support_getaccount_v1

short_description: Retrieve VxRail support account

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.2.0"

description:
- This module will get the current support account set in VxRail.
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
      Time out value for getting telemetry information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Retrieve VxRail support account Information
    dellemc_vxrail_support_getaccount_v1:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"
'''

RETURN = r'''
Support_account:
  description: the current support account set in VxRail
  returned: always
  type: dict
  sample: >-
        {
            "username": "vxrailtest3@example.com"
        }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_support_getaccount_v1", "/tmp/vxrail_ansible_support_account.log", log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailClusterUrls.cluster_url.format(self.vxm_ip)


class VxRailSupport():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

    def get_v1_support_account(self):
        supportInfo = {}
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SupportAccountApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query v1 support account
            response = api_instance.v1_support_account_get()
        except ApiException as e:
            LOGGER.error("Exception when calling SupportAccountApi->v1_support_account_get: %s\n", e)
            return 'error'
        LOGGER.info("v1/support/account api response: %s\n", response)
        data = response
        supportInfo['username'] = data.username
        return dict(supportInfo.items())


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailSupport().get_v1_support_account()
    if result == 'error':
        module.fail_json(msg="Call V1/support/account API failed,please see log file /tmp/vxrail_ansible_support_account.log for more error details.")
    vx_facts = {'Support_Account': result}
    vx_facts_result = dict(changed=False, V1_Support_Account_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
