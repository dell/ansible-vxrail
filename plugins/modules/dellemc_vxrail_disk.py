#!/usr/bin/python3
# Copyright: (c) 2021, Gao Hongmei <s.gao@dell.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
author:  Dell EMC VxRail Ansible Team (@gaohongmei) <s.gao@dell.com>
module: dell_vxrail_disk
short_description: Gathers information about disks attached to given cluster
description: 
This module will  get information of all disks in the cluster or one disk specified by serial number.
options:

  vxmip:
    description:
      The IP address of the VxRail Manager System
    required: true

  vcadmin:
    description:
      Administrative account of the vCenter Server the VxRail Manager is registered to
    required: true

  vcpasswd:
    description:
      The password for the administrator account provided in vcadmin
    required: true
  disk_sn:
    description:
      Optional value to retrieve specific disk information
    required: false
  Timeout:
    description:
      Time out value for the HTTP session to connect to the REST API, the default value is 10 seconds
    required: false

'''

EXAMPLES = """
  - name: Collect Disk Info from VxRail Cluster
    vxrail-disk-info:
      vxmip: " {{ vxm }}"
      vcadmin: "{{ vcadmin }}"
      vcpasswd: "{{ vcpasswd }}"

  - name: Collect Specific Disk Info
    vxrail-disk-info:
      vxmip: " {{ vxm }}"
      vcadmin: "{{ vcadmin }}"
      vcpasswd: "{{ vcpasswd }}"
      disk_sn: "{{ disk_sn }}"
"""

RETURN = """
host_disk_info:
  description: list of information for all disks attached to each ESXi host
  returned: always
  type: list
  sample: >-
  [
    {
        "id": "S47VNA0M300380",
        "sn": "S47VNA0M300380",
        "guid": "NVMe____Dell_Express_Flash_PM1725b_1.6TB_SFF____032C009123382500",
        "disk_type": "SSD",
        "protocol": "PCIe",
        "enclosure": 0,
        "bay": 1,
        "slot": 20,
        "missing": false,
        "capacity": "1.46TB"
    },
    {
        "id": "Y9T0A06BTNUF",
        "sn": "Y9T0A06BTNUF",
        "guid": "58ce38ee20c98849",
        "disk_type": "SSD",
        "protocol": "SAS",
        "enclosure": 0,
        "bay": 1,
        "slot": 0,
        "missing": false,
        "capacity": "1.75TB"
    }
  ]	
"""

import json
import logging
import requests
import chardet
import urllib3
from requests.exceptions import HTTPError
from ansible.module_utils.basic import AnsibleModule
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import ssl

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class CustomLogFormatter(logging.Formatter):
    ''' Logging class for method '''
    info_fmt = "%(asctime)s [%(levelname)s]\t%(message)s"
    debug_fmt = "%(asctime)s [%(levelname)s]\t%(pathname)s:%(lineno)d\t%(message)s"

    def __init__(self, fmt="%(asctime)s [%(levelname)s]\t%(pathname)s:%(lineno)d\t%(message)s"):
        logging.Formatter.__init__(self, fmt)

    def format(self, record):
        if record.levelno == logging.INFO:
            self._fmt = CustomLogFormatter.info_fmt
            # python 3 compatibility
            if hasattr(self, '_style'):
                self._style._fmt = CustomLogFormatter.info_fmt
        else:
            self._fmt = CustomLogFormatter.debug_fmt
            # python 3 compatibility
            if hasattr(self, '_style'):
                self._style._fmt = CustomLogFormatter.debug_fmt
        result = logging.Formatter.format(self, record)
        return result

# Configurations
LOG_FILE_NAME = "/tmp/vxrail_ansible.log"
LOG_FORMAT = CustomLogFormatter()

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

# file output
FILE_HANDLER = logging.FileHandler(LOG_FILE_NAME)
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(LOG_FORMAT)
LOGGER.addHandler(FILE_HANDLER)

class VxrailDiskUrls():
    disks_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailDiskUrls.disks_url.format(self.vxm_ip)

class VxRailDisk():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.admin = module.params.get('vcadmin')
        self.password = module.params.get('vcpasswd')
        self.disk_sn = module.params.get('disk_sn')
        self.disk_url = VxrailDiskUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = swagger_client.Configuration()
        self.configuration.username = self.admin
        self.configuration.password = self.password
        self.configuration.verify_ssl = False
        self.configuration.host = self.disk_url.set_host()
        LOGGER.info("host url: %s", self.configuration.host)
        response = ''

    def get_disks(self):
        disks = {}
        disklist = []
        # create an instance of the API class
        api_instance = swagger_client.DiskDriveInformationApi(swagger_client.ApiClient(self.configuration))
        try:
            # get all disks information in a cluster
            response = api_instance.v1_disks_get()
            LOGGER.info("Response: %s", response)
        except ApiException as e:
            LOGGER.error("Exception when calling DiskDriveInformationApi->v1_disks_get: %s\n" % e)
            return 'error'
        data = response
        LOGGER.info("disks len: %s", len(data))
        if not data:
            return "No available hosts"
        for i in range(len(data)):
            disks['sn'] = data[i].sn
            disks['disk_type'] = data[i].disk_type
            disks['enclosure'] = data[i].enclosure
        #    disks['bay'] = data[i].bay
            disks['slot'] = data[i].slot
            disks['missing'] = data[i].missing
            disks['capacity'] = data[i].capacity
            disks['id'] = data[i].id
            disklist.append(dict(disks.items()))
        return disklist

    def get_specific_disk(self):
        disks = {}
        disklist = []
        # create an instance of the API class
        api_instance = swagger_client.DiskDriveInformationApi(swagger_client.ApiClient(self.configuration))
        try:
            # get specific disk information by serial number in a cluster
            response = api_instance.v1_disks_disk_sn_get(self.disk_sn)
            LOGGER.info("Response: %s", response)
        except ApiException as e:
            LOGGER.error("Exception when calling DiskDriveInformationApi->v1_disks_get: %s\n" % e)
            return 'error'
        data = response
        if not data:
            return "No available hosts"
        disks['sn'] = data.sn
        disks['disk_type'] = data.disk_type
        disks['enclosure'] = data.enclosure
        # disks['bay'] = data[i].bay
        disks['slot'] = data.slot
        disks['missing'] = data.missing
        disks['capacity'] = data.capacity
        disks['id'] = data.id
        disklist.append(dict(disks.items()))
        return disklist

def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
            vxmip=dict(required=True),
            vcadmin=dict(required=True),
            vcpasswd=dict(required=True, no_log=True),
            disk_sn=dict(type='str', default="all"),
            timeout=dict(type='int', default=10),
            )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    if (module.params.get('disk_sn')) == "all":
        result = VxRailDisk().get_disks()
        LOGGER.info("Result:%s", result)
    else:
        result = VxRailDisk().get_specific_disk()
        LOGGER.info("Result:%s", result)
    if result == 'error':
        module.fail_json(msg="Call disk API failed,please see log file for more error details")

    vx_facts = {'disks': result}
    vx_facts_result = dict(changed=False, ansible_facts=vx_facts)
    module.exit_json(**vx_facts_result)

if __name__ == '__main__':
    main()
