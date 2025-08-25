#!/usr/bin/python
# Copyright 2022 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_callhome_enable

short_description: Enable call home functionality by enabling remote connectivity service

description:
- This module will enable call home functionality by enabling remote connectivity service.
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

  serial_number:
    description:
      The node serial number for ESE enablement of both v1 and v2 API version
    required: False
    type: str
  
  appliance_id:
    description:
      The node appliance ID for ESE enablement of v3 API version
    required: False
    type: str

  connection_type:
    description:
      The connection type of callhome, allowed values is DIRECT and GATEWAY
    required: True
    type: str

  pin:
    description:
      the PIN code
    required: False
    type: str

  access_key:
    description:
      the access key
    required: False
    type: str

  proxy_type:
    description:
      The type of proxy, allowed values is USER,SYSTEM and NA
    required: False
    type: str

  proxy_protocol:
    description:
      The protocol of proxy, allowed values is SOCK5, HTTP and HTTPS
    required: False
    type: str

  proxy_address:
    description:
      The address of proxy
    required: False
    type: str

  proxy_port:
    description:
      The port of proxy
    required: False
    type: str

  proxy_user:
    description:
      The user account of the proxy
    required: False
    type: str

  proxy_passwd:
    description:
      The password for the user account provided in proxy
    required: False
    type: str

  gateways_host:
    description:
      The host ip of gateways
    required: False
    type: str

  gateways_port:
    description:
      The port of gateways
    required: False
    type: str

  customer_contact_order:
    description:
      The contact order of customer
    required: False
    type: int

  customer_first_name:
    description:
      The first name of customer
    required: False
    type: str

  customer_last_name:
    description:
      The last name of customer
    required: False
    type: str

  customer_email_address:
    description:
      The email address of customer
    required: False
    type: str

  customer_phone_number:
    description:
     The phone_number of customer
    required: False
    type: str

  customer_pref_language:
    description:
     The preferred language of customer
    required: False
    type: str

  timeout:
    description:
      Time out value for enabling callhome, the default value is 300 seconds
    required: false
    type: int
    default: 300
    
  ip_version:
    description:
      IP version of remote connector. Allowed values are IPV4 and IPV6
    required: False
    type: str
    
  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: false
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Enable call home functionality
    dellemc_vxrail_callhome_enable:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        appliance_id: "{{ appliance_id }}"
        connection_type: "{{ connection_type }}"
        pin: "{{ pin }}"
        access_key: "{{ access_key }}"
        proxy_type: "{{ proxy_type }}"
        proxy_protocol: "{{ proxy_protocol }}"
        proxy_address: "{{ proxy_address }}"
        proxy_port: "{{ proxy_port }}"
        proxy_user: "{{ proxy_user }}"
        proxy_passwd: "{{ proxy_passwd }}"
        gateways_host: "{{ gateways_host }}"
        gateways_port: "{{ gateways_port }}"
        customer_contact_order: "{{ customer_contact_order }}"
        customer_first_name: "{{ customer_first_name }}"
        customer_last_name: "{{ customer_last_name }}"
        customer_phone_number: "{{ customer_phone_number }}"
        customer_email_address: "{{ customer_email_address }}"
        customer_pref_language: "{{ customer_pref_language }}"
        timeout: "{{ timeout }}"
        ip_version: "{{ ip_version }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Enable_Callhome_API:
  description: Enable call home functionality
  returned: always
  type: dict
  sample: >-
    {
      "message": "Callhome is enabled successfully."
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

MODULE = "dellemc_vxrail_callhome_enable"
LOG_FILE_PATH = "/tmp/vxrail_ansible_callhome_enable.log"
LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
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
        self.connection_type = module.params.get('connection_type')
        self.pin = module.params.get('pin')
        self.access_key = module.params.get('access_key')
        self.proxy_type = module.params.get('proxy_type')
        self.proxy_protocol = module.params.get('proxy_protocol')
        self.proxy_address = module.params.get('proxy_address')
        self.proxy_port = module.params.get('proxy_port')
        self.proxy_user = module.params.get('proxy_user')
        self.proxy_passwd = module.params.get('proxy_passwd')
        self.gateways_host = module.params.get('gateways_host')
        self.gateways_port = module.params.get('gateways_port')
        self.customer_contact_order = module.params.get('customer_contact_order')
        self.customer_first_name = module.params.get('customer_first_name')
        self.customer_last_name = module.params.get('customer_last_name')
        self.customer_phone_number = module.params.get('customer_phone_number')
        self.customer_email_address = module.params.get('customer_email_address')
        self.customer_pref_language = module.params.get('customer_pref_language')
        self.ip_version = module.params.get('ip_version')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_number = module.params.get('api_version_number')

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path,
                                                                   LOGGER)
        call_string = self.api_version_string + '_callhome_enable_post'

        LOGGER.info("Using utility method: %s\n", call_string)
        api_callhome_enable_post = getattr(api_instance, call_string)
        callhome_info = self.create_callhome_json()
        return api_callhome_enable_post(callhome_info)

    def create_callhome_json(self):
        self.serial_number = module.params.get('serial_number', None)
        self.appliance_id = module.params.get('appliance_id', None)
        
        # Validation: Only one of serial_number or appliance_id must be provided
        if bool(self.serial_number) == bool(self.appliance_id):
            raise ValueError("You must provide either 'serial_number' or 'appliance_id'.")
        if self.api_version_number <= 2 and self.serial_number is None:
            raise ValueError("Serial number is required for API version less than 2.")
        if self.api_version_number > 2 and self.appliance_id is None:
            raise ValueError("Appliance ID is required for API version greater than 2.")

        callhome_info = {
            'connection_type': self.connection_type
        }

        # Include only the one that was provided
        if self.serial_number:
            callhome_info['serial_number'] = self.serial_number
        else:
            callhome_info['appliance_id'] = self.appliance_id

        # Add optional params if found
        if self.pin is not None:
            callhome_info['pin'] = self.pin
        if self.access_key is not None:
            callhome_info['access_key'] = self.access_key
        if self.proxy_type is not None:
            callhome_info['proxy_type'] = self.proxy_type
        if self.proxy_address is not None:
            proxy_spec = {
                "protocol": self.proxy_protocol,
                "address": self.proxy_address,
                "port": self.proxy_port,
                "user": self.proxy_user,
                "password": self.proxy_passwd
            }
            callhome_info['proxy'] = proxy_spec

        if self.gateways_host is not None:
            gateways_spec = [
                {
                    "host": self.gateways_host,
                    "port": self.gateways_port,
                }
            ]
            callhome_info['gateways'] = gateways_spec

        if self.customer_contact_order is not None:
            customer_contact_spec = [
                {
                    "contact_order": self.customer_contact_order,
                    "first_name": self.customer_first_name,
                    "last_name": self.customer_last_name,
                    "phone_number": self.customer_phone_number,
                    "email_address": self.customer_email_address,
                    "pref_language": self.customer_pref_language,
                }
            ]
            callhome_info['customer_contact_infos'] = customer_contact_spec
        if self.api_version_number >= 2:
          callhome_info['ip_version'] = self.ip_version
        return callhome_info

    def enable_callhome(self):
        api_instance = vxrail_ansible_utility.CallHomeOperationsApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = self.get_versioned_response(api_instance, 'Post callhome/enable')
        except ApiException as e:
            LOGGER.error("Exception when calling CallHomeOperationsApi->%s_callhome_enable_post: %s\n",
                         self.api_version_string, e)
            return 'error'
        LOGGER.info("Call %s/callhome/enable POST api response: %s\n", self.api_version_string, response)
        return response


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(type='str', required=True),
        vcpasswd=dict(type='str', required=True, no_log=True),
        serial_number=dict(type='str', required=False),
        appliance_id=dict(type='str', required=False),
        connection_type=dict(type='str', required=True),
        pin=dict(type='str', required=False),
        access_key=dict(type='str', required=False),
        proxy_type=dict(type='str', required=False),
        proxy_protocol=dict(type='str', required=False),
        proxy_address=dict(type='str', required=False),
        proxy_port=dict(type='str', required=False),
        proxy_user=dict(type='str', required=False),
        proxy_passwd=dict(type='str', required=False, no_log=True),
        gateways_host=dict(type='str', required=False),
        gateways_port=dict(type='str', required=False),
        customer_contact_order=dict(type='int', required=False),
        customer_first_name=dict(type='str', required=False),
        customer_last_name=dict(type='str', required=False),
        customer_phone_number=dict(type='str', required=False),
        customer_email_address=dict(type='str', required=False),
        customer_pref_language=dict(type='str', required=False),
        timeout=dict(type='int', default=300),
        ip_version=dict(type='str', required=False),
        api_version_number=dict(type='int')
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().enable_callhome()
    if result == 'error':
        module.fail_json(
            msg="Call Callhome Enable API failed,please see log file /tmp/vxrail_ansible_callhome_enable.log for more error details.")
    vx_facts = {'msg': "Callhome is enabled successfully."}
    vx_facts_result = dict(changed=False, Callhome_Enanle_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
