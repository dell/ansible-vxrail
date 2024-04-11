#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_cluster_layer3_update_segment_label

short_description: Update segment label for VxRail cluster layer3.

description:
- This module will change the segment label for the current segment
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
      The name of the segment
    required: True
    type: str

  new_segment_label:
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
      Time out value for change the segment label infomation, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Update Cluster Layer3 Segment Label
    dellemc_vxrail_cluster_layer3_update_segment_label:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        segment_label: "{{ segment_label }}"
        new_segment_label: "{{ new_segment_label }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Cluster_Layer3_Update_Segment_Label_Information:
  description: Change the segment label for the current segment
  returned: always
  type: dict
  sample: >-
    {
        "code": '10000003'
        "message": "Successfully changed the label of the rack."
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger(
    "dellemc_vxrail_cluster_layer3_update_segment_label", "/tmp/vxrail_ansible_layer3_update_segment_label.log",
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
        self.new_segment_label = module.params.get('new_segment_label')
        self.new_segment_label_body = {'segment_label': self.new_segment_label}
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
    def get_versioned_response(self, api_instance, module_path, new_segment_label_body, segment_label):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number,
                                                                   module_path, LOGGER)
        call_string = self.api_version_string + '_cluster_layer3_segment_label_patch'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_cluster_layer3_segment_label_patch = getattr(api_instance, call_string)
        return api_cluster_layer3_segment_label_patch(new_segment_label_body, segment_label)

    # dellemc_vxrail_cluster_layer3_update_segment_label
    def update_layer3_segment_label(self):
        response = ''
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.NetworkSegmentManagementApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # patch cluster layer3 segment label
            response = self.get_versioned_response(api_instance, 'Patch /cluster/layer3/segment/{segment-label}', self.new_segment_label_body,
                                                   self.segment_label)
        except ApiException as e:
            LOGGER.error(
                "Exception when calling NetworkSegmentManagementApi->%s_cluster_layer3_segment_label_patch: %s\n",
                self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/cluster/layer3/segment/{segment_label} patch information api response: %s\n",
                    self.api_version_string, response)
        data = response
        if not data:
            return "No segment label to been changed"
        return self._generate_update_segment_label_info_from_response_data(data)

    def _generate_update_segment_label_info_from_response_data(self, data):
        update_segment_label_info_response = {}
        update_segment_label_info_response['code'] = data.code
        update_segment_label_info_response['message'] = data.message
        return update_segment_label_info_response


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
        new_segment_label=dict(required=True),
        timeout=dict(type='int', default=60),
        api_version_number=dict(required=False, type='int')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().update_layer3_segment_label()

    if result == 'error':
        module.fail_json(
            msg="API /cluster/layer3/segment/{segment_label} patch call failed, please refer /tmp/vxrail_ansible_layer3_update_segment_label.log")
    vx_facts = {'Cluster_Layer3_Update_Segment_Label_Information': result}
    vx_facts_result = dict(changed=False, NetworkSegmentManagement_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
