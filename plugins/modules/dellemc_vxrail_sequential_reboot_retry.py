#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_sequential_reboot_retry

short_description: VxRail Hosts Sequential Reboot

description:
- This module will reboot vxrail hosts sequentially
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

  all:
    description:
      Indicates whether all the hosts from the reboot task will reboot.
      Default value is FALSE
    required: false
    type: bool
    default: FALSE

  hosts:
    description:
      Hosts will reboot
    required: true
    type: list

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for retrying task of rebooting hosts, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: VxRail Hosts Sequential Reboot Retry
    dellemc_vxrail_sequential_reboot_retry:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        all: "{{ all }}"
        hosts: "{{ hosts }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Sequential_Reboot_Retry:
  description: Retry sequential rebooting hosts task. Returns the request ID.
  returned: always
  type: dict
  sample: >-
    {
        "request_id": "RebootApply-078ad9ef-9ef6-462c-a754-042b8dfec62b"
    }
'''


import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils


# Defining global variables
LOG_FILE_PATH = "/tmp/vxrail_ansible_sequential_reboot_retry.log"
LOGGER = utils.get_logger("dellemc_vxrail_sequential_reboot_retry", LOG_FILE_PATH, log_devel=logging.DEBUG)
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
        self.request_id = module.params.get('request_id')
        self.all = module.params.get('all')
        self.hosts = module.params.get('hosts')
        self.api_version_number = module.params.get('api_version_number')

        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    def get_versioned_response(self, api_instance, module_path, sequential_reboot_retry_info,request_id):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path,
                                                                   LOGGER)

        # Calls versioned method as attribute (ex: v1_sequential_reboot_retry)
        call_string = self.api_version_string + '_sequential_reboot_retry'
        LOGGER.info("Using utility method: %s\n", call_string)
        sequential_reboot_retry_post = getattr(api_instance, call_string)
        return sequential_reboot_retry_post(sequential_reboot_retry_info,request_id)

    def sequential_reboot_retry(self):
        sequential_reboot_retry_return_info = {}
        sequential_reboot_retry_info = {
            'all': self.all
        }

        if self.hosts:
            sequential_reboot_retry_info['hosts'] = []
            for hostname in self.hosts:
                sequential_reboot_retry_info['hosts'].append({'hostname':hostname})
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SequentialRebootApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        LOGGER.info(sequential_reboot_retry_info)
        try:
            # post sequential reboot apply
            response = self.get_versioned_response(api_instance, "POST /sequential-reboot/{request_id}/retry", sequential_reboot_retry_info, self.request_id)
        except ApiException as e:
            LOGGER.error("Exception when calling SequentialRebootApi->%s_sequential_reboot_retry: %s\n",
                         self.api_version_string, e)
            return 'error'
        data = response
        sequential_reboot_retry_return_info['request_id'] = data.request_id

        return dict(sequential_reboot_retry_return_info.items())



def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        request_id=dict(required=True),
        all=dict(type='bool',default=False),
        hosts=dict(type='list', elements='str'),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().sequential_reboot_retry()
    if result == 'error':
        module.fail_json(
            msg=f"Call POST /sequential-reboot/retry API failed,please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts = {'Sequential_Reboot': result}
    vx_facts_result = dict(changed=True, Sequential_Reboot=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()