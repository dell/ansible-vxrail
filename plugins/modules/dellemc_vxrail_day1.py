#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: dellemc_vxrail_day1

short_description: Perform the Day1 first run initialization of a VxRail Cluster

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.1.0"

description:
- This module will configure and deploy a new VxRail cluster
  based on the provided day1 json file.
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

  day1json_file:
    description:
      The path of Day1 Json file.
    required: True
    type: str

  timeout:
    description:
      Time out value for Day1 bring up, the default value is 18000 seconds
    required: false
    type: int
    default: 18000

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
- name: Day1 initialization
  dellemc_vxrail_day1:
    vxmip: "{{ vxmip }}"
    vcadmin: "{{ vcadmin }}"
    vcpasswd: "{{ vcpasswd }}"
    day1json_file: "{{ day1json_file }}"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
installation_status:
  description: day1 initialization status summary
  returned: always
  type: dict
  sample: >-
   {
    "Day1DryRun": {
        "request_id": "2ce09bde-d987-4fff-8f90-6fc430e2bfc3",
        "status": "COMPLETED"
    },
    "Day1Initialization": {
        "request_id": "433d0a61-06e7-4cb8-a1eb-985ab9a8b5dd",
        "status": "COMPLETED"
    }
    "msg": "Day1 initialization is successful. Please see the /tmp/vxrail_ansible_day1.log for more details"
   }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
import json
import os
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dell_vxrail_day1", "/tmp/vxrail_ansible_day1.log", log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

MAX_ERROR_COUNT = 10
CHECK_STATUS_INTERVAL = 60
MAX_CHECK_COUNT = 300


class VxrailDay1Urls():
    day1_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailDay1Urls.day1_url.format(self.vxm_ip)


class VxRailDay1():
    def __init__(self, new_vxm_ip=None):
        self.vxm_ip = new_vxm_ip if new_vxm_ip else module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.day1_cfg = module.params.get('day1_cfg')
        self.day1_url = VxrailDay1Urls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.day1_url.set_host()

    def start_validation(self, day1_json):
        request_body = day1_json
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.VxRailInstallationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # start day1 DryRun validation
            response = api_instance.v1_system_initialize_post(request_body, dryrun=True)
        except ApiException as e:
            LOGGER.error("Exception when calling VxRailInstallationApi->v1_system_initialize_post?dryrun=True: %s\n", e)
            return 'error'
        job_id = response.request_id
        return job_id

    def start_initialization(self, day1_json):
        request_body = day1_json
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.VxRailInstallationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # start day1 FirstRun
            response = api_instance.v1_system_initialize_post(request_body)
        except ApiException as e:
            LOGGER.error("Exception when calling ClusterExpansionApi->v1_cluster_expansion_post: %s\n", e)
            return 'error'
        job_id = response.request_id
        return job_id

    def get_request_status(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.VxRailInstallationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = api_instance.v1_system_initialize_status_get()
        except Exception as e:
            LOGGER.error("Exception when calling v1_system_initialize_status_get: %s\n", e)
            if hasattr(e, 'status') and e.status == 400 and hasattr(e, 'body'):
                try:
                    body = json.loads(e.body)
                    if 'error_code' in body and body['error_code'] == 20101003:
                        LOGGER.info('Day1 status API return 400 and error_code 20101003, means Day1 is done.')

                        class Obj():
                            pass
                        response = Obj()
                        response.state = 'COMPLETED'
                        return response
                except Exception:
                    return None
            return None
        return response

    @staticmethod
    def get_request_info(response):
        if not hasattr(response, 'id'):
            return None
        statusInfo = {}
        statusInfolist = []
        data = response
        statusInfo['id'] = data.id
        statusInfo['state'] = data.state
        statusInfo['owner'] = data.owner
        statusInfo['progress'] = data.progress
        statusInfo['step'] = data.step
        statusInfo['error'] = data.error
        statusInfo['start_time'] = data.start_time
        statusInfo['end_time'] = data.end_time
        statusInfolist.append(dict(statusInfo.items()))
        return statusInfolist

    @staticmethod
    def check_new_vxm_ip(response):
        if not hasattr(response, 'extension'):
            return False
        for step in response.extension.steps:
            if step.get('id') == 'validation_report':
                return step.get('state') == 'COMPLETED'
        return False


def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        day1json_file=dict(required=True),
        timeout=dict(type='int', default=MAX_CHECK_COUNT * CHECK_STATUS_INTERVAL)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    validation_status = 0
    installation_status = 0
    validation_result = 0
    installation_result = 0
    error = 0
    time_out = 0
    validation_request_id = 0
    installation_request_id = 0
    initial_timeout = module.params.get('timeout')
    file = module.params.get('day1json_file')
    if os.path.isfile(file):
        LOGGER.info('VxRail Initializaion using JSON file %s', module.params.get('day1json_file'))
        with open(file, encoding='utf_8') as f:
            config_json = json.load(f)
    else:
        LOGGER.error('File cannot not be opened or does not exit, please verify and try again')
        module.fail_json(msg="JSON file not found!")

    vxm_ip_in_json = config_json.get("vxrail_manager", {}).get("ip")
    if not vxm_ip_in_json:
        vxm_ip_in_json = config_json.get("vxrail_manager", {}).get("ipv6")
    new_vxm_ip = vxm_ip_in_json if vxm_ip_in_json != module.params.get('vxmip') else None
    if new_vxm_ip:
        LOGGER.info('VxRail Manager IP will change to %s during installation', new_vxm_ip)

    LOGGER.info('----Start validation for the Day1 JSON input file...----')
    request_body = config_json
    validation_request_id = VxRailDay1().start_validation(request_body)
    LOGGER.info('Day1_DryRun: VxRail task_ID: %s.', validation_request_id)
    if validation_request_id == "error":
        module.fail_json(
            msg="validation request id is not returned. Please see the /tmp/vxrail_ansible_day1.log for more details")

    error_count = 0
    while validation_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout and error_count < MAX_ERROR_COUNT:
        validation_response = VxRailDay1().get_request_status()
        if validation_response:
            error_count = 0
            validation_status = validation_response.state
            validation_result = VxRailDay1.get_request_info(validation_response)
            LOGGER.info('Day1_DryRun_Task: status: %s.', validation_status)
            LOGGER.info('Day1_DryRun_Task: details: %s.', validation_result)
            LOGGER.info("Day1_DryRun Task: Sleeping %s seconds...", CHECK_STATUS_INTERVAL)
        else:
            error_count += 1
            LOGGER.info('Fail to get validation status. Count: %s', error_count)

        time.sleep(CHECK_STATUS_INTERVAL)
        time_out = time_out + CHECK_STATUS_INTERVAL

    errors = validation_response.extension.validation.cursory.errors.fields
    if len(errors) != 0:
        error = errors[0].messages
    else:
        errors = validation_response.extension.validation.thorough.errors.fields
        if len(errors) != 0:
            error = errors[0].messages
    if validation_status == 'COMPLETED' and not error:
        LOGGER.info("-------DryRun Completed------")
        LOGGER.info("----Configure and deploy a new VxRail cluster----")
        installation_request_id = VxRailDay1().start_initialization(request_body)
        LOGGER.info('Day1 Initialization: VxRail task_ID: %s.', installation_request_id)

        new_vxm_ip_iswork = False
        error_count = 0
        while installation_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout and error_count < MAX_ERROR_COUNT:
            installation_response = None
            if new_vxm_ip:
                installation_response = VxRailDay1(new_vxm_ip).get_request_status()
                if installation_response and not new_vxm_ip_iswork:
                    new_vxm_ip_iswork = VxRailDay1.check_new_vxm_ip(installation_response)
                    if new_vxm_ip_iswork:
                        LOGGER.info('VxRail Manager IP has been changed to %s', new_vxm_ip)
            if not installation_response and not new_vxm_ip_iswork:
                installation_response = VxRailDay1().get_request_status()
            if installation_response:
                error_count = 0
                installation_status = installation_response.state
                installation_result = VxRailDay1.get_request_info(installation_response)
                LOGGER.info('Installation_Task: status: %s.', installation_status)
                LOGGER.info('Installation_Task: details: %s.', installation_result)
                LOGGER.info("Installation_Task: sleeping %s seconds...", CHECK_STATUS_INTERVAL)
            else:
                error_count += 1
                LOGGER.info('Fail to get installation status. Count: %s', error_count)

            time.sleep(CHECK_STATUS_INTERVAL)
            time_out = time_out + CHECK_STATUS_INTERVAL

        if installation_status == 'COMPLETED':
            LOGGER.info("-----Installation Completed-----")
        else:
            LOGGER.info("------Installation Failed-----")
            vx_initialization = {'request_id': installation_request_id}
            vx_facts_result = dict(failed=True, Day1Initialization=vx_initialization,
                                   msg='Day1 initialization has failed. Please see the /tmp/vxrail_ansible_day1.log for more details')
            module.exit_json(**vx_facts_result)
    else:
        LOGGER.info("------Validation Failed-----")
        LOGGER.info('Day1_DryRun Task: errors: %s.', errors)
        vx_validation = {'request_id': validation_request_id, 'response_error': error}
        vx_facts_result = dict(failed=True, Day1DryRun=vx_validation,
                               msg="Day1 DryRun has failed. Please see the /tmp/vxrail_ansible_day1.log for more details")
        module.exit_json(**vx_facts_result)
    vx_validation = {'status': validation_status, 'request_id': validation_request_id}
    vx_initialization = {'status': installation_status, 'request_id': installation_request_id}
    vx_facts_result = dict(changed=True, Day1Initialization=vx_initialization, Day1DryRun=vx_validation,
                           msg="Day1 initialization is successful. Please see the /tmp/vxrail_ansible_day1.log for more details")
    module.exit_json(**vx_facts_result)


if __name__ == '__main__':
    main()
