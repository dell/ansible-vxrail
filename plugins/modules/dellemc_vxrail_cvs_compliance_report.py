#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_cvs_compliance_report

short_description: Generate an compliance report

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.5.0"

description:
- This module will generate a compliance report containing component drift information against the current system baseline.
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

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for cancelling the host shutdown, the default value is 60 seconds
    required: false
    type: int
    default: 1800

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
    - name: Start to generate cvs compliance report
      dellemc_vxrail_cvs_compliance_report:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
cvs_compliance_Report:
  description: Returns the request ID and whether the operation was successful.
  returned: always
  type: dict
  sample: >-
        {
            "Request_ID": "compliancecheck-57b24b10-0c35-4907-b850-4698ba0149a5",
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

# Defining global variables
API = "/cvs/compliance-report"
MODULE = "dellemc_vxrail_cvs_compliance_report"
LOG_FILE_PATH = "/tmp/vxrail_ansible_cvs_compliance_report.log"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
CHECK_STATUS_INTERVAL = 30
MAX_CHECK_COUNT = 60


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

        # Calls versioned method as attribute (ex: v1_generate_compliance_report_public)
        call_string = self.api_version_string + '_generate_compliance_report_public'
        # call_string = 'generate_compliance_report_public'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_generate_compliance_report_public = getattr(api_instance, call_string)
        return api_generate_compliance_report_public()

    def post_cvs_compliance_report(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.CVSPublicApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # generate compliance report
            response = self.get_versioned_response(api_instance, "Post /cvs/compliance-report")
        except ApiException as e:
            LOGGER.error("Exception when calling CVSPublicApi->%s_generate_compliance_report_public: %s\n", self.api_version_string, e)
            return 'error'
        requestid = response.request_id
        return requestid


def main():
    ''' Entry point into execution flow '''
    result_request_id = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        api_version_number=dict(type='int', required=False),
        timeout=dict(type='int', default=1800)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result_status = 0
    error = 0
    time_out = 0
    initial_timeout = module.params.get('timeout')
    LOGGER.info('----Start to generate cvs compliance report: ----')
    result_request_id = VxRailCluster().post_cvs_compliance_report()
    LOGGER.info('cvs: compliance report task_ID: %s.', result_request_id)
    if result_request_id == "error":
        module.fail_json(
            msg=f"The request id is not returned. Please see the log file {LOG_FILE_PATH} for more details")
    while result_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        result_response = utils.get_request_status(vxm_ip=module.params.get('vxmip'), vcadmin=module.params.get('vcadmin'),
                                                   vcpasswd=module.params.get('vcpasswd'), logger=LOGGER,
                                                   request_id=result_request_id)
        result_status = result_response.state
        LOGGER.info('compliance report_Task: status: %s.', result_status)
        LOGGER.info('compliance report_Task: details: %s.', result_response)
        LOGGER.info("compliance report_Task: Sleeping %s seconds...", CHECK_STATUS_INTERVAL)
        time.sleep(CHECK_STATUS_INTERVAL)
        time_out = time_out + CHECK_STATUS_INTERVAL
    if result_status == 'COMPLETED':
        LOGGER.info("-------cvs compliance report is successful.-----")
    else:
        LOGGER.info("------cvs compliance report Failed to generate.-----")
        error = result_response.error
        LOGGER.info('----Failed reason is : %s.----', error)
        vx_cvs_compliance_report = {'request_id': result_request_id, 'response_error': error}
        vx_facts_result = dict(failed=True, cvs_compliance_Report=vx_cvs_compliance_report,
                               msg=f"cvs compliance report has failed. Please see the {LOG_FILE_PATH} for more details")
        module.exit_json(**vx_facts_result)
    vx_cvs_compliance_report = {'status': result_status, 'request_id': result_request_id}
    vx_facts_result = dict(changed=True, cvs_compliance_Report=vx_cvs_compliance_report,
                           msg=f"cvs compliance report is successful. Please see the {LOG_FILE_PATH} for more details")
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
