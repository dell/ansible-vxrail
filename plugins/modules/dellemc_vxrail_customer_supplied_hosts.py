#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_customer_supplied_hosts

short_description: Return nodes by customer supplied management IP

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.6.0"

description:
- This module will retrieve customer-supplied node information from given management IP addresses
options:

  vxmip:
    description:
      The IP address of the VxRail Manager System
    required: True
    type: str

  hosts:
    description:
      "The list of hosts to search for. Management_ip being the address of the node to collect and current_root_password
      (optional) being the node's esxi root password. Uses default esxi root password if omitted. Should be in the following format:
      \n
      [{
        'management_ip': 'xxx.xxx.xxx.xxx',
        'current_root_password': 'xxxxxxxx'
      },
      {
        'management_ip': 'xxx.xxx.xxx.xxx',
        'current_root_password': 'xxxxxxxx'
      }]
      \n"
    required: true
    type: list

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
  - name: Return nodes by customer supplied management IP
    dellemc_vxrail_customer_supplied_hosts:
        vxmip: "{{ vxmip }}"
        hosts: "{{ hosts }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''
RETURN = r'''
Customer_Supplied_Hosts_Information:
  description: Customer-supplied hosts information summary
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
            "esxi_version": "7.0.3-19899595",
            "vxm_system_version": "7.0.400-27589497",
            "evo_uuid": "564dec59-dbf0-a821-2a01-a7b704b9f677",
            "primary_ip": "fe80::250:56ff:fe62:5868%eth1",
            "fallback_ip": "",
            "idrac_ip": "192.168.104.14",
            "ip": "172.17.0.18",
            "asset_tag": "V010305-01-01",
            "serial_number": "V010305",
            "primary": false,
            "model": "VxRail P570F",
            "id": {
                "appliance_id": "V0103050000000",
                "position": 1,
                "total_supported_nodes": 1
            },
            "uuid": {
                "host": "d24d2042-1040-8581-b266-cf5f4438f3a4"
            },
            "ssl_thumbprint": "97:E0:26:FA:DC:2D:55:55:98:40:85:3A:2E:5C:9A:A4:52:95:4A:8D",
            "ssh_thumbprint": "fZftZF7CqDpaLUHB2VxvhTYOseEt59fcPK+28njwLOs",
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
                        "blocks": 335544320,
                        "block_size": 512
                    },
                    {
                        "ssd": true,
                        "blocks": 335544320,
                        "block_size": 512
                    },
                    {
                        "ssd": true,
                        "blocks": 3355443200,
                        "block_size": 512
                    },
                    {
                        "ssd": true,
                        "blocks": 3355443200,
                        "block_size": 512
                    }
                ],
                "cpu": {
                    "cores": 32,
                    "speed": 2095
                },
                "memory": {
                    "size": 196606
                }
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
import json

LOGGER = utils.get_logger(
    "dellemc_vxrail_customer_supplied_hosts", "/tmp/vxrail_ansible_customer_supplied_hosts.log", log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxRailHostUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxRailHostUrls.cluster_url.format(self.vxm_ip)


class VxRailHost():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.hosts_url = VxRailHostUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.verify_ssl = False
        self.configuration.host = self.hosts_url.set_host()
        self.hosts = module.params.get('hosts')
        self.api_version_number = module.params.get('api_version_number')
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path, customer_hosts_info):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method on string (ex: v1_system_initialize_customer_supplied_hosts_post)
        call_string = self.api_version_string + '_system_initialize_customer_supplied_hosts_post'
        LOGGER.info("Using utility method: %s\n", call_string)
        system_initialize_customer_supplied_hosts = getattr(api_instance, call_string)
        return system_initialize_customer_supplied_hosts(customer_hosts_info)

    def get_customer_hosts(self):
        customer_hosts_info = []
        for customer_host in self.hosts:
            customer_hosts_info.append(customer_host)
        LOGGER.info("Input Host Information: %s\n", customer_hosts_info)
        api_instance = vxrail_ansible_utility.VxRailInstallationApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # get all customer supplied hosts information
            response = self.get_versioned_response(api_instance, 'POST system/initialize/customer-supplied-hosts', customer_hosts_info)
        except ApiException as response:
            if len(json.loads(response.body)) > 1:
                for entry in json.loads(response.body):
                    if "error_code" not in entry:
                        LOGGER.info("Some Response Data Found: %s", response.body)
                        return json.loads(response.body)
                LOGGER.error("Exception when calling VxRailInstallationApi->%s_system_initialize_customer_supplied_hosts_post %s\n",
                             self.api_version_string, response)
                return 'error'
            else:
                LOGGER.error("Exception when calling VxRailInstallationApi->%s_system_initialize_customer_supplied_hosts_post %s\n",
                             self.api_version_string, response)
                return 'error'
        LOGGER.info("Initialize api response: %s\n", response)
        return self._generate_hosts_info(response)

    def _generate_hosts_info(self, response):
        nodes_data = []
        has_some_node_data = False
        if self.api_version_number == 1:
            nodes_data = map(lambda entry: entry.to_dict(), response)
        else:
            nodes_data = response.to_dict().get('nodes')

        nodes_info_list = []
        for entry in nodes_data:
            if entry.get("message") is not None:
                fail_message = {"message": entry.get("message")}
                nodes_info_list.append(fail_message)
            else:
                has_some_node_data = True
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
                        'storage_types': entry.get('storage_types')
                    }
                    if entry.get('disk_group_config') is not None:
                        individual_node_info['disk_group_config'] = entry.get('disk_group_config')
                    if entry.get('vlcm_software_spec') is not None:
                        individual_node_info['vlcm_software_spec'] = entry.get('vlcm_software_spec')
                nodes_info = {**nodes_info, **individual_node_info}
                nodes_info_list.append(nodes_info)
        if not has_some_node_data:
            LOGGER.error("No proper node data returned")
            LOGGER.error("Exception when calling VxRailInstallationApi->%s_system_initialize_customer_supplied_hosts_post %s\n",
                         self.api_version_string, response)
            return 'error'
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
        hosts=dict(required=True, type='list'),
        timeout=dict(type='int', default=60),
        api_version_number=dict(type='int')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailHost().get_customer_hosts()
    if result == 'error':
        module.fail_json(
            msg="Call Customer Supplied Hosts API failed,please see log file /tmp/vxrail_ansible_customer_supplied_hosts.log for more error details.")
    vx_facts = result
    vx_facts_result = dict(changed=False, Customer_Supplied_Hosts_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
