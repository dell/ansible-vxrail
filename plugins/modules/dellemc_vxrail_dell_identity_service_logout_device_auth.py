#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dellemc_vxrail_dell_identity_service_logout_device_auth

short_description: Purge the existing support account configuration

description:
- Purge the existing support account configuration. This also revokes the refresh token cached by the token service. The access token used will not be revoked.
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

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for cancelling the host shutdown, the default value is 60 seconds
    required: False
    type: int
    default: 1800

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

"""

EXAMPLES = r"""
    - name: Logout device authentication via Dell Identity Service
      dellemc_vxrail_dell_identity_service_logout_device_auth:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
"""

RETURN = r"""
"""

import logging

import urllib3
import vxrail_ansible_utility
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.vxrail.plugins.module_utils import (
    dellemc_vxrail_ansible_utils as utils,
)
from vxrail_ansible_utility.rest import ApiException

# Defining global variables
API = "/device-auth/logout"
MODULE = "dellemc_vxrail_dell_identity_service_logout_device_auth"
LOG_FILE_PATH = "/tmp/vxrail_ansible_dell_identity_service_logout_device_auth.log"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
CHECK_STATUS_INTERVAL = 30
MAX_CHECK_COUNT = 60


class VxrailClusterUrls:
    cluster_url = "https://{}/rest/vxm"

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailClusterUrls.cluster_url.format(self.vxm_ip)


class VxRailCluster:
    def __init__(self):
        self.vxm_ip = module.params.get("vxmip")
        self.timeout = module.params.get("timeout")
        self.vc_admin = module.params.get("vcadmin")
        self.vc_password = module.params.get("vcpasswd")
        self.api_version_number = module.params.get("api_version_number")
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        # Added for auto-version detection
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split("v")[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute (ex: v1_post_logout_device_auth)
        call_string = self.api_version_string + "_post_logout_device_auth"
        LOGGER.info("Using utility method: %s\n", call_string)

        # get the parameters
        params = self.getRequestParams()
        LOGGER.info(f"params: {params}")

        api_func = getattr(api_instance, call_string)
        return api_func(**params)

    def getRequestParams(self):
        params = {
            # if you don't set the _preload_content to False, the response will become a string.
            "_preload_content": False,
        }

        return params

    def logout_device_auth(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.TokenServiceApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            return self.get_versioned_response(api_instance, "Post /device-auth/logout")
        except ApiException as e:
            LOGGER.error(
                "Exception when calling Dell Identity ServiceApi->%s_post_logout_device_auth: %s\n", self.api_version_string, e
            )
            return "error"


def main():
    """Entry point into execution flow"""
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        api_version_number=dict(type="int", required=False),
        timeout=dict(type="int", default=1800),
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    LOGGER.info("---- Dell Identity Service logout device authentication: ----")
    response = VxRailCluster().logout_device_auth()
    if response == "error":
        module.fail_json(msg=f"Call {API} API failed, please see log file {LOG_FILE_PATH} for more error details.")

    LOGGER.info(f"Http Result: Status code - {response.status}, URL - {response.geturl()}, Headers - {response.headers}")
    module.exit_json(changed=True, message=f"Dell Identity Service logout device authentication successfully")


if __name__ == "__main__":
    main()
