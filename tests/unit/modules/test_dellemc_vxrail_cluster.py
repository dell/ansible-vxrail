from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import unittest

from unittest import mock
from unittest.mock import patch, Mock
from ansible.module_utils import basic
from ansible_collections.dellemc.vxrail.plugins.modules import dellemc_vxrail_cluster
from ansible_collections.dellemc.vxrail.tests.unit.modules.utils import set_module_args, exit_json, fail_json, AnsibleExitJson
from vxrail_ansible_utility.api.cluster_expansion_api import ClusterExpansionApi
from vxrail_ansible_utility.api.cluster_shutdown_api import ClusterShutdownApi


class TestDellEmcVxrailCluster(unittest.TestCase):

    def setUp(self):
        self.request_id = "request_id"

    @mock.patch.object(ClusterExpansionApi, 'v1_cluster_expansion_validate_post')
    @mock.patch.object(ClusterShutdownApi, 'v1_requests_id_get')
    @mock.patch.object(ClusterExpansionApi, 'v1_cluster_expansion_post')
    def test_node_operation(self, v1_cluster_expansion_validate_post, v1_requests_id_get, v1_cluster_expansion_post):
        with patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json):
            v1_cluster_expansion_validate_post.return_value.request_id = self.request_id
            v1_cluster_expansion_post.return_value.request_id = self.request_id
            v1_requests_id_get.return_value.state = 'FAILED'
            v1_cluster_expansion_post.return_value.state = 'COMPLETED'
            v1_requests_id_get.return_value.owner = ''
            v1_requests_id_get.return_value.progress = 100
            v1_requests_id_get.return_value.extension = '{"hosts":[{"name": "hostname"}]}'
            v1_requests_id_get.return_value.start_time = '123456'
            v1_requests_id_get.return_value.end_time = '123457'

            set_module_args(
                {
                    "vxmip": "vxmip",
                    "vxm_version": "vxm_version",
                    "timeout": 10,
                    "vcadmin": "vc_admin",
                    "vcpasswd": "vc_password",
                    "host_psnt": "host_psnt",
                    "hostname": "hostname",
                    "mgt_account": "mgt_account",
                    "mgt_passwd": "mgt_passwd",
                    "mgt_ip": "mgt_ip",
                    "vmotion_ip": "vmotionip",
                    "vsan_ip": "vsanip",
                    "rack_name": "rackname",
                    "order_number": "order_number",
                    "root_passwd": "root_passwd",
                    "nic_profile": "FOUR_HIGH_SPEED",
                    "maintenance_mode": False
                }
            )

            with self.assertRaises(AnsibleExitJson) as result:
                try:
                    dellemc_vxrail_cluster.main()
                except AssertionError as e:
                    assert isinstance(e, AssertionError)


if __name__ == "__main__":
    unittest.main()
