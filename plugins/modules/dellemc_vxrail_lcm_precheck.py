#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm_precheck

short_description: Perform a health pre-check

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.4.0"

description:
- This module will Perform a separate health pre-check for the VxRail system.
options:
  vxmip:
    description:
      The IP address of the VxRail Manager System
    required: True
    type: str

  bundle_file_locator:
    description:
      the path of lcm bundle on vxm, which is recommended under /data/store2
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
      root account of the vCenter Server the VxRail Manager is registered to
    required: true
    type: str

  vc_root_passwd:
    description:
      The password for the root account provided in vcroot
    required: true
    type: str

  vxm_root_account:
    description:
      root account of VxRail Manager
    required: true
    type: str

  vxm_root_passwd:
    description:
      The password for the root account provided in vxm
    required: true
    type: str

  health_precheck_type:
    description:
      The type of health pre-check to be run. Supported values are LCM_PRECHECK.
    required: false
    type: str
    default: LCM_PRECHECK

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for LCM Upgrade, the default value is 21600 seconds
    required: false
    type: int
    default: 1800

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
- name: LCM Precheck
  dellemc_vxrail_lcm_precheck:
    vxmip: "{{ vxmip }}"
    vcadmin: "{{ vcadmin }}"
    vcpasswd: "{{ vcpasswd }}"
    bundle_file_locator: "{{ bundle_file_locator }}"
    vc_root_account: "{{ vc_root_account }}"
    vc_root_passwd: "{{ vc_root_passwd }}"
    vxm_root_account: "{{ vxm_root_account }}"
    vxm_root_passwd: "{{ vxm_root_passwd }}"
    timeout : "{{ timeout }}"
    api_version_number: "{{ api_version_number }}"
'''
RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
LCM_status:
  description: LCM Precheck status summary
  returned: always
  type: dict
  sample: >-
   {
     "LCM_Precheck": {
            "request_id": "LcmBundleDeployAndPrecheck-d0964e95-1b0c-4c1c-a58a-f9cdf46dab4a",
            "status": "COMPLETED"
        },
        "msg": "LCM Precheck is successful. Please see the /tmp/vxrail_ansible_lcm_v1_precheck.log for more details"

   }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_NAME = "/tmp/vxrail_ansible_lcm_precheck.log"
LOGGER = utils.get_logger("dellemc_vxrail_lcm_precheck", LOG_FILE_NAME, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
CHECK_STATUS_INTERVAL = 30
MAX_CHECK_COUNT = 60


class VxrailVXMUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailVXMUrls.vxm_url.format(self.vxm_ip)


class VxRailLCMPRCHECK():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.bundle_file_locator = module.params.get('bundle_file_locator')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.vc_root_account = module.params.get('vc_root_account')
        self.vc_root_passwd = module.params.get('vc_root_passwd')
        self.vxm_root_account = module.params.get('vxm_root_account')
        self.vxm_root_passwd = module.params.get('vxm_root_passwd')
        self.health_precheck_type = module.params.get('health_precheck_type')
        self.api_version_number = module.params.get('api_version_number')
        self.vxm_url = VxrailVXMUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.vxm_url.set_host()
        # Added for auto-version detection
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path, precheck_json):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute (ex: v1_cluster_remove_host_post)
        call_string = 'precheck_' + self.api_version_string
        LOGGER.info("Using utility method: %s\n", call_string)
        api_prechek_post = getattr(api_instance, call_string)
        request_body = precheck_json
        return api_prechek_post(request_body)

    def create_lcm_precheck_json(self):
        ''' lcm node json '''
        lcm_precheck_json = {}
        lcm_precheck_json['bundle_file_locator'] = self.bundle_file_locator
        lcm_precheck_json['health_precheck_type'] = self.health_precheck_type
        vcenter_dict = {}
        vcenter_dict['vc_admin_user'] = {'username': self.vc_admin, 'password': self.vc_password}
        vcenter_dict['vcsa_root_user'] = {'username': self.vc_root_account, 'password': self.vc_root_passwd}
        lcm_precheck_json['vcenter'] = vcenter_dict
        vxrail_dict = {}
        vxrail_dict['vxm_root_user'] = {'username': self.vxm_root_account, 'password': self.vxm_root_passwd}
        lcm_precheck_json['vxrail'] = vxrail_dict

        return lcm_precheck_json

    def lcm_precheck(self, lcm_precheck_json):
        request_body = lcm_precheck_json
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.LCMPreCheckApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # start LCM Precheck
            response = self.get_versioned_response(api_instance, "/lcm/precheck", request_body)
        except ApiException as e:
            LOGGER.error("Exception when calling LCMPreCheckApi->precheck_%s: %s\n", self.api_version_string, e)
            return 'error'
        job_id = response.request_id
        return job_id

    def get_request_status(self, request_id):
        job_id = request_id
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.RequestStatusApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = api_instance.v1_request_id_get(job_id)
        except Exception as e:
            LOGGER.error("Exception when calling v1_requests_id_get: %s\n", e)
            return 'error'
        return response

    def get_request_info(self, response):
        statusInfo = {}
        statusInfolist = []
        data = response
        statusInfo['id'] = data.id
        statusInfo['owner'] = data.owner
        statusInfo['state'] = data.state
        statusInfo['progress'] = data.progress
        statusInfo['error'] = data.error
        statusInfo['step'] = data.step
        statusInfo['detail'] = data.detail
        statusInfo['start_time'] = data.start_time
        statusInfo['end_time'] = data.end_time
        statusInfolist.append(dict(statusInfo.items()))
        return statusInfolist


def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        bundle_file_locator=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        vc_root_account=dict(required=True),
        vc_root_passwd=dict(required=True, no_log=True),
        vxm_root_account=dict(required=True),
        vxm_root_passwd=dict(required=True, no_log=True),
        health_precheck_type=dict(type='str', default="LCM_PRECHECK"),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=MAX_CHECK_COUNT * CHECK_STATUS_INTERVAL)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    lcm_precheck_status = 0
    lcm_precheck_result = 0
    error = 0
    time_out = 0
    initial_timeout = module.params.get('timeout')
    LOGGER.info('----Start to LCM Precheck with V1 API: ----')
    lcm_precheck_json = VxRailLCMPRCHECK().create_lcm_precheck_json()
    request_body = lcm_precheck_json
    lcm_precheck_request_id = VxRailLCMPRCHECK().lcm_precheck(request_body)
    LOGGER.info('LCM Precheck: VxRail task_ID: %s.', lcm_precheck_request_id)
    if lcm_precheck_request_id == "error":
        module.fail_json(
            msg="lcm precheck request id is not returned. Please see the /tmp/vxrail_ansible_lcm_precheck.log for more details")
    while lcm_precheck_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        lcm_precheck_response = VxRailLCMPRCHECK().get_request_status(lcm_precheck_request_id)
        lcm_precheck_status = lcm_precheck_response.state
        lcm_precheck_result = VxRailLCMPRCHECK().get_request_info(lcm_precheck_response)
        LOGGER.info('LCM_Precheck_Task: status: %s.', lcm_precheck_status)
        LOGGER.info('LCM_Precheck_Task: details: %s.', lcm_precheck_result)
        LOGGER.info("LCM_Precheck_Task: Sleeping %s seconds...", CHECK_STATUS_INTERVAL)
        time.sleep(CHECK_STATUS_INTERVAL)
        time_out = time_out + CHECK_STATUS_INTERVAL
    if lcm_precheck_status == 'COMPLETED':
        LOGGER.info("-------LCM Precheck is successful.-----")
    else:
        LOGGER.info("------LCM Precheck Failed-----")
        if eval(lcm_precheck_response.extension).get('errors') is not None:
            error = eval(lcm_precheck_response.extension).get('errors')
        LOGGER.info('----Failed reason is : %s.----', error)
        vx_lcm_precheck = {'request_id': lcm_precheck_request_id, 'response_error': error}
        vx_facts_result = dict(failed=True, LCM_V1_Precheck=vx_lcm_precheck,
                               msg="LCM Precheck has failed. Please see the /tmp/vxrail_ansible_lcm_precheck.log for more details")
        module.exit_json(**vx_facts_result)
    vx_lcm_precheck = {'status': lcm_precheck_status, 'request_id': lcm_precheck_request_id}
    vx_facts_result = dict(changed=False, LCM_Precheck=vx_lcm_precheck,
                           msg="LCM Precheck is successful. Please see the /tmp/vxrail_ansible_lcm_precheck.log for more details")
    module.exit_json(**vx_facts_result)


if __name__ == '__main__':
    main()
