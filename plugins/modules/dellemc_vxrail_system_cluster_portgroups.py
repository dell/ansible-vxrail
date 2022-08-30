#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_cluster_portgroups

short_description: Retrieve Cluster Portgroups

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.4.0"

description:
- This module retrieves information about cluster portgroups used by a node.
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

  node_fqdn:
    description:
      The Fully Qualified Domain Name of the node to query
    required: True
    type: str

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for getting cluster portgroup information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get Node's Cluster Portgroup Information
    dellemc_vxrail_system_cluster_portgroups:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        node_fqdn: "{{ node_fqdn }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Cluster_Portgroups:
  description: Retrieved information about cluster portgroups used by a node.
  returned: always
  type: dict
  sample: >-
    {
        "name": "VxRail Management-b6f3c545-92b5-422f-9629-e3de49d97c10",
        "type": "VXRAIL_MANAGEMENT",
        "portgroup_key": "dvportgroup-19",
        "portgroup_vlan": 0,
        "vds_name": "VMware HCIA Distributed Switch",
        "vds_moid": "dvs-12",
        "vds_uuid": "50 2e 7f 5b 4b 2b 95 50-c6 47 c3 67 f0 85 37 ec"
    }
'''

from functools import reduce
import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_system_cluster_portgroups",
                          "/tmp/vxrail_ansible_system_cluster_portgroups.log", log_devel=logging.DEBUG)
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
        self.node_fqdn = module.params.get('node_fqdn')
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    def get_versioned_response(self, api_instance, module_path, node_fqdn):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number,
                                                                   module_path,
                                                                   LOGGER)

        # Calls versioned method as attribute (ex: v1_system_cluster_portgroups_get)
        call_string = self.api_version_string + '_system_cluster_portgroups_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        system_cluster_portgroups_get = getattr(api_instance, call_string)
        return system_cluster_portgroups_get(node_fqdn)

    def get_cluster_portgroups(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemNetworkApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query system cluster-portgroup information
            response = self.get_versioned_response(api_instance, "/system/cluster-portgroups", self.node_fqdn)
        except ApiException as e:
            LOGGER.error("Exception when calling SystemNetworkApi->%s_system_cluster_portgroups_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/system/cluster-portgroups api response: %s\n", self.api_version_string, response)
        datalist = response
        if not datalist:
            return "No portgroup info found"
        return self._get_portgroup_info_list(self._generate_cluster_portgroup_info_from_response_data, datalist)

    def _get_portgroup_info_list(self, generate_func, data_list):
        return reduce(lambda infos, data: infos + [generate_func(data)], data_list, [])

    def _generate_cluster_portgroup_info_from_response_data(self, data):
        portgroup_info = {}
        portgroup_info['name'] = data.name
        portgroup_info['type'] = data.type
        portgroup_info['portgroup_key'] = data.portgroup_key
        portgroup_info['portgroup_vlan'] = data.portgroup_vlan
        portgroup_info['vds_name'] = data.vds_name
        portgroup_info['vds_moid'] = data.vds_moid
        portgroup_info['vds_uuid'] = data.vds_uuid
        return portgroup_info


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        node_fqdn=dict(required=True),
        timeout=dict(type='int', default=60),
        api_version_number=dict(type='int')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().get_cluster_portgroups()
    if result == 'error':
        module.fail_json(
            msg="Call /system/cluster-portgroups API failed,"
                "please see log file /tmp/vxrail_ansible_system_cluster_portgroups.log for more error details.")
    vx_facts = {'Cluster_Portgroups': result}
    vx_facts_result = dict(changed=False, Cluster_Portgroups_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
