#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_auto_discovery_hosts

short_description: Get discovery hosts information

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.4.0"

description:
- This module will retrieve information about the auto discovery hosts.
options:

  vxmip:
    description:
      The IP address of the VxRail Manager System
    required: True
    type: str

  timeout:
    description:
      Time out value for getting hosts information, the default value is 60 seconds
    required: false
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
  - name: Retriwves VxRail Discovery Hosts Information
    dellemc_vxrail_auto_discovery_hosts:
        vxmip: "{{ vxmip }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''
RETURN = r'''
Auto_Discovery_Hosts_Information:
  description: hosts information summary
  returned: always
  type: dict
  sample: >-
    {
        "version": "2.0",
        "nodes": [
            {
                "esxi_version": "7.0.3-19580434",
                "vxm_system_version": "7.0.400-27513417",
                "evo_uuid": "564d86b7-aaf1-5d17-b278-675c97b94c7b",
                "primary_ip": "fe80::250:56ff:fe6b:78d6%eth1",
                "idrac_ip": "192.168.105.16",
                "idrac_ipv6": "::",
                "ip": "172.199.10.10",
                "ipv6": "",
                "asset_tag": "V010101-01-01",
                "serial_number": "V010101",
                "primary": true,
                "model": "VxRail E560",
                "id": {
                    "appliance_id": "V0101010000000",
                    "position": 1,
                    "total_supported_nodes": 1
                },
                "uuid": {
                    "host": "04152c42-397a-cf92-c3bc-8b71ec2be299"
                },
                "ssl_thumbprint": "04:50:0C.....<ommited>....1C:0A:3A:77",
                "ssh_thumbprint": "abdce.....<ommited>.....wxyz",
                "configuration_state": "UNCONFIGURED",
                "hardware_profile": {
                    "nics": [
                        {
                            "name": "vmnic0",
                            "speed": 10000,
                            "port_info": "Slot: 1, Port: 1",
                            "product_name": "Intel(R) Ethernet 10G 4P X550 rNDC"
                        },
                        {
                            "name": "vmnic1",
                            "speed": 10000,
                            "port_info": "Slot: 1, Port: 2",
                            "product_name": "Intel(R) Ethernet 10G 4P X550 rNDC"
                        },
                        {
                            "name": "vmnic2",
                            "speed": 10000,
                            "port_info": "Slot: 1, Port: 3",
                            "product_name": "Intel(R) Ethernet 10G 4P X550 rNDC"
                        },
                        {
                            "name": "vmnic3",
                            "speed": 10000,
                            "port_info": "Slot: 1, Port: 4",
                            "product_name": "Intel(R) Ethernet 10G 4P X550 rNDC"
                        }
                    ],
                    "disks": [
                        {
                            "ssd": true,
                            "blocks": 83886080,
                            "block_size": 512
                        },
                        {
                            "ssd": true,
                            "blocks": 83886080,
                            "block_size": 512
                        },
                        {
                            "ssd": false,
                            "blocks": 1258291200,
                            "block_size": 512
                        },
                        {
                            "ssd": false,
                            "blocks": 1258291200,
                            "block_size": 512
                        }
                    ],
                    "cpu": {
                        "cores": 16,
                        "speed": 2893
                    },
                    "memory": {
                        "size": 49150
                    }
                },
                "storage_types": [
                    "LOCAL"
                ]
            },
            {
                "esxi_version": "7.0.3-19580434",
                "vxm_system_version": "7.0.400-27513417",
                "evo_uuid": "564d8f3f-490e-d816-f39c-d35c8f68347b",
                "primary_ip": "fe80::250:56ff:fe6b:7218%eth1",
                "idrac_ip": "192.168.105.16",
                "idrac_ipv6": "::",
                "ip": "172.199.10.17",
                "ipv6": "",
                "asset_tag": "V010104-01-01",
                "serial_number": "V010104",
                "primary": false,
                "model": "VxRail E560",
                "id": {
                    "appliance_id": "V0101040000000",
                    "position": 1,
                    "total_supported_nodes": 1
                },
                "uuid": {
                    "host": "36b32c42-8555-f06e-b8a3-87a7c6d9e536"
                },
                "ssl_thumbprint": "04:50:0C.....<ommited>....1C:0A:3A:77",
                "ssh_thumbprint": "abdce.....<ommited>.....wxyz",
                "configuration_state": "UNCONFIGURED",
                "hardware_profile": {
                    "nics": [
                        {
                            "name": "vmnic0",
                            "speed": 10000,
                            "port_info": "Slot: 1, Port: 1",
                            "product_name": "Intel(R) Ethernet 10G 4P X550 rNDC"
                        },
                        {
                            "name": "vmnic1",
                            "speed": 10000,
                            "port_info": "Slot: 1, Port: 2",
                            "product_name": "Intel(R) Ethernet 10G 4P X550 rNDC"
                        },
                        {
                            "name": "vmnic2",
                            "speed": 10000,
                            "port_info": "Slot: 1, Port: 3",
                            "product_name": "Intel(R) Ethernet 10G 4P X550 rNDC"
                        },
                        {
                            "name": "vmnic3",
                            "speed": 10000,
                            "port_info": "Slot: 1, Port: 4",
                            "product_name": "Intel(R) Ethernet 10G 4P X550 rNDC"
                        }
                    ],
                    "disks": [
                        {
                            "ssd": true,
                            "blocks": 83886080,
                            "block_size": 512
                        },
                        {
                            "ssd": true,
                            "blocks": 83886080,
                            "block_size": 512
                        },
                        {
                            "ssd": false,
                            "blocks": 1258291200,
                            "block_size": 512
                        },
                        {
                            "ssd": false,
                            "blocks": 1258291200,
                            "block_size": 512
                        }
                    ],
                    "cpu": {
                        "cores": 16,
                        "speed": 2893
                    },
                    "memory": {
                        "size": 49150
                    }
                },
                "storage_types": [
                    "LOCAL"
                ]
            },
            {
                "esxi_version": "7.0.3-19580434",
                "vxm_system_version": "7.0.400-27513417",
                "evo_uuid": "564d41b3-7361-072f-05b2-bb5d0c5c57cd",
                "primary_ip": "fe80::250:56ff:fe68:656%eth1",
                "idrac_ip": "192.168.105.16",
                "idrac_ipv6": "::",
                "ip": "172.199.10.13",
                "ipv6": "",
                "asset_tag": "V010103-01-01",
                "serial_number": "V010103",
                "primary": false,
                "model": "VxRail E560",
                "id": {
                    "appliance_id": "V0101030000000",
                    "position": 1,
                    "total_supported_nodes": 1
                },
                "uuid": {
                    "host": "aa482c42-2f77-c793-4a36-644c80042d29"
                },
                "ssl_thumbprint": "04:50:0C.....<ommited>....1C:0A:3A:77",
                "ssh_thumbprint": "abdce.....<ommited>.....wxyz",
                "configuration_state": "UNCONFIGURED",
                "hardware_profile": {
                    "nics": [
                        {
                            "name": "vmnic0",
                            "speed": 10000,
                            "port_info": "Slot: 1, Port: 1",
                            "product_name": "Intel(R) Ethernet 10G 4P X550 rNDC"
                        },
                        {
                            "name": "vmnic1",
                            "speed": 10000,
                            "port_info": "Slot: 1, Port: 2",
                            "product_name": "Intel(R) Ethernet 10G 4P X550 rNDC"
                        },
                        {
                            "name": "vmnic2",
                            "speed": 10000,
                            "port_info": "Slot: 1, Port: 3",
                            "product_name": "Intel(R) Ethernet 10G 4P X550 rNDC"
                        },
                        {
                            "name": "vmnic3",
                            "speed": 10000,
                            "port_info": "Slot: 1, Port: 4",
                            "product_name": "Intel(R) Ethernet 10G 4P X550 rNDC"
                        }
                    ],
                    "disks": [
                        {
                            "ssd": true,
                            "blocks": 83886080,
                            "block_size": 512
                        },
                        {
                            "ssd": true,
                            "blocks": 83886080,
                            "block_size": 512
                        },
                        {
                            "ssd": false,
                            "blocks": 1258291200,
                            "block_size": 512
                        },
                        {
                            "ssd": false,
                            "blocks": 1258291200,
                            "block_size": 512
                        }
                    ],
                    "cpu": {
                        "cores": 16,
                        "speed": 2893
                    },
                    "memory": {
                        "size": 49150
                    }
                },
                "storage_types": [
                    "LOCAL"
                ]
            }
        ]
    }
'''

from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils
from vxrail_ansible_utility.rest import ApiException
import vxrail_ansible_utility
from ansible.module_utils.basic import AnsibleModule
import urllib3
import logging

LOGGER = utils.get_logger(
    "dellemc_vxrail_auto_discovery_hosts", "/tmp/vxrail_ansible_auto_discovery_hosts.log", log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxRailAutoDiscoveryHostsUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxRailAutoDiscoveryHostsUrls.cluster_url.format(self.vxm_ip)


class VxRailAutoDiscoveryHosts():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.hosts_url = VxRailAutoDiscoveryHostsUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.verify_ssl = False
        self.configuration.host = self.hosts_url.set_host()
        self.api_version_number = module.params.get('api_version_number')

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        call_string = self.api_version_string + '_system_initialize_nodes_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_auto_discovery_hosts_get = getattr(api_instance, call_string)
        return api_auto_discovery_hosts_get()

    def get_auto_discovery(self):
        api_instance = vxrail_ansible_utility.VxRailInstallationApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # get all auto discovery  hosts information
            response = self.get_versioned_response(api_instance, 'GET /system/initialize/nodes')
        except ApiException as response:
            LOGGER.error("Exception when calling VxRailInstallationApi->%s_system_initialize_nodes_get %s\n", self.api_version_string, response)
            return 'error'
        LOGGER.info("initialize api response: %s\n", response)
        return self._generate_hosts_info(response)

    def _generate_hosts_info(self, response):
        nodes_data = []
        if self.api_version_number == 1:
            nodes_data = map(lambda entry: entry.to_dict(), response)
        else:
            nodes_data = response.to_dict().get('nodes')

        nodes_info_list = []
        for entry in nodes_data:
            nodes_info = {'esxi_version': entry.get('esxi_version'),
                          'vxm_system_version': entry.get('vxm_system_version'), 'evo_uuid': entry.get('evo_uuid'),
                          'primary_ip': entry.get('primary_ip'), 'idrac_ip': entry.get('idrac_ip'),
                          'ip': entry.get('ip'), 'asset_tag': entry.get('asset_tag'),
                          'serial_number': entry.get('serial_number'), 'primary': entry.get('primary'),
                          'model': entry.get('model'), 'id': entry.get('id'),
                          'uuid': entry.get('uuid'), 'ssl_thumbprint': entry.get('ssl_thumbprint'),
                          'ssh_thumbprint': entry.get('ssh_thumbprint'),
                          'configuration_state': entry.get('configuration_state'),
                          'hardware_profile': entry.get('hardware_profile')}
            if entry.get('violations') is not None:
                nodes_info['violations'] = entry.get('violations')
            individual_node_info = {}
            if self.api_version_number == 1:
                individual_node_info = {
                    'fallback_ip': entry.get('fallback_ip'),
                    'prerecoded_ip': entry.get('prerecoded_ip'),
                    'cluster_affinity': entry.get('cluster_affinity'),
                    'discovered_date': entry.get('discovered_date'),
                    'ip_set': entry.get('ip_set'),
                    'node_version_info': entry.get('node_version_info')
                }
            else:
                individual_node_info = {
                    'idrac_ipv6': entry.get('idrac_ipv6'),
                    'ipv6': entry.get('ipv6'),
                    'storage_types': entry.get('storage_types'),
                }
                if entry.get('disk_group_config') is not None:
                    individual_node_info['disk_group_config'] = entry.get('disk_group_config')
            nodes_info = {**nodes_info, **individual_node_info}
            nodes_info_list.append(nodes_info)

        if self.api_version_number == 1:
            return nodes_info_list
        else:
            return {'version': response.to_dict().get('version'), 'nodes': nodes_info_list}


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        timeout=dict(type='int', default=60),
        api_version_number=dict(type='int')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailAutoDiscoveryHosts().get_auto_discovery()
    if result == 'error':
        module.fail_json(
            msg="Call Auto Discovery Hosts API failed,please see log file /tmp/vxrail_ansible_auto_discovery_hosts.log for more error details.")
    vx_facts = result
    vx_facts_result = dict(changed=False, Auto_Discovery_Hosts_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
