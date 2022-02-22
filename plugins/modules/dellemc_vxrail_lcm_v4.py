#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm_v4

short_description: Perform a full upgrade or a partial upgrade with v4/upgrade api

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.2.0"

description:
- This module will perform a partial upgrade of all VxRail software and hardware. It includes the optional
  variable "target_hosts_name", which indicates the nodes to be upgraded.If "target_hosts" is not provided, this
  module upgrades all nodes in cluster.
options:
  vxmip:
    description:
      The IP address of the VxRail Manager System
    required: True
    type: str

  bundle:
    description:
      the path of lcm bundle on vxm, which is recommended under /data/store2
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

  vxm_root_account:
    description:
      root account of VxRail Manager
    required: true
    type: str

  vxm_root_passwd:
    description:
      The password for the root account provided in vxm
    required: true
    type: str

  target_hosts_name:
    description:
      target hosts name for partial upgrade
    required: false
    type: str
    default: all

  timeout:
    description:
      Time out value for LCM Upgrade, the default value is 21600 seconds
    required: false
    type: int
    default: 21600

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
- name: LCM with v4 api
  dellemc_vxrail_lcm_v4:
    vxmip: "{{ vxmip }}"
    vcadmin: "{{ vcadmin }}"
    vcpasswd: "{{ vcpasswd }}"
    bundle: "{{ bundle }}"
    vc_root_account: "{{ vc_root_account }}"
    vc_root_passwd: "{{ vc_root_passwd }}"
    vxm_root_account: "{{ vxm_root_account }}"
    vxm_root_passwd: "{{ vxm_root_passwd }}"
    target_hosts_name: "{{ target_hosts_name }}"
'''
RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
LCM_status:
  description: LCM status summary
  returned: always
  type: dict
  sample: >-
   {
    "LCM_V4API_Uprade": {
        "request_id": "2ce09bde-d987-4fff-8f90-6fc430e2bfc3",
        "status": "COMPLETED"
    }
    "msg": "LCM is successful. Please see the /tmp/vxrail_ansible_lcm_v4.log for more details"
   }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_NAME = "/tmp/vxrail_ansible_lcm_v4.log"
LOGGER = utils.get_logger("dellemc_vxrail_lcm_v4", LOG_FILE_NAME, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
MAX_RETRY_COUNT = 8
CHECK_STATUS_INTERVAL = 360
MAX_CHECK_COUNT = 60


class VxrailVXMUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailVXMUrls.vxm_url.format(self.vxm_ip)


class VxRailLCMV4():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.bundle = module.params.get('bundle')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.vc_root_account = module.params.get('vc_root_account')
        self.vc_root_passwd = module.params.get('vc_root_passwd')
        self.vxm_root_account = module.params.get('vxm_root_account')
        self.vxm_root_passwd = module.params.get('vxm_root_passwd')
        self.target_hosts_name = module.params.get('target_hosts_name')
        self.vxm_url = VxrailVXMUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.vxm_url.set_host()

    def create_lcm_json(self):
        ''' lcm node json '''
        lcm_json = {}
        lcm_json['bundle_file_locator'] = self.bundle
        vcenter_dict = {}
        vcenter_dict['vc_admin_user'] = {'username': self.vc_admin, 'password': self.vc_password}
        vcenter_dict['vcsa_root_user'] = {'username': self.vc_root_account, 'password': self.vc_root_passwd}
        lcm_json['vcenter'] = vcenter_dict
        vxrail_dict = {}
        vxrail_dict['vxm_root_user'] = {'username': self.vxm_root_account, 'password': self.vxm_root_passwd}
        lcm_json['vxrail'] = vxrail_dict
        if self.target_hosts_name != "all":
            target_hosts_list = []
            if len(self.target_hosts_name.split(",")) != 0:
                for item in self.target_hosts_name.split(","):
                    target_hosts_list.append({'name': item})
            else:
                target_hosts_list = [{'name': self.target_hosts_name}]
            lcm_json['target_hosts'] = target_hosts_list
        return lcm_json

    def v4_upgrade(self, lcm_json):
        request_body = lcm_json
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.LCMUpgradeApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # start LCM with v4 api
            response = api_instance.upgrade_v4(request_body)
        except ApiException as e:
            LOGGER.error("Exception when calling LCMUpgradeApi->upgrade_v4v: %s\n", e)
            return 'error'
        job_id = response.request_id
        return job_id

    def get_request_status(self, request_id):
        job_id = request_id
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.RequestStatusApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = api_instance.v1_request_id_get(job_id)
        except Exception as e:
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
        statusInfo['detail'] = data.detail
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
        bundle=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        vc_root_account=dict(required=True),
        vc_root_passwd=dict(required=True, no_log=True),
        vxm_root_account=dict(required=True),
        vxm_root_passwd=dict(required=True, no_log=True),
        target_hosts_name=dict(type='str', default="all"),
        timeout=dict(type='int', default=MAX_CHECK_COUNT * CHECK_STATUS_INTERVAL)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    lcm_status = 0
    lcm_result = 0
    error = 0
    time_out = 0
    initial_timeout = module.params.get('timeout')
    try_times = 0
    LOGGER.info('----Start to upgrade with V4 API: ----')
    lcm_json = VxRailLCMV4().create_lcm_json()
    request_body = lcm_json
    lcm_request_id = VxRailLCMV4().v4_upgrade(request_body)
    LOGGER.info('LCM: VxRail task_ID: %s.', lcm_request_id)
    if lcm_request_id == "error":
        module.fail_json(
            msg="lcm request id is not returned. Please see the /tmp/vxrail_ansible_lcm_v4.log for more details")
    while lcm_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        lcm_response = VxRailLCMV4().get_request_status(lcm_request_id)
        ''' When VxRail Manager upgrade or Reboot is in progress. Temporary disconnection during this process,
        meed to send request with auth again'''
        while lcm_response == "error" and try_times < MAX_RETRY_COUNT:
            LOGGER.info('----VxRail Manager upgrade or Reboot is in progress, which may be temporary '
                        'disconnection during this process ----')
            LOGGER.info('----Please wait for its back...Need to log in again----')
            time.sleep(15 * 60)
            lcm_response = VxRailLCMV4().get_request_status(lcm_request_id)
            try_times = try_times + 1
        if try_times == MAX_RETRY_COUNT:
            LOGGER.info('----VxRail Manager upgrade or Reboot is failed----')
            vx_lcm = {'request_id': lcm_request_id}
            vx_facts_result = dict(failed=True, LCM_V4API_Uprade=vx_lcm,
                                   msg="LCM has failed. Please see the /tmp/vxrail_ansible_lcm_v4.log for more details")
            module.exit_json(**vx_facts_result)
        lcm_status = lcm_response.state
        lcm_result = VxRailLCMV4().get_request_info(lcm_response)
        LOGGER.info('LCM_Task: status: %s.', lcm_status)
        LOGGER.info('LCM_Task: details: %s.', lcm_result)
        LOGGER.info("LCM_Task: Sleeping %s seconds...", CHECK_STATUS_INTERVAL)
        time.sleep(CHECK_STATUS_INTERVAL)
        time_out = time_out + CHECK_STATUS_INTERVAL
    if lcm_status == 'COMPLETED':
        LOGGER.info("-------LCM is successful.-----")
    else:
        LOGGER.info("------LCM Failed-----")
        if lcm_result[0].get('error') is not None:
            error = lcm_result[0].get('error')
        else:
            error = lcm_result[0].get('detail')
        LOGGER.info('----Failed reason is : %s.----', error)
        vx_lcm = {'request_id': lcm_request_id, 'response_error': error}
        vx_facts_result = dict(failed=True, LCM_V4API_Uprade=vx_lcm,
                               msg="LCM has failed. Please see the /tmp/vxrail_ansible_lcm_v4.log for more details")
        module.exit_json(**vx_facts_result)
    vx_lcm = {'status': lcm_status, 'request_id': lcm_request_id}
    vx_facts_result = dict(changed=True, LCM_V4API_Uprade=vx_lcm,
                           msg="LCM is successful. Please see the /tmp/vxrail_ansible_lcm_v4.log for more details")
    module.exit_json(**vx_facts_result)


if __name__ == '__main__':
    main()
