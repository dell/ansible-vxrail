#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_idrac_updatenetwork

short_description: Update the iDRAC network settings on the specified host.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.5.0"

description:
- This module will update the iDRAC network settings on the specified host.
options:

  vxmip:
    description:
      The IP address of the VxRail Manager System.
    required: True
    type: str

  vcadmin:
    description:
      Administrative account of the vCenter Server the VxRail Manager is registered to.
    required: True
    type: str

  vcpasswd:
    description:
      The password for the administrator account provided in vcadmin.
    required: True
    type: str

  sn:
    description:
      The serial number of the host to be queried.
    required: true
    type: string

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default.
    required: false
    type: int

  ip_address:
    description:
      The MAC address of the iDRAC.
    required: true
    type: string

  netmask:
    description:
      The netmask of the iDRAC.
    required: true
    type: string

  gateway:
    description:
      The gateway address of the iDRAC.
    required: true
    type: string

  dhcp_enabled:
    description:
      Whether DHCP service enabled or not.
    required: false
    type: boolean

  ipv6_address:
    description:
      The IPv6 address of the iDRAC.
    required: true
    type: string

  ipv6_prefix_length:
    description:
      The prefix length of the iDRAC IPv6 address.
    required: true
    type: string

  ipv6_gateway:
    description:
      The gateway address of the iDRAC IPv6 address.
    required: true
    type: string

  ipv6_auto_config_enabled:
    description:
      Whether enable auto config iDRAC IPv6 address or not.
    required: false
    type: boolean

  vlan_id:
    description:
      The VLAN ID setting of the iDRAC. Set 0 to disable.
    required: true
    type: int

  vlan_priority:
    description:
      The VLAN priority setting of the iDRAC. The default value is 0.
    required: false
    type: int
    default: 0

  timeout:
    description:
      Time out value for getting request id, the default value is 300 seconds.
    required: false
    type: int
    default: 300

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Update iDRAC network settings
    dellemc_vxrail_idrac_updatenetwork:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        ip_address: "{{ ip_address }}"
        netmask: "{{ netmask }}"
        gateway: "{{ gateway }}"
        dhcp_enabled: "{{ dhcp_enabled }}"
        ipv6_address: "{{ ipv6_address }}"
        ipv6_prefix_length: "{{ ipv6_prefix_length }}"
        ipv6_gateway: "{{ ipv6_gateway }}"
        ipv6_auto_config_enabled: "{{ ipv6_auto_config_enabled }}"
        vlan_id: "{{ vlan_id }}"
        vlan_priority: "{{ vlan_priority }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Update_iDRAC_Network_Settings:
  description: Update the iDRAC network settings on the specified host
  returned: always
  type: dict
  sample: >-
    {
            "Request_ID": "SBI_17",
            "Request_Status": "COMPLETED"
        }

'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

# Defining global variables
API = "/hosts/{sn}/idrac/network"
MODULE = "dellemc_vxrail_idrac_updatenetwork"
LOG_FILE_PATH = "/tmp/vxrail_ansible_idrac_updatenetwork.log"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
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
        self.type = "ipv4"
        self.ip_address = module.params.get('ip_address')
        self.netmask = module.params.get('netmask')
        self.gateway = module.params.get('gateway')
        self.dhcp_enabled = module.params.get('dhcp_enabled')
        self.ipv6_address = module.params.get('ipv6_address')
        self.ipv6_prefix_length = module.params.get('ipv6_prefix_length')
        self.ipv6_gateway = module.params.get('ipv6_gateway')
        self.ipv6_auto_config_enabled = module.params.get('ipv6_auto_config_enabled')
        self.vlan_id = module.params.get('vlan_id')
        self.vlan_priority = module.params.get('vlan_priority')
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

        # Calls versioned method as attribute (ex: v2_hosts_sn_idrac_network_patch)
        call_string = self.api_version_string + "_hosts_sn_idrac_network_patch"
        LOGGER.info("Using utility method: %s\n", call_string)
        update_idrac_network = getattr(api_instance, call_string)
        '''idrac network json'''
        idrac_network_json = {}
        # when API version v1 is used
        if self.api_version_number == 1:
            idrac_network_json = {
                "ip": {
                    "type": self.type,
                    "ip_address": self.ip_address,
                    "netmask": self.netmask,
                    "gateway": self.gateway
                },
                "dhcp_enabled": self.dhcp_enabled,
                "vlan": {
                    "vlan_id": self.vlan_id,
                    "vlan_priority": self.vlan_priority
                }
            }
        # when API version v2 is used
        if self.api_version_number == 2:
            idrac_network_json = {
                "vlan": {
                    "vlan_id": self.vlan_id,
                    "vlan_priority": self.vlan_priority
                }
            }
            idrac_network_ipv4_info = {}
            idrac_network_ipv6_info = {}
            if self.ip_address:
                idrac_network_ipv4_info["ip_address"] = self.ip_address
                idrac_network_ipv4_info["netmask"] = self.netmask
                idrac_network_ipv4_info["gateway"] = self.gateway
                idrac_network_ipv4_info["dhcp_enabled"] = self.dhcp_enabled
            if self.ipv6_address:
                idrac_network_ipv6_info["ip_address"] = self.ipv6_address
                idrac_network_ipv6_info["ipv6_prefix_length"] = self.ipv6_prefix_length
                idrac_network_ipv6_info["gateway"] = self.ipv6_gateway
                idrac_network_ipv6_info["auto_config_enabled"] = self.ipv6_auto_config_enabled
            if len(idrac_network_ipv4_info) > 0:
                idrac_network_json["ipv4"] = idrac_network_ipv4_info
            if len(idrac_network_ipv6_info) > 0:
                idrac_network_json["ipv6"] = idrac_network_ipv6_info

        LOGGER.info("idrac_network_json: %s\n", idrac_network_json)
        return update_idrac_network(body=idrac_network_json, sn=self.sn)

    def update_network(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.HostIDRACConfigurationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # Update iDRAC network settings
            response = self.get_versioned_response(api_instance, "PATCH /hosts/{sn}/idrac/network")
        except ApiException as e:
            LOGGER.error("Exception when calling HostIDRACConfigurationApi->%s_hosts_sn_idrac_network_patch: %s\n", self.api_version_string,
                         e)
            return 'error'
        LOGGER.info("%s/hosts/{sn}/idrac/network api response: %s\n", self.api_version_string, response)
        requestid = response.request_id
        return requestid


def main():
    ''' Entry point into execution flow '''
    result_request_id = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        sn=dict(required=True),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=1800),
        ip_address=dict(required=False),
        netmask=dict(required=False),
        gateway=dict(required=False),
        dhcp_enabled=dict(type='bool'),
        ipv6_address=dict(required=False),
        ipv6_prefix_length=dict(required=False, type='int'),
        ipv6_gateway=dict(required=False),
        ipv6_auto_config_enabled=dict(type='bool'),
        vlan_id=dict(required=True, type='int'),
        vlan_priority=dict(type='int', default=0)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_together=[
            ('ip_address', 'netmask', 'gateway', 'dhcp_enabled'),
            ('ipv6_address', 'ipv6_prefix_length', 'ipv6_gateway', 'ipv6_auto_config_enabled')
        ],
    )

    result_request_id = VxRailCluster().update_network()
    if result_request_id == 'error':
        module.fail_json(msg="Call /hosts/{sn}/idrac/network API failed,please see log file /tmp/vxrail_ansible_idrac_updatenetwork.log "
                             "for more error details.")

    LOGGER.info('iDRAC update network request_id: %s.', result_request_id)
    vxmip = module.params.get('vxmip')
    vcadmin = module.params.get('vcadmin')
    vcpasswd = module.params.get('vcpasswd')
    task_state = 0
    time_out = 0
    initial_timeout = module.params.get('timeout')
    LOGGER.info('Timeout setting: %s seconds.', initial_timeout)
    while task_state not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        result_response = utils.get_request_status(vxm_ip=vxmip, vcadmin=vcadmin, vcpasswd=vcpasswd, logger=LOGGER, request_id=result_request_id)
        task_state = result_response.state
        LOGGER.info('Request_status: %s', task_state)
        ''' call frequently to capture 'COMPLETED' status'''
        time_out = time_out + 30
        time.sleep(30)
    error_message = result_response.error
    if task_state == 'COMPLETED' and not error_message:
        vx_facts = {'Request_ID': result_request_id, 'Request_Status': task_state}
        LOGGER.info("iDRAC network settings updated")
        vx_facts_result = dict(changed=True, Update_iDRAC_Network_Settings=vx_facts, msg="iDRAC network settings updated. Please see the logs "
                                                                                         "at /tmp/vxrail_ansible_idrac_updatenetwork.log for more details")
    else:
        LOGGER.info("Failed to update iDRAC network settings")
        vx_facts = {'Request_ID': result_request_id}
        vx_facts_result = dict(failed=True, Update_iDRAC_Network_Settings=vx_facts, msg="Failed to update iDRAC network settings. Please see "
                                                                                        "the /tmp/vxrail_ansible_idrac_updatenetwork.log for more details")
    LOGGER.info('Request_info: %s', result_response)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
