#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_system_getprechecksreport

short_description: Get all or one pre-check report using a specified request ID.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.5.0"

description:
- Get a pre-check report using a specified request ID.
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

  id:
    description:
      Request ID of the pre-check status that you want to query
    required: false
    type: str

  timeout:
    description:
      Time out value for getting a system precheck report information, the default value is 60 seconds
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
  - name: Get prechecks reports
    dellemc_vxrail_system_getprechecksreport:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        id: "{{ id }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Prechecks_Report:
  description: A precheck report
  returned: always
  type: dict
  sample: >-
        {
          "id": "ba8901c1-913b-4a2b-9b62-d358bcc2ed47",
          "profile": "string",
          "status": "IN-PROGRESS [IN-PROGRESS,COMPLETED]",
          "progress": "50%",
          "total_severity": "OK [OK, WARN, ERROR, CRITICAL]",
          "complete_check_count": 25,
          "total_success_count": 22,
          "total_warn_count": 0,
          "total_error_count": 3,
          "results": {
            "host_checks": [
              {
                "host_id": "c2-esx01",
                "checks": [
                  {
                    "status": "COMPLETED",
                    "check_id": "vcsa_state_check",
                    "start_time": "string",
                    "end_time": "string",
                    "plugin_name": "string",
                    "plugin_version": "1.0.100",
                    "result": {
                      "severity": "OK [OK, WARN, ERROR, CRITICAL]",
                      "messages": [
                        {
                          "id": "VXR304RADAR0003",
                          "kb": "string",
                          "action": "Ensure there are not critical alarms existing on VCSA.",
                          "alphaid": "check_script_failed",
                          "symptom": "There are critical alarms existing on VCSA.",
                          "severity": "Error [Ok, Warn, Error, Critical]"
                        }
                      ]
                    }
                  }
                ]
              }
            ],
            "general_checks": [
              {
                "status": "COMPLETED",
                "check_id": "vcsa_state_check",
                "start_time": "string",
                "end_time": "string",
                "plugin_name": "string",
                "plugin_version": "1.0.100",
                "result": {
                  "severity": "OK [OK, WARN, ERROR, CRITICAL]",
                  "messages": [
                    {
                      "id": "VXR304RADAR0003",
                      "kb": "string",
                      "action": "Ensure there are not critical alarms existing on VCSA.",
                      "alphaid": "check_script_failed",
                      "symptom": "There are critical alarms existing on VCSA.",
                      "severity": "Error [Ok, Warn, Error, Critical]"
                    }
                  ]
                }
              }
            ]
          }
        }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_system_getprechecksreport", "/tmp/vxrail_ansible_system_getprechecksreport.log", log_devel=logging.DEBUG)
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
        self.id = module.params.get('id')
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

        if self.id:
            # Calls versioned method as attribute (ex: v1_system_precheck_results_id_get)
            call_string = self.api_version_string + '_system_precheck_results_id_get'
            LOGGER.info("Using utility method: %s\n", call_string)
            one_prechecks_report = getattr(api_instance, call_string)
            return one_prechecks_report(self.id)
        else:
            # Calls versioned method as attribute (ex: v1_system_precheck_results_get)
            call_string = self.api_version_string + '_system_precheck_results_get'
            LOGGER.info("Using utility method: %s\n", call_string)
            all_prechecks_reports = getattr(api_instance, call_string)
            return all_prechecks_reports()

    def get_all_prechecks_reports(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemPreCheckApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # Get all prechecks results
            response = self.get_versioned_response(api_instance, "GET /system/prechecks/results")
        except ApiException as e:
            LOGGER.error("Exception when calling SystemPreCheckApi->%s_system_precheck_results_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/system/prechecks/results API response: %s\n", self.api_version_string, response)
        prechecks_results = {}
        prechecks_results['report_list'] = self._get_report_list_from_precheck_results(response.report_list)
        return prechecks_results

    def get_one_precheck_report(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.SystemPreCheckApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # Get one prechecks result
            response = self.get_versioned_response(api_instance, "GET /system/prechecks/{id}/result")
        except ApiException as e:
            LOGGER.error("Exception when calling SystemPreCheckApi->%s_system_precheck_results_id_get: %s\n", self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/system/prechecks/{id}/result API response: %s\n", self.api_version_string, response)
        return self._get_report_dict(response)

    def _get_report_list_from_precheck_results(self, data):
        report_list_combined = []
        if data is not None:
            for i in range(len(data)):
                report_list_info = {}
                report_list_info = self._get_report_dict(data[i])
                report_list_combined.append(dict(report_list_info.items()))
        return report_list_combined

    def _get_report_dict(self, data):
        report_dict = {}
        report_dict['id'] = data.id
        report_dict['profile'] = data.profile
        report_dict['status'] = data.status
        report_dict['progress'] = data.progress
        report_dict['total_severity'] = data.total_severity
        report_dict['complete_check_count'] = data.complete_check_count
        report_dict['total_success_count'] = data.total_success_count
        report_dict['total_warn_count'] = data.total_warn_count
        report_dict['total_error_count'] = data.total_error_count
        if data.results is not None:
            report_dict['results'] = self._get_results_from_report_list(data.results)
        return report_dict

    def _get_results_from_report_list(self, data):
        results = {}
        results['host_checks'] = self._generate_host_checks_info_from_results(data.host_checks)
        results['general_checks'] = self._generate_general_checks_info_from_results(data.general_checks)
        return results

    def _generate_host_checks_info_from_results(self, data):
        host_checks_list = []
        if data is not None:
            for i in range(len(data)):
                host_checks_info = {}
                host_checks_info['host_id'] = data[i].host_id
                host_checks_info['checks'] = self._generate_checks_info_from_host_checks(data[i].checks)
                host_checks_list.append(dict(host_checks_info.items()))
        return host_checks_list

    def _generate_checks_info_from_host_checks(self, data):
        checks_list = []
        if data is not None:
            for i in range(len(data)):
                checks_info = {}
                checks_info['status'] = data[i].status
                checks_info['check_id'] = data[i].check_id
                checks_info['start_time'] = data[i].start_time
                checks_info['end_time'] = data[i].end_time
                checks_info['plugin_name'] = data[i].plugin_name
                checks_info['plugin_version'] = data[i].plugin_version
                checks_info['result'] = self._generate_result_info(data[i].result)
                checks_list.append(dict(checks_info.items()))
        return checks_list

    def _generate_general_checks_info_from_results(self, data):
        general_checks_list = []
        if data is not None:
            for i in range(len(data)):
                general_checks_info = {}
                general_checks_info['status'] = data[i].status
                general_checks_info['check_id'] = data[i].check_id
                general_checks_info['start_time'] = data[i].start_time
                general_checks_info['end_time'] = data[i].end_time
                general_checks_info['plugin_name'] = data[i].plugin_name
                general_checks_info['plugin_version'] = data[i].plugin_version
                general_checks_info['result'] = self._generate_result_info(data[i].result)
                general_checks_list.append(dict(general_checks_info.items()))
        return general_checks_list

    def _generate_result_info(self, data):
        result = {}
        result['severity'] = data.severity
        result['messages'] = self._generate_messages_info(data.messages)
        return result

    def _generate_messages_info(self, data):
        messages_list = []
        if data is not None:
            for i in range(len(data)):
                messages_info = {}
                messages_info['id'] = data[i].id
                messages_info['kb'] = data[i].kb
                messages_info['action'] = data[i].action
                messages_info['alphaid'] = data[i].alphaid
                messages_info['symptom'] = data[i].symptom
                messages_info['severity'] = data[i].severity
                messages_list.append(dict(messages_info.items()))
        return messages_list


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        id=dict(required=False),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    if (module.params.get('id')):
        result = VxRailCluster().get_one_precheck_report()
    else:
        result = VxRailCluster().get_all_prechecks_reports()
    if result == 'error':
        module.fail_json(msg="API call failed, please see log file /tmp/vxrail_ansible_system_getprechecksreport.log for more error details.")
    vx_facts = {'Prechecks_Report': result}
    vx_facts_result = dict(changed=False, Prechecks_Results_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
