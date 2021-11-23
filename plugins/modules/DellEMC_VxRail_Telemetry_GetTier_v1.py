#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: DellEMC_VxRail_Telemetry_GetTier_v1

short_description: Retrieve VxRail Telemetry Tier

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.1.0"

description:
- This module will retrieve the system's Telemetry tier.
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

  timeout:
    description:
      Time out value for getting telemetry information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Retrives VxRail Telemetry Information
    dellemc-vxrail-telemetry-info:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"
'''

RETURN = r'''
Telemetry_tier:
  description: The current telemetry tier for the system
  returned: always
  type: dict
  sample: >-
        {
            "level": "BASIC"
        }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from vxrail_ansible_utility import configuration as utils

LOGGER = utils.get_logger("dellemc_vxrail_telemetry_info", "/tmp/vxrail_ansible_telemetry_info.log", log_devel=logging.DEBUG)
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
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

    def get_v1_telemetry_tier(self):
        TelemInfo = {}
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.TelemetryReportingApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query v1 telemetry information
            response = api_instance.query_telemetry_tier_setting_information()
        except ApiException as e:
            LOGGER.error("Exception when calling TelemetryReportingApi->query_telemetry_tier_setting_information: %s\n", e)
            return 'error'
        LOGGER.info("v1/telemetry/tier api response: %s\n", response)
        data = response
        TelemInfo['level'] = data.level
        return dict(TelemInfo.items())


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().get_v1_telemetry_tier()
    if result == 'error':
        module.fail_json(msg="Call V1/telemetry/tier API failed,please see log file /tmp/vxrail_ansible_telemetry_info.log for more error details.")
    vx_facts = {'Telemetry_Tier': result}
    vx_facts_result = dict(changed=False, V1_Telemetry_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
