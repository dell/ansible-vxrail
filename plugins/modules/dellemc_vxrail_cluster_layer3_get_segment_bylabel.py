#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_cluster_layer3_get_segment_bylabel

short_description: Get segment by label of VxRail cluster layer3.

description:
- This module will get cluster layer3 segment information by label.
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

  segment_label:
    description:
      The label of the current segment to be acted upon
    required: True
    type: str

  api_version_number:
    description:
      The version of API to call
    type: int

  timeout:
    description:
      Time out value for getting lay3 segment infomation, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
    - name: Get Cluster Layer3 Segment By Label
      dellemc_vxrail_cluster_layer3_get_segment_bylabel:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        segment_label: "{{ segment_label }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Cluster_Layer3_Get_Segment_By_Label_Information:
  description: Get the segment configuration for a specified segment
  returned: always
  type: dict
  sample: >-
    {
        "management_gateway"            : "172.19.1.167"
        "management_netmask"            : "255.255.0.0"
        "management_gateway_ipv6"       : "fc00::20:17:1:167"
        "management_prefix_length_ipv6" : 96
        "management_vlan"               : 0
        "vsan_gateway"                  : "172.19.1.167"
        "vsan_init_gateway"             : "172.18.1.16"
        "vsan_netmask"                  : "255.255.0.0"
        "vsan_gateway_ipv6"             : "fc00::20:17:1:167"
        "vsan_init_gateway_ipv6"        : "fc00::20:18:1:167"
        "vsan_prefix_length_ipv6"       : 96
        "vsan_vlan"                     : 0
        "vmotion_gateway"               : "172.19.1.167"
        "vmotion_init_gateway"          : "172.18.1.167"
        "vmotion_netmask"               : "255.255.0.0"
        "vmotion_gateway_ipv6"          : "fc00::20:17:1:167"
        "vmotion_init_gateway_ipv6"     : "fc00::20:18:1:167"
        "vmotion_prefix_length_ipv6"    : 96
        "vmotion_vlan"                  : 0
        "segment_label"                 : "V1SegmentTest1"
        "proxy_ip"                      : "172.19.35.101"
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger(
    "dellemc_vxrail_cluster_layer3_get_segment_bylabel", "/tmp/vxrail_ansible_layer3_get_segment_bylabel.log",
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
        self.segment_label = module.params.get('segment_label')
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
    def get_versioned_response(self, api_instance, module_path, segment_label):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number,
                                                                   module_path, LOGGER)
        call_string = self.api_version_string + '_cluster_layer3_segment_label_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_cluster_layer3_segment_label_get = getattr(api_instance, call_string)
        return api_cluster_layer3_segment_label_get(segment_label)

    # dellemc_vxrail_cluster_layer3_get_segment_bylabel
    def get_layer3_segment_by_label(self):
        response = ''
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.NetworkSegmentManagementApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # get segment information bylabel
            response = self.get_versioned_response(api_instance, 'Get /cluster/layer3/segment/{segment-label}', self.segment_label)
        except ApiException as e:
            LOGGER.error(
                "Exception when calling NetworkSegmentManagementApi->%s_cluster_layer3_segment_label_get: %s\n",
                self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/cluster/layer3/segment/{segment_label} information api response: %s\n", self.api_version_string,
                    response)
        data = response
        if not data:
            return "No segment data in the cluster"
        return self._generate_get_segment_bylabel_from_response_data(data)

    def _generate_get_segment_bylabel_from_response_data(self, data):
        segment_info = {}
        segment_info['management_gateway'] = data.management_gateway
        segment_info['management_netmask'] = data.management_netmask
        segment_info['management_vlan'] = data.management_vlan
        segment_info['vsan_gateway'] = data.vsan_gateway
        segment_info['vsan_init_gateway'] = data.vsan_init_gateway
        segment_info['vsan_netmask'] = data.vsan_netmask
        segment_info['vsan_vlan'] = data.vsan_vlan
        segment_info['vmotion_gateway'] = data.vmotion_gateway
        segment_info['vmotion_init_gateway'] = data.vmotion_init_gateway
        segment_info['vmotion_netmask'] = data.vmotion_netmask
        segment_info['vmotion_vlan'] = data.vmotion_vlan
        segment_info['segment_label'] = data.segment_label
        if self.api_version_number > 1:
            segment_info['management_gateway_ipv6'] = data.management_gateway_ipv6
            segment_info['management_prefix_length_ipv6'] = data.management_prefix_length_ipv6
            segment_info['vsan_gateway_ipv6'] = data.vsan_gateway_ipv6
            segment_info['vsan_init_gateway_ipv6'] = data.vsan_init_gateway_ipv6
            segment_info['vsan_prefix_length_ipv6'] = data.vsan_prefix_length_ipv6
            segment_info['vmotion_gateway_ipv6'] = data.vmotion_gateway_ipv6
            segment_info['vmotion_init_gateway_ipv6'] = data.vmotion_init_gateway_ipv6
            segment_info['vmotion_prefix_length_ipv6'] = data.vmotion_prefix_length_ipv6
        return segment_info


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
        api_version_number=dict(required=False, type='int')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().get_layer3_segment_by_label()

    if result == 'error':
        module.fail_json(
            msg="API /cluster/layer3/segment/{segment_label} get call failed, please refer /tmp/vxrail_ansible_layer3_get_segment_bylabel.log")
    vx_facts = {'Cluster_Layer3_Get_Segment_Bylabel_Information': result}
    vx_facts_result = dict(changed=False, Cluster_Layer3_Segment_Label_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
