#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_certificate_update

short_description: Update the VxRail Manager certificate

description:
- This module will update the VxRail Manager certificate
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

  cert:
    description:
      Content of the new certificate in PEM format. Each line should be followed by an escape character "\n".
    required: True
    type: str

  root_cert_chain:
    description:
      Contents of the certificate chain in PEM format. The root CA certificate comes first, followed by the intermediate CA certificates (if any).
    required: True
    type: list
    elements: str

  private_key:
    description:
      Contents of the private key in PEM format. Only an RSA private key is allowed.
      The private key can be omitted if the provided certificate is issued based on the CSR generated by /v1/certificates/csr.
    required: False
    type: str

  password:
    description:
      Password for the new .pfx file
    required: False
    type: str

  vc_admin_account:
    description:
      VC admin account for invoke VC API to send the new root cert to VC trust store
    required: False
    type: str

  vc_admin_password:
    description:
      VC admin password for invoke VC API to send the new root cert to VC trust store
    required: False
    type: str

  timeout:
    description:
      Time out value for getting update status, the default value is 600 seconds
    required: false
    type: int
    default: 600

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Update the VxRail Manager certificate
    dellemc_vxrail_certificate_update:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        cert: "{{ cert }}"
        root_cert_chain: "{{ root_cert_chain }}"
        private_key: "{{ private_key }}"
        password: "{{ password }}"
        vc_admin_account: "{{ vc_admin_account }}"
        vc_admin_password: "{{ vc_admin_password }}"
        timeout: "{{timeout}}"
        api_version_number: "{{api_version_number}}"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
certificate_update_information:
  description: certificate update status summary
  returned: always
  type: dict
  sample: >-
   {
      "request_id": "9e27ae96-33a2-47f0-89a7-dbd4376db1b6",
      "status": "COMPLETED"
   }
'''

import logging
import urllib3
import time
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

logging.getLogger("urllib3").setLevel(logging.ERROR)
LOGGER = utils.get_logger("dellemc_vxrail_certificate_update", "/tmp/vxrail_ansible_certificate_update.log", log_devel=logging.DEBUG)
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
        self.cert = module.params.get('cert')
        self.root_cert_chain = module.params.get('root_cert_chain')
        self.private_key = module.params.get('private_key')
        self.password = module.params.get('password')
        self.vc_admin_account = module.params.get('vc_admin_account')
        self.vc_admin_password = module.params.get('vc_admin_password')
        self.timeout = module.params.get('timeout')
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

    # Because the type of root_cert_chain is different between V3 and previous version
    def _reassign_req_parameters(self, cert_info):
        if self.api_version_number == 1 or self.api_version_number == 2:
            LOGGER.info("Reassign root_cert_chain and set primary_key\n")
            cert_info['root_cert_chain'] = ''.join(self.root_cert_chain)
            cert_info['primary_key'] = self.private_key

    def check_parameters(self):
        if self.api_version_number not in [1, 2]:
            if not self.vc_admin_account or not self.vc_admin_password:
                LOGGER.error('v3 API needs provide "vc_admin_password" and "vc_admin_password" in request body')
                return 'Missing required arguments: vc_admin_password and vc_admin_password'
        return 'success'

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        cert_info = {}
        cert_info['cert'] = self.cert
        cert_info['root_cert_chain'] = self.root_cert_chain
        cert_info['private_key'] = self.private_key
        cert_info['password'] = self.password
        cert_info['vc_admin_account'] = self.vc_admin_account
        cert_info['vc_admin_password'] = self.vc_admin_password

        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self._reassign_req_parameters(cert_info)
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute (ex: v1_certificates_import_vxm_post)
        call_string = self.api_version_string + '_certificates_import_vxm_post'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_cert_update_post = getattr(api_instance, call_string)
        return api_cert_update_post(cert_info)

    def post_certificate_import(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.CertificatesApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = self.get_versioned_response(api_instance, 'POST /certificates/import-vxm')
        except ApiException as e:
            LOGGER.error("Exception when calling CertificatesApi->%s_certificates_import_vxm_post: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/certificates/import-vxm api response: %s\n", self.api_version_string, response)
        return response

    def get_request_status(self, request_id):
        job_id = request_id
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.RequestStatusApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = api_instance.v1_request_id_get(job_id)
        except (ConnectionError) as e:
            LOGGER.info("Exception when calling v1_requests_id_get e: %s\n", e)
        except Exception as e:
            LOGGER.info("Exception when calling v1_requests_id_get e: %s\n", e)
            response = ""
        return response

    def get_request_info(self, response):
        statusInfo = {}
        statusInfolist = []
        data = response
        statusInfo['id'] = data.id
        statusInfo['state'] = data.state
        statusInfo['owner'] = data.owner
        statusInfo['progress'] = data.progress
        statusInfo['extension'] = data.extension
        statusInfo['start_time'] = data.start_time
        statusInfo['end_time'] = data.end_time
        statusInfolist.append(dict(statusInfo.items()))
        return statusInfolist


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        cert=dict(required=True),
        root_cert_chain=dict(required=True, type='list', elements='str'),
        private_key=dict(required=False, no_log=True),
        password=dict(required=False, no_log=True),
        vc_admin_account=dict(required=False),
        vc_admin_password=dict(required=False, no_log=True),
        timeout=dict(type='int', default=600),
        api_version_number=dict(type='int')
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    initial_timeout = module.params.get('timeout')
    api_version_number = module.params.get('api_version_number')
    update_status = 0
    time_out = 0

    result = VxRailCluster().check_parameters()
    if result != 'success':
        module.fail_json(msg=result + ", please see log file /tmp/vxrail_ansible_certificate_update.log for more error details.")

    result = VxRailCluster().post_certificate_import()
    if result == 'error':
        module.fail_json(msg="Call POST /certificates/import-vxm API failed,"
                             "please see log file /tmp/vxrail_ansible_certificate_update.log for more error details.")

    if api_version_number == 1:
        LOGGER.info('v1 API is not a async API, so return a message only')
        update_status = 'COMPLETED'
    else:
        update_request_id = result.request_id
        LOGGER.info('Update certificate: VxRail task_ID: %s.', update_request_id)

    while update_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        LOGGER.info("Get Update_Task : sleeping 10 seconds...")
        time.sleep(10)
        time_out = time_out + 10
        update_response = VxRailCluster().get_request_status(update_request_id)
        if update_response:
            update_status = update_response.state
            update_result = VxRailCluster().get_request_info(update_response)
            LOGGER.info('Update_Task: status: %s.', update_status)
            LOGGER.info('Update_Task: details: %s.', update_result)

    if update_status == 'COMPLETED':
        LOGGER.info("-----Updating Certificate Completed-----")
    else:
        LOGGER.info("------Updating Certificate Failed-----")
        vx_update_cert = {'request_id': update_request_id, 'response_error': update_result}
        vx_facts_result = dict(failed=True, UPDATE_CERT_API=vx_update_cert, msg="The updating certificate has failed."
                               "Please see the /tmp/vxrail_ansible_certificate_update.log for more details")
        module.exit_json(**vx_facts_result)

    if api_version_number == 1:
        update_info = {'message': result.message}
    else:
        update_info = {'request_id': result.request_id, 'status': update_status}

    vx_facts = {'certificate_update_information': update_info}
    vx_facts_result = dict(changed=True, UPDATE_CERT_API=vx_facts, msg="Update certificate successfully")
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
