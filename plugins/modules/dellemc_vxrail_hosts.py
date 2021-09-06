#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_hosts

short_description: Retrieve VxRail hosts and their associated subcomponent information.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description:
- This module will get information of all hosts in the cluster or one host specified by serial number.
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

  host_sn:
    description:
      Serial number of the host to retrieve specific host information
    required: False
    type: str
    default: all

  timeout:
    description:
      Time out value for getting system infomation, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - Gao Hongmei(@gaohongmei) <s.gao@dell.com>
    - Yan Sun(@sunyan) <yan_sun5@dell.com>

'''

EXAMPLES = r'''
  - name: Retrives All VxRail Hosts Information
    dellemc_vxrail_hosts:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
'''

RETURN = r'''
Hosts_Information:
  description: host information summary
  returned: always
  type: dict
  sample: >-
        {
                "boot_devices": [
                    {
                        "avr_erase_count": null,
                        "block_size": "512",
                        "bootdevice_type": "BOSS",
                        "capacity": "223.57GB",
                        "controller_firmware": "2.5.13.3024",
                        "controller_model": "BOSS-S1",
                        "controller_status": "NORMAL",
                        "device_model": "SSDSCKJB240G7R",
                        "firmware_version": "D0DE008",
                        "health": "100%",
                        "id": "18331E196141",
                        "manufacturer": "Intel",
                        "max_erase_count": null,
                        "part_number": "GST02CPRCM0S80G8S1YQ0A",
                        "power_cycle_count": null,
                        "power_on_hours": null,
                        "sata_type": "SSD",
                        "slot": 0,
                        "sn": "18331E196141",
                        "status": "NORMAL"
                    },
                    {
                        "avr_erase_count": null,
                        "block_size": "512",
                        "bootdevice_type": "BOSS",
                        "capacity": "223.57GB",
                        "controller_firmware": "2.5.13.3024",
                        "controller_model": "BOSS-S1",
                        "controller_status": "NORMAL",
                        "device_model": "SSDSCKJB240G7R",
                        "firmware_version": "D0DE008",
                        "health": "100%",
                        "id": "18331E18542B",
                        "manufacturer": "Intel",
                        "max_erase_count": null,
                        "part_number": "GST02CPRCM0S80D8R16S0A",
                        "power_cycle_count": null,
                        "power_on_hours": null,
                        "sata_type": "SSD",
                        "slot": 1,
                        "sn": "18331E18542B",
                        "status": "NORMAL"
                    }
                ],
                "disks": [
                    {
                        "capacity": "400.0GB",
                        "disk_claim_type": "vSAN",
                        "disk_state": "OK",
                        "disk_type": "HDD",
                        "enclosure": 0,
                        "firmware_revision": "DSLA",
                        "id": "V010104DVSN00",
                        "led_status": "Green:On",
                        "manufacturer": "SAMSUNG",
                        "max_capable_speed": "12 Gb/s",
                        "missing": false,
                        "model": "MZILS1T9HEJH0D3",
                        "protocol": "SAS",
                        "remaining_write_endurance_rate": null,
                        "slot": 0,
                        "sn": "V010104DVSN00",
                        "write_endurance": null,
                        "write_endurance_status": null
                    },
                    {
                        "capacity": "40.0GB",
                        "disk_claim_type": "vSAN",
                        "disk_state": "OK",
                        "disk_type": "SSD",
                        "enclosure": 0,
                        "firmware_revision": "AS10",
                        "id": "V010104DVSN01",
                        "led_status": "Green:On",
                        "manufacturer": "TOSHIBA",
                        "max_capable_speed": "12 Gb/s",
                        "missing": false,
                        "model": "PX05SMB040Y",
                        "protocol": "SAS",
                        "remaining_write_endurance_rate": "97%",
                        "slot": 8,
                        "sn": "V010104DVSN01",
                        "write_endurance": "3",
                        "write_endurance_status": null
                    },
                    {
                        "capacity": "400.0GB",
                        "disk_claim_type": "vSAN",
                        "disk_state": "OK",
                        "disk_type": "HDD",
                        "enclosure": 0,
                        "firmware_revision": "DSLA",
                        "id": "V010104DVSN02",
                        "led_status": "Green:On",
                        "manufacturer": "SAMSUNG",
                        "max_capable_speed": "12 Gb/s",
                        "missing": false,
                        "model": "MZILS1T9HEJH0D3",
                        "protocol": "SAS",
                        "remaining_write_endurance_rate": null,
                        "slot": 4,
                        "sn": "V010104DVSN02",
                        "write_endurance": null,
                        "write_endurance_status": null
                    },
                    {
                        "capacity": "40.0GB",
                        "disk_claim_type": "vSAN",
                        "disk_state": "OK",
                        "disk_type": "SSD",
                        "enclosure": 0,
                        "firmware_revision": "AS10",
                        "id": "V010104DVSN03",
                        "led_status": "Green:On",
                        "manufacturer": "TOSHIBA",
                        "max_capable_speed": "12 Gb/s",
                        "missing": false,
                        "model": "PX05SMB080Y",
                        "protocol": "SAS",
                        "remaining_write_endurance_rate": "100%",
                        "slot": 9,
                        "sn": "V010104DVSN03",
                        "write_endurance": "0",
                        "write_endurance_status": null
                    }
                ],
                "drive_configuration": {
                    "type": "1002"
                },
                "firmware_info": {
                    "bios_revision": "2.11.2",
                    "bmc_revision": "4.40.40.00",
                    "boss_version": "2.5.13.3024",
                    "cpld_version": "1.0.2",
                    "dcpm_version": null,
                    "expander_bpf_version": "2.52",
                    "hba_version": "16.17.01.00",
                    "nonexpander_bpf_version": null
                },
                "geo_location": {
                    "order_number": 1,
                    "rack_name": ""
                },
                "health": "Warning",
                "hostname": "vcluster101-esx04.vv009.local",
                "id": "V010104",
                "led_status": "Blue:On",
                "manufacturer": "Dell Inc.",
                "missing": false,
                "name": "vcluster101-esx04.vv009.local",
                "nics": [
                    {
                        "firmware_family_version": "20.0.16",
                        "id": "00:50:56:a2:fe:bb",
                        "link_speed": "10 Gbps",
                        "link_status": "Up",
                        "mac": "00:50:56:a2:fe:bb",
                        "slot": 1
                    },
                    {
                        "firmware_family_version": "20.0.16",
                        "id": "00:50:56:a2:f0:81",
                        "link_speed": "10 Gbps",
                        "link_status": "Up",
                        "mac": "00:50:56:a2:f0:81",
                        "slot": 2
                    },
                    {
                        "firmware_family_version": "20.0.16",
                        "id": "00:50:56:a2:99:50",
                        "link_speed": "10 Gbps",
                        "link_status": "Up",
                        "mac": "00:50:56:a2:99:50",
                        "slot": 3
                    },
                    {
                        "firmware_family_version": "20.0.16",
                        "id": "00:50:56:a2:66:cd",
                        "link_speed": "10 Gbps",
                        "link_status": "Up",
                        "mac": "00:50:56:a2:66:cd",
                        "slot": 4
                    }
                ],
                "operational_status": "normal",
                "power_status": "on",
                "psnt": "V0101040000000",
                "slot": 1,
                "sn": "V010104",
                "tpm_present": false
        }
'''
from functools import reduce
from vxrail_ansible_utility import configuration as utils
from vxrail_ansible_utility.rest import ApiException
import vxrail_ansible_utility
from ansible.module_utils.basic import AnsibleModule
import urllib3
import logging

LOGGER = utils.get_logger(
    "dellemc_vxrail_hosts", "/tmp/vxrail_ansible_hosts.log", log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxRailHostsUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxRailHostsUrls.cluster_url.format(self.vxm_ip)


class VxRailHosts():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.host_sn = module.params.get('host_sn')
        self.hosts_url = VxRailHostsUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.hosts_url.set_host()
        response = ''

    def get_v4_hosts(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.HostInformationApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # get all v4 hosts information
            response = api_instance.v4_hosts_get()
        except ApiException as e:
            LOGGER.error(
                "Exception when calling HostInformationApi->v4_hosts_get: %s\n", e)
            return 'error'
        LOGGER.info("v4/hosts api response: %s\n", response)
        datalist = response
        if not datalist:
            return "No available hosts"
        return self._get_info_list(self._generate_host_info_from_response_data, datalist)

    def get_specific_v4_hosts(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.HostInformationApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # get specific v4 host information by sn
            response = api_instance.v4_hosts_sn_get(self.host_sn)
        except ApiException as e:
            LOGGER.error(
                "Exception when calling HostInformationApi->v4_hosts_sn_get: %s\n", e)
            return 'error'
        LOGGER.info("v4/hosts/{sn} api response: %s\n", response)
        data = response
        if not data:
            return "No available host"
        return self._generate_host_info_from_response_data(data)

    def _get_info_list(self, generate_func, data_list):
        return reduce(lambda infos, data: infos + [generate_func(data)], data_list, [])

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
        if data.boot_devices is not None:
            host_info['boot_devices'] = self._get_info_list(
                self._generate_boot_device_info_from_response_data, data.boot_devices)
        if data.nics is not None:
            host_info['nics'] = self._get_info_list(
                self._generate_nic_info_from_response_data, data.nics)
        if data.disks is not None:
            host_info['disks'] = self._get_info_list(
                self._generate_disk_info_from_response_data, data.disks)
        if data.firmware_info is not None:
            host_info['firmware_info'] = self._generate_firmware_info_from_response_data(
                data.firmware_info)
        if data.geo_location is not None:
            host_info['geo_location'] = self._generate_geo_location_info_from_response_data(
                data.geo_location)
        if data.drive_configuration is not None:
            host_info['drive_configuration'] = self._generate_drive_configuration_info_from_response_data(
                data.drive_configuration)
        return host_info

    def _generate_boot_device_info_from_response_data(self, data):
        boot_device_info = {}
        boot_device_info['id'] = data.id
        boot_device_info['sn'] = data.sn
        boot_device_info['device_model'] = data.device_model
        boot_device_info['sata_type'] = data.sata_type
        boot_device_info['power_on_hours'] = data.power_on_hours
        boot_device_info['power_cycle_count'] = data.power_cycle_count
        boot_device_info['max_erase_count'] = data.max_erase_count
        boot_device_info['avr_erase_count'] = data.avr_erase_count
        boot_device_info['capacity'] = data.capacity
        boot_device_info['health'] = data.health
        boot_device_info['firmware_version'] = data.firmware_version
        boot_device_info['bootdevice_type'] = data.bootdevice_type
        boot_device_info['block_size'] = data.block_size
        boot_device_info['slot'] = data.slot
        boot_device_info['status'] = data.status
        boot_device_info['part_number'] = data.part_number
        boot_device_info['manufacturer'] = data.manufacturer
        boot_device_info['controller_firmware'] = data.controller_firmware
        boot_device_info['controller_model'] = data.controller_model
        boot_device_info['controller_status'] = data.controller_status
        return boot_device_info

    def _generate_nic_info_from_response_data(self, data):
        nic_info = {}
        nic_info['id'] = data.id
        nic_info['mac'] = data.mac
        nic_info['link_status'] = data.link_status
        nic_info['link_speed'] = data.link_speed
        nic_info['slot'] = data.slot
        nic_info['firmware_family_version'] = data.firmware_family_version
        return nic_info

    def _generate_disk_info_from_response_data(self, data):
        disk_info = {}
        disk_info['id'] = data.id
        disk_info['sn'] = data.sn
        disk_info['manufacturer'] = data.manufacturer
        disk_info['model'] = data.model
        disk_info['disk_type'] = data.disk_type
        disk_info['protocol'] = data.protocol
        disk_info['max_capable_speed'] = data.max_capable_speed
        disk_info['enclosure'] = data.enclosure
        disk_info['slot'] = data.slot
        disk_info['disk_state'] = data.disk_state
        disk_info['led_status'] = data.led_status
        disk_info['missing'] = data.missing
        disk_info['capacity'] = data.capacity
        disk_info['write_endurance'] = data.write_endurance
        disk_info['write_endurance_status'] = data.write_endurance_status
        disk_info['remaining_write_endurance_rate'] = data.remaining_write_endurance_rate
        disk_info['firmware_revision'] = data.firmware_revision
        disk_info['disk_claim_type'] = data.disk_claim_type
        return disk_info

    def _generate_firmware_info_from_response_data(self, data):
        firmware_info = {}
        firmware_info['bios_revision'] = data.bios_revision
        firmware_info['bmc_revision'] = data.bmc_revision
        firmware_info['hba_version'] = data.hba_version
        firmware_info['expander_bpf_version'] = data.expander_bpf_version
        firmware_info['nonexpander_bpf_version'] = data.nonexpander_bpf_version
        firmware_info['boss_version'] = data.boss_version
        firmware_info['cpld_version'] = data.cpld_version
        firmware_info['dcpm_version'] = data.dcpm_version
        return firmware_info

    def _generate_geo_location_info_from_response_data(self, data):
        geo_location_info = {}
        geo_location_info['rack_name'] = data.rack_name
        geo_location_info['order_number'] = data.order_number
        return geo_location_info

    def _generate_drive_configuration_info_from_response_data(self, data):
        drive_configuration_info = {}
        drive_configuration_info['type'] = data.type
        return drive_configuration_info


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        host_sn=dict(type='str', default="all"),
        timeout=dict(type='int', default=60),
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailHosts().get_v4_hosts() if (module.params.get('host_sn')
                                              ) == "all" else VxRailHosts().get_specific_v4_hosts()
    if result == 'error':
        module.fail_json(
            msg="Call V4/Hosts API failed,please see log file /tmp/vxrail_ansible_system.log for more error details.")
    vx_facts = {"Hosts_Information": result}
    vx_facts_result = dict(changed=False, V4_Hosts_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
