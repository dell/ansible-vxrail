#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_getclusterinfo

short_description: Retrieve VxRail Cluster Information

description:
- This module will retrieve VxRail cluster information and basic applicance information list.
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
      Time out value for getting cluster infomation, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Retrieves VxRail Cluster Information
    dellemc-vxrail-getclusterinfo:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Cluster_Information:
  description: cluster information summary
  returned: always
  type: dict
  sample: >-
    {
        "chassises": [
                        {
                            "generation": 3,
                            "health": "Healthy",
                            "id": "V0109010000000",
                            "missing": false,
                            "model": "VxRail E560",
                            "psnt": "V0109010000000",
                            "render_category": "DELL_R640"
                        },
                        {
                            "generation": 3,
                            "health": "Healthy",
                            "id": "V0109020000000",
                            "missing": false,
                            "model": "VxRail E560",
                            "psnt": "V0109020000000",
                            "render_category": "DELL_R640"
                        },
                        {
                            "generation": 3,
                            "health": "Healthy",
                            "id": "V0109030000000",
                            "missing": false,
                            "model": "VxRail E560",
                            "psnt": "V0109030000000",
                            "render_category": "DELL_R640"
                        },
                        {
                            "generation": 3,
                            "health": "Healthy",
                            "id": "V0109040000000",
                            "missing": false,
                            "model": "VxRail E560",
                            "psnt": "V0109040000000",
                            "render_category": "DELL_R640"
                        }
        ],
        "cluster_id": "522181ca-44e0-0533-c291-b46ef7d83dc1",
        "device_type": "VSPEXBLUE",
        "health": "Healthy",
        "last_time": "2021-09-03T14:07:17.968000+00:00",
        "operational_status": "ok",
        "product_type": "VSPEXPLUS",
        "suppressed": false,
        "vc_connected": true

    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_getclusterinfo", "/tmp/vxrail_ansible_getclusterinfo.log", log_devel=logging.DEBUG)
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

        call_string = self.api_version_string + '_cluster_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_cluster_get = getattr(api_instance, call_string)
        return api_cluster_get()

    def get_cluster(self):
        clusterInfos = {}
        clusterInfolist = []
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.ClusterInformationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query cluster information
            response = self.get_versioned_response(api_instance, "GET /cluster")
        except ApiException as e:
            LOGGER.error("Exception when calling ClusterInformationApi->%s_cluster_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("/cluster api response: %s\n", response)
        data = response
        clusterInfos['cluster_id'] = data.cluster_id
        clusterInfos['product_type'] = data.product_type
        clusterInfos['device_type'] = data.device_type
        clusterInfos['vc_connected'] = data.vc_connected
        clusterInfos['health'] = data.health
        clusterInfos['operational_status'] = data.operational_status
        if self.api_version_number == 1:
            if data.chassises is not None:
                clusterInfos['chassises'] = VxRailCluster().get_chassis_basic_info(chassis_data=data.chassises)
        if self.api_version_number == 2:
            if data.chassis is not None:
                clusterInfos['chassis'] = VxRailCluster().get_chassis_basic_info(chassis_data=data.chassis)
        clusterInfos['suppressed'] = data.suppressed
        clusterInfos['last_time'] = data.last_time
        clusterInfolist.append(dict(clusterInfos.items()))
        return clusterInfolist

    def get_chassis_basic_info(self, chassis_data):
        chassisInfos = {}
        chassisInfolist = []
        for i in range(len(chassis_data)):
            chassisInfos['id'] = chassis_data[i].id
            chassisInfos['psnt'] = chassis_data[i].psnt
            chassisInfos['model'] = chassis_data[i].model
            chassisInfos['render_category'] = chassis_data[i].render_category
            chassisInfos['generation'] = chassis_data[i].generation
            chassisInfos['health'] = chassis_data[i].health
            chassisInfos['missing'] = chassis_data[i].missing
            chassisInfolist.append(dict(chassisInfos.items()))
        return chassisInfolist


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
    result = VxRailCluster().get_cluster()
    if result == 'error':
        module.fail_json(msg="Call /cluster API failed,please see log file /tmp/vxrail_ansible_getclusterinfo.log for more error details.")
    vx_facts = {'Cluster_Information': result}
    vx_facts_result = dict(changed=False, Cluster_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
