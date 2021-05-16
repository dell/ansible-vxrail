#!/usr/bin/python3
# Copyright: (c) 2021, Gao Hongmei <s.gao@dell.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type



ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
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


import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
import json


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
LOG_FILE_NAME = "/tmp/vxrail_ansible_nodevalidation.log"
LOG_FORMAT = CustomLogFormatter()

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

# file output
FILE_HANDLER = logging.FileHandler(LOG_FILE_NAME)
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(LOG_FORMAT)
LOGGER.addHandler(FILE_HANDLER)

logger = logging.getLogger(__name__)
class VxrailClusterUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailClusterUrls.cluster_url.format(self.vxm_ip)

class VxRailCluster():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.vxm_version = module.params.get('vxm_version')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.host_psnt = module.params.get('host_psnt')
        self.hostname = module.params.get('hostname')
        self.mgt_account = module.params.get('mgt_account')
        self.mgt_passwd = module.params.get('mgt_passwd')
        self.mgt_ip = module.params.get('mgt_ip')
        self.vmotionip = module.params.get('vmotion_ip')
        self.vsanip = module.params.get('vsan_ip')
        self.rackname = module.params.get('rack_name')
        self.order_number = module.params.get('order_number')
        self.root_passwd = module.params.get('root_passwd')
        self.is_four_port = module.params.get('is_four_port')
        self.cluster_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.cluster_url.set_host()
        self.configuration.logger_file = "/tmp/vxrail_ansible_addnode1.log"
        self.configuration.debug = True
        response = ''

    def start_validation(self, validate_json):
        request_body = validate_json
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.ClusterExpansionApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # get all disks information in a cluster
            response = api_instance.v1_cluster_expansion_validate_post(request_body)
        except ApiException as e:
            logging.error("Exception when calling ClusterExpansionApi->v1_cluster_expansion_validate_post: %s\n" % e)
            return 'error'
        self.configuration.logger.debug("Response: %s", response)
        job_id = response.request_id
        return job_id

    def get_request_status(self, request_id):
        job_id = request_id
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.ClusterShutdownApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = api_instance.v1_requests_id_get(job_id)
            LOGGER.info('get request_id status response: %s.', response)
        except ApiException as e:
            logging.error("Exception when calling v1_requests_id_get: %s\n" % e)
            return 'error'
        status = response.state
        return status

    def create_validation_json(self):
        ''' validate list of nodes as expansion candidates '''
        validate_json = {}
        validate_json['version'] = self.vxm_version
        vcenter_section = {}
        vcenter_section['username'] = self.vc_admin
        vcenter_section['password'] = self.vc_password
        validate_json['vcenter'] = vcenter_section
        validate_json['hosts'] = []
        validate_json['hosts'].append(self._create_one_host_section())
        return validate_json

    def _create_one_host_section(self):
        host = {}
        host['host_psnt'] = self.host_psnt
        host['hostname'] = self.hostname
        accounts = self._create_accounts_section()
        host['accounts'] = accounts
        network = self._create_network_section()
        host['network'] = network
        host['geo_location'] = {}
        host['geo_location'] = {"rack_name" : self.rackname, "order_number" : self.order_number}
        nic_mapping = self._create_nicmapping_section(self.is_four_port)
        host['nic_mappings'] = nic_mapping
        return host

    def _create_accounts_section(self):
        accounts, manage_account, root_account = {}, {}, {}
        manage_account = {"username": self.mgt_account, "password": self.mgt_passwd}
        root_account = {"username": "root", "password": self.root_passwd}
        accounts['root'] = root_account
        accounts['management'] = manage_account
        return accounts

    def _create_network_section(self):
        network, manage_dict, vsan_dict, vmotion_dict = [], {}, {}, {}
        manage_dict['type'] = 'MANAGEMENT'
        manage_dict['ip'] = self.mgt_ip
        network.append(manage_dict)
        vsan_dict['type'] = 'VSAN'
        vsan_dict['ip'] = self.vsanip
        network.append(vsan_dict)
        vmotion_dict['type'] = 'VMOTION'
        vmotion_dict['ip'] = self.vmotionip
        network.append(vmotion_dict)
        return network

    def _create_nicmapping_section(self,is_four_port):
        four_port_sign = is_four_port
        vds_name = "VMware HCIA Distributed Switch"
        if four_port_sign:
            nic_mappings = [{"vds_name": vds_name, "name": "uplink1", "physical_nic": "vmnic0"},
                            {"vds_name": vds_name, "name": "uplink2", "physical_nic": "vmnic1"},
                            {"vds_name": vds_name, "name": "uplink3", "physical_nic": "vmnic2"},
                            {"vds_name": vds_name, "name": "uplink4", "physical_nic": "vmnic3"}]
            return nic_mappings

        else:
            nic_mappings = [{"vds_name": vds_name, "name": "uplink1", "physical_nic": "vmnic0"},
                            {"vds_name": vds_name, "name": "uplink2", "physical_nic": "vmnic1"}]

            return nic_mappings


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
            vxm_version=dict(required=True),
            vxmip=dict(required=True),
            vcadmin=dict(required=True),
            vcpasswd=dict(required=True, no_log=True),
            host_psnt=dict(required=True),
            hostname=dict(required=True),
            mgt_account=dict(required=True),
            mgt_passwd=dict(required=True, no_log=True),
            root_passwd=dict(required=True, no_log=True),
            mgt_ip=dict(required=True),
            vsan_ip=dict(required=True),
            vmotion_ip=dict(required=True),
            rack_name=dict(required=True),
            order_number=dict(required=True),
            is_four_port=dict(type='bool', default=True),
            maintenance_mode=dict(type='bool', default=False),
            timeout=dict(type='int', default=10),
            )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    validation_status = 0
    validation_json = VxRailCluster().create_validation_json()
    #request_body = json.dumps(validation_json)
    request_body = validation_json
    LOGGER.info('validation_json: %s.', request_body)
    validation_request_id = VxRailCluster().start_validation(request_body)
    LOGGER.info('node_check: VxRail request id: %s.', validation_request_id)
    if validation_request_id == "error":
        module.fail_json(
            msg="validation request id is not returned. Please see the /tmp/vxrail_ansilbe.log for more details")
    #validation_request_id= "d08ac804-60b3-410f-8308-ab134388ada8"
    # validation_status = VxRailCluster().get_request_status(validation_request_id)
    # LOGGER.info('validation_status: status: %s.', validation_status)
    while validation_status not in ('COMPLETED', 'FAILED'):
        validation_status = VxRailCluster().get_request_status(validation_request_id)
        LOGGER.info('validation_status: status: %s.', validation_status)
        LOGGER.info("Validation Task: Sleeping 30 seconds...")
        time.sleep(30)

    if validation_status == 'COMPLETED':
        #expansion_json = VxRailCluster().create_validation_json()
        # hexp_json = json.dumps(expansion_json)
        LOGGER.info("Validation Completed")
        #expansion_requst_id = VxRailCluster().start_expansion(expansion_json)
        #LOGGER.info('Cluster_expansion: VxRail task_ID: %s.', task_id)
        # while expansion_status not in ('COMPLETED', 'FAILED'):
        #     LOGGER.info("cluster_expansion: sleeping 60 seconds...")
        #     time.sleep(60)
        #expansion_status = VxRailCluster().get_request_status()(expansion_requst_id)
            #LOGGER.info('cluster_expansion: track_expansion status: %s', expansion_status)
    else:
        module.fail_json(
            msg="The node validaiton has failed. Please see the /tmp/vxrail_ansilbe.log for more details")

    vx_facts = {'expansion_status': validation_status}
    vx_facts_result = dict(changed=False, ansible_facts=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == '__main__':
    main()
