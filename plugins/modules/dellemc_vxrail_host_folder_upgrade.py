#!/usr/bin/python
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_host_folder_upgrade

short_description: Perform host folder LCM

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.4.0"

description:
- This module will perform node upgrade for all eligible satellite nodes in the specific host folder

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

  action:
    description:
      STAGE will transfer the upgrade bundle to the nodes but will not initiate the upgrade procedure. UPGRADE will initiate the upgrade procedure.
    choices: [UPGRADE, STAGE]
    required: True
    type: str

  folder_id:
    description:
      The specific folder id
    required: True
    type: str

  target_version:
    description:
      The target VxRail system version
    required: True
    type: str

  failure_rate:
    description:
      The failure rate of LCM batch job.
      failure_rate = failed nodes count / total nodes count. This parameter is only valid for UPGRADE requests.
    required: false
    type: int

  concurrent_size:
    description:
      Number of nodes that can be upgraded in parallel. This parameter is only valid for UPGRADE requests.
    required: false
    type: int

  timeout:
    description:
      Time out value for host folder upgrade, the default value is 21600 seconds
    required: false
    type: int
    default: 21600

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: false
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Start host folder upgrade
    dellemc_vxrail_host_folder_upgrade:
      vxmip: "{{ vxmip }}"
      vcadmin: "{{ vcadmin }}"
      vcpasswd: "{{ vcpasswd }}"
      action: "{{ action }}"
      folder_id: "{{ folder_id }}"
      target_version: "{{ target_version }}"
      failure_rate: "{{ failure_rate | default(omit) }}"
      concurrent_size: "{{ concurrent_size | default(omit) }}"
      api_version_number: "{{ api_version_number | default(omit) }}"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
upgrade_status:
  description: host folder upgrade status summary
  returned: always
  type: dict
  sample: >-
   {
    "FolderUpgrade": {
        "request_id": "433d0a61-06e7-4cb8-a1eb-985ab9a8b5dd",
        "status": "COMPLETED"
    }
    "msg": "The host folder upgrade is successful. Please see the /tmp/vxrail_ansible_host_folder_upgrade.log for more details"
   }
'''

import traceback
import logging
import time
from ansible.module_utils.basic import AnsibleModule, missing_required_lib

try:
    import urllib3
    import vxrail_ansible_utility
    from vxrail_ansible_utility.rest import ApiException
    from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils
    LOGGER = utils.get_logger("dellemc_vxrail_host_folder_upgrade", "/tmp/vxrail_ansible_host_folder_upgrade.log",
                              log_devel=logging.DEBUG)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except ImportError:
    HAS_ANOTHER_LIBRARY = False
    ANOTHER_LIBRARY_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_ANOTHER_LIBRARY = True

TIME_SLEEP = 30


class VxrailClusterUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxmip):
        self.vxmip = vxmip

    def set_host(self):
        return VxrailClusterUrls.cluster_url.format(self.vxmip)


class VxRailHostFolder():
    def __init__(self):
        self.vxmip = module.params.get('vxmip')
        self.vcadmin = module.params.get('vcadmin')
        self.vcpasswd = module.params.get('vcpasswd')
        self.action = module.params.get('action')
        self.folder_id = module.params.get('folder_id')
        self.target_version = module.params.get('target_version')
        self.failure_rate = module.params.get('failure_rate')
        self.concurrent_size = module.params.get('concurrent_size')
        self.api_version_number = module.params.get('api_version_number')

        self.cluster_url = VxrailClusterUrls(self.vxmip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vcadmin
        self.configuration.password = self.vcpasswd
        self.configuration.verify_ssl = False
        self.configuration.host = self.cluster_url.set_host()

    def validate(self):
        return self.action == 'UPGRADE' or (self.failure_rate is None and self.concurrent_size is None)

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def start_versioned_upgrade(self, api_instance, module_path, request_body):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxmip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxmip, self.api_version_number, module_path, LOGGER)

        call_string = self.api_version_string + '_lcm_folders_upgrade'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_lcm_folders_upgrade = getattr(api_instance, call_string)
        return api_lcm_folders_upgrade(request_body)

    def start_upgrade(self):
        request_body = {
            'action': self.action,
            'host_folder_id': self.folder_id,
            'target_version': self.target_version
        }

        if self.failure_rate is not None:
            if 'control' not in request_body:
                request_body['control'] = {}
            request_body['control']['failure_rate'] = self.failure_rate

        if self.concurrent_size is not None:
            if 'control' not in request_body:
                request_body['control'] = {}
            request_body['control']['concurrent_size'] = self.concurrent_size

        # create an instance of the API class
        api_instance = vxrail_ansible_utility.HostFolderLCMApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # start host-folder upgrade
            response = self.start_versioned_upgrade(api_instance, "Post /lcm/host-folder/upgrade", request_body)
        except ApiException as e:
            LOGGER.error("Exception when calling HostFolderLCMApi->%s_lcm_folders_upgrade: %s\n", self.api_version_string, e)
            return 'error'
        return response.request_id

    def get_request_status(self, request_id):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.RequestStatusApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = api_instance.v1_request_id_get(request_id)
        except ApiException as e:
            LOGGER.error("Exception when calling v1_requests_id_get: %s\n", e)
            return 'error'
        return response

    def get_request_info(self, response):
        statusInfo = {}
        statusInfo['id'] = response.id
        statusInfo['state'] = response.state
        statusInfo['owner'] = response.owner
        statusInfo['progress'] = response.progress
        statusInfo['extension'] = response.extension
        statusInfo['start_time'] = response.start_time
        statusInfo['end_time'] = response.end_time
        statusInfolist = []
        statusInfolist.append(statusInfo)
        return statusInfolist


def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        action=dict(required=True, choices=['UPGRADE', 'STAGE']),
        folder_id=dict(required=True),
        target_version=dict(required=True),
        failure_rate=dict(type='int'),
        concurrent_size=dict(type='int'),
        timeout=dict(type='int', default=30 * 720),
        api_version_number=dict(type='int')
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    if not HAS_ANOTHER_LIBRARY:
        module.fail_json(
            msg=missing_required_lib('another_library'),
            exception=ANOTHER_LIBRARY_IMPORT_ERROR)

    if not VxRailHostFolder().validate():
        module.fail_json(msg='The Parameters of hosts are not legal. Only when the action is UPGRADE, '
                             'the variables failure_rate_var and concurrent_size_var are needed. '
                             'Please see the /tmp/vxrail_ansible_host_folder_upgrade.log for more details')

    LOGGER.info('----Start host folder upgrade.----')
    request_id = VxRailHostFolder().start_upgrade()
    if request_id == 'error':
        module.fail_json(
            msg="The request id is not returned. Please see the /tmp/vxrail_ansible_host_folder_upgrade.log for more details")

    LOGGER.info('host_folder_upgrade: VxRail task_ID: %s.', request_id)

    initial_timeout = module.params.get('timeout')
    time_out = 0
    upgrade_status = 0
    while upgrade_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        upgrade_response = VxRailHostFolder().get_request_status(request_id)
        upgrade_status = upgrade_response.state
        upgrade_result = VxRailHostFolder().get_request_info(upgrade_response)
        LOGGER.info('Upgrade_Task: status: %s.', upgrade_status)
        LOGGER.info('Upgrade_Task: details: %s.', upgrade_result)
        LOGGER.info('Upgrade Task: sleeping %s seconds...', TIME_SLEEP)
        time.sleep(TIME_SLEEP)
        time_out += TIME_SLEEP

    if upgrade_status != 'COMPLETED':
        LOGGER.info("------Upgrade Failed-----")

        hosts = eval(upgrade_result[0].get('extension')).get('hosts')
        error = hosts[0].get('errors')
        vx_upgrade = {'request_id': request_id, 'response_error': error}
        vx_facts_result = dict(failed=True, FolderUpgrade=vx_upgrade,
                               msg='The host folder upgrade has failed. Please see the /tmp/vxrail_ansible_host_folder_upgrade.log for more details')
        module.exit_json(**vx_facts_result)

    LOGGER.info("-----Upgrade Completed-----")
    vx_upgrade = {'status': upgrade_status, 'request_id': request_id}
    vx_facts_result = dict(changed=True, FolderUpgrade=vx_upgrade,
                           msg='The host folder upgrade is successful. Please see the /tmp/vxrail_ansible_host_folder_upgrade.log for more details')
    module.exit_json(**vx_facts_result)


if __name__ == '__main__':
    main()
