#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_certificate_generate_csr

short_description: Generate a CSR

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.4.0"

description:
- This module will generate a Certificate Signing Request.
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

  country:
    description:
      The two-letter country code
    required: True
    type: str

  state:
    description:
      The state or province name
    required: false
    type: str

  locality:
    description:
      The locality name
    required: True
    type: str

  organization:
    description:
      The organization name
    required: True
    type: str

  organization_unit:
    description:
      The organization unit name
    required: True
    type: str

  common_name:
    description:
      The common name
    required: True
    type: str

  email_address:
    description:
      The email address
    required: false
    type: str

  subject_alt_name:
    description:
      Specify the IP addresses or domains as the alternative names
    required: false
    type: list
    elements: str

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Generate a Certificate Signing Request
    dellemc_vxrail_certificate_generate_csr:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        country: "{{ country }}"
        state: "{{ state }}"
        locality: "{{ locality }}"
        organization: "{{ organization }}"
        organization_unit: "{{ organization_unit }}"
        common_name: "{{ common_name }}"
        email_address: "{{ email_address }}"
        subject_alt_name: "{{ subject_alt_name }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
csr_information:
  description: Return the the Certificate Signing Request information.
  returned: always
  type: dict
  sample: >-
    {
        "csr": "-----BEGIN CERTIFICATE REQUEST-----\n......\n-----END CERTIFICATE REQUEST-----"
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_certificate_generate_csr", "/tmp/vxrail_ansible_certificate_generate_csr.log", log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailClusterUrls.cluster_url.format(self.vxm_ip)


class VxRailCluster():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.country = module.params.get('country')
        self.state = module.params.get('state')
        self.locality = module.params.get('locality')
        self.organization = module.params.get('organization')
        self.organization_unit = module.params.get('organization_unit')
        self.common_name = module.params.get('common_name')
        self.email_address = module.params.get('email_address')
        self.subject_alt_name = module.params.get('subject_alt_name')
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        csr_info = {}
        csr_info['country'] = self.country
        csr_info['state'] = self.state
        csr_info['locality'] = self.locality
        csr_info['organization'] = self.organization
        csr_info['organization_unit'] = self.organization_unit
        csr_info['common_name'] = self.common_name
        csr_info['email_address'] = self.email_address
        csr_info['subject_alt_name'] = self.subject_alt_name

        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute (ex: v1_certificates_csr_post)
        call_string = self.api_version_string + '_certificates_csr_post'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_csr_post = getattr(api_instance, call_string)
        return api_csr_post(csr_info)

    def post_generate_csr(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.CertificatesApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = self.get_versioned_response(api_instance, 'Post /certificates/csr')
        except ApiException as e:
            LOGGER.error("Exception when calling CertificatesApi->%s_certificates_csr_post: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/certificates/csr api response: %s\n", self.api_version_string, response)
        return response


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        country=dict(required=True),
        state=dict(required=False),
        locality=dict(required=True),
        organization=dict(required=True),
        organization_unit=dict(required=True),
        common_name=dict(required=True),
        email_address=dict(required=False),
        subject_alt_name=dict(required=False, type='list', elements='str'),
        api_version_number=dict(type='int'),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    result = VxRailCluster().post_generate_csr()
    if result == 'error':
        module.fail_json(msg="Call POST /certificates/csr API failed, "
                             "please see log file /tmp/vxrail_ansible_certificate_generate_csr.log for more error details.")
    csr_info = {'csr': result.csr}
    vx_facts = {'csr_information': csr_info}
    vx_facts_result = dict(changed=True, GENERATE_CSR_API=vx_facts, msg="Generate a CSR successfully")
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
