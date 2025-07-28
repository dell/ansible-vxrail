#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm_vlcm_commit_draft

short_description: commit vlcm draft

description:
- This module will commit vLCM draft.
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
      Specify the API version to perform the upgrade.
    required: false
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

RETURN = r'''
VLCM_COMMIT_DRAFT_API:
  description: Commit vLCM draft
  returned: always
  type: dict
  sample: >-
        { "result": vlcm_draft_commit_result}
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
import json
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_NAME = "/tmp/vxrail_ansible_lcm_vlcm_commit_draft.log"
LOGGER = utils.get_logger("dellemc_vxrail_lcm_vlcm_commit_draft", LOG_FILE_NAME, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
CHECK_STATUS_INTERVAL = 60
MAX_CHECK_COUNT = 60


class VxrailVXMUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailVXMUrls.vxm_url.format(self.vxm_ip)


class VxRailLCMCommitVLCMDraft():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
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

    def post_commit_vlcm_draft(self):
        try:
            # create an instance of the API class
            api_instance = vxrail_ansible_utility.VLCMApi(vxrail_ansible_utility.ApiClient(self.configuration))
            # start commit vLCM draft with versioned api
            api_version_string = self.get_versioned_response('Post /lcm/vlcm/enablement/draft/commit')
            call_string = 'vlcm_enablement_draft_commit_post_' + api_version_string
            LOGGER.info("LCM vlcm_commit_draft version: %s", call_string)
            commit_vlcm_draft = getattr(api_instance, call_string)
            response = commit_vlcm_draft()
            LOGGER.info("commit vLCM draft api response:")
            LOGGER.info(response)
        except ApiException as e:
            LOGGER.error("Exception when calling VLCMApi vlcm_enablement_draft_commit_post_v1->%s: %s\n", call_string, e)
            return 'Fail to enable vLCM'
        return response.message

def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module

    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        api_version_number=dict(type='int', required=False)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    LOGGER.info('----Start to commit vLCM draft: ----')
    vlcm_draft_commit_result = VxRailLCMCommitVLCMDraft().post_commit_vlcm_draft()
    vx_lcm = {'result': vlcm_draft_commit_result}
    if vlcm_draft_commit_result == 'Successfully enable vLCM':
        LOGGER.info("-------Commit vLCM draft successfully.-----")
    else:
        LOGGER.info("------Commit vLCM draft unsuccessfully-----")

        LOGGER.info('----Failed reason is : %s.----', vlcm_draft_commit_result)
        vx_facts_result = dict(failed=True, VLCM_COMMIT_DRAFT_API=vx_lcm,
                               msg=f"Commit vLCM draft has failed. Please see the {LOG_FILE_NAME} for more details")
        module.exit_json(**vx_facts_result)
    vx_facts_result = dict(VLCM_COMMIT_DRAFT_API=vx_lcm,
                           msg=f"Commit vLCM draft is successful. Please see the {LOG_FILE_NAME} for more details")
    LOGGER.info("vx_facts_result: %s\n", vx_facts_result)
    module.exit_json(**vx_facts_result)

if __name__ == '__main__':
    main()
