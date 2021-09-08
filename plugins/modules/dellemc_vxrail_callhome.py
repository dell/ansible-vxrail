#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_callhome

short_description: Get call home server information (v2)

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description:
- This module will retrieve information about the call home servers.
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
      Time out value for getting callhome information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - Hongmei Gao(@gaohongmei) <s.gao@dell.com>

'''

EXAMPLES = r'''
  - name: Retrives VxRail Callhome Information
    dellemc_vxrail_callhome:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"
'''

RETURN = r'''
Callhome_Information:
  description: callhome information summary
  returned: always
  type: dict
  sample: >-
    {
     "address_list": [
                        {
                            "address": "20.11.73.109",
                            "primary": true,
                            "upgradeRequestId": null,
                            "version": "3.52.00.08"
                        }
                    ],
     "integrated": true,
     "site_id": "11145366",
     "status": "registered"   
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from vxrail_ansible_utility import configuration as utils

LOGGER = utils.get_logger("dellemc_vxrail_callhome", "/tmp/vxrail_ansible_callhome.log", log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailCallhomeUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailCallhomeUrls.cluster_url.format(self.vxm_ip)


class VxRailCallhome():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.system_url = VxrailCallhomeUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        response = ''

    def get_v2_callhome(self):
        callhomeInfos = {}
        callhomeInfolist = []
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.CallHomeOperationsApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query v2 callhome information
            response = api_instance.v2_callhome_info_get()
        except ApiException as e:
            LOGGER.error("Exception when calling CallHomeOperationsApi->v2_callhome_info_get: %s\n", e)
            return 'error'
        LOGGER.info("v2/callhome api response: %s\n", response)
        data = response
        callhomeInfos['status'] = data.status
        callhomeInfos['integrated'] = data.integrated
        callhomeInfos['address_list'] = data.address_list
        if data.site_id is not None:
            callhomeInfos['site_id'] = data.site_id
        if len(data.address_list) > 0:
            callhomeInfos['address_list'] = []
            callhome_list = data.address_list
            callhome = {}
            systemInfo_callhome_list = []
            for i in range(len(callhome_list)):
                callhome['address'] = callhome_list[i].address
                callhome['primary'] = callhome_list[i].primary
                callhome['version'] = callhome_list[i].version
                callhome['upgradeRequestId'] = callhome_list[i].upgrade_request_id
                systemInfo_callhome_list.append(dict(callhome.items()))
            callhomeInfos['address_list'] = systemInfo_callhome_list
        callhomeInfolist.append(dict(callhomeInfos.items()))
        return callhomeInfolist


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
    result = VxRailCallhome().get_v2_callhome()
    if result == 'error':
        module.fail_json(msg="Call V2/callhome API failed,please see log file /tmp/vxrail_ansible_callhome.log for more error details.")
    vx_facts = {'Callhome_Information': result}
    vx_facts_result = dict(changed=False, V2_Callhome_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
