#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm_vlcm_image
short_description: Retrieve vLCM image informations

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".

version_added: "1.6.0"

description:
- This module will retrieve vLCM image informations
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

  vxm_root_account:
    description:
      The root account of VxRail Manager
    required: true
    type: str

  vxm_root_passwd:
    description:
      The password for the root account provided in vxm
    required: true
    type: str

  bundle:
    description:
      the file path of upgrade bundle on vxm
    required: True
    type: str

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for uploading customized component, the default value is 3600 seconds
    required: false
    type: int
    default: 3600

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
    - name: Start to retrieve vLCM image information from the provided bundle.
      dellemc_vxrail_lcm_vlcm_image:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        vxm_root_account: "{{ vxm_root_account }}"
        vxm_root_passwd: "{{ vxm_root_passwd }}"
        bundle: "{{ bundle }}"
        timeout: "{{ timeout | default(omit) }}"
        api_version_number: "{{ api_version_number | default(omit) }}"
'''

RETURN = r'''
VLCM_IMAGE_API:
  description: The vLCM image information from vLCM image information
  returned: always
  type: dict
  sample: >-
        {
          "VLCM_IMAGE_INFO": {
            "base_image": {
              "version": "7.0.3-0.0.18644231"
            },
            "components": {
              "MRVL-E4-CNA-Driver-Bundle": "5.0.219.0-1OEM.700.1.0.15843807",
              "Mellanox-nmlx5": "4.19.70.1-1OEM.700.1.0.15525992"
            },
            "hardware_support": {
              "com.vxrail.hsp": {
                "version": "8.0.000-27818744",
                "pkg": "vxrail"
              }
            }
          },
          "msg": ""
        }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_PATH = "/tmp/vxrail_ansible_lcm_vlcm_image.log"
MODULE = "dellemc_vxrail_ansible_lcm_vlcm_image"
LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailVXMUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailVXMUrls.vxm_url.format(self.vxm_ip)


class VxrailLCMVlcmImage():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.vxm_root_account = module.params.get('vxm_root_account')
        self.vxm_root_passwd = module.params.get('vxm_root_passwd')
        self.bundle = module.params.get('bundle')
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailVXMUrls(self.vxm_ip)
        self.api_version_string = "v?"
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        LOGGER.info("self.vxm_ip: %s\n", self.vxm_ip)

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path, request_body):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)
        call_string = self.api_version_string + '_vlcm_image_query'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_lcm_upgrade_vlcm_image_post = getattr(api_instance, call_string)
        return api_lcm_upgrade_vlcm_image_post(request_body)

    def create_request_json(self):
        ''' lcm node json '''
        request_json = {}
        request_json['bundle_file_locator'] = self.bundle
        vxrail_dict = {}
        vxrail_dict['vxm_root_user'] = {'username': self.vxm_root_account, 'password': self.vxm_root_passwd}
        request_json['vxrail'] = vxrail_dict
        LOGGER.info("Request body: %s\n", request_json)

        return request_json

    def queryContent(self, request_body):
        response = {}
        try:
            # create an instance of the API class
            LOGGER.info("Retrieve vLCM image information")
            api_instance = vxrail_ansible_utility.LCMUpgradeApi(vxrail_ansible_utility.ApiClient(self.configuration))
            response = self.get_versioned_response(api_instance, "Post /lcm/upgrade/vlcm/image", request_body)
            LOGGER.info("Response: %s\n", response)
        except ApiException as e:
            LOGGER.error("Exception when calling %s %s, response: %s\n", self.api_version_string, e, response)
            return 'error'
        return response.to_dict()


def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module

    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        vxm_root_account=dict(required=True),
        vxm_root_passwd=dict(required=True, no_log=True),
        bundle=dict(required=True),
        api_version_number=dict(type='int', required=False),
        timeout=dict(type='int', default=3600)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    request_json = VxrailLCMVlcmImage().create_request_json()
    result = VxrailLCMVlcmImage().queryContent(request_json)
    if result == 'error':
        module.fail_json(msg=f"Retrieve vLCM image informations has failed. Please see the {LOG_FILE_PATH} for more details")

    vx_facts = result
    vx_facts_result = dict(VLCM_IMAGE_INFO=vx_facts, msg=f"Retrieve vLCM image informations success. Please see the {LOG_FILE_PATH} for more details")
    LOGGER.info("vx_facts_result: %s\n", vx_facts_result)
    module.exit_json(**vx_facts_result)


if __name__ == '__main__':
    main()
