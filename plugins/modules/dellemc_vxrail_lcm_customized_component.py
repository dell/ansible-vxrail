#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm_customized_component

short_description: Perform a upload with lcm upload api

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".

version_added: "1.6.0"

description:
- This module will upload a customized component for legacy lcm.
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

  customized_component:
    description:
      Specifies if the uploading file is a customized component. (true/false)
    required: True
    type: str

  checksum:
    description:
      Specifies the checksum of uploading file encoded in SHA512
    required: True
    type: str

  type:
    description:
      Only support driver/firmware/bundle customized type
    required: True
    type: str

  component_bundle:
    description:
      The path of the file to be uploaded on the local machine
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
    - name: Start to upload customized component
      dellemc_vxrail_lcm_customized_component:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        customized_component: "{{ customized_component }}"
        checksum: "{{ checksum }}"
        type: "{{ type }}"
        component_bundle: "{{ component_bundle }}"
        timeout: "{{ timeout | default(omit) }}"
        api_version_number: "{{ api_version_number | default(omit) }}"
'''

RETURN = r'''
UPLOAD_CUSTOMIZED_COMPONENT_API:
  description: The upload path of customized component.
  returned: always
  type: dict
  sample: >-
        {
            "file": "/data/store2/customized/tmp/components/NVD-VGPU_460.32.04-1OEM.700.0.0.15525992_17478485.zip"
        }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_PATH = "/tmp/vxrail_ansible_lcm_customized_component.log"
MODULE = "dellemc_vxrail_lcm_customized_component"
LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailCustomizedComponentUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailCustomizedComponentUrls.vxm_url.format(self.vxm_ip)


class VxrailCustomizedComponent():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.api_version_number = module.params.get('api_version_number')
        self.customized_component = module.params.get('customized_component')
        self.checksum = module.params.get('checksum')
        self.type = module.params.get('type')
        self.component_bundle = module.params.get('component_bundle')
        self.system_url = VxrailCustomizedComponentUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

        LOGGER.info("self.vxm_ip: %s\n", self.vxm_ip)

    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute
        LOGGER.info("Calls versioned method: %s\n", self.api_version_string)
        call_string = self.api_version_string + '_upload_bundle_customized_component'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_upload_bundle_customized_component_public = getattr(api_instance, call_string)
        return api_upload_bundle_customized_component_public(customized_component=self.customized_component, checksum=self.checksum, type=self.type,
                                                             component_bundle=self.component_bundle, _request_timeout=self.timeout)

    def upload_Customized_Component(self):
        response = {}
        try:
            # create an instance of the API class
            LOGGER.info("Upload customized component")
            api_instance = vxrail_ansible_utility.LCMPreCheckApi(vxrail_ansible_utility.ApiClient(self.configuration))
            response = self.get_versioned_response(api_instance, "Post /lcm/upgrade/upload-bundle")
            LOGGER.info("Response: %s\n", response)
        except ApiException as e:
            LOGGER.error("Exception when calling %s %s, response: %s\n", self.api_version_string, e, response)
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
        customized_component=dict(required=True),
        checksum=dict(required=True),
        type=dict(required=True),
        component_bundle=dict(required=True),
        api_version_number=dict(type='int', required=False),
        timeout=dict(type='int', default=3600)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    result = VxrailCustomizedComponent().upload_Customized_Component()
    if result == 'error':
        module.fail_json(msg=f"Uploading a customized component has failed. Please see the {LOG_FILE_PATH} for more details")

    vx_facts = {'file': result.file}
    vx_facts_result = dict(changed=True, UPLOAD_CUSTOMIZED_COMPONENT_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == '__main__':
    main()
