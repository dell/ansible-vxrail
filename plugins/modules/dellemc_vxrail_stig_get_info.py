#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_stig_get_info

short_description: Retrieve information related to STIG regulations.

description:
- This module will retrieve information related to STIG regulations.
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
      Time out value for getting STIG information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get information related to STIG regulations
    dellemc_vxrail_stig_get_info:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
STIG_Information:
  description: Information related to STIG regulations
  returned: always
  type: dict
  sample: >-
        {
          "vmware": {
              "server_management_host": "vcluster101-vcsa.vv009.local",
              "virtualization_systems": [
                  {
                      "id": "vm-24",
                      "server_type": "VXM"
                  },
                  {
                      "id": "vm-25",
                      "server_type": "VCENTER"
                  }
              ],
              "configured_hosts": [
                  {
                      "hypervisor_hostname": "vcluster101-esx01.vv009.local",
                      "hypervisor_management_usernames": [
                          "management"
                      ]
                  },
                  {
                      "hypervisor_hostname": "vcluster102-esx01.vv009.local",
                      "hypervisor_management_usernames": [
                          "management"
                      ]
                  },
                  {
                      "hypervisor_hostname": "vcluster103-esx01.vv009.local",
                      "hypervisor_management_usernames": [
                          "management"
                      ]
                  }
              ],
              "satellite_node_hosts": [
                  {
                      "hypervisor_hostname": "vcluster301-esx01.vvst.local",
                      "hypervisor_management_usernames": [
                          "management"
                      ]
                  },
                  {
                      "hypervisor_hostname": "vcluster302-esx01.vvst.local",
                      "hypervisor_management_usernames": [
                          "management"
                      ]
                  }
              ]
          },
          "ntp_servers": [
            "172.16.1.167",
            "172.16.1.168"
          ],
          "syslog_servers": [
            "172.16.1.169",
            "172.16.1.170"
          ]
        }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_stig_get_info",
                          "/tmp/vxrail_ansible_stig_get_info.log",
                          log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return f"https://{self.vxm_ip}/rest/vxm"


class VxRailCluster():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        self.api_version_number = module.params.get('api_version_number')

        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number,
                                                                   module_path,
                                                                   LOGGER)

        # Calls versioned method as attribute (ex: get_v1_stig_info)
        call_string = f'get_{self.api_version_string }_stig_info'
        LOGGER.info("Using utility method: %s\n", call_string)
        stig_info_get = getattr(api_instance, call_string)
        return stig_info_get()

    def get_stig_info(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.STIGInformationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query STIG information
            response = self.get_versioned_response(api_instance, "GET /stig/info")
        except ApiException as e:
            LOGGER.error("Exception when calling STIGInformationApi->get_%s_stig_info: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/stig/info api response: %s\n", self.api_version_string, response)
        return response.to_dict()


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        timeout=dict(type='int', default=60),
        api_version_number=dict(type='int')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().get_stig_info()
    if result == 'error':
        module.fail_json(msg="Call /stig/info API failed,"
                             "please see log file /tmp/dellemc_vxrail_stig_get_info.log for more error details.")
    vx_facts = {'STIG_Information': result}
    vx_facts_result = dict(changed=False, Stig_Info_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
