#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_precheck

short_description: Perform a system pre-check.

description:
  - This module will perform a system pre-check.
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

  timeout:
    description:
      Time out value for performing a system precheck, the default value is 300 seconds
    required: False
    type: int
    default: 300

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  profile:
    description:
      The profile name. Allowed only PRE_UPGRADE, PROACTIVE_HEALTH or NODE_EXPANSION.
    required: true
    type: str

  vxm_root_username:
    description:
      Username of VxRail Manager root user account
    required: True
    type: str

  vxm_root_password:
    description:
      The password of VxRail Manager root user account
    required: True
    type: str

  vc_root_username:
    description:
      Username of vCenter root user account
    required: True
    type: str

  vc_root_password:
    description:
      The password of vCenter root user account
    required: True
    type: str

  witness_username:
    description:
      The username information of witness user account for a stretched cluster, including a vSAN 2-node cluster.
      The witness object only applies to a cluster when vLCM is not enabled.
    required: False
    type: str

  witness_password:
    description:
      The password information of witness user account for a stretched cluster, including a vSAN 2-node cluster.
      The witness object only applies to a cluster when vLCM is not enabled.
    required: False
    type: str

  auto_witness_upgrade:
    description:
      Whether VxRail will automatically upgrade the witness node
    required: False
    type: bool

  vc_temporary_ip:
    description:
      Temporary IP settings for the vCenter upgrade
    required: False
    type: str

  vc_temporary_gateway:
    description:
      Temporary IP settings for the vCenter upgrade
    required: False
    type: str

  vc_temporary_netmask:
    description:
      Temporary IP settings for the vCenter upgrade
    required: False
    type: str

  sn:
    description:
      Serial number of the new node to be added
    required: False
    type: str

  version:
    description:
      Install version of the new node to be added
    required: False
    type: str

  ip:
    description:
      IP address of the new node to be added
    required: False
    type: str

  root_user:
    description:
      Root user of the new node to be added
    required: False
    type: str

  root_password:
    description:
      Root passwrod of the new node to be added
    required: False
    type: str

author:
  - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>
'''

EXAMPLES = r'''
  - name: Perform a system precheck
    dellemc_vxrail_system_precheck:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        profile: "{{ profile }}"
        vxm_root_username: "{{ vxm_root_username }}"
        vxm_root_password: "{{ vxm_root_password }}"
        vc_root_username: "{{ vc_root_username }}"
        vc_root_password: "{{ vc_root_password }}"
        witness_username: "{{ witness_username }}"
        witness_password: "{{ witness_password }}"
        auto_witness_upgrade: "{{ auto_witness_upgrade }}"
        vc_temporary_ip: "{{ vc_temporary_ip }}"
        vc_temporary_gateway: "{{ vc_temporary_gateway }}"
        vc_temporary_netmask: "{{ vc_temporary_netmask }}"
        sn: "{{ sn }}"
        version: "{{ version }}"
        ip: "{{ ip }}"
        root_user: "{{ root_user }}"
        root_password: "{{ root_password }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Post_System_Precheck_API:
    description: perform system precheck
    returned: always
    type: dict
    sample: >-
      {
        "request_iD": "a6146c2f-73fd-4415-a596-9e372f406d98"
      }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

# Defining global variables
API = "/system/precheck"
MODULE = "dellemc_vxrail_system_precheck"
LOG_FILE_PATH = "/tmp/vxrail_ansible_system_precheck.log"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
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
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.profile = module.params.get('profile')
        self.vxm_root_username = module.params.get('vxm_root_username')
        self.vxm_root_password = module.params.get('vxm_root_password')
        self.vc_root_username = module.params.get('vc_root_username')
        self.vc_root_password = module.params.get('vc_root_password')
        self.witness_username = module.params.get('witness_username')
        self.witness_password = module.params.get('witness_password')
        self.auto_witness_upgrade = module.params.get('auto_witness_upgrade')
        self.vc_temporary_ip = module.params.get('vc_temporary_ip')
        self.vc_temporary_gateway = module.params.get('vc_temporary_gateway')
        self.vc_temporary_netmask = module.params.get('vc_temporary_netmask')
        self.sn = module.params.get('sn')
        self.version = module.params.get('version')
        self.ip = module.params.get('ip')
        self.root_user = module.params.get('root_user')
        self.root_password = module.params.get('root_password')
        self.timeout = module.params.get('timeout')
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        call_string = self.api_version_string + '_system_precheck_post'
        LOGGER.info("Using utility method: %s\n", call_string)

        api_system_precheck_post = getattr(api_instance, call_string)
        system_precheck_json = {
            "profile": self.profile,
            "vxm_root_user": {
                "username": self.vxm_root_username,
                "password": self.vxm_root_password
            },
            "vc_admin_user": {
                "username": self.vc_admin,
                "password": self.vc_password
            },
            "vc_root_user": {
                "username": self.vc_root_username,
                "password": self.vc_root_password
            }
        }
        if self.witness_username:
            witness_spec = {
                "witness_user": {
                    "username": self.witness_username,
                    "password": self.witness_password
                },
                "auto_witness_upgrade": self.auto_witness_upgrade,
            }
            system_precheck_json["witness_spec"] = witness_spec
        if self.vc_temporary_ip:
            migration_spec = {
                "temporary_ip_setting": {
                    "vc_temporary_ip": self.vc_temporary_ip,
                    "vc_temporary_gateway": self.vc_temporary_gateway,
                    "vc_temporary_netmask": self.vc_temporary_netmask
                }
            }
            system_precheck_json["migration_spec"] = migration_spec
        if self.sn:
            node_list = [
                {
                    "sn": self.sn,
                    "version": self.version,
                    "ip": self.ip,
                    "root_user": self.root_user,
                    "root_password": self.root_password
                }
            ]
            system_precheck_json["node_list"] = node_list
        return api_system_precheck_post(body=system_precheck_json)

    def post_system_precheck(self):
        # create an instance of the API class
        response = ''
        api_instance = vxrail_ansible_utility.SystemPreCheckApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # post system precheck
            response = self.get_versioned_response(api_instance, "POST /system/precheck")
        except ApiException as e:
            LOGGER.error("Exception when calling SystemPreCheckApi->%s_system_precheck_post: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/system/precheck api response: %s\n", self.api_version_string, response)
        requestid = response.request_id
        return requestid


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        profile=dict(required=True),
        vxm_root_username=dict(required=True),
        vxm_root_password=dict(required=True, no_log=True),
        vc_root_username=dict(required=True),
        vc_root_password=dict(required=True, no_log=True),
        witness_username=dict(required=False),
        witness_password=dict(required=False, no_log=True),
        auto_witness_upgrade=dict(required=False, type='bool'),
        vc_temporary_ip=dict(required=False),
        vc_temporary_gateway=dict(required=False),
        vc_temporary_netmask=dict(required=False),
        sn=dict(required=False),
        version=dict(required=False),
        ip=dict(required=False),
        root_user=dict(required=False),
        root_password=dict(required=False, no_log=True),
        timeout=dict(required=False, type='int', default=300),
        api_version_number=dict(required=False, type='int')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().post_system_precheck()
    if result == 'error':
        module.fail_json(msg="Call system/precheck API failed,please see log file /tmp/vxrail_ansible_system_precheck.log for more error details.")
    vx_facts = {'request_id': result}
    vx_facts_result = dict(changed=False, Post_System_Precheck_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
