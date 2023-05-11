#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm_retry

short_description: Retry a Failed LCM Upgrade

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.6.0"

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

EXAMPLES = r'''
- name: Retry the LCM Upgrade
  dellemc_vxrail_lcm:
    vxmip: "{{ vxmip }}"
    vcadmin: "{{ vcadmin }}"
    vcpasswd: "{{ vcpasswd }}"
    timeout: "{{ timeout }}"
    api_version_number: "{{ api_version_number }}"
'''
RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
LCM_status:
  description: LCM status summary
  returned: always
  type: dict
  sample: >-
   {
    "LCM_API_Upgrade": {
        "request_id": "2ce09bde-d987-4fff-8f90-6fc430e2bfc3",
        "status": "COMPLETED"
    }
    "msg": "LCM is successful. Please see the /tmp/vxrail_ansible_lcm.log for more details"
   }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_NAME = "/tmp/vxrail_ansible_lcm.log"
LOGGER = utils.get_logger("dellemc_vxrail_lcm", LOG_FILE_NAME, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
MAX_RETRY_COUNT = 8
CHECK_STATUS_INTERVAL = 360
MAX_CHECK_COUNT = 60


class VxrailVXMUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailVXMUrls.vxm_url.format(self.vxm_ip)


class VxRailLCMRetry():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.vxm_url = VxrailVXMUrls(self.vxm_ip)
        self.api_version_number = module.params.get('api_version_number')
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.vxm_url.set_host()

    def upgrade(self):
        try:
            # create an instance of the API class
            api_instance = vxrail_ansible_utility.LCMUpgradeApi(vxrail_ansible_utility.ApiClient(self.configuration))
            # retry LCM with versioned api
            api_version_string = self.get_versioned_response('POST /lcm/upgrade/retry')
            call_string = 'upgrade_retry_' + api_version_string
            LOGGER.info("LCM Retry upgrade version: %s", call_string)
            lcm_upgrade_retry = getattr(api_instance, call_string)
            response = lcm_upgrade_retry()
        except ApiException as e:
            LOGGER.error("Exception when calling LCMUpgradeApi->%s: %s\n", call_string, e)
            return 'error'
        job_id = response.request_id
        return job_id

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


def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        timeout=dict(type='int', default=MAX_CHECK_COUNT * CHECK_STATUS_INTERVAL),
        api_version_number=dict(type='int')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    lcm_status = 0
    lcm_result = 0
    error = 0
    time_out = 0
    initial_timeout = module.params.get('timeout')
    try_times = 0
    vxmip = module.params.get('vxmip')
    vcadmin = module.params.get('vcadmin')
    vcpasswd = module.params.get('vcpasswd')

    LOGGER.info('----Retry upgrade with LCM API: ----')
    lcm_request_id = VxRailLCMRetry().upgrade()

    LOGGER.info('LCM: VxRail task_ID: %s.', lcm_request_id)
    if lcm_request_id == "error":
        module.fail_json(
            msg="lcm request id is not returned. Please see the /tmp/vxrail_ansible_lcm.log for more details")
    while lcm_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        lcm_response = utils.get_request_status(vxm_ip=vxmip, vcadmin=vcadmin, vcpasswd=vcpasswd, logger=LOGGER, request_id=lcm_request_id)
        ''' When VxRail Manager upgrade or Reboot is in progress. Temporary disconnection during this process,
        meed to send request with auth again'''
        while lcm_response == "error" and try_times < MAX_RETRY_COUNT:
            LOGGER.info('----VxRail Manager upgrade or Reboot is in progress, which may be temporary '
                        'disconnection during this process ----')
            LOGGER.info('----Please wait for its back...Need to log in again----')
            time.sleep(15 * 60)
            lcm_response = utils.get_request_status(vxm_ip=vxmip, vcadmin=vcadmin, vcpasswd=vcpasswd, logger=LOGGER, request_id=lcm_request_id)
            try_times = try_times + 1
        if try_times == MAX_RETRY_COUNT:
            LOGGER.info('----VxRail Manager upgrade or Reboot is failed----')
            vx_lcm = {'request_id': lcm_request_id}
            vx_facts_result = dict(failed=True, LCM_API_Upgrade=vx_lcm,
                                   msg="LCM has failed. Please see the /tmp/vxrail_ansible_lcm.log for more details")
            module.exit_json(**vx_facts_result)
        lcm_status = lcm_response.state
        lcm_result = utils.get_request_info(lcm_response)
        LOGGER.info('LCM_Task: status: %s.', lcm_status)
        LOGGER.info('LCM_Task: details: %s.', lcm_result)
        LOGGER.info("LCM_Task: Sleeping %s seconds...", CHECK_STATUS_INTERVAL)
        time.sleep(CHECK_STATUS_INTERVAL)
        time_out = time_out + CHECK_STATUS_INTERVAL
    if lcm_status == 'COMPLETED':
        LOGGER.info("-------LCM is successful.-----")
    else:
        LOGGER.info("------LCM Failed-----")
        if lcm_result[0].get('error') is not None:
            error = lcm_result[0].get('error')
        else:
            error = lcm_result[0].get('detail')
        LOGGER.info('----Failed reason is : %s.----', error)
        vx_lcm = {'request_id': lcm_request_id, 'response_error': error}
        vx_facts_result = dict(failed=True, LCM_API_Upgrade=vx_lcm,
                               msg="LCM has failed. Please see the /tmp/vxrail_ansible_lcm.log for more details")
        module.exit_json(**vx_facts_result)
    vx_lcm = {'status': lcm_status, 'request_id': lcm_request_id}
    vx_facts_result = dict(changed=True, LCM_API_Upgrade=vx_lcm,
                           msg="LCM is successful. Please see the /tmp/vxrail_ansible_lcm.log for more details")
    module.exit_json(**vx_facts_result)


if __name__ == '__main__':
    main()
