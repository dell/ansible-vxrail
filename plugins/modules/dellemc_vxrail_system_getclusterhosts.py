#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_getclusterhosts

short_description: Get information about configured hosts.

description:
- This module will get information about configured hosts in the VxRail cluster.
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
      Time out value for getting system infomation, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Retrives All VxRail Hosts Information
    dellemc_vxrail_system_getclusterhosts:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Hosts_Information:
  description: host information summary
  returned: always
  type: dict
  sample: >-
        {
                "health": "Error",
                "id": "9RVKNX20000000-01-01",
                "ip_set": {
                        "management_ip": "20.13.143.103",
                        "vmotion_ip": "192.168.102.143",
                        "vsan_ip": "192.168.101.123"
                },
                "ip_set_ipv6": {
                        "management_ip": "",
                        "vmotion_ip": "",
                        "vsan_ip": ""
                },
                "led_status": "Blue:On",
                "manufacturer": "Dell Inc.",
                "missing": false,
                "operational_status": "normal",
                "power_status": "on",
                "psnt": "9RVKNX20000000",
                "slot": 1,
                "tpm_present": true,
                "appliance_id": "VXRAILVIP470F2",
                "is_primary_node": true,
                "discovered_date": "1533460206",
                "cluster_affinity": true,
                "bios_uuid": "420e8b96-4602-9d96-35b9-906808c40985",
                "segment_label": null
        }
'''
from functools import reduce
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils
from vxrail_ansible_utility.rest import ApiException
import vxrail_ansible_utility
from ansible.module_utils.basic import AnsibleModule
import urllib3
import logging

LOGGER = utils.get_logger(
    "dellemc_vxrail_system_getclusterhosts", "/tmp/vxrail_ansible_system_getclusterhosts.log", log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxRailHostsUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxRailHostsUrls.cluster_url.format(self.vxm_ip)


class VxRailHosts():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.api_version_number = module.params.get('api_version_number')
        self.hosts_url = VxRailHostsUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.hosts_url.set_host()
        # Added for auto-version detection
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute (ex: v1_system_cluster_hosts_get)
        call_string = self.api_version_string + '_system_cluster_hosts_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_system_cluster_hosts_get = getattr(api_instance, call_string)
        return api_system_cluster_hosts_get()

    def get_system_cluster_hosts(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemInformationApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # get all cluster hosts information
            response = self.get_versioned_response(api_instance, "GET /system/cluster-hosts")
        except ApiException as e:
            LOGGER.error(
                "Exception when calling SystemInformationApi->%s_system_cluster_hosts_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("Call %s/system/cluster-hosts api response: %s\n", self.api_version_string, response)
        datalist = response
        if not datalist:
            return "No available hosts"
        return self._get_info_list(self._generate_host_info_from_response_data, datalist)

    def _get_info_list(self, generate_func, data_list):
        return reduce(lambda infos, data: infos + [generate_func(data)], data_list, [])

    def _generate_host_info_from_response_data(self, data):
        host_info = {}
        host_info['id'] = data.id
        host_info['serial_number'] = data.serial_number
        host_info['slot'] = data.slot
        host_info['host_name'] = data.host_name
        host_info['appliance_id'] = data.appliance_id
        host_info['manufacturer'] = data.manufacturer
        host_info['model'] = data.model
        host_info['psnt'] = data.psnt
        host_info['led_status'] = data.led_status
        host_info['health'] = data.health
        host_info['missing'] = data.missing
        host_info['tpm_present'] = data.tpm_present
        host_info['operational_status'] = data.operational_status
        host_info['power_status'] = data.power_status
        host_info['is_primary_node'] = data.is_primary_node
        host_info['cluster_affinity'] = data.cluster_affinity
        host_info['discovered_date'] = data.discovered_date
        host_info['bios_uuid'] = data.bios_uuid
        host_info['segment_label'] = data.segment_label
        if data.ip_set is not None:
            host_info['ip_set'] = self._generate_ip_set_info_from_response_data(
                data.ip_set)
        if self.api_version_number >= 2:
            if data.ip_set_ipv6 is not None:
                host_info['ip_set_ipv6'] = self._generate_ip_set_ipv6_from_response_data(
                    data.ip_set_ipv6)
        return host_info

    def _generate_ip_set_info_from_response_data(self, data):
        ip_set_info = {}
        ip_set_info['management_ip'] = data.management_ip
        ip_set_info['vsan_ip'] = data.vsan_ip
        ip_set_info['vmotion_ip'] = data.vmotion_ip
        return ip_set_info

    def _generate_ip_set_ipv6_from_response_data(self, data):
        ip_set_ipv6_info = {}
        ip_set_ipv6_info['management_ip'] = data.management_ip
        ip_set_ipv6_info['vsan_ip'] = data.vsan_ip
        ip_set_ipv6_info['vmotion_ip'] = data.vmotion_ip
        return ip_set_ipv6_info


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
    result = VxRailHosts().get_system_cluster_hosts()
    if result == 'error':
        module.fail_json(
            msg="Call /system/cluster-hostsHosts API failed,please see log file /tmp/vxrail_ansible_system_getclusterhosts.log for more error details.")
    vx_facts = {"Hosts_Information": result}
    vx_facts_result = dict(changed=False, System_CLuster_Hosts_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
