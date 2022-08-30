#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: dellemc_vxrail_satellite_node_remove
short_description: Remove a satellite host from the cluster
# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.4.0"
description:
- This module will Remove a satellite host from the cluster.
options:
  vxmip:
    description:
      The IP address of the VxRail Manager System
    required: True
    type: str
  host_sn:
    description:
      Serial number of the host to be removed
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
      Time out value for Day1 bring up, the default value is 1800 seconds
    required: false
    type: int
    default: 1800
  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: false
    type: int
author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>
'''

EXAMPLES = r'''
- name: Remove a node
  dellemc_vxrail_satellite_node_remove:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        host_sn: "{{ host_sn }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
Remove_Node_status:
  description: Node Removal status summary
  returned: always
  type: dict
  sample: >-
   {
    "Remove_Node": {
        "host_sn": "BB8VG03"
    }
    "msg": "Removing Node is successful. Please see the /tmp/vxrail_ansible_satellite_node_remove.log for more details"
   }
'''

import logging
import traceback
from ansible.module_utils.basic import AnsibleModule, missing_required_lib

LOG_FILE_NAME = "/tmp/vxrail_ansible_satellite_node_remove.log"

try:
    import urllib3
    import vxrail_ansible_utility
    from vxrail_ansible_utility.rest import ApiException
    from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils
    LOGGER = utils.get_logger("dellemc_vxrail_satellite_node_remove", LOG_FILE_NAME, log_devel=logging.DEBUG)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except ImportError:
    HAS_ANOTHER_LIBRARY = False
    ANOTHER_LIBRARY_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_ANOTHER_LIBRARY = True


class VxrailVXMUrls():
    vxm_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailVXMUrls.vxm_url.format(self.vxm_ip)


class VxRailRemoveSatelliteNode():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.host_sn = module.params.get('host_sn')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.api_version_number = module.params.get('api_version_number')
        self.vxm_url = VxrailVXMUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.vxm_url.set_host()

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path, host_sn):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        call_string = 'remove_satellite_host'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_remove_satellite_host = getattr(api_instance, call_string)
        return api_remove_satellite_host(host_sn)

    def remove_satellite_node(self, host_sn):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SatelliteNodeExpansionApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # start Node Removal
            self.get_versioned_response(api_instance, "/host-folder/hosts/{sn}", host_sn)
        except ApiException as e:
            LOGGER.error("Exception when calling SatelliteNodeRemoveApi->remove_satellite_host: %s\n", e)
            return "error"
        return "success"


def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        host_sn=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        timeout=dict(type='int', default=30 * 60),
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

    LOGGER.info('----Start to remove satellite node: %s.----', module.params.get('host_sn'))
    rmnode_result = VxRailRemoveSatelliteNode().remove_satellite_node(module.params.get('host_sn'))
    if rmnode_result == "error":
        module.fail_json(
            msg="Exception when calling SatelliteNodeRemoveApi->remove_satellite_host."
                "Please see the /tmp/vxrail_ansible_satellite_node_remove.log for more details")
    else:
        LOGGER.info("-------The Satellite Node has been successfully removed-----")
        vx_rmnode = {'host_sn': module.params.get('host_sn')}
        vx_facts_result = dict(changed=True, Remove_Node=vx_rmnode,
                               msg="Removing Satellite_Node is successful. Please see the /tmp/vxrail_ansible_satellite_node_remove.log for more details")
        module.exit_json(**vx_facts_result)


if __name__ == '__main__':
    main()
