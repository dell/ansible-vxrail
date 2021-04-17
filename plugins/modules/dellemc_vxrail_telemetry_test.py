#!/usr/bin/python3
# Copyright: (c) 2021, Gao Hongmei <s.gao@dell.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
author:  Dell EMC VxRail Ansible Team (@gaohongmei) <s.gao@dell.com>
module: dellemc_vxrail_telemetry
short_description: This module is used to retrieve and set the current telemetry tier
description: The module release upon the VxRail Telemetry API to obtain the current telemetry tier, as well as perform the configuration of vxRail telemetry tier.
dependencies:
 - VxRail Manager has been deployed and is in good health

options:
    name:
        description:
           - Name of the module. User defined name
        type: str
        required: false
    vxmip:
        description:
            - VxRail Manager IP address.
        type: str
        required: true
    vcadmin:
        description:
            - The vcenter administrative user account defined to VxRail Manager
        type: str
        required: true
    vcpasswd:
        description:
            - The vcenter administrator password defined to VxRail Manager
        type: str
        required: true
    modify_telemetry:
        description:
            - Force the connection if the host is already being managed by another vCenter server.
        type: bool
        default: False
        required: false
    level:
        description:
            - Level of telemetry tier to be set
        type: str
        required: false
        choices: [NONE, LIGHT,BASIC,ADVANCED]
    
    timeout:
        description:
            - The timeout value, in milliseconds, assigned to the REST URL request. Default value is 10.
        type: int
        required: false

version_added: "2.10"

'''
EXAMPLES = """
  - name: Retrieve the current telemetry tier
    dellemc_vxrail_telemetry:
      vxmip: " {{vxmip }}"
      vcadmin: "{{ vcadmin }}"
      vcpasswd: "{{ vcpasswd }}"

  - name: Set the telemetry tier
    dellemc_vxrail_telemetry:
      vxmip: " {{vxmip }}"
      vcadmin: "{{ vcadmin }}"
      vcpasswd: "{{ vcpasswd }}"
      modify_telemetry: True
      level: 'ADVANCED'

"""

RETURN = """
"""

import json
import logging
import requests
import chardet
import urllib3
from requests.exceptions import HTTPError
from ansible.module_utils.basic import AnsibleModule

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class CustomLogFormatter(logging.Formatter):
    ''' Logging class for method '''
    info_fmt = "%(asctime)s [%(levelname)s]\t%(message)s"
    debug_fmt = "%(asctime)s [%(levelname)s]\t%(pathname)s:%(lineno)d\t%(message)s"

    def __init__(self, fmt="%(asctime)s [%(levelname)s]\t%(pathname)s:%(lineno)d\t%(message)s"):
        logging.Formatter.__init__(self, fmt)

    def format(self, record):
        if record.levelno == logging.INFO:
            self._fmt = CustomLogFormatter.info_fmt
            # python 3 compatibility
            if hasattr(self, '_style'):
                self._style._fmt = CustomLogFormatter.info_fmt
        else:
            self._fmt = CustomLogFormatter.debug_fmt
            # python 3 compatibility
            if hasattr(self, '_style'):
                self._style._fmt = CustomLogFormatter.debug_fmt
        result = logging.Formatter.format(self, record)
        return result

def byte_to_json(body):
    ''' conversion of http content to json format '''
    return json.loads(body.decode(chardet.detect(body)["encoding"]))

# Configurations
LOG_FILE_NAME = "telemetry.log"
LOG_FORMAT = CustomLogFormatter()

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

# file output
FILE_HANDLER = logging.FileHandler(LOG_FILE_NAME)
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(LOG_FORMAT)
LOGGER.addHandler(FILE_HANDLER)

class TelemetryUrls():
    ''' vxrail Map api to python method '''
    telemetry_tier_url = 'https://{}/rest/vxm/v1/telemetry/tier'


    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def telemetry_tier(self):
        ''' get call home config info '''
        return TelemetryUrls.telemetry_tier_url.format(self.vxm_ip)

    def esrs_deploy(self):
        ''' deploy esrs tasks  '''
        return ExpansionUrls.esrs_deploy_tpl.format(self.vxm_ip)

    def esrs_mode(self):
        ''' get current mode '''
        return ExpansionUrls.esrs_mode_tpl.format(self.vxm_ip)

class VxrailTelemetry():
    ''' Main Class for module execution '''
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.vcadmin = module.params.get('vcadmin')
        self.vcpasswd = module.params.get('vcpasswd')
        self.modify_telemetry = module.params.get('modify_telemetry')
        self.telemetry_tier = module.params.get('level')
        self.timeout = module.params.get('timeout')
        self.telemetry_urls = TelemetryUrls(self.vxm_ip)

    def get_telemetry_tier(self):
        ''' check the current esrs mode and settings '''
        try:
            response = requests.get(url=self.expansion_urls.esrs_info(),
                                    verify=False,
                                    auth=(self.vcadmin, self.vcpasswd),
                                    )
            response.raise_for_status()
        except HTTPError as http_err:
            LOGGER.error("HTTP error %s request to vxrail Manager %s", http_err, self.vxm_ip)
            return 'error'
        except Exception as api_exception:
            LOGGER.error(' %s Cannot connect to vxrail Manager %s', api_exception, self.vxm_ip)
            return 'error'

        if response.status_code == 200 or 404:
            data = byte_to_json(response.content)
            LOGGER.info(data)
            return data
        else:
            status = "Call Home not configured!"
            LOGGER.info(status)
            return status

    def create_payload(self):
        ''' build telemetry deployment payload '''
        payload = {}
        payload['level'] = self.vcpasswd
        payload['company'] = self.company
        payload['email'] = self.email
        payload['first_name'] = self.fname
        payload['ip'] = self.ip
        payload['last_name'] = self.last_name
        payload['phone'] = self.phone
        payload['root_pwd'] = self.root_passwd
        payload['site_id'] = self.siteid
        return payload

    def set_telemetry_tier(self, payload):
        ''' begin the configuration of the esrs service '''
        try:
            response = requests.post(url=self.expansion_urls.esrs_deploy(),
                                     verify=False,
                                     headers={'Content-type': 'application/json'},
                                     auth=(self.vcadmin, self.vcpasswd),
                                     data=json.dumps(payload)
                                     )

            response.raise_for_status()
        except HTTPError as http_err:
            LOGGER.error("HTTP error %s request to vxrail Manager %s", http_err, self.vxm_ip)
            return 'error'
        except Exception as api_exception:
            LOGGER.error(' %s Cannot connect to vxrail Manager %s', api_exception, self.vxm_ip)
            return 'error'

        if response.status_code == 200:
            data = byte_to_json(response.content)
            return data or "No content in deployment response"
        else:
            LOGGER.error('Request resulted in unexpected result code %d.', response.status_code)
            LOGGER.info(response)
            return "Unexpected response from deployment request"

def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
            name=dict(required=False),
            vxmip=dict(required=True),
            vcadmin=dict(required=True),
            vcpasswd=dict(required=True, no_log=True),
            modify_telemetry=dict(type='bool', default=False),
            level=dict(required=False),
            )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    if (module.params.get('modify_telemetry')):
        result = VxrailTelemetry().get_telemetry_tier()
    else:
        payload_data = VxrailTelemetry().create_payload()
        LOGGER.info(payload_data)
        task_id = VxrailTelemetry().set_telemetry_tier(payload_data)
        LOGGER.info(task_id)
    if result == 'error':
        module.fail_json(msg="VxRail Manager is unreachable")

    vx_facts = {'telemetry': result}
    vx_facts_result = dict(changed=False, ansible_facts=vx_facts)
    module.exit_json(**vx_facts_result)

if __name__ == '__main__':
    main()
