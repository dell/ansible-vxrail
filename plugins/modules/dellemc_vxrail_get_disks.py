#!/usr/bin/python
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_get_disks

short_description: Retrieve VxRail Disk Information

description:
- This module will retrieve the VxRail Disk Information.
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

  disk_sn:
    description:
      Disk serial number to retrieve specific disk information, the default value is all.
    required: False
    type: str
    default: all

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for getting disks information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get VxRail Disk Information
    dellemc_vxrail_get_disks:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        disk_sn: "{{ disk_sn }}"
        api_version_number: "{{ api_version_number }}"
        timeout : "{{ timeout }}"
'''

RETURN = r'''
Disks_Info:
  description: The list of retrieved VxRail Disk Information
  returned: always
  type: dict
  sample: >-
    [
        {
            "id": "WLX016PY",
            "sn": "WLX016PY",
            "guid": "5000cca0b570ce48",
            "disk_type": "SSD",
            "protocol": "SAS",
            "enclosure": 0,
            "bay": 1,
            "slot": 1,
            "missing": false,
            "capacity": "3.49TB"
        },
        {
            "id": "WLX015VY",
            "sn": "WLX015VY",
            "guid": "5000cca0b570cde0",
            "disk_type": "SSD",
            "protocol": "SAS",
            "enclosure": 0,
            "bay": 1,
            "slot": 3,
            "missing": false,
            "capacity": "3.49TB"
        },
        {
            "id": "V6X0U8MA",
            "sn": "V6X0U8MA",
            "guid": "5000cca0a6723798",
            "disk_type": "SSD",
            "protocol": "SAS",
            "enclosure": 0,
            "bay": 1,
            "slot": 0,
            "missing": false,
            "capacity": "745.21GB"
        },
        {
            "id": "WLX018RY",
            "sn": "WLX018RY",
            "guid": "5000cca0b570cf44",
            "disk_type": "SSD",
            "protocol": "SAS",
            "enclosure": 0,
            "bay": 1,
            "slot": 4,
            "missing": false,
            "capacity": "3.49TB"
        }
    ]
'''

from functools import reduce
import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

# Defining global variables
# API = "GET /v1/disks"
MODULE = "dellemc_vxrail_get_disks"
LOG_FILE_PATH = "/tmp/vxrail_ansible_get_disks.log"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return f"https://{self.vxm_ip}/rest/vxm"


class VxRailCluster():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.api_version_number = module.params.get('api_version_number')
        self.disk_sn = module.params.get('disk_sn')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number,
                                                                   module_path,
                                                                   LOGGER)
        # Calls versioned method as attribute (ex: v1_disks_get)
        if self.disk_sn == 'all':
            call_string = self.api_version_string + '_disks_get'
            LOGGER.info("Using utility method: %s\n", call_string)
            disks_get = getattr(api_instance, call_string)
            return disks_get()
        else:
            call_string = self.api_version_string + '_disks_sn_get'
            LOGGER.info("Using utility method: %s\n", call_string)
            disks_sn_get = getattr(api_instance, call_string)
            return disks_sn_get(self.disk_sn)

    def get_disks(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.DiskInformationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query disk information
            response = self.get_versioned_response(api_instance, "/disks")
        except ApiException as e:
            LOGGER.error("Exception when calling DiskInformationApi->%s_disks_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/disks api response: %s\n", self.api_version_string, response)
        data = response
        return self._get_disks_list(self._generate_disks_info, data)

    def get_specific_disk(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.DiskInformationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query disk information
            response = self.get_versioned_response(api_instance, "/disks/{disk_sn}")
        except ApiException as e:
            LOGGER.error("Exception when calling DiskInformationApi->%s_disks_sn_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/disks/{disk_sn} api response: %s", self.api_version_string, response)
        data = response
        return self._generate_disks_info(data)

    def _get_disks_list(self, generate_func, data_list):
        return reduce(lambda infos, data: infos + [generate_func(data)], data_list, [])

    def _generate_disks_info(self, data):
        disks_info = {}
        disks_info['id'] = data.id
        disks_info['sn'] = data.sn
        disks_info['guid'] = data.guid
        disks_info['disk_type'] = data.disk_type
        disks_info['protocol'] = data.protocol
        disks_info['enclosure'] = data.enclosure
        disks_info['bay'] = data.bay
        disks_info['slot'] = data.slot
        disks_info['missing'] = data.missing
        disks_info['capacity'] = data.capacity
        return disks_info


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        disk_sn=dict(type='str', default='all'),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    API = "GET /v1/disks"
    if module.params.get('disk_sn') == "all":
        result = VxRailCluster().get_disks()
    else:
        result = VxRailCluster().get_specific_disk()
        API = "GET /v1/disks/{disk_sn}"
    if result == 'error':
        module.fail_json(
            msg=f"Call {API} API failed, please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts = {'Disks_Info': result}
    vx_facts_result = dict(changed=False, DISKS_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
