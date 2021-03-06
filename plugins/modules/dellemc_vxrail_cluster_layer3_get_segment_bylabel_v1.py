#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_cluster_layer3_get_segment_bylabel_v1

short_description: Get segment by label of VxRail cluster layer3.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.3.0"

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
      dellemc_vxrail_cluster_layer3_get_segment_bylabel_v1:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        segment_label: "{{ segment_label }}"
'''

RETURN = r'''
Cluster_Layer3_Get_Segment_By_Label_Information:
  description: Get the segment configuration for a specified segment
  returned: always
  type: dict
  sample: >-
    {
        "management_gateway" : "172.19.1.167"
        "management_netmask" : "255.255.0.0"
        "management_vlan"    : 0
        "vsan_gateway"       : "172.19.1.167"
        "vsan_netmask"       : "255.255.0.0"
        "vsan_vlan"          : 0
        "vmotion_gateway"    : "172.19.1.167"
        "vmotion_netmask"    : "255.255.0.0"
        "vmotion_vlan"       : 0
        "segment_label"      : "V1SegmentTest1"
        "proxy_ip"           : "172.19.35.101"
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger(
    "dellemc_vxrail_cluster_layer3_get_segment_bylabel_v1", "/tmp/vxrail_ansible_layer3_get_segment_bylabel_v1.log", log_devel=logging.DEBUG)
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
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

    # dellemc_vxrail_cluster_layer3_get_segment_bylabel_v1
    def get_layer3_segment_by_label(self):
        response = ''
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.NetworkSegmentManagementApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query v1 layer3 cluster get segment bylabel information
            response = api_instance.v1_cluster_layer3_segment_label_get(self.segment_label)
        except ApiException as e:
            LOGGER.error(
                "Exception when calling NetworkSegmentManagementApi->v1_cluster_layer3_segment_label_get: %s\n", e)
            return 'error'
        LOGGER.info("v1/cluster/layer3/segment/{segment-label} information api response: %s\n", response)
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
        segment_info['vsan_netmask'] = data.vsan_netmask
        segment_info['vsan_vlan'] = data.vsan_vlan
        segment_info['vmotion_gateway'] = data.vmotion_gateway
        segment_info['vmotion_netmask'] = data.vmotion_netmask
        segment_info['vmotion_vlan'] = data.vmotion_vlan
        segment_info['segment_label'] = data.segment_label
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
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().get_layer3_segment_by_label()

    if result == 'error':
        module.fail_json(msg="API call failed, please refer /tmp/vxrail_ansible_layer3_get_segment_bylabel_v1.log")
    vx_facts = {'Cluster_Layer3_Get_Segment_Bylabel_Information': result}
    vx_facts_result = dict(changed=False, V1_Cluster_Layer3_Segment_Label_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
