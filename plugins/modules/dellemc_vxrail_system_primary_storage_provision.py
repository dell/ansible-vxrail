#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_primary_storage_provision

short_description: VxRail Primary Storage Provision

description:
- This module will provision the primary storage according to primary_storage_name
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

  primary_storage_name:
    description:
      The name of the primary storage
    required: true
    type: str

  primary_storage_type:
    description:
      The type of the primary storage
    required: true
    type: str

  storage_policy_profile_name:
    description:
      The name of the storage policy profile
    required: true
    type: str

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for tirggering task of rebooting hosts, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>
'''

EXAMPLES = r'''
  - name: VxRail Primary Storage Provision
    dellemc_vxrail_system_primary_storage_provision:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        primary_storage_name: "{{ primary_storage_name }}"
        primary_storage_type: "{{ primary_storage_type }}"
        storage_policy_profile_name: "{{ storage_policy_profile_name }}"
'''

RETURN = r'''
VxRail Primary Storage Provision:
  description: VxRail Primary Storage Provision. Returns request_id.
  returned: always
  type: dict
  sample: >-
    {
        "request_id": "request_id"
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils


# Defining global variables
LOG_FILE_PATH = "/tmp/vxrail_ansible_primary_storage_provision.log"
LOGGER = utils.get_logger("dellemc_vxrail_system_primary_storage_provision", LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return f"https://{self.vxm_ip}/rest/vxm"


class VxRailCluster():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.primary_storage_name = module.params.get('primary_storage_name')
        self.primary_storage_type = module.params.get('primary_storage_type')
        self.storage_policy_profile_name = module.params.get('storage_policy_profile_name')
        self.api_version_number = module.params.get('api_version_number')

        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    def get_versioned_response(self, api_instance, module_path, datastore_update_info):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path,
                                                                   LOGGER)

        # Calls versioned method as attribute (ex: v2_system_primary_storage_post)
        call_string = self.api_version_string + '_system_primary_storage_post'
        LOGGER.info("Using utility method: %s\n", call_string)
        storage_provision_patch = getattr(api_instance, call_string)
        return storage_provision_patch(datastore_update_info)

    def primary_storage_provision(self):
        primary_storage_provision_return_info = {}
        primary_storage_provision_info = {
            'primary_storage_name': self.primary_storage_name,
            'primary_storage_type': self.primary_storage_type,
            'storage_policy_profile_name': self.storage_policy_profile_name
        }

        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemInformationApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        LOGGER.info(primary_storage_provision_info)
        try:
            # patch datastore ID update
            response = self.get_versioned_response(api_instance, "POST /system/primary-storage", primary_storage_provision_info)
        except ApiException as e:
            LOGGER.error("Exception when calling DatastoreIDUpdateApi->%s_datastore_update_info: %s\n",
                         self.api_version_string, e)
            return 'error'
        data = response
        primary_storage_provision_return_info['request_id'] = data.request_id

        return dict(primary_storage_provision_return_info.items())


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        primary_storage_name=dict(type='str', required=True),
        primary_storage_type=dict(type='str', required=True),
        storage_policy_profile_name=dict(type='str', required=True),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().primary_storage_provision()
    if result == 'error':
        module.fail_json(
            msg=f"Call POST /system/primary-storage API failed,please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts_result = dict(changed=True, Primary_Storage_Provision=result)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
