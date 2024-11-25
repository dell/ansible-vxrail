#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_certificates_get_all_info

short_description: Get the information of all the certificates in the trust store.

description:
- This module will return the information of all the certificates in the trust store.
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
      Time out value for getting system information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get the information of all the certificates in the trust store.
    dellemc_vxrail_certificates_get_all_info:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
'''

RETURN = r'''
Cert_content:
  description: Return the information of all the certificates in the trust store.
  returned: always
  type: list
  sample: >-
    [
        {
            "name": "Security Communication RootCA3",
            "status": "VALID",
            "status_message": "The certificate will expire in 59 days. For more information, see KB000082108.",
            "issued_by": "Security Communication RootCA3",
            "signature_algorithm": "sha256WithRSAEncryption",
            "issued_time": "Mar  4 18:38:26 2023 UTC",
            "expiration_time": "Mar  1 18:38:26 2033 UTC",
            "cert": "-----BEGIN CERTIFICATE-----\nMIIEMTCCAxmgAwIBAgIJAPK/2rz8EB+sMA...\n-----END CERTIFICATE-----",
            "filepath": "/var/lib/vmware-marvin/trust/lin/f081611a.0",
            "fingerprint": "27:96:BA:E6:3F:18:01:E2:77:26:1B:A0:D7:77:70:02:8F:20:EE:E4"
        }
    ]
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

RESULT = "Cert_content"
API = "/trust-store/certificates"
LOG_FILE_PATH = "/tmp/vxrail_ansible_certificates_get_all_info.log"
MODULE = "dellemc_vxrail_certificates_get_all_info"

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
        self.api_version_number = module.params.get('api_version_number')
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    def _format_cert_info(slef, certs_info):
        certInfolist = []
        for cert in certs_info:
            LOGGER.info(type(cert))
            cert_info = {}
            cert_info['name'] = cert.name
            cert_info['status'] = cert.status
            cert_info['status_message'] = cert.status_message
            cert_info['issued_by'] = cert.issued_by
            cert_info['signature_algorithm'] = cert.signature_algorithm
            cert_info['issued_time'] = cert.issued_time
            cert_info['expiration_time'] = cert.expiration_time
            cert_info['cert'] = cert.cert
            cert_info['filepath'] = cert.filepath
            cert_info['fingerprint'] = cert.fingerprint
            certInfolist.append(cert_info)
        return certInfolist      
        
        
    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        call_string = self.api_version_string + '_trust_store_certificates_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_all_cert_get = getattr(api_instance, call_string)
        return api_all_cert_get()

    def invoke_public_api(self) -> dict:
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.TrustStoreCertificatesInfoApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # Invoke api
            response = self.get_versioned_response(api_instance, "GET /trust-store/certificates")
        except ApiException as e:
            LOGGER.error("Exception when calling CertificatesApi->%s_trust_store_certificates_get: %s\n", str(self.api_version_string), e)
            return 'error'
        information = (f"{API} api response: %s\n", response)
        LOGGER.info(information)
        return self._format_cert_info(response)


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
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailSystem().invoke_public_api()
    if result == 'error':
        module.fail_json(
            msg=f"Call {API} API failed,please see log file {LOG_FILE_PATH} for more error details.")

    vx_facts = {'certificats': result}
    vx_facts_result = dict(changed=False, Certificate_Info=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
