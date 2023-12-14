#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_cluster_expansion

short_description: Add a node discovered by LoudMouth to an existing VxRail Cluster

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.4.0"

description:
- This module will validate a L2 cluster expansion, perform a L2 cluster expansion
  based on the provided expansion specification and query status.
options:
  vxm_version:
    description: The version of the VxRail Manager System.
    required: true
    type: str

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

  host_psnt:
    description:
      The psnt number for the ESX Host.
    required: True
    type: str

  hostname:
    description:
      The name for the ESX Host.
    required: True
    type: str

  mgt_ip:
    description:
      The management IP address for the ESX Host.
    required: True
    type: str

  vsan_ip:
    description:
      The vsan IP address for the ESX Host.
    required: True
    type: str

  vmotion_ip:
    description:
      The vmotion IP address for the ESX Host.
    required: True
    type: str

  mgt_ipv6:
    description:
      The management IPv6 address for the ESX Host.
    required: True
    type: str

  vsan_ip:
    description:
      The vsan IPv6 address for the ESX Host.
    required: True
    type: str

  vmotion_ip:
    description:
      The vmotion IPv6 address for the ESX Host.
    required: True
    type: str

  mgt_account:
    description:
      Management account the VxRail Manager is registered to
    required: true
    type: str

  mgt_passwd:
    description:
      The password for the Management account
    required: true
    type: str

  root_passwd:
    description:
      The password for the root account
    required: true
    type: str

  rack_name:
    description:
     The name of the rack that houses the host,the default value is default-rack
    required: false
    type: str
    default: default-rack

  order_number:
    description:
      The position of the node in the rack,the default value is 5
    required: false
    type: int
    default: 5

  maintenance_mode:
    description:
       Whether the hosts remain in maintenance mode after being added to the cluster, the default value is false
    required: false
    type: bool
    default: FALSE

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for cluster expansion, the default value is 1800 seconds
    required: false
    type: int
    default: 1800

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Start a cluster expansion
    dellemc_vxrail_cluster_expansion:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        vxm_version: "{{ vxm_version }}"
        host_psnt: "{{ host_psnt }}"
        hostname: "{{ hostname }}"
        mgt_account: "{{ mgt_account }}"
        mgt_passwd: "{{ mgt_passwd }}"
        root_passwd: "{{ root_passwd }}"
        mgt_ip: "{{ mgt_ip }}"
        vsan_ip: "{{ vsan_ip }}"
        vmotion_ip: "{{ vmotion_ip }}"
        mgt_ipv6: "{{ mgt_ipv6 }}"
        vsan_ipv6: "{{ vsan_ipv6 }}"
        vmotion_ipv6: "{{ vmotion_ipv6 }}"
        rack_name: "{{ rack_name }}"
        order_number: "{{ order_number }}"
        maintenance_mode : "{{ maintenance_mode }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
expansion_status:
  description: cluster expansion status summary
  returned: always
  type: dict
  sample: >-
   {
    "NodeCompatiblityValidation": {
        "request_id": "2ce09bde-d987-4fff-8f90-6fc430e2bfc3",
        "status": "COMPLETED"
    },
    "NodeExpansion": {
        "request_id": "433d0a61-06e7-4cb8-a1eb-985ab9a8b5dd",
        "status": "COMPLETED"
    }
    "msg": "The cluster expansion is successful. Please see the /tmp/vxrail_ansible_cluster_expansion.log for more details"
   }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_cluster_expansion", "/tmp/vxrail_ansible_cluster_expansion.log", log_devel=logging.DEBUG)
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
        self.vxm_version = module.params.get('vxm_version')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.host_psnt = module.params.get('host_psnt')
        self.hostname = module.params.get('hostname')
        self.mgt_account = module.params.get('mgt_account')
        self.mgt_passwd = module.params.get('mgt_passwd')
        self.mgt_ip = module.params.get('mgt_ip')
        self.mgt_ipv6 = module.params.get('mgt_ipv6')
        self.vmotionip = module.params.get('vmotion_ip')
        self.vmotionipv6 = module.params.get('vmotion_ipv6')
        self.vsanip = module.params.get('vsan_ip')
        self.vsanipv6 = module.params.get('vsan_ipv6')
        self.rackname = module.params.get('rack_name')
        self.order_number = module.params.get('order_number')
        self.root_passwd = module.params.get('root_passwd')
        self.mm = module.params.get('maintenance_mode')
        self.api_version_number = module.params.get('api_version_number')
        self.cluster_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.cluster_url.set_host()
        # Added for auto-version detection
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response_validate(self, api_instance, module_path, node_json):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute (ex: v1_cluster_expansion_validate_post)
        call_string = self.api_version_string + '_cluster_expansion_validate_post'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_cluster_expansion_validate_post = getattr(api_instance, call_string)
        request_body = node_json
        return api_cluster_expansion_validate_post(request_body)

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response_expansion(self, api_instance, module_path, node_json):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute (ex: v1_cluster_expansion_post)
        call_string = self.api_version_string + '_cluster_expansion_post'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_cluster_expansion_post = getattr(api_instance, call_string)
        request_body = node_json
        return api_cluster_expansion_post(request_body)

    def start_validation(self, validate_json):
        request_body = validate_json
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.ClusterExpansionApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # start cluster expansion validation
            response = self.get_versioned_response_validate(api_instance, "Post /cluster/expansion/validate", request_body)
        except ApiException as e:
            LOGGER.error("Exception when calling ClusterExpansionApi->%s_cluster_expansion_validate_post: %s\n", self.api_version_string, e)
            return 'error'
        job_id = response.request_id
        return job_id

    def start_expansion(self, expansion_json):
        request_body = expansion_json
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.ClusterExpansionApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # start cluster expansion
            response = self.get_versioned_response_expansion(api_instance, "/cluster/expansion", request_body)
        except ApiException as e:
            LOGGER.error("Exception when calling ClusterExpansionApi->%s_cluster_expansion_post: %s\n", self.api_version_string, e)
            return 'error'
        job_id = response.request_id
        return job_id

    def get_request_status(self, request_id):
        job_id = request_id
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.RequestStatusApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = api_instance.v1_request_id_get(job_id)
        except ApiException as e:
            LOGGER.error("Exception when calling v1_requests_id_get: %s\n", e)
            return 'error'
        return response

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

    def get_request_info(self, response):
        statusInfo = {}
        statusInfolist = []
        data = response
        statusInfo['id'] = data.id
        statusInfo['state'] = data.state
        statusInfo['owner'] = data.owner
        statusInfo['progress'] = data.progress
        statusInfo['extension'] = data.extension
        statusInfo['start_time'] = data.start_time
        statusInfo['end_time'] = data.end_time
        statusInfolist.append(dict(statusInfo.items()))
        return statusInfolist

    def _create_one_host_section(self):
        host = {}
        host['host_psnt'] = self.host_psnt
        host['hostname'] = self.hostname
        accounts = self._create_accounts_section()
        host['accounts'] = accounts
        network = self._create_network_section()
        host['network'] = network
        host['maintenance_mode'] = self.mm
        host['geo_location'] = {}
        host['geo_location'] = {"rack_name": self.rackname, "order_number": self.order_number}
        nic_mapping = self._create_nicmapping_section()
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
        vsan_dict['type'] = 'VSAN'
        vmotion_dict['type'] = 'VMOTION'

        if self.mgt_ip:
          manage_dict['ip'] = self.mgt_ip
          vsan_dict['ip'] = self.vsanip
          vmotion_dict['ip'] = self.vmotionip

        if self.mgt_ipv6:
          manage_dict['ipv6'] = self.mgt_ipv6
          vsan_dict['ipv6'] = self.vsanipv6
          vmotion_dict['ipv6'] = self.vmotionipv6

        network.append(manage_dict)
        network.append(vsan_dict)
        network.append(vmotion_dict)

        return network

    def _create_nicmapping_section(self):
        LOGGER.info('configuration: %s.', self.configuration)
        nic_mappings = []
        api_instance = vxrail_ansible_utility.HostInformationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # get nic mapping
            response = api_instance.v1_system_cluster_hosts_pnics_get()
        except ApiException as e:
            LOGGER.error("Exception when calling ClusterExpansionApi->query_cluster_configured_host_info: %s\n", e)
            return 'error'
        system_cluster_hosts = response
        vmnic_name = system_cluster_hosts[0].vmnics
        for i in range(len(vmnic_name)):
            nic_mappings.append({
                "vds_name": vmnic_name[i].vds_name, "name": vmnic_name[i].uplink_name,
                "physical_nic": vmnic_name[i].vmnic_name
            })
        return nic_mappings


def main():
    ''' Entry point into execution flow '''
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
        mgt_ip=dict(required=False),
        vsan_ip=dict(required=False),
        vmotion_ip=dict(required=False),
        mgt_ipv6=dict(required=False),
        vsan_ipv6=dict(required=False),
        vmotion_ipv6=dict(required=False),
        rack_name=dict(type='str', default="default-rack"),
        order_number=dict(type='int', default=5),
        maintenance_mode=dict(type='bool', default=False),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=30 * 60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_together=[
            ('mgt_ip', 'vsan_ip', 'vmotion_ip'),
            ('mgt_ipv6', 'vsan_ipv6', 'vmotion_ipv6')
        ],
    )
    validation_status = 0
    expansion_status = 0
    validation_result = 0
    expansion_result = 0
    error = 0
    time_out = 0
    validation_request_id = 0
    expansion_request_id = 0
    initial_timeout = module.params.get('timeout')
    LOGGER.info('----Start cluster expansion validation for host: %s.----', module.params.get('host_psnt'))
    validation_json = VxRailCluster().create_validation_json()
    request_body = validation_json
    validation_request_id = VxRailCluster().start_validation(request_body)
    LOGGER.info('Node_validation: VxRail task_ID: %s.', validation_request_id)
    if validation_request_id == "error":
        module.fail_json(
            msg="validation request id is not returned. Please see the /tmp/vxrail_ansible_cluster_expansion.log for more details")

    while validation_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        validation_response = VxRailCluster().get_request_status(validation_request_id)
        validation_status = validation_response.state
        validation_result = VxRailCluster().get_request_info(validation_response)
        LOGGER.info('Validation_Task: status: %s.', validation_status)
        LOGGER.info('Validation_Task: details: %s.', validation_result)
        LOGGER.info("Validation Task: Sleeping 30 seconds...")
        time.sleep(30)
        time_out = time_out + 30
    hosts = eval(validation_result[0].get('extension')).get('hosts')
    error = hosts[0].get('errors')

    if validation_status == 'COMPLETED' and not error:
        LOGGER.info("-------Validation Completed------")
        LOGGER.info('----Start cluster expansion for host: %s.----', module.params.get('host_psnt'))
        expansion_json = validation_json
        expansion_request_id = VxRailCluster().start_expansion(expansion_json)
        LOGGER.info('Cluster_expansion: VxRail task_ID: %s.', expansion_request_id)
        while expansion_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
            expansion_response = VxRailCluster().get_request_status(expansion_request_id)
            expansion_status = expansion_response.state
            expansion_result = VxRailCluster().get_request_info(expansion_response)
            LOGGER.info('Expansion_Task: status: %s.', expansion_status)
            LOGGER.info('Expansion_Task: details: %s.', expansion_result)
            LOGGER.info("Expansion Task: sleeping 30 seconds...")
            time.sleep(30)
            time_out = time_out + 30
        if expansion_status == 'COMPLETED':
            LOGGER.info("-----Expansion Completed-----")
        else:
            LOGGER.info("------Expansion Failed-----")
            hosts = eval(expansion_result[0].get('extension')).get('hosts')
            error = hosts[0].get('errors')
            vx_expansion = {'request_id': expansion_request_id, 'response_error': error}
            vx_facts_result = dict(failed=True, NodeExpansion=vx_expansion,
                                   msg='The node expansion has failed. Please see the /tmp/vxrail_ansible_cluster_expansion.log for more details')
            module.exit_json(**vx_facts_result)
    else:
        LOGGER.info("------Validation Failed-----")
        vx_validation = {'request_id': validation_request_id, 'response_error': error}
        vx_facts_result = dict(failed=True, NodeCompatiblityValidation=vx_validation,
                               msg="The node validaiton has failed. Please see the /tmp/vxrail_ansible_cluster_expansion.log for more details")
        module.exit_json(**vx_facts_result)
    vx_validation = {'status': validation_status, 'request_id': validation_request_id}
    vx_expansion = {'status': expansion_status, 'request_id': expansion_request_id}
    vx_facts_result = dict(changed=True, NodeExpansion=vx_expansion, NodeCompatiblityValidation=vx_validation,
                           msg="The cluster expansion is successful. Please see the /tmp/vxrail_ansible_cluster_expansion.log for more details")
    module.exit_json(**vx_facts_result)


if __name__ == '__main__':
    main()
