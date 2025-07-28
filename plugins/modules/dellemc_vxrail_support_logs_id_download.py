#!/usr/bin/python
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_support_logs_id_download

short_description: Download the log binary by log id.

description:
- This module will download the support log binary by log id
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

  log_id:
    description:
      ID of the specific log
    required: False
    type: str

  output_file_path:
    description:
      Specifies the path to save the downloaded file. For example, '/path/to/output_file' indicates the file will be downloaded successfully to that location.
    required: True
    type: str 

  timeout:
    description:
      Time out value for downloading support log, the default value is 1800 seconds
    required: false
    type: int
    default: 1800
    
  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Download Support Logs
    dellemc_vxrail_support_logs_id_download:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        log_id: "{{ log_id }}"
        output_file_path: "{{ output_file_path }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"  
'''

RETURN = r'''
changed:
  description: Whether or not the resource has changed
  returned: always
  type: bool
message:
  description: Returns a success message with the downloaded file's name
  returned: always
  type: str
  sample: '/path/to/output_file downloaded successfully'
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

MODULE = "dellemc_vxrail_support_logs_id_download"
LOG_FILE_PATH = "/tmp/vxrail_log_support_logs_id_download.log"
LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return f"https://{self.vxm_ip}/rest/vxm"


class VxRailCluster():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.log_id = module.params.get('log_id')
        self.timeout = module.params.get('timeout')
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
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path,
                                                                   LOGGER)
            
        call_string = self.api_version_string + '_support_logs_id_download_get'

        LOGGER.info("Using utility method: %s\n", call_string)
        api_support_logs_download_get = getattr(api_instance, call_string)
        # get the parameters
        params = self.getRequestParams()
        LOGGER.info(f"params: {params}")
        return api_support_logs_download_get(self.log_id, **params)

    def getRequestParams(self):
        params = {
            # if you don't set the _preload_content to False, the response will become a string.
            '_preload_content': False,
        }

        return params 

    def download_support_logs_by_id(self):
        api_instance = vxrail_ansible_utility.SupportLogsApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = self.get_versioned_response(api_instance, 'Get support/logs/{logId}/download')
        except ApiException as e:
            LOGGER.error("Exception when calling SupportLogsApi->%s_support_logs_id_download_get: %s\n",
                         self.api_version_string, e)
            return 'error'
        LOGGER.info("Call %s/support/logs/{self.log_id}/download Get api response: %s\n", self.api_version_string, response)
        return response

def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(type='str', required=True),
        vcpasswd=dict(type='str', required=True, no_log=True),
        log_id=dict(type='str', required=True),
        output_file_path=dict(required=True),
        timeout=dict(type='int', default=1800),
        api_version_number=dict(type='int')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    result = VxRailCluster().download_support_logs_by_id()
    if result == 'error':
        module.fail_json(
            msg="Call Get support/logs/{{logId}}/download failed, please see log file {} for more error details.".format(LOG_FILE_PATH))
    LOGGER.info(f"Http Result: Status code - {result.status}")
    output_file_path = module.params.get('output_file_path')
    LOGGER.info('Outputfile Path: %s\n', output_file_path)
    with open(output_file_path, 'wb') as file:
        file.write(result.data)         
        module.exit_json(changed=True, message=f'{output_file_path} downloaded successfully')

if __name__ == "__main__":
    main()
