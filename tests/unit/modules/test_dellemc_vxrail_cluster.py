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


class ExpansionResponse():
    pass


class TestDellEmcVxrailCluster(unittest.TestCase):

    def setUp(self):
        self.request_id = "request_id"
        self.expansion_response = ExpansionResponse()
        self.expansion_response.request_id = self.request_id
        self.expansion_response.state = 'COMPLETED'
        self.expansion_response.owner = 'owner1'
        self.expansion_response.progress = 100
        self.expansion_response.extension = '{"hosts":[{"name": "hostname"}]}'
        self.expansion_response.start_time = '123456'
        self.expansion_response.end_time = '123457'
        self.expansion_response.id = 123

    @mock.patch.object(ClusterExpansionApi, 'v1_cluster_expansion_validate_post')
    @mock.patch.object(ClusterShutdownApi, 'v1_requests_id_get')
    @mock.patch.object(ClusterExpansionApi, 'v1_cluster_expansion_post')
    def test_node_operation(self, v1_cluster_expansion_validate_post, v1_requests_id_get, v1_cluster_expansion_post):
        with patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json):
            v1_cluster_expansion_validate_post.return_value.request_id = self.request_id
            v1_cluster_expansion_post.return_value.request_id = self.request_id
            v1_cluster_expansion_post.return_value.state = 'COMPLETED'
            v1_requests_id_get.side_effect = [self.expansion_response, self.expansion_response]
            v1_requests_id_get.return_value = self.expansion_response

            set_module_args(
                {
                    "vxmip": "vxmip",
                    "vxm_version": "vxm_version",
                    "timeout": 50,
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
                dellemc_vxrail_cluster.main()


if __name__ == "__main__":
    unittest.main()
