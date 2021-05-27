from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import unittest

from unittest import mock
from unittest.mock import patch, Mock
from ansible.module_utils import basic
from ansible_collections.dellemc.vxrail.plugins.modules import dellemc_vxrail_disk
from ansible_collections.dellemc.vxrail.tests.unit.modules.utils import set_module_args, exit_json, fail_json, AnsibleExitJson
from vxrail_ansible_utility.api.disk_drive_information_api import DiskDriveInformationApi
from vxrail_ansible_utility.models.disk_info import DiskInfo


class TestDellEmcVxrailDisk(unittest.TestCase):

    def setUp(self):
        self.api_query_result = DiskInfo()
        self.api_query_result.sn = 'sn123456'
        self.api_query_result.disk_type = 'disk_type12356'

        self.api_query_disks_result = [self.api_query_result]

    @mock.patch.object(DiskDriveInformationApi, 'v1_disks_disk_sn_get')
    def test_get_disk_with_sn(self, v1_disks_disk_sn_get):
        with patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json):
            v1_disks_disk_sn_get.return_value = self.api_query_result
            set_module_args(
                {
                    "disk_sn": "sn123",
                    "vcadmin": "adm",
                    "vcpasswd": "pwd",
                    "vxmip": "ip"
                }
            )

            with self.assertRaises(AnsibleExitJson) as result:
                dellemc_vxrail_disk.main()
            print(result.exception.args[0]['ansible_facts']['disks'][0]['sn'])
            self.assertFalse(result.exception.args[0]['changed'])
            self.assertEqual(result.exception.args[0]['ansible_facts']['disks'][0]['sn'], 'sn123456')
            self.assertEqual(result.exception.args[0]['ansible_facts']['disks'][0]['disk_type'], 'disk_type12356')

    @mock.patch.object(DiskDriveInformationApi, 'v1_disks_get')
    def test_get_disks(self, v1_disks_get):
        with patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json):
            v1_disks_get.return_value = self.api_query_disks_result
            set_module_args(
                {
                    "disk_sn": "all",
                    "vcadmin": "adm",
                    "vcpasswd": "pwd",
                    "vxmip": "ip"
                }
            )

            with self.assertRaises(AnsibleExitJson) as result:
                dellemc_vxrail_disk.main()
            print(result.exception.args[0]['ansible_facts']['disks'][0]['sn'])
            self.assertFalse(result.exception.args[0]['changed'])
            self.assertEqual(result.exception.args[0]['ansible_facts']['disks'][0]['sn'], 'sn123456')
            self.assertEqual(result.exception.args[0]['ansible_facts']['disks'][0]['disk_type'], 'disk_type12356')


if __name__ == "__main__":
    unittest.main()
