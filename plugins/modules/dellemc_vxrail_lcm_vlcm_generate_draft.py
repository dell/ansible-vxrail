#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm_vlcm_generate_draft

short_description: generate vlcm draft

description:
- This module will generate vLCM draft.
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
VLCM_GENERATE_DRAFT_API:
  description: Generate vLCM draft
  returned: always
  type: dict
  sample: >-
        { "status": vlcm_enable_status, 'task_id': vlcm_task_id}
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
import json
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_NAME = "/tmp/vxrail_ansible_lcm_vlcm_generate_draft.log"
LOGGER = utils.get_logger("dellemc_vxrail_lcm_vlcm_generate_draft", LOG_FILE_NAME, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
CHECK_STATUS_INTERVAL = 60
MAX_CHECK_COUNT = 60


class VxrailVXMUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailVXMUrls.vxm_url.format(self.vxm_ip)


class VxRailLCMGenerateVLCMDraft():
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

    def create_generate_draft_json(self):
        draft_json = {}
        draft_json['vc_admin_user'] = {'username': self.vc_admin, 'password': self.vc_password}
        draft_json['vcsa_root_user'] = {'username': self.vc_root_account, 'password': self.vc_root_passwd}
        draft_json['customized_components'] = json.loads(self.customized_components.replace("'", '"'))

        return draft_json

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

    def post_generate_vlcm_draft(self):
        try:
            # create an instance of the API class
            api_instance = vxrail_ansible_utility.VLCMApi(vxrail_ansible_utility.ApiClient(self.configuration))
            # start generate vLCM draft with versioned api
            api_version_string = self.get_versioned_response('Post /lcm/vlcm/enablement/draft/generate')
            call_string = 'vlcm_enablement_draft_generate_post_' + api_version_string
            LOGGER.info("LCM vlcm_generate_draft version: %s", call_string)
            generate_vlcm_draft = getattr(api_instance, call_string)

            # create request body with API version
            request_body = self.create_generate_draft_json()
            LOGGER.info("generate vLCM draft api request body:")
            LOGGER.info(request_body)
            response = generate_vlcm_draft(request_body)
            LOGGER.info("generate vLCM draft api response:")
            LOGGER.info(response)
        except ApiException as e:
            LOGGER.error("Exception when calling VLCMApi vlcm_enablement_draft_generate_post_v1->%s: %s\n", call_string, e)
            return 'error'
        job_id = response.task_id
        return job_id

    def get_vlcm_task_status(self, task_id):
        job_id = task_id
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

    generate_vlcm_draft_status = 0
    generate_vlcm_draft_step = 0
    time_out = 0
    initial_timeout = module.params.get('timeout')

    LOGGER.info('----Start to generate vLCM draft: ----')
    vlcm_task_id = VxRailLCMGenerateVLCMDraft().post_generate_vlcm_draft()
    LOGGER.info('LCM: generate vLCM draft task_id: %s.', vlcm_task_id)
    if vlcm_task_id == "error":
        module.fail_json(
            msg=f"Generate vLCM draft task_id is not returned. Please see the {LOG_FILE_NAME} for more details")
    while generate_vlcm_draft_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        LOGGER.info('----Generate vLCM draft is in progress----')
        vlcm_response = VxRailLCMGenerateVLCMDraft().get_vlcm_task_status(vlcm_task_id)
        if vlcm_response == "error":
          time.sleep(CHECK_STATUS_INTERVAL)
          time_out = time_out + CHECK_STATUS_INTERVAL
          continue
        LOGGER.info(vlcm_response)
        generate_vlcm_draft_status = vlcm_response.state
        generate_vlcm_draft_step = vlcm_response.step
        LOGGER.info('Generate_VLCM_Draft_Task: status: %s.', generate_vlcm_draft_status)
        LOGGER.info('Generate_VLCM_Draft_Task: current step: %s.', generate_vlcm_draft_step)
        LOGGER.info('Generate_VLCM_Draft_Task: details: %s.', vlcm_response.extension[generate_vlcm_draft_step])
        LOGGER.info("Generate_VLCM_Draft_Task: Sleeping %s seconds...", CHECK_STATUS_INTERVAL)
        time.sleep(CHECK_STATUS_INTERVAL)
        time_out = time_out + CHECK_STATUS_INTERVAL

    if generate_vlcm_draft_status == 'COMPLETED':
        LOGGER.info("-------Generate vLCM draft successfully.-----")
    else:
        LOGGER.info("------Generate vLCM draft unsuccessfully-----")

        LOGGER.info('----Failed reason is : %s.----', vlcm_response)
        vx_lcm = {'task_id': vlcm_task_id, 'response_error_step': vlcm_response.extension[generate_vlcm_draft_step]}
        vx_facts_result = dict(failed=True, VLCM_GENERATE_DRAFT_API=vx_lcm,
                               msg=f"Generate vLCM draft has failed. Please see the {LOG_FILE_NAME} for more details")
        module.exit_json(**vx_facts_result)
    vx_lcm = {'status': generate_vlcm_draft_status, 'task_id': vlcm_task_id}
    vx_facts_result = dict(VLCM_GENERATE_DRAFT_API=vx_lcm,
                           msg=f"Generate vLCM draft is successful. Please see the {LOG_FILE_NAME} for more details")
    LOGGER.info("vx_facts_result: %s\n", vx_facts_result)
    module.exit_json(**vx_facts_result)

if __name__ == '__main__':
    main()
