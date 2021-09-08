#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_clusterinfo

short_description: Retrieve VxRail Cluster Information

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

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

  timeout:
    description:
      Time out value for getting cluster infomation, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - Himanshu Saxena(@saxenh1) <himanshu.saxena@dell.com>

'''

EXAMPLES = r'''
  - name: Retrives VxRail Cluster Information
    dellemc-vxrail-clusterinfo:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"
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
from vxrail_ansible_utility import configuration as utils
import time
import json

LOGGER = utils.get_logger("dellemc_vxrail_clusterinfo", "/tmp/vxrail_ansible_clusterinfo.log", log_devel=logging.DEBUG)
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
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        response = ''

    def get_v1_cluster(self):
        clusterInfos = {}
        clusterInfolist = []
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.ClusterInformationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query v1 cluster information
            response = api_instance.v1_cluster_get()
        except ApiException as e:
            LOGGER.error("Exception when calling ClusterInformationApi->v1_cluster_get: %s\n", e)
            return 'error'
        LOGGER.info("v1/cluster api response: %s\n", response)
        data = response
        clusterInfos['cluster_id'] = data.cluster_id
        clusterInfos['product_type'] = data.product_type
        clusterInfos['device_type'] = data.device_type
        clusterInfos['vc_connected'] = data.vc_connected
        clusterInfos['health'] = data.health
        clusterInfos['operational_status'] = data.operational_status
        if data.chassises is not None:
            clusterInfos['chassises'] = []
            chassises_list = data.chassises
            chassises = {}
            clusterInfo_chassises_list = []
            for i in range(len(chassises_list)):
                chassises['id'] = chassises_list[i].id
                chassises['psnt'] = chassises_list[i].psnt
                chassises['model'] = chassises_list[i].model
                chassises['render_category'] = chassises_list[i].render_category
                chassises['generation'] = chassises_list[i].generation
                chassises['health'] = chassises_list[i].health
                chassises['missing'] = chassises_list[i].missing
                clusterInfo_chassises_list.append(dict(chassises.items()))
            clusterInfos['chassises'] = clusterInfo_chassises_list
        clusterInfos['suppressed'] = data.suppressed
        clusterInfos['last_time'] = data.last_time
        clusterInfolist.append(dict(clusterInfos.items()))
        return clusterInfolist


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().get_v1_cluster()
    if result == 'error':
        module.fail_json(msg="Call V1/ClusterInfo API failed,please see log file /tmp/vxrail_ansible_clusterinfo.log for more error details.")
    vx_facts = {'Cluster_Information': result}
    vx_facts_result = dict(changed=False, V1_Cluster_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()