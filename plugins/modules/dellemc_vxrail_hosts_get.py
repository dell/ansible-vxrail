#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_hosts_get

short_description: Retrieve VxRail hosts and their associated subcomponent information.

description:
- This module will get information of all hosts in the cluster with /hosts api or one host specified by serial number with /hosts/{sn}.
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

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for getting system infomation, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Retrieves All VxRail Hosts Information From Highest Version
    dellemc_vxrail_hosts_get:
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
                        "disk_claim_type": "VSAN",
                        "disk_state": "OK",
                        "disk_type": "HDD",
                        "disk_tier": "CAPACITY",
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
                        "disk_claim_type": "VSAN",
                        "disk_state": "OK",
                        "disk_type": "SSD",
                        "disk_tier": "CACHE",
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
                        "disk_claim_type": "VSAN",
                        "disk_state": "OK",
                        "disk_type": "HDD",
                        "disk_tier": "CAPACITY",
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
                        "disk_claim_type": "VSAN",
                        "disk_state": "OK",
                        "disk_type": "SSD",
                        "disk_tier": "CACHE",
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
                    "fpga_version": "1.0.2",
                    "dcpm_version": null,
                    "expander_bpf_version": "2.52",
                    "passive_bpf_version": "1.72",
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
                "type": "CLUSTER",
                "tpm_present": false
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
        self.api_version_number = module.params.get('api_version_number')
        self.hosts_url = VxRailHostsUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.hosts_url.set_host()
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)
        if self.host_sn == "all":
            # Calls versioned method as attribute (ex: v1_hosts_get)
            call_string = self.api_version_string + '_hosts_get'
            LOGGER.info("Using utility method: %s\n", call_string)
            api_hosts_get = getattr(api_instance, call_string)
            return api_hosts_get()
        else:
            # Calls versioned method as attribute (ex: v1_hosts_sn_get)
            call_string = self.api_version_string + '_hosts_sn_get'
            LOGGER.info("Using utility method: %s\n", call_string)
            api_hosts_sn_get = getattr(api_instance, call_string)
            return api_hosts_sn_get(self.host_sn)

    def get_hosts(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.HostInformationApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # get all hosts information
            response = self.get_versioned_response(api_instance, "Get /hosts")
        except ApiException as e:
            LOGGER.error("Exception when calling HostInformationApi->%s_hosts_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("Call %s/hosts api response: %s\n", self.api_version_string, response)
        datalist = response
        if not datalist:
            return "No available hosts"
        return self._get_info_list(self._generate_host_info_from_response_data, datalist)

    def get_specific_hosts(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.HostInformationApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # get specific host information by sn
            response = self.get_versioned_response(api_instance, "GET /hosts/{sn}")
        except ApiException as e:
            LOGGER.error("Exception when calling HostInformationApi->%s_hosts_sn_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("Call %s/hosts/{sn} api response: %s\n", self.api_version_string, response)
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
        host_info['led_color'] = data.led_color if self.api_version_number >= 15 else utils.field_not_found(1)
        host_info['health'] = data.health
        host_info['missing'] = data.missing
        host_info['tpm_present'] = data.tpm_present
        host_info['operational_status'] = data.operational_status
        host_info['power_status'] = data.power_status

        host_info['dpus'] = \
            self._get_info_list(self._generate_dpu_info_from_response_data, data.dpus) \
            if hasattr(data, 'dpus') else []

        if self.api_version_number >= 10:
            host_info['part_number'] = data.part_number
            if data.gpus:
                host_info['gpus'] = self._get_info_list(self._generate_gpu_info_from_response_data, data.gpus)
            else:
                host_info['gpus'] = []

        host_info['tpm_version'] = data.tpm_version if hasattr(data, 'tpm_version') else utils.field_not_found(14)
        host_info['tpm_status'] = data.tpm_status if hasattr(data, 'tpm_status') else utils.field_not_found(14)

        # Only found in v5+
        if self.api_version_number >= 5:
            host_info['type'] = data.type
        else:
            host_info['type'] = utils.field_not_found(5)

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

        # Only found in v7+
        if self.api_version_number >= 7:
            if data.encryption_status is not None:
                host_info['encryption_status'] = self._generate_encryption_status_info_from_response_data(
                    data.encryption_status)
        else:
            host_info['encryption_status'] = utils.field_not_found(7)

        # Only found in v4+
        if self.api_version_number >= 4:
            if data.drive_configuration is not None:
                host_info['drive_configuration'] = self._generate_drive_configuration_info_from_response_data(
                    data.drive_configuration)
        else:
            host_info['drive_configuration'] = utils.field_not_found(4)

        # Only found in v2+
        if self.api_version_number >= 2:
            if data.geo_location is not None:
                host_info['geo_location'] = self._generate_geo_location_info_from_response_data(
                    data.geo_location)
        else:
            host_info['geo_location'] = utils.field_not_found(2)

        return host_info

    def _generate_boot_device_info_from_response_data(self, data):
        boot_device_info = {}
        boot_device_info['id'] = data.id
        boot_device_info['sn'] = data.sn
        boot_device_info['device_model'] = data.device_model
        if self.api_version_number < 10:
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

        # Only found in v10+
        if self.api_version_number >= 10:
            boot_device_info['device_type'] = data.device_type
            boot_device_info['protocol'] = data.protocol

        # Only found in v4+
        if self.api_version_number >= 4:
            boot_device_info['status'] = data.status
            boot_device_info['part_number'] = data.part_number
            boot_device_info['manufacturer'] = data.manufacturer
            boot_device_info['controller_firmware'] = data.controller_firmware
            boot_device_info['controller_model'] = data.controller_model
            boot_device_info['controller_status'] = data.controller_status
        else:
            boot_device_info['status'] = utils.field_not_found(4)
            boot_device_info['part_number'] = utils.field_not_found(4)
            boot_device_info['manufacturer'] = utils.field_not_found(4)
            boot_device_info['controller_firmware'] = utils.field_not_found(4)
            boot_device_info['controller_model'] = utils.field_not_found(4)
            boot_device_info['controller_status'] = utils.field_not_found(4)

        # Only found in v15+
        if self.api_version_number >= 15:
            boot_device_info['encryption_ability'] = data.encryption_ability
            boot_device_info['encryption_status'] = data.encryption_status
            boot_device_info['controller_encryption_capability'] = data.controller_encryption_capability
            boot_device_info['controller_encryption_mode'] = data.controller_encryption_mode
        else:
            boot_device_info['encryption_ability'] = utils.field_not_found(15)
            boot_device_info['encryption_status'] = utils.field_not_found(15)
            boot_device_info['controller_encryption_capability'] = utils.field_not_found(15)
            boot_device_info['controller_encryption_mode'] = utils.field_not_found(15)

        return boot_device_info

    def _generate_nic_info_from_response_data(self, data):
        nic_info = {}
        nic_info['id'] = data.id
        nic_info['mac'] = data.mac
        nic_info['link_status'] = data.link_status
        nic_info['link_speed'] = data.link_speed
        nic_info['slot'] = data.slot
        nic_info['firmware_family_version'] = data.firmware_family_version

        # Only found in v8+, but v9 don't support these field
        if self.api_version_number >= 8 and self.api_version_number != 9:
            nic_info['wwnn'] = data.wwnn
            nic_info['wwpn'] = data.wwpn
        else:
            nic_info['wwnn'] = utils.field_not_found(8)
            nic_info['wwpn'] = utils.field_not_found(8)

        # Only found in v7+
        if self.api_version_number >= 7:
            nic_info['type'] = data.type
            if data.drivers is not None:
                nic_info['drivers'] = self._get_info_list(
                    self._generate_drivers_info_from_response_data, data.drivers)
        else:
            nic_info['type'] = utils.field_not_found(7)
            nic_info['drivers'] = utils.field_not_found(7)

        # Only found in v6+
        if self.api_version_number >= 6:
            nic_info['port'] = data.port
        else:
            nic_info['port'] = utils.field_not_found(6)

        # Only found in v15+
        if self.api_version_number >= 15:
            nic_info['vendor'] = data.vendor
            nic_info['model'] = data.model
        else:
            nic_info['vendor'] = utils.field_not_found(15)
            nic_info['model'] = utils.field_not_found(15)
        return nic_info

    def _generate_disk_info_from_response_data(self, data):
        disk_info = {}
        disk_info['id'] = data.id
        disk_info['sn'] = data.sn
        disk_info['disk_type'] = data.disk_type
        disk_info['protocol'] = data.protocol
        disk_info['enclosure'] = data.enclosure
        disk_info['slot'] = data.slot
        disk_info['missing'] = data.missing
        disk_info['capacity'] = data.capacity

        disk_info['disk_tier'] = data.disk_tier if hasattr(data, 'disk_tier') else utils.field_not_found(16)
        # Only found in v3+
        if self.api_version_number >= 3:
            disk_info['manufacturer'] = data.manufacturer
            disk_info['model'] = data.model
            disk_info['disk_state'] = data.disk_state
            disk_info['led_status'] = data.led_status
            disk_info['write_endurance'] = data.write_endurance
            disk_info['write_endurance_status'] = data.write_endurance_status
            disk_info['remaining_write_endurance_rate'] = data.remaining_write_endurance_rate
            disk_info['firmware_revision'] = data.firmware_revision
            disk_info['disk_claim_type'] = data.disk_claim_type
            disk_info['max_capable_speed'] = data.max_capable_speed

        else:
            disk_info['manufacturer'] = utils.field_not_found(3)
            disk_info['model'] = utils.field_not_found(3)
            disk_info['disk_state'] = utils.field_not_found(3)
            disk_info['led_status'] = utils.field_not_found(3)
            disk_info['write_endurance'] = utils.field_not_found(3)
            disk_info['write_endurance_status'] = utils.field_not_found(3)
            disk_info['remaining_write_endurance_rate'] = utils.field_not_found(3)
            disk_info['firmware_revision'] = utils.field_not_found(3)
            disk_info['disk_claim_type'] = utils.field_not_found(3)
            disk_info['max_capable_speed'] = utils.field_not_found(3)

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

        # Only found in v10+
        if self.api_version_number >= 10:
            firmware_info['idsdm_version'] = data.idsdm_version

        # Only found in v5+
        if self.api_version_number >= 5:
            firmware_info['perc_version'] = data.perc_version
        else:
            firmware_info['perc_version'] = utils.field_not_found(5)

        # Only found in v3+
        if self.api_version_number >= 3:
            firmware_info['dcpm_version'] = data.dcpm_version
        else:
            firmware_info['dcpm_version'] = utils.field_not_found(3)

        # Only found in v4+
        if self.api_version_number >= 17:
            firmware_info['fpga_version'] = data.fpga_version
            firmware_info['passive_bpf_version'] = data.passive_bpf_version
        else:
            firmware_info['fpga_version'] = utils.field_not_found(17)
            firmware_info['passive_bpf_version'] = utils.field_not_found(17)

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

    def _generate_drivers_info_from_response_data(self, data):
        drivers_info = {}
        drivers_info['driver_name'] = data.driver_name
        drivers_info['driver_version'] = data.driver_version
        return drivers_info

    def _generate_encryption_status_info_from_response_data(self, data):
        encryption_status_info = {}
        if data.encryption_mode is not None:
            encryption_status_info['encryption_mode'] = self._generate_encryption_mode_info_from_response_data(data.encryption_mode)
        if data.security_status is not None:
            encryption_status_info['security_status'] = self._generate_security_status_info_from_response_data(data.security_status)

        return encryption_status_info

    def _generate_encryption_mode_info_from_response_data(self, data):
        encryption_mode_info = {}
        encryption_mode_info['key'] = data.key
        encryption_mode_info['value'] = data.value

        return encryption_mode_info

    def _generate_security_status_info_from_response_data(self, data):
        security_status_info = {}
        security_status_info['key'] = data.key
        security_status_info['value'] = data.value

        return security_status_info

    def _generate_gpu_info_from_response_data(self, data):
        gpu_info = {}
        gpu_info['type'] = data.type
        gpu_info['slot'] = data.slot
        gpu_info['vendor_description'] = data.vendor_description
        gpu_info['supplier'] = data.supplier
        # Only found in v12+
        if self.api_version_number >= 12:
            gpu_info['marketing_name'] = data.marketing_name
            gpu_info['firmware_version'] = data.firmware_version
            gpu_info['gpu_health'] = data.gpu_health
            gpu_info['gpu_part_number'] = data.gpu_part_number
            gpu_info['gpu_state'] = data.gpu_state
            gpu_info['last_update_time'] = data.last_update_time
            gpu_info['serial_number'] = data.serial_number
        return gpu_info

    def _generate_dpu_info_from_response_data(self, data):
        dpu_info = {}
        dpu_info['sn'] = data.sn
        dpu_info['model'] = data.model
        dpu_info['os_name'] = data.os_name
        dpu_info['health'] = data.health
        return dpu_info


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
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60),
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    if (module.params.get('host_sn')) == "all":
        result = VxRailHosts().get_hosts()
    else:
        result = VxRailHosts().get_specific_hosts()
    if result == 'error':
        module.fail_json(
            msg="Call /Hosts API failed,please see log file /tmp/vxrail_ansible_hosts.log for more error details.")
    vx_facts = {"Hosts_Information": result}
    vx_facts_result = dict(changed=False, Hosts_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
