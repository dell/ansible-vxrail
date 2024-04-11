#!/usr/bin/python
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_set_proxy

short_description: Set VxRail System Proxy settings

description:
- This module will set the VxRail system's proxy settings. Returns the newly-set values.
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

  esrs_passwd:
    description:
      Password for the Secure Remote Services. If internal SRS is enabled, the password is required.
    required: False
    type: str

  server:
    description:
      The IP address of the proxy server.
    required: True
    type: str

  proxy_port:
    description:
      The port number used by the proxy server.
    required: True
    type: int

  proxy_user:
    description:
      The client username for the proxy server
    required: True
    type: str

  proxy_passwd:
    description:
      The client password for the proxy server
    required: True
    type: str

  type:
    description:
      Type of proxy server. Supported types are ( "HTTP" ) and ( "SOCKS" ). Must be capitalized.
    required: True
    type: str

  socks_version:
    description:
      The version of the Socks proxy server. This parameter is only required if the proxy type is SOCKS.
    required: False
    type: int

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for setting proxy information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Sets the VxRail System proxy settings
    dellemc_vxrail_system_set_proxy:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        esrs_passwd: "{{ esrs_passwd }}"
        server: "{{ server }}"
        proxy_port: "{{ port }}"
        proxy_user: "{{ proxy_user }}"
        proxy_passwd: "{{ proxy_passwd }}"
        type: "{{ type }}"
        socks_version: "{{ socks_version }}"
        api_version_number: "{{ api_version_number }}"
        timeout: "{{ timeout }}"
'''

RETURN = r'''
System_Proxy_Set:
  description: Sets the VxRail System Proxy settings. Returns the values that were set.
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

API = "POST /system/proxy"
MODULE = "dellemc_vxrail_system_set_proxy"
LOG_FILE_PATH = "/tmp/vxrail_ansible_system_set_proxy.log"
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
        self.esrs_password = module.params.get('esrs_passwd')
        self.server = module.params.get('server')
        self.proxy_port = module.params.get('proxy_port')
        self.proxy_username = module.params.get('proxy_user')
        self.proxy_password = module.params.get('proxy_passwd')
        self.type = module.params.get('type')
        self.socks_version = module.params.get('socks_version')
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    def get_versioned_response(self, api_instance, module_path, proxy_change_info):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number,
                                                                   module_path,
                                                                   LOGGER)

        # Calls versioned method as attribute (ex: v1_system_proxy_post)
        call_string = self.api_version_string + '_system_proxy_post'
        LOGGER.info("Using utility method: %s\n", call_string)
        system_proxy_post = getattr(api_instance, call_string)
        return system_proxy_post(proxy_change_info)

    def post_proxy(self):
        proxy_change_info = {}
        spec_info = {
            "server": self.server,
            "port": self.proxy_port,
            "username": self.proxy_username,
            "pwd": self.proxy_password,
            "type": self.type
        }

        # Add optional params if found
        if self.esrs_password:
            proxy_change_info['esrs_password'] = self.esrs_password
        if self.socks_version:
            spec_info["socks_version"] = self.socks_version

        proxy_change_info["proxy_spec"] = spec_info

        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemProxySettingsApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # post proxy information
            response = self.get_versioned_response(api_instance, "POST /system/proxy", proxy_change_info)
        except ApiException as e:
            LOGGER.error("Exception when calling SystemProxySettingsApi->%s_system_proxy_post: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("Call %s api response: %s\n", API, response)

        # Remove Password fields from logged result
        del proxy_change_info["proxy_spec"]["pwd"]
        if self.esrs_password:
            del proxy_change_info["esrs_password"]
        LOGGER.info("Set proxy to: %s\n", proxy_change_info)
        return dict(proxy_change_info.items())


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        esrs_passwd=dict(type='str', no_log=True),
        server=dict(type='str', required=True),
        proxy_port=dict(type='int', required=True),
        proxy_user=dict(type='str', required=True),
        proxy_passwd=dict(type='str', required=True, no_log=True),
        type=dict(type='str', required=True),
        socks_version=dict(type='int'),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().post_proxy()
    if result == 'error':
        module.fail_json(
            msg=f"Call {API} API failed,please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts = {'System_Proxy_Set': result}
    vx_facts_result = dict(changed=True, System_Proxy_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
