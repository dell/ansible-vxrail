#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_certificates_get_scep_config

short_description: Get automated renewal configurations of the certificate.

description:
- This module will call /cluster/certificates/scep/config api to get automated renewal configurations of the VxRail Manager TLS certificate
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
      Time out value for getting automated renewal configurations, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get automated renewal configurations of the certificate
    dellemc_vxrail_certificates_get_scep_config:
      vxmip: "{{ vxmip }}"
      vcadmin: "{{ vcadmin }}"
      vcpasswd: "{{ vcpasswd }}"
'''

RETURN = r'''
SCEP_CONFIG:
  description: automated renewal configurations
  returned: always
  type: dict
  sample: >-
        {
          "scep_enabled": true,
          "error_code": null,
          "error_message": null,
          "caserver_url": "http://<server IP>/certsrv/mscep/mscep.dll/pkiclient.exe",
          "scep_on": true,
          "scep_renewal_interval_in_minutes": 180,
          "scep_days_before_expire": 30
        }
'''
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils
from vxrail_ansible_utility.rest import ApiException
import vxrail_ansible_utility
from ansible.module_utils.basic import AnsibleModule
import urllib3
import logging
import json


CLASS = "CertificatesApi"
API = "Certificates_SCEP_Config_Get"
FUNC = API.lower()
URI = "Get /cluster/certificates/scep/config"
RESULT = "SCEP_Config"
LOG_FILE_NAME = f"/tmp/vxrail_ansible_{FUNC}.log"
LOGGER = utils.get_logger(
    f"dellemc_vxrail_{FUNC}", LOG_FILE_NAME, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxRailUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxRailUrls.cluster_url.format(self.vxm_ip)


class VxRailHosts():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.api_version_number = module.params.get('api_version_number')
        self.hosts_url = VxRailUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.hosts_url.set_host()
        # Added for auto-version detection
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute
        call_string = f"{self.api_version_string}_{FUNC}"
        LOGGER.info("Using utility method: %s\n", call_string)
        api_call = getattr(api_instance, call_string)
        return api_call(_preload_content=False)

    def get_api_response(self):
        # create an instance of the API class
        api_class = getattr(vxrail_ansible_utility, CLASS)
        api_instance = api_class(
            vxrail_ansible_utility.ApiClient(self.configuration))
        response = None
        try:
            response = self.get_versioned_response(api_instance, URI)
        except ApiException as e:
            LOGGER.error("Exception when calling %s->%s_%s: %s\n", CLASS, self.api_version_string, FUNC, e)
            return 'error'
        LOGGER.info("Call %s%s api response: %s\n", self.api_version_string, URI, response)
        if not response:
            return "No available hosts"
        return json.loads(response.data)


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60),
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailHosts().get_api_response()

    if result == 'error':
        module.fail_json(
            msg=f"Call {URI} API failed,please see log file {LOG_FILE_NAME} for more error details.")
    vx_facts = {RESULT: result}
    vx_facts_result = {"changed": False, f"{API}_API": vx_facts}
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
