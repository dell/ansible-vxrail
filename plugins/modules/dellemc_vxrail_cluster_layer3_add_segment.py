#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_cluster_layer3_add_segment

short_description: Add segment for VxRail cluster layer3.

description:
- This module will create a new segment.
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

  ip_version:
    description:
      The type of ip address
    required: True
    type: str

  management_gateway:
    description:
      The IPv4 gateway address of the management traffic for the segment
    required: False
    type: str

  management_netmask:
    description:
      The subnet mask of the management traffic for the segment
    required: False
    type: str

  management_gateway_ipv6:
    description:
      The IPv6 gateway address of the management traffic for the segment
    required: False
    type: str

  management_prefix_length_ipv6:
    description:
      The prefix length of the management traffic for the segment
    required: False
    type: int

  management_topology:
    description:
      The topology type for management traffic for the VxRail cluster
    required: True
    type: str

  management_vlan:
    description:
      The VLAN ID of the management traffic for the segment
    required: False
    type: int

  proxy_ip:
    description:
      The IP address of the node which provides proxy service
    required: True
    type: str

  segment_label:
    description:
      The name of the segment
    required: True
    type: str

  vmotion_gateway:
    description:
      The IPv4 gateway address of the vMotion traffic of the segment
    required: False
    type: str

  vmotion_init_gateway:
    description:
      The IPv4 gateway address of the vMotion traffic for the initial segment
    required: False
    type: str

  vmotion_netmask:
    description:
      The subnet mask for the vMotion traffic of the segment
    required: False
    type: str

  vmotion_gateway_ipv6:
    description:
      The IPv6 gateway address of the vMotion traffic of the segment
    required: False
    type: str

  vmotion_init_gateway_ipv6:
    description:
      The IPv6 gateway address of the vMotion traffic for the initial segment
    required: False
    type: str

  vmotion_prefix_length_ipv6:
    description:
      The prefix length for the vMotion traffic of the segment
    required: False
    type: int

  vmotion_topology:
    description:
      The topology type for the vMotion traffic for the VxRail cluster
    required: True
    type: str

  vmotion_vlan:
    description:
      The VLAN ID for the vMotion traffic of the segment
    required: false
    type: int

  vsan_gateway:
    description:
      The IPv4 gateway address of the vSAN traffic for the segment
    required: False
    type: str

  vsan_init_gateway:
    description:
      The IPv4 gateway address of the vSAN traffic for the initial segment
    required: False
    type: str

  vsan_netmask:
    description:
      The subnet mask for the vSAN traffic for the segment
    required: False
    type: str

  vsan_gateway_ipv6:
    description:
      The IPv6 gateway address of the vSAN traffic for the segment
    required: False
    type: str

  vsan_init_gateway_ipv6:
    description:
      The IPv6 gateway address of the vSAN traffic for the initial segment
    required: False
    type: str

  vsan_prefix_length_ipv6:
    description:
      The prefix length for the vSAN traffic for the segment
    required: False
    type: int

  vsan_topology:
    description:
      The topology type for the vSAN traffic for the VxRail cluster
    required: True
    type: str

  vsan_vlan:
    description:
      The VLAN ID for the vSAN traffic for the current segment
    required: false
    type: int

  version:
    description:
      Version number of VXM
    required: True
    type: str

  api_version_number:
    description:
      The version of API to call
    type: int

  timeout:
    description:
      Time out value for add lay3 segment infomation, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Add Cluster Layer3 Segment
    dellemc_vxrail_cluster_layer3_add_segment:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        ip_version: "{{ ip_version }}"
        management_gateway: "{{ management_gateway }}"
        management_netmask: "{{ management_netmask }}"
        management_gateway_ipv6: "{{ management_gateway_ipv6 }}"
        management_prefix_length_ipv6: "{{ management_prefix_length_ipv6 }}"
        management_topology: "{{ management_topology }}"
        management_vlan: "{{ management_vlan }}"
        proxy_ip: "{{ proxy_ip }}"
        segment_label: "{{ segment_label }}"
        vmotion_gateway: "{{ vmotion_gateway }}"
        vmotion_init_gateway: "{{ vmotion_init_gateway }}"
        vmotion_netmask: "{{ vmotion_netmask }}"
        vmotion_gateway_ipv6: "{{ vmotion_gateway_ipv6 }}"
        vmotion_init_gateway_ipv6: "{{ vmotion_init_gateway_ipv6 }}"
        vmotion_prefix_length_ipv6: "{{ vmotion_prefix_length_ipv6 }}"
        vmotion_topology: "{{ vmotion_topology }}"
        vmotion_vlan: "{{ vmotion_vlan }}"
        vsan_gateway: "{{ vsan_gateway }}"
        vsan_init_gateway: "{{ vsan_init_gateway }}"
        vsan_netmask: "{{ vsan_netmask }}"
        vsan_gateway_ipv6: "{{ vsan_gateway_ipv6 }}"
        vsan_init_gateway_ipv6: "{{ vsan_init_gateway_ipv6 }}"
        vsan_prefix_length_ipv6: "{{ vsan_prefix_length_ipv6 }}"
        vsan_topology: "{{ vsan_topology }}"
        vsan_vlan: "{{ vsan_vlan }}"
        version: "{{ version }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Cluster_Layer3_Add_Segment_Information:
  description: Create a new segment.
  returned: always
  type: dict
  sample: >-
    {
        "code": "10000002",
        "message": "Successfully to create a new segment."
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger(
    "dellemc_vxrail_cluster_layer3_add_segment", "/tmp/vxrail_ansible_layer3_add_segment.log",
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
        self.ip_version = module.params.get('ip_version').upper()
        self.management_gateway = module.params.get('management_gateway')
        self.management_gateway_ipv6 = module.params.get('management_gateway_ipv6')
        self.management_netmask = module.params.get('management_netmask')
        self.management_prefix_length_ipv6 = module.params.get('management_prefix_length_ipv6')
        self.management_topology = module.params.get('management_topology').upper()
        self.management_vlan = module.params.get('management_vlan')
        self.proxy_ip = module.params.get('proxy_ip')
        self.segment_label = module.params.get('segment_label')
        self.vmotion_gateway = module.params.get('vmotion_gateway')
        self.vmotion_gateway_ipv6 = module.params.get('vmotion_gateway_ipv6')
        self.vmotion_init_gateway = module.params.get('vmotion_init_gateway')
        self.vmotion_init_gateway_ipv6 = module.params.get('vmotion_init_gateway_ipv6')
        self.vmotion_netmask = module.params.get('vmotion_netmask')
        self.vmotion_prefix_length_ipv6 = module.params.get('vmotion_prefix_length_ipv6')
        self.vmotion_topology = module.params.get('vmotion_topology').upper()
        self.vmotion_vlan = module.params.get('vmotion_vlan')
        self.vsan_gateway = module.params.get('vsan_gateway')
        self.vsan_gateway_ipv6 = module.params.get('vsan_gateway_ipv6')
        self.vsan_init_gateway = module.params.get('vsan_init_gateway')
        self.vsan_init_gateway_ipv6 = module.params.get('vsan_init_gateway_ipv6')
        self.vsan_netmask = module.params.get('vsan_netmask')
        self.vsan_prefix_length_ipv6 = module.params.get('vsan_prefix_length_ipv6')
        self.vsan_topology = module.params.get('vsan_topology').upper()
        self.vsan_vlan = module.params.get('vsan_vlan')
        self.version = module.params.get('version')
        self.api_version_number = module.params.get('api_version_number')
        self.api_version_string = "v?"
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path, request_body):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number,
                                                                   module_path, LOGGER)
        call_string = self.api_version_string + '_cluster_layer3_segment_post'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_cluster_layer3_segment_post = getattr(api_instance, call_string)
        return api_cluster_layer3_segment_post(request_body)

    def create_segment_json(self):
        ''' Layer3 segment json '''
        segment_json = {}
        segment_json["segment"] = {}
        segment_json["segment"]["ip_version"] = self.ip_version
        segment_json["segment"]["management_gateway"] = self.management_gateway
        segment_json["segment"]["management_gateway_ipv6"] = self.management_gateway_ipv6
        segment_json["segment"]["management_netmask"] = self.management_netmask
        segment_json["segment"]["management_prefix_length_ipv6"] = self.management_prefix_length_ipv6
        segment_json["segment"]["management_topology"] = self.management_topology
        segment_json["segment"]["management_vlan"] = self.management_vlan
        segment_json["segment"]["proxy_ip"] = self.proxy_ip
        segment_json["segment"]["segment_label"] = self.segment_label
        segment_json["segment"]["vmotion_gateway"] = self.vmotion_gateway
        segment_json["segment"]["vmotion_gateway_ipv6"] = self.vmotion_gateway_ipv6
        segment_json["segment"]["vmotion_init_gateway"] = self.vmotion_init_gateway
        segment_json["segment"]["vmotion_init_gateway_ipv6"] = self.vmotion_init_gateway_ipv6
        segment_json["segment"]["vmotion_netmask"] = self.vmotion_netmask
        segment_json["segment"]["vmotion_prefix_length_ipv6"] = self.vmotion_prefix_length_ipv6
        segment_json["segment"]["vmotion_topology"] = self.vmotion_topology
        segment_json["segment"]["vmotion_vlan"] = self.vmotion_vlan
        segment_json["segment"]["vsan_gateway"] = self.vsan_gateway
        segment_json["segment"]["vsan_gateway_ipv6"] = self.vsan_gateway_ipv6
        segment_json["segment"]["vsan_init_gateway"] = self.vsan_init_gateway
        segment_json["segment"]["vsan_init_gateway_ipv6"] = self.vsan_init_gateway_ipv6
        segment_json["segment"]["vsan_netmask"] = self.vsan_netmask
        segment_json["segment"]["vsan_prefix_length_ipv6"] = self.vsan_prefix_length_ipv6
        segment_json["segment"]["vsan_topology"] = self.vsan_topology
        segment_json["segment"]["vsan_vlan"] = self.vsan_vlan
        segment_json["vcenter"] = {}
        segment_json["vcenter"]["password"] = self.vc_password
        segment_json["vcenter"]["username"] = self.vc_admin
        segment_json["version"] = self.version
        return segment_json

    # dellemc_vxrail_cluster_layer3_add_segment
    def add_layer3_segment(self):
        response = ''
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.NetworkSegmentManagementApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        request_body = self.create_segment_json()
        try:
            # post cluster lay3 segment
            response = self.get_versioned_response(api_instance, 'Post /cluster/layer3/segment', request_body)
        except ApiException as e:
            LOGGER.error(
                "Exception when calling NetworkSegmentManagementApi-> %s_cluster_layer3_segment_post: %s\n",
                self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/cluster/layer3/segment post api response: %s\n", self.api_version_string, response)
        data = response
        if not data:
            return "No new segment have been created"
        return self._generate_add_segment_info_from_response_data(data)

    def _generate_add_segment_info_from_response_data(self, data):
        add_segment_info_response = {}
        add_segment_info_response['code'] = data.code
        add_segment_info_response['message'] = data.message
        return add_segment_info_response


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        segment_label=dict(required=True),
        timeout=dict(type='int', default=60),
        ip_version=dict(required=True, choices=['IPV4', 'IPV6', 'DUALSTACK']),
        management_gateway=dict(required=False),
        management_gateway_ipv6=dict(required=False),
        management_netmask=dict(required=False),
        management_prefix_length_ipv6=dict(type='int', required=False),
        management_topology=dict(required=True, choices=['DIFF_SUBNET', 'SAME_SUBNET']),
        management_vlan=dict(type='int', default=0),
        proxy_ip=dict(required=True),
        vmotion_gateway=dict(required=False),
        vmotion_gateway_ipv6=dict(required=False),
        vmotion_init_gateway=dict(required=False),
        vmotion_init_gateway_ipv6=dict(required=False),
        vmotion_netmask=dict(required=False),
        vmotion_prefix_length_ipv6=dict(type='int', required=False),
        vmotion_topology=dict(required=True, choices=['DIFF_SUBNET', 'SAME_SUBNET']),
        vmotion_vlan=dict(type='int', default=0),
        vsan_gateway=dict(required=False),
        vsan_gateway_ipv6=dict(required=False),
        vsan_init_gateway=dict(required=False),
        vsan_init_gateway_ipv6=dict(required=False),
        vsan_netmask=dict(required=False),
        vsan_prefix_length_ipv6=dict(type='int', required=False),
        vsan_topology=dict(required=True, choices=['DIFF_SUBNET', 'SAME_SUBNET']),
        vsan_vlan=dict(type='int', default=0),
        version=dict(required=True),
        api_version_number=dict(required=False, type='int')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[
          ('management_topology', 'DIFF_SUBNET', ('management_gateway', 'management_gateway_ipv6'), True),
          ('vmotion_topology', 'DIFF_SUBNET', ('vmotion_gateway', 'vmotion_gateway_ipv6'), True),
          ('vsan_topology', 'DIFF_SUBNET', ('vsan_gateway', 'vsan_gateway_ipv6'), True),
        ]
    )
    result = VxRailCluster().add_layer3_segment()

    if result == 'error':
        module.fail_json(
            msg="API /cluster/layer3/segment post call failed, please refer /tmp/vxrail_ansible_layer3_add_segment.log")
    vx_facts = {'Cluster_Layer3_Add_Segment_Information': result}
    vx_facts_result = dict(changed=False, Cluster_Layer3_Add_Segment_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
