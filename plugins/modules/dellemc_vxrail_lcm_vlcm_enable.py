#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm_vlcm_get

short_description: get vlcm info

description:
- This module will retry the LCM full upgrade or partial upgrade if started through the LCM API call.
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
      The password for the root account provided in vcadmin
    required: True
    type: str

  vc_root_passwd:
    description:
      The password for the root password provided in vcadmin
    required: True
    type: str

  customized_components:
    description:
      The customized_components vlcm enablement
    type: dict

  timeout:
    description:
      Time out value for LCM Upgrade Retry, the default value is 21600 seconds
    required: false
    type: int
    default: 21600

  api_version_number:
    description:
      Specify the API version to perform the upgrade.
    required: false
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

RETURN = r'''
VLCM_ENABLE_API:
  description: The current vlcm info
  returned: always
  type: dict
  sample: >-
        { "status": vlcm_enable_status, 'request_id': vlcm_request_id}
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
import json
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_NAME = "/tmp/vxrail_ansible_lcm_vlcm_enable.log"
LOGGER = utils.get_logger("dellemc_vxrail_lcm_vlcm_enable", LOG_FILE_NAME, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
CHECK_STATUS_INTERVAL = 60
MAX_CHECK_COUNT = 60
MAX_RETRY_COUNT = 20


class VxrailVXMUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailVXMUrls.vxm_url.format(self.vxm_ip)


class VxRailLCMEnableVLCM():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.vc_root_account = module.params.get('vc_root_account')
        self.vc_root_passwd = module.params.get('vc_root_passwd')
        self.customized_components = module.params.get('customized_components')

        self.vxm_url = VxrailVXMUrls(self.vxm_ip)
        self.api_version_number = module.params.get('api_version_number')
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.vxm_url.set_host()

    def create_enablement_json(self):
        enablement_json = {}
        enablement_json['vc_admin_user'] = {'username': self.vc_admin, 'password': self.vc_password}
        enablement_json['vcsa_root_user'] = {'username': self.vc_root_account, 'password': self.vc_root_passwd}
        enablement_json['customized_components'] = json.loads(self.customized_components)

        return enablement_json

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, module_path):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(api_version_string.split('v')[1])
        else:
            api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path,
                                                              LOGGER)
        return api_version_string

    def post_vlcm_enablement(self):
        try:
            # create an instance of the API class
            api_instance = vxrail_ansible_utility.VLCMApi(vxrail_ansible_utility.ApiClient(self.configuration))
            # start LCM with versioned api
            api_version_string = self.get_versioned_response('Post /lcm/vlcm/enablement')
            call_string = 'vlcm_enablement_post_' + api_version_string
            LOGGER.info("LCM vlcm_enablement version: %s", call_string)
            vlcm_enablement = getattr(api_instance, call_string)

            # create request body with API version
            request_body = self.create_enablement_json()
            LOGGER.info("vLCM enable api request body:")
            LOGGER.info(request_body)
            response = vlcm_enablement(request_body)
            LOGGER.info("vLCM enable api response:")
            LOGGER.info(response)
        except ApiException as e:
            LOGGER.error("Exception when calling VLCMApi vlcm_enablement_post_v1->%s: %s\n", call_string, e)
            return 'error'
        job_id = response.request_id
        return job_id

    def get_vlcm_enablement_status(self, request_id):
        job_id = request_id
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.VLCMApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = api_instance.vlcm_enablement_status_get_v1(job_id)
        except Exception as e:
            LOGGER.error("Exception when calling vlcm_enablement_status_get_v1: %s\n", e)
            return 'error'
        return response

def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module

    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        vc_root_account=dict(required=True),
        vc_root_passwd=dict(required=True, no_log=True),
        customized_components=dict(default={}),
        api_version_number=dict(type='int', required=False),
        timeout=dict(type='int', default=1800)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    vlcm_enable_status = 0
    vlcm_enable_step = 0
    try_times = 0
    time_out = 0
    initial_timeout = module.params.get('timeout')

    LOGGER.info('----Start to vLCM enablement: ----')
    vlcm_request_id = VxRailLCMEnableVLCM().post_vlcm_enablement()
    LOGGER.info('LCM: vLCM enablement request_id: %s.', vlcm_request_id)
    if vlcm_request_id == "error":
        module.fail_json(
            msg=f"vLCM enablement request_id is not returned. Please see the {LOG_FILE_NAME} for more details")
    while vlcm_enable_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        LOGGER.info('----vLCM enablement is in progress----')
        vlcm_response = VxRailLCMEnableVLCM().get_vlcm_enablement_status(vlcm_request_id)
        LOGGER.info(vlcm_response)
        ''' When update_cert step is in progress. Temporary disconnection during this process,
        meed to send request with auth again'''
        while vlcm_response == "error" and try_times < MAX_RETRY_COUNT:
            LOGGER.info('----When update_cert step is in progress, which may be temporary '
                        'disconnection during this process ----')
            LOGGER.info('----Please wait for its back...Need to log in again----')
            time.sleep(3 * 60)
            vlcm_response = VxRailLCMEnableVLCM().get_vlcm_enablement_status(vlcm_request_id)
            try_times = try_times + 1
        if try_times == MAX_RETRY_COUNT:
            LOGGER.info('----VxRail Manager upgrade or Reboot is failed----')
            vx_lcm = {'request_id': vlcm_response}
            vx_facts_result = dict(failed=True, VLCM_ENABLE_API=vx_lcm,
                                   msg="vLCM enablement has failed. Please see the {LOG_FILE_NAME} for more details")
            module.exit_json(**vx_facts_result)
        vlcm_enable_status = vlcm_response.state
        vlcm_enable_step = vlcm_response.step
        LOGGER.info('VLCM_Enable_Task: status: %s.', vlcm_enable_status)
        LOGGER.info('VLCM_Enable_Task: current step: %s.', vlcm_enable_step)
        LOGGER.info('VLCM_Enable_Task: details: %s.', vlcm_response.extension[vlcm_enable_step])
        LOGGER.info("VLCM_Enable_Task: Sleeping %s seconds...", CHECK_STATUS_INTERVAL)
        time.sleep(CHECK_STATUS_INTERVAL)
        time_out = time_out + CHECK_STATUS_INTERVAL

    if vlcm_enable_status == 'COMPLETED':
        LOGGER.info("-------vLCM enablement is successful.-----")
    else:
        LOGGER.info("------vLCM enablement Failed-----")

        LOGGER.info('----Failed reason is : %s.----', vlcm_response)
        vx_lcm = {'request_id': vlcm_request_id, 'response_error_step': vlcm_response.extension[vlcm_enable_step]}
        vx_facts_result = dict(failed=True, VLCM_ENABLE_API=vx_lcm,
                               msg=f"vLCM enablement has failed. Please see the {LOG_FILE_NAME} for more details")
        module.exit_json(**vx_facts_result)
    vx_lcm = {'status': vlcm_enable_status, 'request_id': vlcm_request_id}
    vx_facts_result = dict(VLCM_ENABLE_API=vx_lcm,
                           msg=f"vLCM enablement is successful. Please see the {LOG_FILE_NAME} for more details")
    LOGGER.info("vx_facts_result: %s\n", vx_facts_result)
    module.exit_json(**vx_facts_result)

if __name__ == '__main__':
    main()
