#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: dellemc_vxrail_cluster_rmhost_v1

short_description: Remove a host from the cluster

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.1.0"

description:
- This module will Remove a host from the cluster.
options:
  vxmip:
    description:
      The IP address of the VxRail Manager System
    required: True
    type: str

  host_sn:
    description:
      Serial number of the host to be removed
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

  vc_root_account:
    description:
      root account of the vCenter Server the VxRail Manager is registered to
    required: true
    type: str

  vc_root_passwd:
    description:
      The password for the root account provided in vcroot
    required: true
    type: str

  timeout:
    description:
      Time out value for Day1 bring up, the default value is 1800 seconds
    required: false
    type: int
    default: 1800

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
- name: Remove a node
  dellemc_vxrail_cluster_rmhost_v1:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        host_sn: "{{ host_sn }}"
        vc_root_account: "{{ vc_root_account }}"
        vc_root_passwd: "{{ vc_root_passwd }}"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
Remove_Node_status:
  description: Node Removal status summary
  returned: always
  type: dict
  sample: >-
   {
    "Remove_Node": {
        "request_id": "2ce09bde-d987-4fff-8f90-6fc430e2bfc3",
        "status": "COMPLETED"
    }
    "msg": "Removing Node is successful. Please see the /tmp/vxrail_ansible_rmnode.log for more details"
   }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils
LOG_FILE_NAME = "/tmp/vxrail_ansible_rmnode.log"
LOGGER = utils.get_logger("dellemc_vxrail_cluster_rmhost_v1", LOG_FILE_NAME, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailVXMUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailVXMUrls.vxm_url.format(self.vxm_ip)


class VxRailRemoveHost():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.host_sn = module.params.get('host_sn')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.vc_root_account = module.params.get('vc_root_account')
        self.vc_root_passwd = module.params.get('vc_root_passwd')
        self.vxm_url = VxrailVXMUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.vxm_url.set_host()

    def create_removal_json(self):
        ''' removal node json '''
        node_json = {}
        node_json['serial_number'] = self.host_sn
        vc_admin_dict = {}
        vc_admin_dict['username'] = self.vc_admin
        vc_admin_dict['password'] = self.vc_password
        vcsa_root_dict = {}
        vcsa_root_dict['username'] = self.vc_root_account
        vcsa_root_dict['password'] = self.vc_root_passwd
        node_json['vc_admin_user'] = vc_admin_dict
        node_json['vcsa_root_user'] = vcsa_root_dict
        return node_json

    def remove_host(self, node_json):
        request_body = node_json
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.HostRemovalApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # start Node Removal
            response = api_instance.v1_cluster_remove_host_post(request_body)
        except ApiException as e:
            LOGGER.error("Exception when calling HostRemovalApi->v1_cluster_remove_host_post: %s\n", e)
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
        statusInfo['owner'] = data.owner
        statusInfo['state'] = data.state
        statusInfo['progress'] = data.progress
        statusInfo['error'] = data.error
        statusInfo['step'] = data.step
        statusInfo['extension'] = data.extension
        statusInfo['start_time'] = data.start_time
        statusInfo['end_time'] = data.end_time
        statusInfolist.append(dict(statusInfo.items()))
        return statusInfolist


def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        host_sn=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        vc_root_account=dict(required=True),
        vc_root_passwd=dict(required=True, no_log=True),
        timeout=dict(type='int', default=30 * 60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    rmnode_status = 0
    rmnode_result = 0
    error = 0
    time_out = 0
    initial_timeout = module.params.get('timeout')
    LOGGER.info('----Start to remove node: %s.----', module.params.get('host_sn'))
    removal_json = VxRailRemoveHost().create_removal_json()
    request_body = removal_json
    rmnode_request_id = VxRailRemoveHost().remove_host(request_body)
    LOGGER.info('Remove_Node: VxRail task_ID: %s.', rmnode_request_id)
    if rmnode_request_id == "error":
        module.fail_json(
            msg="remove_node request id is not returned. Please see the /tmp/vxrail_ansible_rmnode.log for more details")

    while rmnode_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        removal_response = VxRailRemoveHost().get_request_status(rmnode_request_id)
        rmnode_status = removal_response.state
        rmnode_result = VxRailRemoveHost().get_request_info(removal_response)
        LOGGER.info('Node_Removal_Task: status: %s.', rmnode_status)
        LOGGER.info('Node_Removal_Task: details: %s.', rmnode_result)
        LOGGER.info("Node_Removal_Task: Sleeping 30 seconds...")
        time.sleep(30)
        time_out = time_out + 30
    if rmnode_result[0].get('error') is not None:
        error = eval(rmnode_result[0].get('error')).get('detail')
    if rmnode_status == 'COMPLETED' and not error:
        LOGGER.info("-------The Node has been successfully removed-----")
    else:
        LOGGER.info("------Removing Node Failed-----")
        LOGGER.info('----Failed reason is : %s.----', error)
        vx_rmnode = {'request_id': rmnode_request_id, 'response_error': error}
        vx_facts_result = dict(failed=True, Remove_Node=vx_rmnode,
                               msg="Removing Node has failed. Please see the /tmp/vxrail_ansible_rmnode.log for more details")
        module.exit_json(**vx_facts_result)
    vx_rmnode = {'status': rmnode_status, 'request_id': rmnode_request_id}
    vx_facts_result = dict(changed=True, Remove_Node=vx_rmnode,
                           msg="Removing Node is successful. Please see the /tmp/vxrail_ansible_rmnode.log for more details")
    module.exit_json(**vx_facts_result)


if __name__ == '__main__':
    main()
