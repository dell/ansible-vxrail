#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_getprecheckprofiles

short_description: Retrieve the list precheck profiles.

description:
- Get a list of available precheck profiles. Each profile represents a different type of precheck that you can perform.
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
      Time out value for getting system precheck profiles information, the default value is 60 seconds
    required: false
    type: int
    default: 60

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: false
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get system precheck profiles information
    dellemc_vxrail_system_getprecheckprofiles:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Precheck_Profiles:
  description: List precheck profiles
  returned: always
  type: dict
  sample: >-
        {
            "description": "This is to check if new node is compatible with the configured nodes in the cluster.
            It is used in the scenario that user perform a validation before performing node expansion.
            When the precheck is run by calling /v1/system/precheck with the profile, the parameter node_list is required",
            "profile": "NODE_EXPANSION"
        },
        {
            "description": "This is used to check pre-upgrade issues before performing VxRail System upgrade.
            When the precheck is run by calling /v1/system/precheck with the profile, the parameters vxm_root_user,
            vc_admin_user, vc_root_user, witness_spec and migration_spec are expected.",
            "profile": "PRE_UPGRADE"
        },
        {
            "description": "This is used for daily proactive precheck.  E.g. checking whether specific critical
            VC/VSAN alarms have been triggered.   When the precheck is run by calling /v1/system/precheck with
            the profile, the parameter vc_admin_user is optional.",
            "profile": "PROACTIVE_HEALTH"
        }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_system_getprecheckprofiles", "/tmp/vxrail_ansible_system_getprecheckprofiles.log", log_devel=logging.DEBUG)
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

        # Calls versioned method as attribute (ex: v1_system_prechecks_profiles_get)
        call_string = self.api_version_string + '_system_prechecks_profiles_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        system_prechecks_profiles = getattr(api_instance, call_string)
        return system_prechecks_profiles()

    def get_precheck_profiles(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemPreCheckApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # query Prechecks Profiles API
            response = self.get_versioned_response(api_instance, "GET /system/prechecks/profiles")
        except ApiException as e:
            LOGGER.error("Exception when calling SystemPreCheckApi->%s_system_prechecks_profiles_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/system/prechecks/profiles api response: %s\n", self.api_version_string, response)
        PrecheckProfiles = {}
        PrecheckProfiles_list = []
        for i in range(len(response)):
            PrecheckProfiles['profile'] = response[i].profile
            PrecheckProfiles['description'] = response[i].description
            PrecheckProfiles_list.append(dict(PrecheckProfiles.items()))
        return PrecheckProfiles_list


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().get_precheck_profiles()
    if result == 'error':
        module.fail_json(msg="Call GET /system/prechecks/profiles API failed,"
                             "please see log file /tmp/vxrail_ansible_system_getprecheckprofiles.log for more error details.")
    vx_facts = {'Precheck_Profiles': result}
    vx_facts_result = dict(changed=False, Precheck_Profiles_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
