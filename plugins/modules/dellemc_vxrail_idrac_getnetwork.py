#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_idrac_getnetwork

short_description: Retrieve the iDRAC network settings on the specified host.

description:
  - "This module will retrieve iDRAC network settings on the specified host."
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

  sn:
    description:
      The serial number of the host to be queried
    required: True
    type: str

  timeout:
    description:
      Time out value for getting iDRAC network settings, the default value is 60 seconds
    required: false
    type: int
    default: 60

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: false
    type: int

author:
  - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>
'''

EXAMPLES = r'''
  - name: Get iDRAC Network Settings
    dellemc_vxrail_idrac_getnetworks:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        sn: "{{ sn }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
iDRAC_Network_Settings:
  description: iDRAC Network Settings summary
  returned: always
  type: dict
  sample: >-
    {
                "dhcp_enabled": true,
                "ip": {
                    "gateway": "192.168.105.252",
                    "ip_address": "192.168.105.16",
                    "netmask": "255.255.255.0",
                    "type": "ipv4"
                },
                "vlan": {
                    "vlan_id": 0,
                    "vlan_priority": 0
                }
            }

'''
import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils
LOG_FILE_NAME = "/tmp/vxrail_ansible_idrac_getnetwork.log"
LOGGER = utils.get_logger("dellemc_vxrail_idrac_getnetwork", LOG_FILE_NAME, log_devel=logging.DEBUG)
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
        self.sn = module.params.get('sn')
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
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        call_string = self.api_version_string + '_hosts_sn_idrac_network_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_system_get = getattr(api_instance, call_string)
        return api_system_get(self.sn)

    def get_idrac_network(self):
        # create an instance of the API class
        response = ''
        api_instance = vxrail_ansible_utility.HostIDRACConfigurationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query host idrac network information
            response = self.get_versioned_response(api_instance, "GET /hosts/{sn}/idrac/network")
        except ApiException as e:
            LOGGER.error("Exception when calling HostIDRACConfigurationApi->%s_hosts_sn_idrac_network_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/hosts/{sn}/idrac/network api response: %s\n", self.api_version_string, response)
        data = response
        # when API version v1 is called
        if self.api_version_number == 1:
            ip_list = data.ip
            vlan_list = data.vlan
            idracInfos = {
                'ip': {'type': ip_list.type,
                       'ip_address': ip_list.ip_address,
                       'netmask': ip_list.netmask,
                       'gateway': ip_list.gateway},
                'dhcp_enabled': data.dhcp_enabled,
                'vlan': {'vlan_id': vlan_list.vlan_id,
                         'vlan_priority': vlan_list.vlan_priority}}
        # When API version v2 is called
        if self.api_version_number == 2:
            ipv4_list = data.ipv4
            ipv6_list = data.ipv6
            vlan_list = data.vlan
            idracInfos = {
                'ipv4': {'ip_address': ipv4_list.ip_address,
                         'netmask': ipv4_list.netmask,
                         'gateway': ipv4_list.gateway,
                         'dhcp_enabled': ipv4_list.dhcp_enabled},
                'ipv6': {'ip_address': ipv6_list.ip_address,
                         'prefix_length': ipv6_list.prefix_length,
                         'gateway': ipv6_list.gateway,
                         'auto_config_enabled': ipv6_list.auto_config_enabled},
                'vlan': {'vlan_id': vlan_list.vlan_id,
                         'vlan_priority': vlan_list.vlan_priority}}
        return idracInfos


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
        api_version_number=dict(type='int'),
        sn=dict(required=True)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().get_idrac_network()
    if result == 'error':
        module.fail_json(msg="/hosts/{sn}/idrac/network api call failed, please see log file /tmp/vxrail_ansible_idrac_getnetwork.log for details.")
    vx_facts = {'iDRAC_Network_Settings': result}
    vx_facts_result = dict(changed=False, iDRAC_Network_Settings_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
