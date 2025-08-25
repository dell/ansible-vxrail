#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm_acg_available_online_download

short_description: Get a available online package download

description:
- This module will downoad available online package from ACG server
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

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
    - name: Get available online updates packages
      dellemc.vxrail.dellemc_vxrail_lcm_acg_available_online_download:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
'''

RETURN = r'''
GET_AVAILABLE_DOWNLOAD_API:
  description: Get available online updates packages.
  returned: always
  type: dict 
'''

import logging
import urllib3
import time
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

# Defining global variables
MODULE = "dellemc_vxrail_lcm_acg_available_online_download"
LOG_FILE_PATH = "/tmp/vxrail_ansible_lcm_acg_available_online_download.log"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailAvailableDownloadUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailAvailableDownloadUrls.vxm_url.format(self.vxm_ip)
      

class VxrailACGAvailableDownload():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.api_version_number = module.params.get('api_version_number')
        self.timeout = module.params.get('timeout')
        self.system_url = VxrailAvailableDownloadUrls(self.vxm_ip)
        self.update_id = ""
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_instance = vxrail_ansible_utility.LCMUpgradeApi(vxrail_ansible_utility.ApiClient(self.configuration))
        
        LOGGER.info("self.vxm_ip: %s, self.vc_admin: %s, self.vc_password: %s\n", self.vxm_ip, self.vc_admin, self.vc_password)
    
    def get_versioned_response(self, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)
        
        # Calls versioned method as attribute
        LOGGER.info("Calls versioned method: %s\n", self.api_version_string)
        call_string = self.api_version_string + '_lcm_available_online_updates_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        get_api = getattr(self.api_instance, call_string)
        LOGGER.info(get_api())
        return get_api()
      
    def download_api_with_versioned_response(self, module_path):
      # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)
            
        # Calls versioned method as attributeclea
        LOGGER.info("Calls versioned method: %s\n", self.api_version_string)
        call_string = self.api_version_string + '_lcm_available_online_updates_download_post'
        LOGGER.info("Using utility method: %s\n", call_string)
        post_api = getattr(self.api_instance, call_string)
        return post_api
    
    def get_status_response(self, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attributeclea
        LOGGER.info("Calls versioned method: %s\n", self.api_version_string)
        call_string = self.api_version_string + '_lcm_download_progress_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        get_status_api = getattr(self.api_instance, call_string)
        return get_status_api
      
    def get_available_download(self):
        response = {}
        try:
            LOGGER.info("Get available download packages from ACG server")
            response = self.get_versioned_response("Get /lcm/available-online-updates")
        except ApiException as e:
            LOGGER.error("Exception when calling %s %s, response: %s\n", self.api_version_string, e, response)
        return response
    
    def start_download_package_with_id(self, package_id):
        downlad_status = 0
        time_out = 0
        check_interval = 1
        LOGGER.info("Start download available download packages from ACG server")
        get_download_status = self.get_status_response("Get /lcm/download-progress/{request_id}")
        download_api = self.download_api_with_versioned_response("Post /lcm/available-online-updates/{update_id}/download")
        try:
          response = download_api(package_id)
          LOGGER.info("Get Request_id: %s and timeout: %s", response.request_id, self.timeout)
        except ApiException as e:
          LOGGER.error("Exception: %s\n", e)
          vx_facts = {'response_error': "Call download API fail"}
          vx_facts_result = dict(failed=True, GET_AVAILABLE_DOWNLOAD_API=vx_facts, msg="Task has failed. Please see the /tmp/vxrail_ansible_lcm_acg_available_online_download.log for more details")
          module.exit_json(**vx_facts_result)
          return
        
        while downlad_status not in ('COMPLETED', 'FAILED') and time_out < self.timeout:
            progress = get_download_status(str(response.request_id))
            LOGGER.info("Progress status: %s", progress.status)
            downlad_status = progress.status
            time.sleep(check_interval)
            time_out = time_out + check_interval

        if downlad_status == "COMPLETED":
            LOGGER.info("Download is completed")
        elif time_out >= self.timeout:
            LOGGER.info("Due to task timeout %s sec, the download process failed", self.timeout)
            vx_facts = {'request_id': response.request_id, 'response_error': "timeout"}
            vx_facts_result = dict(failed=True, GET_AVAILABLE_DOWNLOAD_API=vx_facts, msg="Task has failed. Please see the /tmp/vxrail_ansible_lcm_acg_available_online_download.log for more details")
            module.exit_json(**vx_facts_result)
        else:
            LOGGER.info("The download process failed")
            vx_facts = {'request_id': response.request_id, 'response_error': "timeout"}
            vx_facts_result = dict(failed=True, GET_AVAILABLE_DOWNLOAD_API=vx_facts, msg="Task has failed. Please see the /tmp/vxrail_ansible_lcm_acg_available_online_download.log for more details")
            module.exit_json(**vx_facts_result)
        
def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module
    
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        api_version_number=dict(type='int', required=False),
        timeout=dict(type='int', default=3600)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    
    result = VxrailACGAvailableDownload().get_available_download()
 
    if not result:
        module.fail_json(msg=f"Get available download packages has failed. Please see the {LOG_FILE_PATH} for more details")
    else:
        LOGGER.info("Try to download by id: %s\n", result[0].id)
        VxrailACGAvailableDownload().start_download_package_with_id(result[0].id)

        
    vx_facts = {'id': result[0].id}
    vx_facts_result = dict(changed=True, GET_AVAILABLE_DOWNLOAD_API=vx_facts)
    module.exit_json(**vx_facts_result)
    

if __name__ == '__main__':
    main()