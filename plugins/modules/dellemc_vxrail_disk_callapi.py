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
This module will collect VxRail Node disk details at cluster level, as well as can retrieve information about a specific disk.
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
      Time out value for the HTTP session to connect to the REST API
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

def byte_to_json(body):
    ''' conversion of http content to json format '''
    return json.loads(body.decode(chardet.detect(body)["encoding"]))

# Configurations
LOG_FILE_NAME = "/tmp/vxraildisk.log"
LOG_FORMAT = CustomLogFormatter()

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

# file output
FILE_HANDLER = logging.FileHandler(LOG_FILE_NAME)
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(LOG_FORMAT)
LOGGER.addHandler(FILE_HANDLER)

class VxrailDiskUrls():
    disks_url = 'https://{}/rest/vxm/v1/disks'
    specific_disk_url = 'https://{}/rest/vxm/v1/disks/{}'

    def __init__(self, vxm_ip, disk_sn):
        self.vxm_ip = vxm_ip
        self.disk_sn = disk_sn

    def get_disks(self):
        return VxrailDiskUrls.disks_url.format(self.vxm_ip)

    def get_specific_disk(self):
        return VxrailDiskUrls.specific_disk_url.format(self.vxm_ip, self.disk_sn)

class VxRailDisk():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.admin = module.params.get('vcadmin')
        self.password = module.params.get('vcpasswd')
        self.disk_sn = module.params.get('disk_sn')
        self.disk_url = VxrailDiskUrls(self.vxm_ip, self.disk_sn)
        response = ''

    def get_disks(self):
        disks = {}
        disklist = []
        try:
            response = requests.get(url=self.disk_url.get_disks(),
                                    verify=False,
                                    auth=(self.admin, self.password),
                                    )
            LOGGER.info("Response: %s", response.content)
            response.raise_for_status()
        except HTTPError as http_err:
            LOGGER.error("HTTP error %s request to VxRail Manager %s", http_err, self.vxm_ip)
            return 'error'
        except Exception as ERR:
            LOGGER.error(' %s Cannot connect to VxRail Manager %s', ERR, self.vxm_ip)
            return 'error'

        if response.status_code == 200:
            data = byte_to_json(response.content)
            LOGGER.info("DATA: %s", data)
            if not data:
                return "No available hosts"
            for i in range(len(data)):
                disks['sn'] = data[i].get('sn')
                disks['disk_type'] = data[i].get('disk_type')
                disks['enclosure'] = data[i].get('enclosure')
                disks['bay'] = data[i].get('bay')
                disks['slot'] = data[i].get('slot')
                disks['missing'] = data[i].get('missing')
                disks['capacity'] = data[i].get('capacity')
                disklist.append(dict(disks.items()))
            LOGGER.info("disklist: %s", disklist)
            return disklist

    def get_specific_disk(self):
        disks = {}
        disklist = []
        try:
            response = requests.get(url=self.disk_url.get_specific_disk(),
                                    verify=False,
                                    auth=(self.admin, self.password),
                                    )
            response.raise_for_status()
        except HTTPError as http_err:
            LOGGER.error("HTTP error %s request to VxRail Manager %s", http_err, self.vxm_ip)
            return 'error'
        except Exception as ERR:
            LOGGER.error(' %s Cannot connect to VxRail Manager %s', ERR, self.vxm_ip)
            return 'error'

        if response.status_code == 200:
            data = byte_to_json(response.content)
            if not data:
                return "No available hosts"
            return data

def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
            name=dict(required=False),
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
    else:
        result = VxRailDisk().get_specific_disk()
        LOGGER.info(result)
    if result == 'error':
        module.fail_json(msg="VxRail Manager is unreachable")

    vx_facts = {'disks': result}
    vx_facts_result = dict(changed=False, ansible_facts=vx_facts)
    module.exit_json(**vx_facts_result)

if __name__ == '__main__':
    main()
