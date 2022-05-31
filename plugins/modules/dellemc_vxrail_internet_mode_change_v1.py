#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_internet_mode_change_v1

short_description: Change VxRail Internet Mode

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.3.0"

description:
- This module will change the system's Internet Mode.
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

  is_dark_site:
    description:
      Whether the system network should be set to a dark site or not.
    required: True
    type: bool

  timeout:
    description:
      Time out value for changing internet mode information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>
'''

EXAMPLES = r'''
  - name: Changes the VxRail Internet Mode
    dellemc_vxrail_internet_mode_change_v1:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        is_dark_site: "{{ is_dark_site }}"
        timeout : "{{ timeout }}"
'''

RETURN = r'''
Internet_Mode_Change:
  description: Change the current internet mode (is_dark_site) for the system. Returns the value that was set.
  returned: always
  type: dict
  sample: >-
        {
            "is_dark_site": false
        }

'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_internet_mode_change_v1",
                          "/tmp/vxrail_ansible_internet_mode_change_v1.log",
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
        self.is_dark_site = module.params.get('is_dark_site')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

    def put_v1_internet_mode(self):
        internet_mode_info = {}
        internet_mode_info['is_dark_site'] = self.is_dark_site
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemNetworkApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # put v1 internet mode information
            response = api_instance.v1_system_internet_mode_put(internet_mode_info)
        except ApiException as e:
            LOGGER.error("Exception when calling SystemNetworkApi->v1_system_internet_mode_put: %s\n",
                         e)
            return 'error'
        LOGGER.info("v1/system/internet-mode PUT api response: %s\n", response)
        LOGGER.info("is_dark_site set to: %s\n", self.is_dark_site)
        return dict(internet_mode_info.items())


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        is_dark_site=dict(type='bool', required=True),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().put_v1_internet_mode()
    if result == 'error':
        module.fail_json(msg="Call PUT V1/system/internet-mode API failed,please see log file "
                             "/tmp/vxrail_ansible_internet_mode_change_v1.log for more error details.")
    vx_facts = {'Internet_Mode_Change': result}
    vx_facts_result = dict(changed=True, V1_System_Internet_Mode_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
