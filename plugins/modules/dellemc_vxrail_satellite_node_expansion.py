#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_satellite_node_expansion

short_description: Add a satellite node to an existing VxRail Cluster

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.2.0"

description:
- This module will perform a satellite node expansion
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

  folder_id:
    description:
      The specific folder id
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

  hostname:
    description:
      The hostname for the ESX Host.
    required: True
    type: str

  domain_name:
    description:
      The domain name for the ESX Host.
    required: True
    type: str

  root_account:
    description:
      Root account the VxRail root user is registered to
    required: true
    type: str

  root_passwd:
    description:
      The password for the root account
    required: true
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

  mgt_ip:
    description:
      The management IP address for the ESX Host.
    required: True
    type: str

  network_ip:
    description:
      The network IP address for the ESX Host.
    required: True
    type: str

  current_root_password:
    description:
      The root password for the ESX Host.
    required: True
    type: str

  mgt_vlan:
    description:
      The management vlan id for the ESX Host.
    required: True
    type: str

  mgt_netmask:
    description:
      Netmask of the component.
    required: True
    type: str

  mgt_gateway:
    description:
      Gateway of the component.
    required: True
    type: str

  dns_server:
    description:
     An array of dns servers information for the host components
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
    type: str
    default: 5

  ntp_server:
    description:
     An array of ntp servers information for the host components
    required: false
    type: str
    default: ""

  syslog_server:
    description:
     An array of syslog servers information for the host components
    required: false
    type: str
    default: ""

  timeout:
    description:
      Time out value for satellite node expansion, the default value is 1800 seconds
    required: false
    type: int
    default: 1800

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Start a satellite node expansion
    dellemc_vxrail_satellite_node_expansion:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        vxm_version: "{{ vxm_version }}"
        folder_id: "{{ folder_id }}"
        mgt_ip: "{{ mgt_ip }}"
        network_ip: "{{ network_ip }}"
        current_root_password: "{{ current_root_password }}"
        hostname: "{{ hostname }}"
        domain_name: "{{ domain_name }}"
        root_account: "{{ root_account }}"
        root_passwd: "{{ root_passwd }}"
        mgt_account: "{{ mgt_account }}"
        mgt_passwd: "{{ mgt_passwd }}"
        mgt_vlan: "{{ mgt_vlan }}"
        mgt_netmask: "{{ mgt_netmask }}"
        mgt_gateway: "{{ mgt_gateway }}"
        dns_server: "{{ dns_server }}"
        ntp_server: "{{ ntp_server }}"
        syslog_server: "{{ syslog_server }}"
        rack_name: "{{ rack_name }}"
        order_number: "{{ order_number }}"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
expansion_status:
  description: satellite node expansion status summary
  returned: always
  type: dict
  sample: >-
   {
    "NodeExpansion": {
        "request_id": "433d0a61-06e7-4cb8-a1eb-985ab9a8b5dd",
        "status": "COMPLETED"
    }
    "msg": "The satellite node expansion is successful. Please see the /tmp/vxrail_ansible_satellite_node_expansion.log for more details"
   }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_satellite_node_expansion", "/tmp/vxrail_ansible_satellite_node_expansion.log",
                          log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailClusterUrls.cluster_url.format(self.vxm_ip)


class VxRailSatelliteNode():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.vxm_version = module.params.get('vxm_version')
        self.folder_id = module.params.get('folder_id')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.mgt_ip = module.params.get('mgt_ip')
        self.network_ip = module.params.get('network_ip')
        self.current_root_password = module.params.get('current_root_password')
        self.hostname = module.params.get('hostname')
        self.domain_name = module.params.get('domain_name')
        self.root_account = module.params.get('root_account')
        self.root_passwd = module.params.get('root_passwd')
        self.mgt_account = module.params.get('mgt_account')
        self.mgt_passwd = module.params.get('mgt_passwd')
        self.mgt_vlan = module.params.get('mgt_vlan')
        self.mgt_netmask = module.params.get('mgt_netmask')
        self.mgt_gateway = module.params.get('mgt_gateway')
        self.dns_server = module.params.get('dns_server')
        self.ntp_server = module.params.get('ntp_server')
        self.syslog_server = module.params.get('syslog_server')
        self.rack_name = module.params.get('rack_name')
        self.order_number = module.params.get('order_number')
        self.cluster_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.cluster_url.set_host()

        self.mgt_ip_list = self.mgt_ip.split(',')
        self.network_ip_list = self.network_ip.split(',')
        self.current_root_password_list = self.current_root_password.split(',')
        self.hostname_list = self.hostname.split(',')
        self.domain_name_list = self.domain_name.split(',')
        self.root_account_list = self.root_account.split(',')
        self.root_passwd_list = self.root_passwd.split(',')
        self.mgt_account_list = self.mgt_account.split(',')
        self.mgt_passwd_list = self.mgt_passwd.split(',')
        self.mgt_netmask_list = self.mgt_netmask.split(',')
        self.mgt_gateway_list = self.mgt_gateway.split(',')
        self.mgt_vlan_list = self.mgt_vlan.split(',')
        self.dns_server_list = self.dns_server.split(',')
        self.ntp_server_list = self.ntp_server.split(',')
        self.syslog_server_list = self.syslog_server.split(',')
        self.rack_name_list = self.rack_name.split(',')
        self.order_number_list = self.order_number.split(',')

    def validate(self):
        list_all = [len(self.mgt_ip_list), len(self.current_root_password_list), len(self.hostname_list),
                    len(self.domain_name_list),
                    len(self.root_account_list), len(self.root_passwd_list), len(self.mgt_account_list),
                    len(self.mgt_passwd_list),
                    len(self.mgt_netmask_list), len(self.mgt_gateway_list), len(self.mgt_vlan_list),
                    len(self.dns_server_list), len(self.network_ip_list)]
        if self.ntp_server != "":
            list_all.append(len(self.ntp_server_list))
        if self.syslog_server != "":
            list_all.append(len(self.syslog_server_list))
        if self.rack_name != "default-rack":
            list_all.append(len(self.rack_name_list))
            list_all.append(len(self.order_number_list))
        set_len = len(set(list_all))
        if set_len == 1:
            return True
        else:
            return False

    def cancel_expansion(self):
        api_instance = vxrail_ansible_utility.SatelliteNodeExpansionApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # cancel cluster expansion
            api_instance.v1_satellite_node_expansion_cancel_post()
        except ApiException as e:
            LOGGER.error(
                "Exception when calling SatelliteNodeExpansionApi->v1_satellite_node_expansion_cancel_post: %s\n", e)
            return 'error'
        return 'success'

    def start_expansion(self, expansion_json):
        request_body = expansion_json
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SatelliteNodeExpansionApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # start cluster expansion
            response = api_instance.v1_satellite_node_expansion_post(request_body)
        except ApiException as e:
            LOGGER.error("Exception when calling SatelliteNodeExpansionApi->v1_satellite_node_expansion_post: %s\n", e)
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

    def create_validation_json(self):
        ''' validate list of nodes as expansion candidates '''
        validate_json = {}
        validate_json['version'] = self.vxm_version
        validate_json['folder_id'] = self.folder_id
        validate_json['hosts'] = []
        host_num = len(self.mgt_ip_list)
        for index in range(host_num):
            validate_json['hosts'].append(self._create_one_host_section(index))
        vcenter_section = {}
        vcenter_section['username'] = self.vc_admin
        vcenter_section['password'] = self.vc_password
        validate_json['vcenter'] = vcenter_section
        return validate_json

    def _create_one_host_section(self, index):
        host = {}
        host['customer_supplied'] = {"management_ip": self.mgt_ip_list[index],
                                     "current_root_password": self.current_root_password_list[index]}
        host['hostname'] = self.hostname_list[index]
        host['domain_name'] = self.domain_name_list[index]
        accounts = self._create_accounts_section(index)
        host['accounts'] = accounts
        network = self._create_network_section(index)
        host['network'] = network
        host['dns_servers'] = [self.dns_server_list[index]]
        if self.ntp_server != "":
            host['ntp_server'] = [self.ntp_server_list[index]]
        if self.syslog_server != "":
            host['syslog_server'] = [self.syslog_server_list[index]]
        if self.rack_name != "default-rack":
            host['geo_location'] = {}
            host['geo_location'] = {"rack_name": self.rack_name_list[index],
                                    "order_number": int(self.order_number_list[index])}
        return host

    def _create_accounts_section(self, index):
        accounts, manage_account, root_account = {}, {}, {}
        manage_account = {"username": self.mgt_account_list[index], "password": self.mgt_passwd_list[index]}
        root_account = {"username": self.root_account_list[index], "password": self.root_passwd_list[index]}
        accounts['root'] = root_account
        accounts['management'] = manage_account
        return accounts

    def _create_network_section(self, index):
        network, manage_dict = [], {}
        manage_dict['type'] = 'MANAGEMENT'
        manage_dict['ip'] = self.network_ip_list[index]
        manage_dict['vlan'] = int(self.mgt_vlan_list[index])
        manage_dict['netmask'] = self.mgt_netmask_list[index]
        manage_dict['gateway'] = self.mgt_gateway_list[index]
        network.append(manage_dict)
        return network


def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxm_version=dict(required=True),
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        folder_id=dict(required=True),
        mgt_ip=dict(required=True),
        network_ip=dict(required=True),
        current_root_password=dict(required=True, no_log=True),
        hostname=dict(required=True),
        domain_name=dict(required=True),
        root_account=dict(required=True),
        root_passwd=dict(required=True, no_log=True),
        mgt_account=dict(required=True),
        mgt_passwd=dict(required=True, no_log=True),
        mgt_vlan=dict(required=True),
        mgt_netmask=dict(required=True),
        mgt_gateway=dict(required=True),
        rack_name=dict(type='str', default="default-rack"),
        order_number=dict(type='str', default="5"),
        dns_server=dict(required=True),
        ntp_server=dict(type='str', default=""),
        syslog_server=dict(type='str', default=""),
        timeout=dict(type='int', default=30 * 60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    json_validation = VxRailSatelliteNode().validate()
    if not json_validation:
        vx_expansion = {'status': 'FAILED'}
        vx_facts_result = dict(failed=True, NodeExpansion=vx_expansion,
                               msg='The Parameters of hosts are not legal. '
                                   'Please see the /tmp/vxrail_ansible_satellite_node_expansion.log for more details')
        module.exit_json(**vx_facts_result)
    else:
        expansion_status = 0
        expansion_result = 0
        error = 0
        time_out = 0
        time_sleep = 30
        expansion_request_id = 0
        initial_timeout = module.params.get('timeout')
        LOGGER.info('----Start satellite node expansion for host: %s.----',
                    module.params.get('hostname') + "." + module.params.get('domain_name'))
        expansion_json = VxRailSatelliteNode().create_validation_json()
        expansion_request_id = VxRailSatelliteNode().start_expansion(expansion_json)
        if expansion_request_id == 'error':
            module.fail_json(
                msg="Expansion request id is not returned. Please see the /tmp/vxrail_ansible_satellite_node_expansion.log for more details")
        else:
            LOGGER.info('Satellite_node_expansion: VxRail task_ID: %s.', expansion_request_id)
            while expansion_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
                expansion_response = VxRailSatelliteNode().get_request_status(expansion_request_id)
                expansion_status = expansion_response.state
                expansion_result = VxRailSatelliteNode().get_request_info(expansion_response)
                LOGGER.info('Expansion_Task: status: %s.', expansion_status)
                LOGGER.info('Expansion_Task: details: %s.', expansion_result)
                LOGGER.info('Expansion Task: sleeping %s seconds...', time_sleep)
                time.sleep(time_sleep)
                time_out = time_out + time_sleep
            if expansion_status == 'COMPLETED':
                LOGGER.info("-----Expansion Completed-----")
            else:
                LOGGER.info("------Expansion Failed-----")
                LOGGER.info("------Expansion Cancelling-----")
                cancel_response = VxRailSatelliteNode().cancel_expansion()
                if cancel_response == 'error':
                    LOGGER.info("------Expansion Cancellation Failed-----")
                else:
                    LOGGER.info("------Expansion Cancelled-----")
                hosts = eval(expansion_result[0].get('extension')).get('hosts')
                error = hosts[0].get('errors')
                vx_expansion = {'request_id': expansion_request_id, 'response_error': error}
                vx_facts_result = dict(failed=True, NodeExpansion=vx_expansion,
                                       msg='The expansion has failed. Please see the /tmp/vxrail_ansible_satellite_node_expansion.log for more details')
                module.exit_json(**vx_facts_result)
        vx_expansion = {'status': expansion_status, 'request_id': expansion_request_id}
        vx_facts_result = dict(changed=True, NodeExpansion=vx_expansion,
                               msg="The expansion is successful. Please see the /tmp/vxrail_ansible_satellite_node_expansion.log for more details")
        module.exit_json(**vx_facts_result)


if __name__ == '__main__':
    main()
