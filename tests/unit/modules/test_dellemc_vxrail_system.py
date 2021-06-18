from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import unittest

from unittest import mock
from unittest.mock import patch, Mock
from ansible.module_utils import basic
from ansible_collections.dellemc.vxrail.plugins.modules import dellemc_vxrail_system
from ansible_collections.dellemc.vxrail.tests.unit.modules.utils import set_module_args, exit_json, fail_json, AnsibleExitJson
from vxrail_ansible_utility.api.system_information_api import SystemInformationApi


class TestDellEmcVxrailSystem(unittest.TestCase):

    def setUp(self):
        pass

    @mock.patch.object(SystemInformationApi, 'query_vx_rail_manager_system_information_v3')
    def test_v3_system(self, query_vx_rail_manager_system_information_v3):
        with patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json):
            query_vx_rail_manager_system_information_v3.return_value.description = "description"
            query_vx_rail_manager_system_information_v3.return_value.version = "version"
            query_vx_rail_manager_system_information_v3.return_value.health = "health"
            query_vx_rail_manager_system_information_v3.return_value.installed_time = "installed_time"
            query_vx_rail_manager_system_information_v3.return_value.number_of_host = "number_of_host"
            query_vx_rail_manager_system_information_v3.return_value.is_external_vc = False
            query_vx_rail_manager_system_information_v3.return_value.network_connected = "network_connected"
            query_vx_rail_manager_system_information_v3.return_value.vc_connected = "vc_connected"
            query_vx_rail_manager_system_information_v3.return_value.deployment_type = "deployment_type"
            query_vx_rail_manager_system_information_v3.return_value.logical_view_status = "logical_view_status"

            set_module_args(
                {
                    "vcadmin": "adm",
                    "vcpasswd": "pwd",
                    "vxmip": "ip",
                    "timeout": 60
                }
            )

            with self.assertRaises(AnsibleExitJson) as result:
                dellemc_vxrail_system.main()
            self.assertEqual(result.exception.args[0]['V3_System_API']['System_Information'][0]['description'], 'description')
            self.assertEqual(result.exception.args[0]['V3_System_API']['System_Information'][0]['version'], 'version')
            self.assertFalse(result.exception.args[0]['changed'])


if __name__ == "__main__":
    unittest.main()
