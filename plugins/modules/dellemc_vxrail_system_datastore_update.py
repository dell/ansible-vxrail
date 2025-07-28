#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_datastore_update
short_description: VxRail Datastore ID Update
description:
- This module will update datastore_id according to datastore_name
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
  datastore_name:
    description:
      The name of the datastore
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
  - name: VxRail Datastore ID Update
    dellemc_vxrail_system_datastore_update:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        datastore_name: "{{ datastore_name }}"
'''

RETURN = r'''
Datastire_ID_Update:
  description: Update datastore_id. Returns datastore_id and datastore_name.
  returned: always
  type: dict
  sample: >-
    {
        "datastore_id": "datastore_id",
        "datastore_name":  "datastore_name"    
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils


# Defining global variables
LOG_FILE_PATH = "/tmp/vxrail_ansible_datastore_update.log"
LOGGER = utils.get_logger("dellemc_vxrail_system_datastore_update", LOG_FILE_PATH, log_devel=logging.DEBUG)
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
        self.datastore_name = module.params.get('datastore_name')
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

        # Calls versioned method as attribute (ex: v1_datastore_id_update_patch)
        call_string = self.api_version_string + '_datastore_id_update_patch'
        LOGGER.info("Using utility method: %s\n", call_string)
        datastore_update_patch = getattr(api_instance, call_string)
        return datastore_update_patch(datastore_update_info)

    def datastore_id_update(self):
        datastore_id_update_return_info = {}
        datastore_id_update_info = {
            'datastore_name': self.datastore_name
        }

        # create an instance of the API class


        api_instance = vxrail_ansible_utility.DatastoreIDUpdateApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        LOGGER.info(datastore_id_update_info)
        try:
            # patch datastore ID update
            response = self.get_versioned_response(api_instance, "PATCH /system/datastore/id", datastore_id_update_info)
        except ApiException as e:
            LOGGER.error("Exception when calling DatastoreIDUpdateApi->%s_datastore_update_info: %s\n",
                         self.api_version_string, e)
            return 'error'
        data = response
        datastore_id_update_return_info['datastore_id'] = data.datastore_id
        datastore_id_update_return_info['datastore_name'] = data.datastore_name

        return dict(datastore_id_update_return_info.items())


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        datastore_name=dict(type='str', required=True),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().datastore_id_update()
    if result == 'error':
        module.fail_json(
            msg=f"Call PATCH /system/datastore/id API failed,please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts = {'Datastore_ID_Update': result}
    vx_facts_result = dict(changed=True, Datastore_ID_Update=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()