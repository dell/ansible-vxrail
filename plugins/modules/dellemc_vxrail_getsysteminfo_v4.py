#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_getsysteminfo_v4

short_description: Retrieve VxRail System Information

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.3.0"

description:
- This module will retrieve VxRail System Information.
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
      Time out value for getting system information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get VxRail System Information
    dellemc_vxrail_getsysteminfo_v4:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout : "{{ timeout }}"
'''

RETURN = r'''
System_Information:
  description: system information summary
  returned: always
  type: dict
  sample: >-
    {
                    "cluster_host_count": 4,
                    "deployment_type": [
                        "STANDARD"
                    ],
                    "description": "A hyperconverged infrastructure appliance that combines VMware compute,
                    networking and storage into one single system for ease of deployment and management.",
                    "health": "Healthy",
                    "installed_components": [
                        {
                            "baseline_drifted": false,
                            "component": "MysticManager",
                            "current_version": "7.0.350-27282917",
                            "description": "The management component that orchestrates the\ndeployment and
                            management of VxRail system.",
                            "multiple_version": false,
                            "name": "VxRail Manager",
                            "supported": true,
                        },
                        {
                            "baseline_drifted": false,
                            "component": "Vcenter",
                            "current_version": "7.0.3-18778458",
                            "description": "Centralized visibility, proactive management and\nextensibility for
                            VMware vSphere from a single console VMware vCenter\nServer provides a centralized platform
                            for managing your VMware vSphere\nenvironments, so you can automate and deliver a virtual
                            infrastructure\nwith confidence.",
                            "multiple_version": false,
                            "name": "VMware vCenter Server Appliance",
                            "supported": true,
                        },
                        {
                            "baseline_drifted": false,
                            "component": "VxRailVib",
                            "current_version": "7.0.350-18878128",
                            "description": "VxRail Manager agent installed on ESXi.",
                            "installed_time": 1637280120832000,
                            "multiple_version": false,
                            "name": "VxRail Manager VIB",
                            "supported": true,
                        },
                        {
                            "baseline_drifted": false,
                            "component": "Esx",
                            "current_version": "7.0.3-18644231",
                            "description": "VMware ESXi is a thin hypervisor integrated into server hardware.
                            The compact, hardware embedded architecture of VMware ESXi raises the bar for security
                            and reliability and lays the foundation for a dynamic, automated datacenter.",
                            "installed_time": 1637280120832000,
                            "multiple_version": false,
                            "name": "VMware ESXi",
                            "supported": true,
                        }
                    ],
                    "installed_time": 1637282371606,
                    "is_external_vc": false,
                    "logical_view_status": false,
                    "network_connected": true,
                    "satellite_host_count": 0,
                    "shared_storage": [
                        {
                            "datastore_id": "datastore-12",
                            "is_primary": true,
                            "name": "VxRail-Virtual-SAN-Datastore-ea21cec8-7a09-4e5b-8fea-39cffbb817a7",
                            "protocol": "VSAN",
                            "type": "VSAN"
                        }
                    ],
                    "vc_connected": true,
                    "version": "7.0.350-27282917"
                }
            ]
        },
        "changed": false,
        "failed": false
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_getsysteminfo_v4", "/tmp/vxrail_ansible_getsysteminfo_v4.log", log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailSystemUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailSystemUrls.cluster_url.format(self.vxm_ip)


class VxRailSystem():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.system_url = VxrailSystemUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

    def get_v4_system(self):
        systemInfos = {}
        systemInfolist = []
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemInformationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query v4 system information
            response = api_instance.query_vx_rail_manager_system_information_v4()
        except ApiException as e:
            LOGGER.error("Exception when calling SystemInformationApi->query_vx_rail_manager_system_information_v4: %s\n", e)
            return 'error'
        LOGGER.info("v4/system api response: %s\n", response)
        data = response
        systemInfos['description'] = data.description
        systemInfos['version'] = data.version
        systemInfos['health'] = data.health
        if data.installed_time is not None:
            systemInfos['installed_time'] = data.installed_time
        systemInfos['cluster_host_count'] = data.cluster_host_count
        systemInfos['satellite_host_count'] = data.satellite_host_count
        systemInfos['is_external_vc'] = data.is_external_vc
        systemInfos['network_connected'] = data.network_connected
        systemInfos['vc_connected'] = data.vc_connected
        if data.upgrade_status is not None:
            systemInfos['upgrade_status'] = data.upgrade_status
        if data.installed_components is not None:
            systemInfos['installed_components'] = []
            installed_components_list = data.installed_components
            installed_components = {}
            systemInfo_installed_components_list = []
            for i in range(len(installed_components_list)):
                installed_components['component'] = installed_components_list[i].component
                installed_components['name'] = installed_components_list[i].name
                installed_components['description'] = installed_components_list[i].description
                installed_components['current_version'] = installed_components_list[i].current_version
                installed_components['supported'] = installed_components_list[i].supported
                if installed_components_list[i].installed_time is not None:
                    installed_components['installed_time'] = installed_components_list[i].installed_time
                if installed_components_list[i].baseline is not None:
                    installed_components['baseline'] = installed_components_list[i].baseline
                installed_components['baseline_drifted'] = installed_components_list[i].baseline_drifted
                if installed_components_list[i].incompatibilities is not None:
                    installed_components['incompatibilities'] = installed_components_list[i].incompatibilities
                installed_components['multiple_version'] = installed_components_list[i].multiple_version
                if installed_components_list[i].upgrade_status is not None:
                    installed_components['upgrade_status'] = installed_components_list[i].upgrade_status
                systemInfo_installed_components_list.append(dict(installed_components.items()))
            systemInfos['installed_components'] = systemInfo_installed_components_list
        systemInfos['deployment_type'] = data.deployment_type
        systemInfos['logical_view_status'] = data.logical_view_status
        if data.shared_storage is not None:
            systemInfos['shared_storage'] = []
            shared_storage_list = data.shared_storage
            shared_storage = {}
            systemInfo_shared_storage_list = []
            for i in range(len(shared_storage_list)):
                shared_storage['datastore_id'] = shared_storage_list[i].datastore_id
                shared_storage['name'] = shared_storage_list[i].name
                shared_storage['type'] = shared_storage_list[i].type
                shared_storage['is_primary'] = shared_storage_list[i].is_primary
                if shared_storage_list[i].protocol is not None:
                    shared_storage['protocol'] = shared_storage_list[i].protocol
                systemInfo_shared_storage_list.append(dict(shared_storage.items()))
            systemInfos['shared_storage'] = systemInfo_shared_storage_list
        systemInfolist.append(dict(systemInfos.items()))
        return systemInfolist


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
    result = VxRailSystem().get_v4_system()
    if result == 'error':
        module.fail_json(msg="Call V4/System API failed,please see log file /tmp/vxrail_ansible_getsysteminfo_v4.log for more error details.")
    vx_facts = {'System_Information': result}
    vx_facts_result = dict(changed=False, V4_System_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
