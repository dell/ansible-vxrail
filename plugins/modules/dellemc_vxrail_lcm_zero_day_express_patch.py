#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm_0day_express_patch
short_description: Vxrail 0 day express patch

description:
- This module will execute Vxrail 0 day express patch
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
  component_bundle:
    description:
      The patch package path for the VxRail 0 day express patch
    required: True
    type: multipart-file
author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>
'''

EXAMPLES = r'''
    - name: Execute VxRail 0 Day Express Patch
      dellemc.vxrail.dellemc_vxrail_lcm_0day_express_patch:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        component_bundle: "{{ component_bundle }}"
        timeout: "{{ timeout | default(omit) }}"
        api_version_number: "{{ api_version_number | default(omit) }}"
'''
RETURN = r'''
VXRAIL_0DAY_EXPRESS_PATCH_API:
  description: Execute Vxrail 0 day express patch.
  returned: always
  type: dict {
  
  }
'''

import logging
import urllib3
import time
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

# Defining global variables
MODULE = "dellemc_vxrail_lcm_zero_day_express_patch"
LOG_FILE_PATH = "/tmp/vxrail_ansible_lcm_zero_day_express_patch.log"
DEFAULT_ERROR_MSG = "Please see the " + LOG_FILE_PATH + " for more details."

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class VxrailZeroDayExpressPatchUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailZeroDayExpressPatchUrls.vxm_url.format(self.vxm_ip)
    
class VxRailZeroDayExpressPatch():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.component_bundle = module.params.get('component_bundle')
        self.witness_user_name = module.params.get('witness_user_name')
        self.witness_user_password = module.params.get('witness_user_password')
        self.auto_witness_upgrade = module.params.get('auto_witness_upgrade')
        self.api_version_number = module.params.get('api_version_number')
        self.timeout = module.params.get('timeout')
        self.spent_time = 0
        self.check_interval = 1
        self.bundle_name = ""
        self.system_url = VxrailZeroDayExpressPatchUrls(self.vxm_ip)

        # API Instance
        self.get_status_api = None
        self.upload_api = None
        self.cancel_api = None
        self.upgrade_api = None
        self.precheck_api = None

        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = ""

        # patch upgrade request body
        
        self.upgrade_request_body = {'vcenter': {'vc_admin_user': {'username': self.vc_admin,'password': self.vc_password}}, 
                                     'witness': {'witness_user': {'username': self.witness_user_name, 'password':self.witness_user_password},
                                     'auto_witness_upgrade':self.auto_witness_upgrade}}

        #LOGGER.info("Body:%s\n", self.upgrade_request_body)
        
        # API instance
        self.api_instance = vxrail_ansible_utility.LCMUpgradeApi(vxrail_ansible_utility.ApiClient(self.configuration))
        LOGGER.info("self.vxm_ip: %s\n", self.vxm_ip)

    def getZeroDayPatchAPIs(self):
        LOGGER.info("Set all APIs for 0 day express patch\n")

        if self.get_status_api is None:
          if self.api_version_number is None:
             self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, "Get /lcm/patch/status", LOGGER)
             self.api_version_number = int(self.api_version_string.split('v')[1])
          else:
             self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, "Get /lcm/patch/status", LOGGER)
        
          call_string = self.api_version_string + '_lcm_patch_status_get'
          LOGGER.info("Using utility method: %s\n", call_string)
          self.get_status_api = getattr(self.api_instance, call_string)

        if self.upload_api is None:
          if self.api_version_number is None:
             self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, "Post /lcm/patch/upload", LOGGER)
             self.api_version_number = int(self.api_version_string.split('v')[1])
          else:
             self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, "Post /lcm/patch/upload", LOGGER)

          call_string = self.api_version_string + '_lcm_patch_upload_post'
          LOGGER.info("Using utility method: %s\n", call_string)
          self.upload_api = getattr(self.api_instance, call_string)

        if self.cancel_api is None:
          if self.api_version_number is None:
             self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, "Post /lcm/patch/cancel", LOGGER)
             self.api_version_number = int(self.api_version_string.split('v')[1])
          else:
             self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, "Post /lcm/patch/cancel", LOGGER)

          call_string = self.api_version_string + '_lcm_patch_cancel_post'
          LOGGER.info("Using utility method: %s\n", call_string)
          self.cancel_api = getattr(self.api_instance, call_string)

        if self.upgrade_api is None:
          if self.api_version_number is None:
             self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, "Post /lcm/patch/upgrade", LOGGER)
             self.api_version_number = int(self.api_version_string.split('v')[1])
          else:
             self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, "Post /lcm/patch/upgrade", LOGGER)

          call_string = self.api_version_string + '_lcm_patch_upgrade_post'
          LOGGER.info("Using utility method: %s\n", call_string)
          self.upgrade_api = getattr(self.api_instance, call_string)

        if self.precheck_api is None:
          if self.api_version_number is None:
             self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, "Post /lcm/patch/precheck", LOGGER)
             self.api_version_number = int(self.api_version_string.split('v')[1])
          else:
             self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, "Post /lcm/patch/precheck", LOGGER)

          call_string = self.api_version_string + '_lcm_patch_precheck_post'
          LOGGER.info("Using utility method: %s\n", call_string)
          self.precheck_api = getattr(self.api_instance, call_string)

        return
    
    def getZeroDayPatchStatus(self):
        respone = {}
        try:
          respone = self.get_status_api()
          LOGGER.info("Respone: %s\n", respone)
          return respone
        except ApiException as e:
          LOGGER.error("Error: %s\n", e)
        return respone
    
    def cancelZeroDayPatch(self):
        try:
          LOGGER.info("Cancel Zero Day Patch\n")
          self.cancel_api()
        except ApiException as e:
          LOGGER.error("Cancel with error: %s\n", e)
          vx_facts = {'Error message': " Cancel patch task failed, " + DEFAULT_ERROR_MSG}
          vx_facts_result = dict(failed=True, VXRAIL_ZERO_DAY_PATCH_API=vx_facts)
          module.exit_json(**vx_facts_result)

    def uploadPatchBundle(self):
        response = {}
        try:
            self.upload_api(component_bundle=self.component_bundle)
            response = self.getZeroDayPatchStatus()
            LOGGER.info("Upload Response: Step: %s, Status: %s\n", response.step, response.status)
            if response.step == "UPLOAD" and response.status == "COMPLETED":
               self.bundle_name = response.bundle_name
               return response
            else:
               LOGGER.error("Upload patch bundle fail")
               return None
        except ApiException as e:
          LOGGER.error("Error: %s\n", e)
        return None
    
    def precheckPatchBundle(self):
        response = {}
        precheck_status = 0
        try:
          self.precheck_api()
          while precheck_status not in ('COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED') and self.spent_time <= self.timeout:
              time.sleep(self.check_interval)
              self.spent_time = self.spent_time + self.check_interval
              response = self.getZeroDayPatchStatus()
              precheck_status = response.status
              if precheck_status in ("COMPLETED_WITH_ERRORS", 'FAILED'):
                 LOGGER.error("Precheck bundle fail")
                 return None
              else:
                 LOGGER.info("Precheck Response: Step: %s, Status: %s\n", response.step, response.status)

          if precheck_status == 'COMPLETED':
             return precheck_status
          else:
             return None
        except ApiException as e:
          LOGGER.error("Error: %s\n", e)

        return None
    
    def executeUpgradePacth(self):
        response = {}
        upgrade_status = 0
        LOGGER.info("Do patch upgrdde flow")
        try:
           self.upgrade_api(self.upgrade_request_body)
           while upgrade_status not in ('COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED') and self.spent_time <= self.timeout:
              time.sleep(self.check_interval)
              self.spent_time = self.spent_time + self.check_interval
              response = self.getZeroDayPatchStatus()
              upgrade_status = response.status
              if upgrade_status in ("COMPLETED_WITH_ERRORS", 'FAILED'):
                 LOGGER.error("Patch upgrade fail")
                 return None
              else:
                 LOGGER.info("Patch upgrade Response: Step: %s, Status: %s\n", response.step, response.status)

           if upgrade_status == 'COMPLETED':
              return upgrade_status
           else:
              return None
        except ApiException as e:
          LOGGER.error("Error: %s\n", e)

        return None
       

    def executeZeroDayExpressPatch(self):
        
        # Upload patch bundle
        upload_status = self.uploadPatchBundle()
        if upload_status is None:
           self.cancelZeroDayPatch()
           vx_facts = {'Error message': "Uploading patch bundle failed, " + DEFAULT_ERROR_MSG}
           vx_facts_result = dict(failed=True, VXRAIL_ZERO_DAY_PATCH_API=vx_facts)
           module.exit_json(**vx_facts_result)
        else:
           LOGGER.info("Upload patch bundle completed")

        # Precheck patch bundle
        precheck_status = self.precheckPatchBundle()
        if precheck_status is None:
           self.cancelZeroDayPatch()
           vx_facts = {'Error message': " Precheck patch bundle failed, " + DEFAULT_ERROR_MSG}
           vx_facts_result = dict(failed=True, VXRAIL_ZERO_DAY_PATCH_API=vx_facts)
           module.exit_json(**vx_facts_result)
        else:
           LOGGER.info("Precheck patch bundle completed")
           
        # Patch upgrade
        upgrade_status = self.executeUpgradePacth()
        if upgrade_status is None:
           self.cancelZeroDayPatch()
           vx_facts = {'Error message': " Patch bundle failed, " + DEFAULT_ERROR_MSG}
           vx_facts_result = dict(failed=True, VXRAIL_ZERO_DAY_PATCH_API=vx_facts)
           module.exit_json(**vx_facts_result)
        else:
           LOGGER.info("Precheck patch bundle completed")

        LOGGER.info("The Zero Day Patch process completed successfully")
        
def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module

    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        component_bundle=dict(required=True),
        witness_user_name=dict(type='str', required=False, default=""),
        witness_user_password=dict(type='str', required=False, no_log=True, default=""),
        auto_witness_upgrade=dict(type='bool', required=False, default=False),
        api_version_number=dict(type='int', required=False),
        timeout=dict(type='int', default=3600)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    zeroDayPatch = VxRailZeroDayExpressPatch()
    zeroDayPatch.getZeroDayPatchAPIs()
    init = zeroDayPatch.getZeroDayPatchStatus()

    if init.step == "NONE" and init.status == "NOT_STARTED":
      LOGGER.info("Start process\n")
      zeroDayPatch.executeZeroDayExpressPatch()
    else:
      zeroDayPatch.cancelZeroDayPatch()
      vx_facts = {'Step': init.step, 'Status': init.status, 'Message': DEFAULT_ERROR_MSG}
      vx_facts_result = dict(failed=True, VXRAIL_ZERO_DAY_PATCH_API=vx_facts)
      module.exit_json(**vx_facts_result)


    vx_facts = {}
    vx_facts_result = dict(changed=True, VXRAIL_ZERO_DAY_PATCH_API=vx_facts)
    module.exit_json(**vx_facts_result)

if __name__ == '__main__':
    main()