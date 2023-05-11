#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_idrac_getavailableuserids

short_description: Get a list of iDRAC user slot IDs

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.5.0"

description:
- This module will retrieve a list of the available iDRAC user slot IDs.
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

  host_sn:
    description:
      Serial number of the host to retrieve specific host information
    required: True
    type: str

  timeout:
    description:
      Time out value for getting the list of iDRAC user slot IDs, the default value is 60 seconds
    required: False
    type: int
    default: 60

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Retrieve available user slot IDs
    dellemc_vxrail_idrac_getavailableuserids:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        host_sn: "{{ host_sn }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
IDRAC_USER_ID_API:
  description: Get a list of iDRAC user slot IDs
  returned: always
  type: dict
  sample: >-
    {
            "Available_User_Slot_IDs": [
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                12,
                13,
                14
            ]
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_idrac_getavailableuserids", "/tmp/vxrail_ansible_idrac_getavailableuserids.log",
                          log_devel=logging.DEBUG)
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
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.host_sn = module.params.get('host_sn')
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path,
                                                                   LOGGER)

        # Calls versioned method as attribute (ex: v1_hosts_sn_idrac_id_get)
        call_string = self.api_version_string + "_hosts_sn_idrac_id_get"
        LOGGER.info("Using utility method: %s\n", call_string)
        callhome_mode_change = getattr(api_instance, call_string)
        return callhome_mode_change(self.host_sn)

    def get_idrac_id(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.HostIDRACConfigurationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # Get iDRAC available user slot IDs
            response = self.get_versioned_response(api_instance, "GET /hosts/{sn}/idrac/available-user-ids")
        except ApiException as e:
            LOGGER.error("Exception when calling HostIDRACConfigurationApi->%s_hosts_sn_idrac_id_get: %s\n", self.api_version_string,
                         e)
            return 'error'
        LOGGER.info("%s/hosts/{sn}/idrac/available-user-ids api response: %s\n", self.api_version_string, response)
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
        host_sn=dict(type='str', required=True),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().get_idrac_id()
    if result == 'error':
        module.fail_json(msg="Call GET /hosts/{sn}/idrac/available-user-ids API failed,"
                             "please see log file /tmp/vxrail_ansible_idrac_getavailableuserids.log for more error details.")
    vx_facts = {"Available_User_Slot_IDs": result}
    vx_facts_result = dict(changed=True, IDRAC_USER_ID_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
