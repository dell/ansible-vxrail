from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import pytest
import unittest
import mock
from unittest import mock
from unittest.mock import patch, Mock

from ansible.module_utils import basic
from plugins.modules import my_test
from utils import set_module_args, exit_json, AnsibleExitJson, fail_json


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_run_module(self):
        m = mock.mock_open()
        with patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json):
            set_module_args(
                {
                    "name": "helloworld",
                    "new": True,
                }
            )

            with pytest.raises(AnsibleExitJson) as result:
                my_test.main()
            print('-------------------------')
            print(result)
            print('-------------------------')
if __name__ == "__main__":
    unittest.main()
