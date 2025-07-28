#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_change_vxmipaddress

short_description: Change the VxRail manager IP address

description:
- This module will Change the VxRail manager IP address
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

  vcroot:
    description:
      root account of the vCenter Server the VxRail Manager is registered to
    required: True
    type: str

  vcroot_passwd:
    description:
      The password for the root account provided in vcroot
    required: True
    type: str
    
  ip:
    description:
      The new IP address to assign to the VxRail manager
    required: False
    type: str

  gateway:
    description:
      The new gateway IP for the VxRail manager
    required: False
    type: str

  netmask:
    description:
      The new subnet mask for the VxRail manager
    required: False
    type: str

  ipv6:
    description:
      The new IPv6 address to assign to the VxRail manager
    required: False
    type: str

  gateway_ipv6:
    description:
      The new gateway IPv6 for the VxRail manager
    required: False
    type: str

  prefix_length_ipv6:
    description:
      The new prefix length for the VxRail manager
    required: False
    type: int

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for getting telemetry information, the default value is 300 seconds
    required: false
    type: int
    default: 900

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Change the VxRail manager IP address
    dellemc_vxrail_change_vxmipaddress:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        vcroot: "{{ vcroot }}"
        vcroot_passwd: "{{ vcroot_passwd }}"
        ip: "{{ ip }}"
        gateway: "{{ gateway }}"
        netmask: "{{ netmask }}"
        ipv6: "{{ ipv6 }}"
        gateway_ipv6: "{{ gateway_ipv6 }}"
        prefix_length_ipv6: "{{ prefix_length_ipv6 }}"
'''


import logging
import urllib3
import time
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_system_vxmipaddress_change.log", "/tmp/vxrail_ansible_system_vxmipaddress_change.log", log_devel=logging.DEBUG)
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
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.api_version_number = module.params.get('api_version_number')
        self.vc_root = module.params.get('vcroot')
        self.vc_root_password = module.params.get('vcroot_passwd')
        self.ip = module.params.get('ip')
        self.gateway = module.params.get('gateway')
        self.netmask = module.params.get('netmask')
        self.ipv6 = module.params.get('ipv6')
        self.gateway_ipv6 = module.params.get('gateway_ipv6')
        self.prefix_length_ipv6 = module.params.get('prefix_length_ipv6')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    def get_versioned_response(self, api_instance, module_path, vxmip_change_info):
        # Set api version string and version number if undefined
        try:
          if self.api_version_number is None:
              self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
              self.api_version_number = int(self.api_version_string.split('v')[1])
          else:
              self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)
          call_string = self.api_version_string + '_system_vxm_ipaddress_' + 'post'
        except:
          call_string = "v1_system_vxm_ipaddress_post"
          
        # Calls versioned method as attribute      
        LOGGER.info("Using utility method: %s\n", call_string)
        system_vxm_ipaddress_post = getattr(api_instance, call_string)
        return system_vxm_ipaddress_post(body=vxmip_change_info)

    def post_system_vxm_ipaddress(self):
        return_info = {}
        vxmip_change_info = {
            "vxm_info": {},
            "vc_admin_user": {"username": self.vc_admin, "password": self.vc_password},
            "vc_root_user": {"username": self.vc_root, "password": self.vc_root_password},
        }
        if self.ip:
            vxmip_change_info["vxm_info"]["ip"] = self.ip
        if self.gateway:
            vxmip_change_info["vxm_info"]["gateway"] = self.gateway
        if self.netmask:
            vxmip_change_info["vxm_info"]["netmask"] = self.netmask
        if self.ipv6:
            vxmip_change_info["vxm_info"]["ipv6"] = self.ipv6
        if self.gateway_ipv6:
            vxmip_change_info["vxm_info"]["gateway_ipv6"] = self.gateway_ipv6
        if self.prefix_length_ipv6:
            vxmip_change_info["vxm_info"]["prefix_length_ipv6"] = self.prefix_length_ipv6

        LOGGER.info("Sending Configuration: %s", vxmip_change_info)

        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemInformationApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = self.get_versioned_response(api_instance, "POST /system/vxm-ipaddress", vxmip_change_info)
        except ApiException as e:
            LOGGER.error("Exception when calling SystemInformationApi->%s_system_vxm_ipaddress_post: %s\n",
                         self.api_version_string, e)
            return 'error'
        data = response
        return_info['request_id'] = data.request_id

        return dict(return_info.items())


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        vcroot=dict(required=True),
        vcroot_passwd=dict(required=True, no_log=True),
        ip=dict(required=False),
        gateway=dict(required=False),
        netmask=dict(required=False),
        ipv6=dict(required=False),
        gateway_ipv6=dict(required=False),
        prefix_length_ipv6=dict(type='int', required=False),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=900)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().post_system_vxm_ipaddress()
    if result == 'error':
        module.fail_json(msg="Call POST system/vxm-ipaddress API failed,"
                             "please see log file /tmp/vxrail_ansible_system_vxnipaddress_change.log for more error details.")
    # vx_facts_result = dict(changed=True, Change_VxM_IPaddress=result)
    # module.exit_json(**vx_facts_result)
    result_request_id = result['request_id']
    LOGGER.info('Request_id: %s.', result['request_id'])
    vxmip = module.params.get('vxmip')
    newvxmip = module.params.get('ip') if module.params.get('ip') else '[{}]'.format(module.params.get('ipv6'))
    vcadmin = module.params.get('vcadmin')
    vcpasswd = module.params.get('vcpasswd')
    task_state = 0
    time_out = 0
    initial_timeout = module.params.get('timeout')
    LOGGER.info('Timeout setting: %s seconds.', initial_timeout)
    # Check call to v1/requests/{request_id}
    result_response = utils.get_request_status(vxm_ip=vxmip, vcadmin=vcadmin, vcpasswd=vcpasswd, logger=LOGGER, request_id=result_request_id)
    if result_response == 'error':
        module.fail_json(msg="Call v1/requests/request_id API failed,please see "
                             "log file /tmp/vxrail_ansible_system_vxmipaddress_change.log for more error details.")
    else:
        LOGGER.info('No issues found in call to v1/requests/request_id API. Begin checking status of operation.')
    while task_state not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        ''' call frequently to capture 'COMPLETED' status '''
        LOGGER.info('Request_status is not COMPLETED yet.')
        time_out = time_out + 10
        time.sleep(10)
        try:
            result_response = utils.get_request_status(vxm_ip=vxmip, vcadmin=vcadmin, vcpasswd=vcpasswd, logger=LOGGER, request_id=result_request_id)
            task_state = result_response.state
            LOGGER.info('Request_status: %s, Request_steps: %s', task_state, result_response.extension)
            continue
        except:
            LOGGER.info('Request %s failed, try %s', vxmip, newvxmip)
            
        try:
            result_response = utils.get_request_status(vxm_ip=newvxmip, vcadmin=vcadmin, vcpasswd=vcpasswd, logger=LOGGER, request_id=result_request_id)
            task_state = result_response.state
            LOGGER.info('Request_status: %s, Request_steps: %s', task_state, result_response.extension)
        except:
            LOGGER.info('Request %s failed, wait for 10 seconds', newvxmip)

    error_message = result_response.error
    if task_state == 'COMPLETED' and not error_message:
        LOGGER.info("change VxM IPaddress Completed")
        vx_facts = {'Request_ID': result_request_id, 'Request_Status': task_state}
        vx_facts_result = dict(changed=True, Change_VxM_IPaddress=vx_facts, msg=task_state)
    else:
        LOGGER.info("change VxM IPaddress Failed")
        vx_facts = {'Request_ID': result_request_id}
        vx_facts_result = dict(failed=True, Change_VxM_IPaddress=vx_facts, msg=error_message)
    LOGGER.info('Request_info: %s', result_response)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
