#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_idrac_getusers_v1

short_description: Get list of the iDRAC user accounts on the specified host.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.2.0"

description:
  - "This module will get list of the iDRAC user accounts on the specified host."
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

  sn:
    description:
      The serial number of the host to be queried
    required: True
    type: str

  timeout:
    description:
      Time out value for getting iDRAC network settings, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
  - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>
'''

EXAMPLES = r'''
  - name: Get iDRAC User Accounts
    dellemc_vxrail_idrac_getusers_v1:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        sn: "{{ sn }}"
        timeout: "{{ timeout }}"
'''

RETURN = r'''
iDRAC_Users:
  description: iDRAC user accounts
  returned: always
  type: dict
  sample: >-
                {
                    "id": 2,
                    "name": "root",
                    "privilege": "ADMIN"
                },
                {
                    "id": 15,
                    "name": "vxpsvc",
                    "privilege": "ADMIN"
                },
                {
                    "id": 16,
                    "name": "PTAdmin",
                    "privilege": "ADMIN"
                }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils


LOG_FILE_NAME = "/tmp/vxrail_ansible_idrac_getusers_v1.log"
LOGGER = utils.get_logger("dellemc_vxrail_idrac_getusers_v1", LOG_FILE_NAME, log_devel=logging.DEBUG)
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
        self.sn = module.params.get('sn')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

    def get_v1_idrac_getusers(self):
        # create an instance of the API class
        response = ''
        api_instance = vxrail_ansible_utility.HostIDRACConfigurationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query v1 host idrac users information
            response = api_instance.v1_hosts_sn_idrac_user_get(self.sn)
        except ApiException as e:
            LOGGER.error("Exception when calling HostIDRACConfigurationApi->v1_hosts_sn_idrac_users_get: %s\n", e)
            return 'error'
        LOGGER.info("v1/idrac users api response: %s\n", response)
        idrac_users = {}
        idrac_users_list = []
        for i in range(len(response)):
            idrac_users['id'] = response[i].id
            idrac_users['name'] = response[i].name
            idrac_users['privilege'] = response[i].privilege
            idrac_users_list.append(dict(idrac_users.items()))
        return idrac_users_list


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        timeout=dict(type='int', default=60),
        sn=dict(required=True)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().get_v1_idrac_getusers()
    if result == 'error':
        module.fail_json(msg="iDRAC API call failed, please see log file /tmp/vxrail_ansible_idrac_getusers_v1.log for details.")
    vx_facts = {'iDRAC_Users': result}
    vx_facts_result = dict(changed=False, V1_iDRAC_Users_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
