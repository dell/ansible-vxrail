#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_certificates_getcontent

short_description: Get certificate content according to fingerprint.

description:
- This module will return a fingerprint list.
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

  fingerprint:
    description:
      Target certificate's fingerprint you want to retrieve content from
    required: True
    type: str

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for getting system information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get a fingerprint list
    dellemc_vxrail_certificates_getcontent:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        fingerprint: "{{ fingerprint }}"
'''

RETURN = r'''
Cert_content:
  description: Return the content of certificate file according to the fingerprint parameter.
  returned: always
  type: dict
  sample: >-
    {
        "cert": "-----BEGIN CERTIFICATE-----\n......\n-----END X509 CRL-----"
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

RESULT = "Cert_content"
API = "/trust-store/certificates/{fingerprint}"
LOG_FILE_PATH = "/tmp/vxrail_ansible_getcertcontent.log"
MODULE = "dellemc_vxrail_certificates_getcontent"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailSystemUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailSystemUrls.cluster_url.format(self.vxm_ip)


class VxRailSystem():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.system_url = VxrailSystemUrls(self.vxm_ip)
        self.fingerprint = module.params.get('fingerprint')
        self.api_version_number = module.params.get('api_version_number')
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        call_string = self.api_version_string + '_trust_store_certificates_fingerprint_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_chassis_get = getattr(api_instance, call_string)
        return api_chassis_get(self.fingerprint)

    def invoke_public_api(self) -> dict:
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.CertificatesApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # Invoke api
            response = self.get_versioned_response(api_instance, "GET /trust-store/certificates/{fingerprint}")
        except ApiException as e:
            LOGGER.error("Exception when calling CertificatesApi->%s_trust_store_certificates_get: %s\n", str(self.api_version_string), e)
            return 'error'
        information = (f"{API} api response: %s\n", response)
        LOGGER.info(information)
        content_info = {'cert': response.cert}
        return content_info


def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        timeout=dict(type='int', default=60),
        api_version_number=dict(type='int'),
        fingerprint=dict(required=True)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailSystem().invoke_public_api()
    if result == 'error':
        module.fail_json(
            msg=f"Call {API} API failed,please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts = {RESULT: result}
    vx_facts_result = dict(changed=False, API_Facts=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
