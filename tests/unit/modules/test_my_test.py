from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import unittest
from unittest.mock import patch

from ansible.module_utils import basic
from ansible_collections.dellemc.vxrail.plugins.modules import my_test
from ansible_collections.dellemc.vxrail.tests.unit.modules.utils import set_module_args, exit_json, fail_json, AnsibleExitJson

class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_run_module(self):
        with patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json):
            set_module_args(
                {
                    "name": "helloworld",
                    "new": True,
                }
            )

            with self.assertRaises(AnsibleExitJson) as result:
                my_test.main()
            self.assertTrue(result.exception.args[0]['changed'])
            self.assertEqual(result.exception.args[0]['message'],'goodbye')


if __name__ == "__main__":
    unittest.main()
