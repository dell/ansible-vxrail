#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_chassis_get

short_description: Get chassis list & every node information for each chassis or the user-specified VxRail chassis.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
# Displays information up to version 4 (v4). Check the log for full API response from highest version.
version_added: "1.4.0"

description:
- This module will call /chassis api to get chassis list & every node information for each chassis and provide more host level information.
  If "chassis_id" is provided, this module will call /chassis/{chassis_id} to get information about the user-specified VxRail chassis.
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

  chassis_id:
    description:
      chassis id to retrieve specific chassis information
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
      Time out value for getting chassis infomation, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Retrieves All VxRail Chassis Information
    dellemc_vxrail_chassis_get:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
'''

RETURN = r'''
Chassis_Information:
  description: chassis information summary
  returned: always
  type: dict
  sample: >-
        {
                    "description": "Hubble",
                    "generation": 3,
                    "health": "Critical",
                    "hosts": [
                        {
                            "firmware_information": {
                                "bios_revision": "2.10.2",
                                "bmc_revision": "4.40.10.00",
                                "boss_version": null,
                                "cpld_version": "1.1.0",
                                "expander_bpf_version": null,
                                "hba_version": "16.17.01.00",
                                "nonexpander_bpf_version": "4.35"
                            },
                            "geo_location": {
                                "order_number": 1,
                                "rack_name": "c1-esx01"
                            },
                            "health": "Critical",
                            "hostname": "c1-esx01.rackh18.local",
                            "id": "9GMGHL2",
                            "led_status": "Blue:On",
                            "manufacturer": "Dell Inc.",
                            "missing": false,
                            "name": "c1-esx01.rackh18.local",
                            "operational_status": "normal",
                            "power_status": "on",
                            "psnt": "9GMGHL20000000",
                            "slot": 1,
                            "sn": "9GMGHL2",
                            "tpm_present": false
                        },
                        {
                            "firmware_information": {
                                "bios_revision": "2.10.2",
                                "bmc_revision": "4.40.10.00",
                                "boss_version": null,
                                "cpld_version": "1.1.0",
                                "expander_bpf_version": null,
                                "hba_version": "16.17.01.00",
                                "nonexpander_bpf_version": "4.35"
                            },
                            "geo_location": {
                                "order_number": 2,
                                "rack_name": "c1-esx01"
                            },
                            "health": "Critical",
                            "hostname": "c1-esx02.rackh18.local",
                            "id": "9GMHHL2",
                            "led_status": "Blue:On",
                            "manufacturer": "Dell Inc.",
                            "missing": false,
                            "name": "c1-esx02.rackh18.local",
                            "operational_status": "normal",
                            "power_status": "on",
                            "psnt": "9GMHHL20000000",
                            "slot": 3,
                            "sn": "9GMHHL2",
                            "tpm_present": true
                        },
                        {
                            "firmware_information": {
                                "bios_revision": "2.10.2",
                                "bmc_revision": "4.40.10.00",
                                "boss_version": null,
                                "cpld_version": "1.1.0",
                                "expander_bpf_version": null,
                                "hba_version": "16.17.01.00",
                                "nonexpander_bpf_version": "4.35"
                                "idsdm_version": "1.9",
                                "dcpm_version": null,
                                "perc_version": null
                            },
                            "geo_location": {
                                "order_number": 3,
                                "rack_name": "default-rack"
                            },
                            "health": "Critical",
                            "hostname": "c1-esx03.rackh18.local",
                            "id": "9GMKHL2",
                            "led_status": "Blue:On",
                            "manufacturer": "Dell Inc.",
                            "missing": false,
                            "name": "c1-esx03.rackh18.local",
                            "operational_status": "normal",
                            "power_status": "on",
                            "psnt": "9GMKHL20000000",
                            "slot": 4,
                            "sn": "9GMKHL2",
                            "tpm_present": true
                        },
                        {
                            "firmware_information": {
                                "bios_revision": "2.10.2",
                                "bmc_revision": "4.40.10.00",
                                "boss_version": null,
                                "cpld_version": "1.1.0",
                                "expander_bpf_version": null,
                                "hba_version": "16.17.01.00",
                                "nonexpander_bpf_version": "4.35"
                            },
                            "geo_location": {
                                "order_number": 4,
                                "rack_name": "c1-esx01"
                            },
                            "health": "Critical",
                            "hostname": "c1-esx04.rackh18.local",
                            "id": "9GMJHL2",
                            "led_status": "Blue:On",
                            "manufacturer": "Dell Inc.",
                            "missing": false,
                            "name": "c1-esx04.rackh18.local",
                            "operational_status": "normal",
                            "power_status": "maintenance",
                            "psnt": "9GMJHL20000000",
                            "slot": 2,
                            "sn": "9GMJHL2",
                            "tpm_present": false
                        }
                    ],
                    "id": "CTPMHL20000000",
                    "missing": false,
                    "model": "VxRail G560F",
                    "part_number": null,
                    "power_supplies": [
                        {
                            "health": "Critical",
                            "manufacturer": null,
                            "missing": true,
                            "name": null,
                            "part_number": null,
                            "revision_number": null,
                            "slot": 1,
                            "sn": "CTPMHL200000001"
                        },
                        {
                            "health": "Healthy",
                            "manufacturer": "DELL",
                            "missing": false,
                            "name": "Power Supply 2",
                            "part_number": "0W1R7VA00",
                            "revision_number": "0.1c.53",
                            "slot": 2,
                            "sn": "CTPMHL200000002"
                        }
                    ],
                    "psnt": "CTPMHL20000000",
                    "render_category": "DELL_C6420",
                    "service_tag": "CTPMHL2",
                    "sn": "9GMJHL2"
                    "bay": false

        }
'''
from functools import reduce
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils
from vxrail_ansible_utility.rest import ApiException
import vxrail_ansible_utility
from ansible.module_utils.basic import AnsibleModule
import urllib3
import logging

LOGGER = utils.get_logger(
    "dellemc_vxrail_chassis", "/tmp/vxrail_ansible_chassis.log", log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxRailChassisUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxRailChassisUrls.cluster_url.format(self.vxm_ip)


class VxRailHosts():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.chassis_id = module.params.get('chassis_id')
        self.api_version_number = module.params.get('api_version_number')
        self.hosts_url = VxRailChassisUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.hosts_url.set_host()
        # Added for auto-version detection
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        if self.chassis_id == "all":
            # Calls versioned method as attribute (ex: v1_chassis_get)
            call_string = self.api_version_string + '_chassis_get'
            LOGGER.info("Using utility method: %s\n", call_string)
            api_chassis_get = getattr(api_instance, call_string)
            return api_chassis_get()
        else:
            # Calls versioned method as attribute (ex: v1_chassis_id_get)
            call_string = self.api_version_string + '_chassis_id_get'
            LOGGER.info("Using utility method: %s\n", call_string)
            api_chassis_id_get = getattr(api_instance, call_string)
            return api_chassis_id_get(self.chassis_id)

    def get_chassis(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.ChassisInformationApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # get all chassis information
            response = self.get_versioned_response(api_instance, '/chassis')
        except ApiException as e:
            LOGGER.error("Exception when calling ChassisInformationApi->%s_chassis_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("Call %s/chassis api response: %s\n", self.api_version_string, response)
        datalist = response
        if not datalist:
            return "No available hosts"
        return self._get_info_list(self._generate_chassis_info, datalist)

    def get_specific_chassis(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.ChassisInformationApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # get specific chassis information by chassis id
            response = self.get_versioned_response(api_instance, '/chassis/{chassis_id}')
        except ApiException as e:
            LOGGER.error("Exception when calling ChassisInformationApi->%s/chassis/{chassis_id}: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("Call %s/chassis/{chassis_id} api response: %s\n", self.api_version_string, response)
        data = response
        if not data:
            return "No available host"
        return self._generate_chassis_info(data)

    def _get_info_list(self, generate_func, data_list):
        return reduce(lambda infos, data: infos + [generate_func(data)], data_list, [])

    def _generate_chassis_info(self, data):
        chassis_info = {}
        chassis_info['id'] = data.id
        chassis_info['sn'] = data.sn
        chassis_info['part_number'] = data.part_number
        chassis_info['description'] = data.description
        chassis_info['service_tag'] = data.service_tag
        chassis_info['psnt'] = data.psnt
        chassis_info['model'] = data.model
        chassis_info['health'] = data.health
        chassis_info['missing'] = data.missing
        chassis_info['render_category'] = data.render_category
        chassis_info['generation'] = data.generation

        # Only found in v4+
        if self.api_version_number >= 4:
            chassis_info['bay'] = data.bay
        else:
            chassis_info['bay'] = utils.field_not_found(4)

        if data.hosts is not None:
            chassis_info['hosts'] = self._get_info_list(
                self._generate_host_info_from_response_data, data.hosts)
        if data.power_supplies is not None:
            chassis_info['power_supplies'] = self._get_info_list(
                self._generate_power_supplies_info_from_response_data, data.power_supplies)
        return chassis_info

    def _generate_host_info_from_response_data(self, data):
        host_info = {}
        host_info['id'] = data.id
        host_info['sn'] = data.sn
        host_info['slot'] = data.slot
        host_info['hostname'] = data.hostname
        host_info['name'] = data.name
        host_info['manufacturer'] = data.manufacturer
        host_info['psnt'] = data.psnt
        host_info['led_status'] = data.led_status
        host_info['health'] = data.health
        host_info['missing'] = data.missing
        host_info['tpm_present'] = data.tpm_present
        host_info['operational_status'] = data.operational_status
        host_info['power_status'] = data.power_status

        # Only found in v3+
        if self.api_version_number >= 3:
            if data.firmware_info is not None:
                host_info['firmware_info'] = self._generate_firmware_info_from_response_data(data.firmware_info)
        else:
            host_info['firmware_info'] = utils.field_not_found(3)

        # Only found in v2+
        if self.api_version_number >= 2:
            if data.geo_location is not None:
                host_info['geo_location'] = self._generate_geo_location_info_from_response_data(
                    data.geo_location)
        else:
            host_info['geo_location'] = utils.field_not_found(2)

        return host_info

    def _generate_power_supplies_info_from_response_data(self, data):
        nic_info = {}
        nic_info['sn'] = data.sn
        nic_info['part_number'] = data.part_number
        nic_info['revision_number'] = data.revision_number
        nic_info['name'] = data.name
        nic_info['manufacturer'] = data.manufacturer
        nic_info['slot'] = data.slot
        nic_info['health'] = data.health
        nic_info['missing'] = data.missing
        return nic_info

    def _generate_firmware_info_from_response_data(self, data):
        firmware_info = {}
        firmware_info['bios_revision'] = data.bios_revision
        firmware_info['bmc_revision'] = data.bmc_revision
        firmware_info['hba_version'] = data.hba_version
        firmware_info['expander_bpf_version'] = data.expander_bpf_version
        firmware_info['nonexpander_bpf_version'] = data.nonexpander_bpf_version
        firmware_info['boss_version'] = data.boss_version
        firmware_info['cpld_version'] = data.cpld_version

        # Only found in v4+
        if self.api_version_number >= 4:
            firmware_info['idsdm_version'] = data.idsdm_version
            firmware_info['dcpm_version'] = data.dcpm_version
            firmware_info['perc_version'] = data.perc_version
        else:
            firmware_info['idsdm_version'] = utils.field_not_found(4)
            firmware_info['dcpm_version'] = utils.field_not_found(4)
            firmware_info['perc_version'] = utils.field_not_found(4)

        return firmware_info

    def _generate_geo_location_info_from_response_data(self, data):
        geo_location_info = {}
        geo_location_info['rack_name'] = data.rack_name
        geo_location_info['order_number'] = data.order_number
        return geo_location_info


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        chassis_id=dict(type='str', default="all"),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60),
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    if module.params.get('chassis_id') == "all":
        result = VxRailHosts().get_chassis()
    else:
        result = VxRailHosts().get_specific_chassis()
    if result == 'error':
        module.fail_json(
            msg="Call /chassis API failed,please see log file /tmp/vxrail_ansible_chassis.log for more error details.")
    vx_facts = {"Chassis_Information": result}
    vx_facts_result = dict(changed=False, Chassis_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
