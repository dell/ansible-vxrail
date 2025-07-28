#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm_vlcm_delete_draft

short_description: delete vlcm draft

description:
- This module will delete vLCM draft.
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

  api_version_number:
    description:
      Specify the API version to perform the upgrade.
    required: false
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

RETURN = r'''
VLCM_DELETE_DRAFT_API:
  description: Delete vLCM draft
  returned: always
  type: dict
  sample: >-
        { "result": vlcm_delete_draft_result}
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
import json
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_NAME = "/tmp/vxrail_ansible_lcm_vlcm_delete_draft.log"
LOGGER = utils.get_logger("dellemc_vxrail_lcm_vlcm_delete_draft", LOG_FILE_NAME, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
CHECK_STATUS_INTERVAL = 60
MAX_CHECK_COUNT = 60


class VxrailVXMUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailVXMUrls.vxm_url.format(self.vxm_ip)


class VxRailLCMDeleteVLCMDraft():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.vc_root_account = module.params.get('vc_root_account')
        self.vc_root_passwd = module.params.get('vc_root_passwd')

        self.vxm_url = VxrailVXMUrls(self.vxm_ip)
        self.api_version_number = module.params.get('api_version_number')
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.vxm_url.set_host()

    def create_delete_draft_json(self):
        draft_json = {}
        draft_json['vc_admin_user'] = {'username': self.vc_admin, 'password': self.vc_password}
        draft_json['vcsa_root_user'] = {'username': self.vc_root_account, 'password': self.vc_root_passwd}

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

    def delete_vlcm_draft(self):
        try:
            # create an instance of the API class
            api_instance = vxrail_ansible_utility.VLCMApi(vxrail_ansible_utility.ApiClient(self.configuration))
            # start delete vLCM draft with versioned api
            api_version_string = self.get_versioned_response('Delete /lcm/vlcm/enablement/draft')
            call_string = 'vlcm_enablement_draft_delete_' + api_version_string
            LOGGER.info("LCM vlcm_delete_draft version: %s", call_string)
            delete_vlcm_draft = getattr(api_instance, call_string)

            # create request body with API version
            request_body = self.create_delete_draft_json()
            LOGGER.info("delete vLCM draft api request body:")
            LOGGER.info(request_body)
            delete_vlcm_draft(body=request_body)
            LOGGER.info("delete vLCM draft api successful")
        except ApiException as e:
            LOGGER.error("Exception when calling VLCMApi vlcm_enablement_draft_delete_v1->%s: %s\n", call_string, e)
            return 'error'
        return "success"

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
        api_version_number=dict(type='int', required=False)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    LOGGER.info('----Start to delete vLCM draft: ----')
    vlcm_delete_draft_result = VxRailLCMDeleteVLCMDraft().delete_vlcm_draft()
    LOGGER.info('LCM: delete vLCM draft result: %s.', vlcm_delete_draft_result)

    if vlcm_delete_draft_result == 'success':
        LOGGER.info("-------Delete vLCM draft successfully.-----")
        vx_lcm = {'result': 'Successfully delete vLCM draft'}
    else:
        LOGGER.info("------Delete vLCM draft unsuccessfully-----")
        vx_lcm = {'result': 'Fail to delete vLCM draft'}
        module.fail_json(
            msg=f"Delete vLCM draft has failed. Please see the {LOG_FILE_NAME} for more details")
    vx_facts_result = dict(VLCM_DELETE_DRAFT_API=vx_lcm,
                           msg=f"Delete vLCM draft is successful. Please see the {LOG_FILE_NAME} for more details")
    LOGGER.info("vx_facts_result: %s\n", vx_facts_result)
    module.exit_json(**vx_facts_result)

if __name__ == '__main__':
    main()
