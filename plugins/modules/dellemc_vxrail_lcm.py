#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_lcm

short_description: Perform a upgrade with lcm upgrade api

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.6.0"

description:
- This module will perform the LCM full upgrade or partial upgrade via v4+ API of all VxRail software and hardware.
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

  psc_root_account:
    description:
      root account of the PSC the VxRail Manager is registered to
    required: false
    type: str

  psc_root_passwd:
    description:
      The password for the root account provided in PSC
    required: false
    type: str

  source_vcsa_host_name:
    description:
      Hostname of the ESXi host
    required: false
    type: str

  source_vcsa_host_user_name:
    description:
      The username of account provided in the ESXi host
    required: false
    type: str

  source_vcsa_host_user_passwd:
    description:
      The password of account provided in the ESXi host
    required: false
    type: str

  source_psc_host_name:
    description:
      Hostname of the ESXi host
    required: false
    type: str

  source_psc_host_user_name:
    description:
      The username of account provided in the ESXi host
    required: false
    type: str

  source_psc_host_user_passwd:
    description:
      The password of account provided in the ESXi host
    required: false
    type: str

  target_vcsa_host_name:
    description:
      Hostname of the ESXi host
    required: false
    type: str

  target_vcsa_host_user_name:
    description:
      The username of account provided in the ESXi host
    required: false
    type: str

  target_vcsa_host_user_passwd:
    description:
      The password of account provided in the ESXi host
    required: false
    type: str

  temporary_ip:
    description:
      Temporary IP to be used during the vCenter upgrade
    required: false
    type: str

  temporary_gateway:
    description:
      Gateway to be used during the vCenter upgrade
    required: false
    type: str

  temporary_netmask:
    description:
      Netmask to be used during the vCenter upgrade
    required: false
    type: str

  witness_username:
    description:
      Username of the witness account
    required: false
    type: str

  witness_password:
    description:
      Password of the witness account
    required: false
    type: str

  auto_witness_upgrade:
    description:
      Automatically upgrade the witness node by VxRail
    required: false
    type: bool

  preferred_fault_domain_first:
    description:
      Upgrade preferred fault domain hosts first
    required: false
    type: bool

  target_hosts_name:
    description:
      target hosts name for partial upgrade
    required: false
    type: str
    default: all

  missing_file_check:
    description:
      If you are using the customizing upgrade bundle i.e. Smart Bundle, this option should be set to false.
    required: false
    type: bool
    default: true

  skip_failed_hosts:
    description:
      If set to true, any nodes that fail the upgrade will be ignored.
    required: false
    type: bool

  ecosystem_check_continue_with_incompatible:
    description:
      if set to true, will ignore the ecosystem pre-check according to the inputs in "continue_with_incompatible" and "components".
    required: false
    type: bool

  ecosystem_check_components:
    description:
      The ecosystem pre-check will be ignored according to the value in "continue_with_incompatible" and "components".
    required: false
    type: str

  timeout:
    description:
      Time out value for LCM Upgrade, the default value is 21600 seconds
    required: false
    type: int
    default: 21600

  api_version_number:
    description:
      Specify the API version to perform the upgrade.
    required: false
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
- name: LCM api
  dellemc_vxrail_lcm:
    vxmip: "{{ vxmip }}"
    vcadmin: "{{ vcadmin }}"
    vcpasswd: "{{ vcpasswd }}"
    bundle: "{{ bundle }}"
    vc_root_account: "{{ vc_root_account }}"
    vc_root_passwd: "{{ vc_root_passwd }}"
    vxm_root_account: "{{ vxm_root_account }}"
    vxm_root_passwd: "{{ vxm_root_passwd }}"
    target_hosts_name: "{{ target_hosts_name }}"
    missing_file_check: "{{ missing_file_check }}"
    skip_failed_hosts: "{{ skip_failed_hosts }}"
    ecosystem_check_continue_with_incompatible: "{{ ecosystem_check_continue_with_incompatible }}"
    ecosystem_check_components: "{{ ecosystem_check_components }}"
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
    "LCM_API_Upgrade": {
        "request_id": "2ce09bde-d987-4fff-8f90-6fc430e2bfc3",
        "status": "COMPLETED"
    }
    "msg": "LCM is successful. Please see the /tmp/vxrail_ansible_lcm.log for more details"
   }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_NAME = "/tmp/vxrail_ansible_lcm.log"
LOGGER = utils.get_logger("dellemc_vxrail_lcm", LOG_FILE_NAME, log_devel=logging.DEBUG)
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


class VxRailLCM():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.bundle = module.params.get('bundle')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.vc_root_account = module.params.get('vc_root_account')
        self.vc_root_passwd = module.params.get('vc_root_passwd')
        self.vc_mgmt_account = module.params.get('vc_mgmt_account')
        self.vc_mgmt_passwd = module.params.get('vc_mgmt_passwd')
        self.vxm_root_account = module.params.get('vxm_root_account')
        self.vxm_root_passwd = module.params.get('vxm_root_passwd')
        self.psc_root_account = module.params.get('psc_root_account')
        self.psc_root_passwd = module.params.get('psc_root_passwd')
        self.source_vcsa_host_name = module.params.get('source_vcsa_host_name')
        self.source_vcsa_host_user_name = module.params.get('source_vcsa_host_user_name')
        self.source_vcsa_host_user_passwd = module.params.get('source_vcsa_host_user_passwd')
        self.source_psc_host_name = module.params.get('source_psc_host_name')
        self.source_psc_host_user_name = module.params.get('source_psc_host_user_name')
        self.source_psc_host_user_passwd = module.params.get('source_psc_host_user_passwd')
        self.target_vcsa_host_name = module.params.get('target_vcsa_host_name')
        self.target_vcsa_host_user_name = module.params.get('target_vcsa_host_user_name')
        self.target_vcsa_host_user_passwd = module.params.get('target_vcsa_host_user_passwd')
        self.temporary_ip = module.params.get('temporary_ip')
        self.temporary_gateway = module.params.get('temporary_gateway')
        self.temporary_netmask = module.params.get('temporary_netmask')
        self.witness_username = module.params.get('witness_username')
        self.witness_password = module.params.get('witness_password')
        self.auto_witness_upgrade = module.params.get('auto_witness_upgrade')
        self.preferred_fault_domain_first = module.params.get('preferred_fault_domain_first')
        self.target_hosts_name = module.params.get('target_hosts_name')
        self.missing_file_check = module.params.get('missing_file_check')
        self.skip_failed_hosts = module.params.get('skip_failed_hosts')
        self.ecosystem_check_continue_with_incompatible = module.params.get('ecosystem_check_continue_with_incompatible')
        self.ecosystem_check_components = module.params.get('ecosystem_check_components')
        self.vxm_url = VxrailVXMUrls(self.vxm_ip)
        self.api_version_number = module.params.get('api_version_number')
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

        vxrail_dict = {}
        vxrail_dict['vxm_root_user'] = {'username': self.vxm_root_account, 'password': self.vxm_root_passwd}
        lcm_json['vxrail'] = vxrail_dict

        if self.psc_root_passwd and self.api_version_number <= 2:
            vcenter_dict['psc_root_user'] = {'username': self.psc_root_account, 'password': self.psc_root_passwd}

        migration_spec_dict = {}
        if self.source_vcsa_host_name:
            source_vcsa_host_dict = {}
            source_vcsa_host_dict['name'] = self.source_vcsa_host_name
            source_vcsa_host_dict['user'] = {'username': self.source_vcsa_host_user_name,
                                             'password': self.source_vcsa_host_user_passwd}
            migration_spec_dict['source_vcsa_host'] = source_vcsa_host_dict
        if self.source_psc_host_name and self.api_version_number <= 2:
            source_psc_host_dict = {}
            source_psc_host_dict['name'] = self.source_psc_host_name
            source_psc_host_dict['user'] = {'username': self.source_psc_host_user_name,
                                            'password': self.source_psc_host_user_passwd}
            migration_spec_dict['source_psc_host'] = source_psc_host_dict
        if self.target_vcsa_host_name:
            target_vcsa_host_dict = {}
            target_vcsa_host_dict['name'] = self.target_vcsa_host_name
            target_vcsa_host_dict['user'] = {'username': self.target_vcsa_host_user_name,
                                             'password': self.target_vcsa_host_user_passwd}
            migration_spec_dict['target_vcsa_host'] = target_vcsa_host_dict
        if self.temporary_ip:
            migration_spec_dict['temporary_ip_setting'] = {'temporary_ip': self.temporary_ip,
                                                           'gateway': self.temporary_gateway,
                                                           'netmask': self.temporary_netmask}
        if any(migration_spec_dict):
            vcenter_dict['migration_spec'] = migration_spec_dict
        lcm_json['vcenter'] = vcenter_dict

        if self.api_version_number >= 2:
            if self.witness_username:
                witness_dict = {}
                witness_user_dict = {'username': self.witness_username,
                                     'password': self.witness_password}
                witness_dict['witness_user'] = witness_user_dict
                witness_dict['auto_witness_upgrade'] = self.auto_witness_upgrade
                lcm_json['witness'] = witness_dict

            if self.preferred_fault_domain_first:
                lcm_json['upgrade_sequence'] = {'preferred_fault_domain_first': self.preferred_fault_domain_first}

        if self.api_version_number >= 4:
            if self.target_hosts_name != "all":
                target_hosts_list = []
                if len(self.target_hosts_name.split(",")) != 0:
                    for item in self.target_hosts_name.split(","):
                        target_hosts_list.append({'name': item})
                else:
                    target_hosts_list = [{'name': self.target_hosts_name}]
                lcm_json['target_hosts'] = target_hosts_list

        if self.api_version_number >= 5:
            update_rules = {}
            ecosystem_check = {}

            if self.missing_file_check is not None:
                update_rules['missing_file_check'] = self.missing_file_check

            if self.skip_failed_hosts is not None:
                update_rules['skip_failed_hosts'] = self.skip_failed_hosts

            if self.ecosystem_check_components:
                components = self.ecosystem_check_components.split(",")
                ecosystem_check['components'] = components
                ecosystem_check['continue_with_incompatible'] = self.ecosystem_check_continue_with_incompatible

            update_rules['ecosystem_check'] = ecosystem_check
            lcm_json['update_rules'] = update_rules

        # for api v6
        if hasattr(self, 'vc_mgmt_account') and hasattr(self, 'vc_mgmt_passwd'):
            vcenter_dict['vc_mgmt_user'] = {'username': self.vc_mgmt_account, 'password': self.vc_mgmt_passwd}
        else:
            vcenter_dict['vc_mgmt_user'] = utils.field_not_found(6)

        return lcm_json

    def upgrade(self):
        try:
            # create an instance of the API class
            api_instance = vxrail_ansible_utility.LCMUpgradeApi(vxrail_ansible_utility.ApiClient(self.configuration))
            # start LCM with versioned api
            api_version_string = self.get_versioned_response('Post /lcm/upgrade')
            call_string = 'upgrade_' + api_version_string
            LOGGER.info("LCM upgrade version: %s", call_string)
            lcm_upgrade = getattr(api_instance, call_string)

            # create request body with API version
            request_body = self.create_lcm_json()
            response = lcm_upgrade(request_body)
        except ApiException as e:
            LOGGER.error("Exception when calling LCMUpgradeApi->%s: %s\n", call_string, e)
            return 'error'
        job_id = response.request_id
        return job_id

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, module_path):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(api_version_string.split('v')[1])
        else:
            api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        return api_version_string

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
    common_module_args = dict(
        vxmip=dict(required=True),
        bundle=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        vc_root_account=dict(required=True),
        vc_root_passwd=dict(required=True, no_log=True),
        vxm_root_account=dict(required=True),
        vxm_root_passwd=dict(required=True, no_log=True),
        psc_root_account=dict(type='str'),
        psc_root_passwd=dict(type='str', no_log=True),
        source_vcsa_host_name=dict(type='str'),
        source_vcsa_host_user_name=dict(type='str'),
        source_vcsa_host_user_passwd=dict(type='str', no_log=True),
        source_psc_host_name=dict(type='str'),
        source_psc_host_user_name=dict(type='str'),
        source_psc_host_user_passwd=dict(type='str', no_log=True),
        target_vcsa_host_name=dict(type='str'),
        target_vcsa_host_user_name=dict(type='str'),
        target_vcsa_host_user_passwd=dict(type='str', no_log=True),
        temporary_ip=dict(type='str'),
        temporary_gateway=dict(type='str'),
        temporary_netmask=dict(type='str'),
        timeout=dict(type='int', default=MAX_CHECK_COUNT * CHECK_STATUS_INTERVAL),
        api_version_number=dict(type='int')
    )
    v2_module_args = dict(
        witness_username=dict(type='str'),
        witness_password=dict(type='str', no_log=True),
        auto_witness_upgrade=dict(type='bool'),
        preferred_fault_domain_first=dict(type='bool')
    )
    v4_module_args = dict(
        target_hosts_name=dict(type='str', default="all")
    )
    v5_module_args = dict(
        missing_file_check=dict(type='bool', default=True),
        skip_failed_hosts=dict(type='bool'),
        ecosystem_check_continue_with_incompatible=dict(type='bool'),
        ecosystem_check_components=dict(type='str')
    )
    v6_module_args = dict(
        vc_mgmt_account=dict(required=True),
        vc_mgmt_passwd=dict(required=True, no_log=True),
    )

    module_args = dict(**common_module_args, **v2_module_args, **v4_module_args, **v5_module_args, **v6_module_args)
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

    LOGGER.info('----Start to upgrade with LCM API: ----')
    lcm_request_id = VxRailLCM().upgrade()

    LOGGER.info('LCM: VxRail task_ID: %s.', lcm_request_id)
    if lcm_request_id == "error":
        module.fail_json(
            msg="lcm request id is not returned. Please see the /tmp/vxrail_ansible_lcm.log for more details")
    while lcm_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        lcm_response = VxRailLCM().get_request_status(lcm_request_id)
        ''' When VxRail Manager upgrade or Reboot is in progress. Temporary disconnection during this process,
        meed to send request with auth again'''
        while lcm_response == "error" and try_times < MAX_RETRY_COUNT:
            LOGGER.info('----VxRail Manager upgrade or Reboot is in progress, which may be temporary '
                        'disconnection during this process ----')
            LOGGER.info('----Please wait for its back...Need to log in again----')
            time.sleep(15 * 60)
            lcm_response = VxRailLCM().get_request_status(lcm_request_id)
            try_times = try_times + 1
        if try_times == MAX_RETRY_COUNT:
            LOGGER.info('----VxRail Manager upgrade or Reboot is failed----')
            vx_lcm = {'request_id': lcm_request_id}
            vx_facts_result = dict(failed=True, LCM_API_Upgrade=vx_lcm,
                                   msg="LCM has failed. Please see the /tmp/vxrail_ansible_lcm.log for more details")
            module.exit_json(**vx_facts_result)
        lcm_status = lcm_response.state
        lcm_result = VxRailLCM().get_request_info(lcm_response)
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
        vx_facts_result = dict(failed=True, LCM_API_Upgrade=vx_lcm,
                               msg="LCM has failed. Please see the /tmp/vxrail_ansible_lcm.log for more details")
        module.exit_json(**vx_facts_result)
    vx_lcm = {'status': lcm_status, 'request_id': lcm_request_id}
    vx_facts_result = dict(changed=True, LCM_API_Upgrade=vx_lcm,
                           msg="LCM is successful. Please see the /tmp/vxrail_ansible_lcm.log for more details")
    module.exit_json(**vx_facts_result)


if __name__ == '__main__':
    main()
