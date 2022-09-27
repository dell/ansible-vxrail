#!/usr/bin/python
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_get_proxy

short_description: Retrieve VxRail System Proxy Settings

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.4.0"

description:
- This module will retrieve the VxRail System Proxy Settings.
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
      Time out value for getting proxy information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get VxRail System Proxy Information
    dellemc_vxrail_system_get_proxy:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        api_version_number: "{{ api_version_number }}"
        timeout : "{{ timeout }}"
'''

RETURN = r'''
System_Proxy_Info:
  description: The retrieved VxRail system proxy information
  returned: always
  type: dict
  sample: >-
    {
        "server": "192.168.106.108",
        "port": 3128,
        "username": "proxyclient",
        "type": "SOCKS",
        "socks_version": 5
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

# Defining global variables
API = "GET /system/proxy"
MODULE = "dellemc_vxrail_system_get_proxy"
LOG_FILE_PATH = "/tmp/vxrail_ansible_system_get_proxy.log"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():

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
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
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

        # Calls versioned method as attribute (ex: v1_system_proxy_get)
        call_string = self.api_version_string + '_system_proxy_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        system_proxy_get = getattr(api_instance, call_string)
        return system_proxy_get()

    def get_proxy_settings(self):
        proxy_info = {}
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemProxySettingsApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query proxy information
            response = self.get_versioned_response(api_instance, "/system/proxy")
        except ApiException as e:
            LOGGER.error("Exception when calling SystemProxySettingsApi->%s_system_proxy_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s api response: %s", API, response)
        data = response
        proxy_info['server'] = data.server
        proxy_info['port'] = data.port
        proxy_info['username'] = data.username
        proxy_info['type'] = data.type
        if data.socks_version:
            proxy_info['socks_version'] = data.socks_version
        return dict(proxy_info.items())


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
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().get_proxy_settings()
    if result == 'error':
        module.fail_json(
            msg=f"Call {API} API failed, please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts = {'System_Proxy_Info': result}
    vx_facts_result = dict(changed=False, SYSTEM_PROXY_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
