#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_idrac_update_useraccount

short_description: Update an iDRAC user account.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.5.0"

description:
  - "This module will update the iDRAC user account."
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
      Time out value for updating iDRAC user account, the default value is 60 seconds
    required: False
    type: int
    default: 60

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  id:
    description:
      The unique identifier of the iDRAC user. The available range is between 3 and 16.
    required: True
    type: int

  name:
    description:
      The iDRAC user name.
    required: True
    type: str

  password:
    description:
      The iDRAC user password.
    required: True
    type: str

  privilege:
    description:
      The permissions (privilege) of the iDRAC user
    required: True
    type: str

author:
  - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>
'''

EXAMPLES = r'''
  - name: Update iDRAC User Account
    dellemc_vxrail_idrac_update_useraccount:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        sn: "{{ sn }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
        id: "{{ id }}"
        name: "{{ name }}"
        password: "{{ password }}"
        privilege: "{{ privilege }}"
'''

RETURN = r'''
Update_iDRAC_User_API:
  description: Update an iDRAC user account
  returned: always
  type: dict
  sample: >-
    {
            "Request_ID": "SBI_11",
            "Request_Status": "COMPLETED"
        }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils


LOG_FILE_NAME = "/tmp/vxrail_ansible_idrac_update_useraccount.log"
LOGGER = utils.get_logger("dellemc_vxrail_idrac_update_useraccount", LOG_FILE_NAME, log_devel=logging.DEBUG)
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
        self.id = module.params.get('id')
        self.name = module.params.get('name')
        self.password = module.params.get('password')
        self.privilege = module.params.get('privilege')
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
    def get_versioned_response(self, api_instance, module_path, request_body, sn, id):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        call_string = self.api_version_string + '_hosts_sn_idrac_user_id_put'
        LOGGER.info("Using utility method: %s\n", call_string)

        put_idrac_userid = getattr(api_instance, call_string)
        return put_idrac_userid(request_body, sn, id)

    def create_user_json(self):
        '''idrac user json'''
        idrac_user_json = {}
        idrac_user_json['name'] = self.name
        idrac_user_json['password'] = self.password
        idrac_user_json['privilege'] = self.privilege
        return idrac_user_json

    def put_idrac_userid(self):
        # create an instance of the API class
        response = ''
        api_instance = vxrail_ansible_utility.HostIDRACConfigurationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        request_body = self.create_user_json()
        try:
            # put host idrac user information
            response = self.get_versioned_response(api_instance, "PUT /hosts/{sn}/idrac/users/{userId}", request_body, self.sn, self.id)
        except ApiException as e:
            LOGGER.error("Exception when calling HostIDRACConfigurationApi->%s_hosts_sn_idrac_user_id_put: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/hosts/{sn}/idrac/users/{userId} api response: %s\n", self.api_version_string, response)
        requestid = response.request_id
        return requestid


def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        timeout=dict(type='int', default=300),
        api_version_number=dict(type='int'),
        sn=dict(required=True),
        id=dict(required=True, type='int'),
        name=dict(required=True),
        password=dict(required=True, no_log=True),
        privilege=dict(required=True)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result_request_id = VxRailCluster().put_idrac_userid()
    if result_request_id == 'error':
        module.fail_json(msg="/hosts/{sn}/idrac/users/{userId} API call failed, please "
                             "see log file /tmp/vxrail_ansible_idrac_update_useraccount.log for details.")
    LOGGER.info('iDRAC update user account request_id: %s.', result_request_id)
    vxmip = module.params.get('vxmip')
    vcadmin = module.params.get('vcadmin')
    vcpasswd = module.params.get('vcpasswd')
    task_state = 0
    time_out = 0
    initial_timeout = module.params.get('timeout')
    LOGGER.info('Timeout setting: %s seconds.', initial_timeout)
    while task_state not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        result_response = utils.get_request_status(vxm_ip=vxmip, vcadmin=vcadmin, vcpasswd=vcpasswd, logger=LOGGER, request_id=result_request_id)
        task_state = result_response.state
        LOGGER.info('Request_status: %s', task_state)
        ''' call frequently to capture 'COMPLETED' status before cluster shut down'''
        time_out = time_out + 1
        time.sleep(1)
    error_message = result_response.error
    if task_state == 'COMPLETED' and not error_message:
        vx_facts = {'Request_ID': result_request_id, 'Request_Status': task_state}
        LOGGER.info("iDRAC user account information updated")
        vx_facts_result = dict(changed=True, Update_iDRAC_User_API=vx_facts, msg="iDRAC user information updated. Please see the "
                                                                                 "logs at /tmp/vxrail_ansible_idrac_update_useraccount.log for more details")
    else:
        LOGGER.info("Failed to update iDRAC user account information")
        vx_facts = {'Request_ID': result_request_id}
        vx_facts_result = dict(failed=True, Update_iDRAC_User_API=vx_facts, msg="Please see the /tmp/vxrail_ansible_idrac_update_useraccount.log "
                                                                                "for more details")
    LOGGER.info('Request_info: %s', result_response)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
