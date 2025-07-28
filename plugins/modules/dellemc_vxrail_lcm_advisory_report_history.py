#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm_advisory_report_history

short_description: Get the list of advisory report history

description:
- This module will get the list of advisory report history that contains information about all online and local lifecycle management updates.
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
    - name: Start to get lcm advisory report history
      dellemc_vxrail_lcm_advisory_report_history:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
LCM_Advisory_Report_History:
  description: Returns the request ID and whether the operation was successful.
  returned: always
  type: dict
  sample: >-
        {
            "history": [
              {
                "id": "00000000-0134-b23f-0000-00000134b23f"
                "report": ...
              }
            ]
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
API = "/cvs/report/history"
MODULE = "dellemc_vxrail_lcm_advisory_report_history"
LOG_FILE_PATH = "/tmp/vxrail_ansible_lcm_advisory_report_history.log"

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

        # Calls versioned method as attribute (ex: v1_cvs_advisory_report_history)
        call_string = self.api_version_string + '_cvs_advisory_report_history'
        # call_string = 'cvs_advisory_report_history'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_cvs_advisory_report_history = getattr(api_instance, call_string)
        return api_cvs_advisory_report_history()

    def get_lcm_advisory_report_history(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.CVSPublicApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # generate advisory report
            response = self.get_versioned_response(api_instance, "Get /cvs/report/history")
        except ApiException as e:
            LOGGER.error("Exception when calling CVSPublicApi->%s_cvs_advisory_report_history: %s\n", self.api_version_string, e)
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
        api_version_number=dict(type='int', required=False),
        timeout=dict(type='int', default=1800)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    LOGGER.info('----Start to get lcm advisory report history: ----')
    result = VxRailCluster().get_lcm_advisory_report_history()
    LOGGER.info('LCM: Advisory report hisory: %s.', result)
    history = [report.to_dict() for report in result]
    vx_lcm_advisory_report_history = {'history': history}
    vx_facts_result = dict(changed=True, LCM_Advisory_Report_History=vx_lcm_advisory_report_history,
                           msg=f"Get LCM advisory report history successfully. Please see the {LOG_FILE_PATH} for more details")
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
