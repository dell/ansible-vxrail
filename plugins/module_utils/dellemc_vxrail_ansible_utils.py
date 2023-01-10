# #!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)
import logging
import ast
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import urllib.error
import urllib.request
import yaml
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
__metaclass__ = type

'''
This method is to initialize logger and return the logger object
parameters:
     - module_name: Name of module to be part of log message.
     - log_file_name: name of the file in which the log messages get
      appended.
     - log_devel: log level.
returns logger object
'''


def get_logger(module_name, log_file_name='/tmp/vxrail_ansible.log', log_devel=logging.INFO):
    LOG_FILE_NAME = log_file_name
    LOG_FORMAT = CustomLogFormatter()
    LOGGER = logging.getLogger()
    LOGGER.setLevel(log_devel)

    # file output
    FILE_HANDLER = logging.FileHandler(LOG_FILE_NAME)
    FILE_HANDLER.setLevel(log_devel)
    FILE_HANDLER.setFormatter(LOG_FORMAT)
    LOGGER.addHandler(FILE_HANDLER)
    return LOGGER


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


'''
This method validates and returns an API version string (ex: "v4") for the specified module_path (ex: "/hosts/{sn}")
parameters:
     - vxm_ip: The IP Address of the VxRail Manager to query.
     - api_version_number: The version number to use. Returns the highest available version if set to None.
     - module_path: The API path for a specified module (ex: "/hosts" or "/system/initialize/status").
                    The path can also specify a particular method to use in the form of a 2-word string.
                    (ex: "GET /hosts/{sn}" or "PATCH /hosts/{sn}")
     - logger: A logger object to record the functionality.
returns The API version string to use in future API calls.
'''


def get_api_version_string(vxm_ip, api_version_number, module_path, logger):
    def numbers_only(seq):
        seq_type = type(seq)
        return seq_type().join(filter(seq_type.isdigit, seq))

    api_version_string = "v" + numbers_only(str(api_version_number))
    if APIVersionHandler(vxm_ip, logger).version_exists(api_version_string, module_path):
        logger.info("API Version: %s\n" % api_version_string)
        return api_version_string
    else:
        raise Exception("API Version %s does not exist for path %s" % (api_version_string, module_path))


'''
This method is to return the highest API version string (ex: "v4") for the specified module_path (ex: "/hosts/{sn}")
parameters:
     - vxm_ip: The IP Address of the VxRail Manager to query.
     - module_path: The API path for a specified module (ex: "/hosts" or "/system/initialize/status").
                    The path can also specify a particular method to use in the form of a 2-word string.
                    (ex: "GET /hosts/{sn}" or "PATCH /hosts/{sn}")
     - logger: A logger object to record the functionality.
returns The API version string to use in future API calls.
'''


def get_highest_api_version_string(vxm_ip, module_path, logger):
    ret_version = APIVersionHandler(vxm_ip, logger).get_highest_version(module_path)
    if ret_version != 'error':
        logger.info("API Version: %s\n" % ret_version['highest_version'])
        return ret_version['highest_version']
    else:
        raise Exception("Could not obtain highest API version for %s" % module_path)


'''
This method returns the a message telling the user only the input API version and above contain the specified field
parameters:
     - api_version_number: The int version number to inject into the string
     - cluster_version: An optional parameter that includes the input cluster version into the returned message
returns The API version string to use in future API calls.
'''


def field_not_found(api_version_number, cluster_version=None):
    if cluster_version is None:
        field_not_found_text = "INFO AVAILABLE IN API VERSION v%s OR GREATER"
        return field_not_found_text % str(api_version_number)
    else:
        field_not_found_text = "INFO AVAILABLE IN API VERSION v%s (CLUSTER VERSION %s) OR GREATER"
        return field_not_found_text % (str(api_version_number), cluster_version)


class APIVersionHandler:
    def __init__(self, vxm_ip, logger):
        # The ip to the vxm to use
        self.vxm_ip = vxm_ip
        # The logging object, so errors in API version processing can be logged
        self.logger = logger

    # Returns a Boolean representing if the given API version string (such as 'v5')
    # exists for the given module path in the Manager's schema
    def version_exists(self, api_version_string, module_path):
        schema = self.get_api_schema()
        if schema == -1:
            self.logger.info("Error collecting API schema from the VxRail Manager")
            return False

        # Split module if method specified (ex: "GET /hosts/{sn}" or "PATCH /hosts/{sn}")
        split_module = module_path.split(" ")
        method = None
        if len(split_module) == 2:
            method, module_path = split_module
            self.logger.info(f"Method specified as: {method}")

        paths = schema['paths'].keys()
        valid_paths = []
        for path in paths:
            if path.endswith(module_path):
                if method is not None:
                    if method.lower() in schema['paths'][path]:
                        valid_paths.append(path.split('/')[1])
                else:
                    valid_paths.append(path.split('/')[1])
        if len(valid_paths) < 1:
            self.logger.error(f"Path {module_path} not found in API schema.")
            return False
        else:
            if api_version_string in valid_paths:
                self.logger.info(f"Found version: {api_version_string}")
                return True
            else:
                self.logger.error(f"Could not find version {api_version_string} for {module_path}.\n")
                return False

    # Returns the highest API version of the given module path (ex: /hosts)
    def get_highest_version(self, module_path):
        schema = self.get_api_schema()
        if schema == -1:
            self.logger.error("Could not collect Stoplight/Swagger Schema.\n")
            return 'error'
        else:
            return self.get_highest_module_version_from_schema(schema, module_path)

    # Returns the highest API version of the given module path from the input schema
    def get_highest_module_version_from_schema(self, schema, module_path):
        def sort_versions(v):
            return int(v.split('v')[1])

        # Split module if method specified (ex: "GET /hosts/{sn}" or "PATCH /hosts/{sn}")
        split_module = module_path.split(" ")
        method = None
        if len(split_module) == 2:
            method, module_path = split_module
            self.logger.info(f"Method specified as: {method}")

        paths = schema['paths'].keys()
        valid_paths = []
        for path in paths:
            if path.endswith(module_path):
                if method is not None:
                    if method.lower() in schema['paths'][path]:
                        valid_paths.append(path.split('/')[1])
                else:
                    valid_paths.append(path.split('/')[1])
        valid_paths.sort(key=sort_versions)
        if len(valid_paths) < 1:
            self.logger.error(f"Path {module_path} not found in API schema.")
            return 'error'
        else:
            highest_version = {"highest_version": valid_paths[-1]}
            self.logger.info(f"Highest version found: {highest_version}")
            return dict(highest_version.items())

    # Obtains the api schema from the VxRail manager.
    # First attempts to obtain the Stoplight API yaml, then, if 404 is returned, search for the Swagger API yaml
    def get_api_schema(self):
        try:
            self.logger.info("Collecting API schema from Stoplight service...")
            return self.get_api_schema_stoplight()
        except urllib.error.HTTPError as err:
            self.logger.info("Exception code %s when collecting Stoplight info: %s\n", err.code, str(err))
            self.logger.info("Stoplight API schema not found, attempting to collect Swagger API schema instead.")
            return self.get_api_schema_swagger()

    # Obtains the Stoplight API schema from the Manager (Version <= 7.0.350
    def get_api_schema_stoplight(self):
        url = 'https://%s/rest/vxm/api-doc/vxrail_public_api.yaml' % self.vxm_ip
        self.logger.info("Attempting to collect Stoplight API schema from resource: %s" % url)
        with urllib.request.urlopen(url) as response:
            html = response.read()
            yml = yaml.safe_load(html)
            return yml

    # Obtains the Swagger API Schema from the Manager (Version < 7.0.350)
    def get_api_schema_swagger(self):
        groups = ["day1", "lcm", "callhome", "certificates", "chassis", "cluster", "disks", "hosts",
                  "network", "requests", "support", "system", "telemetry", "healthcheck", "vc"]
        combo_yml = {'paths': {}}
        for group in groups:
            url = 'https://%s/rest/vxm/v1/swagger-resources/api-specs?group=%s' % (self.vxm_ip, group)
            self.logger.info(f"Collecting from group '{group}' with url: {url}")
            try:
                with urllib.request.urlopen(url) as response:
                    html = response.read()
                    yml = yaml.safe_load(html)
                    for key in yml['paths'].keys():
                        combo_yml['paths'][key] = yml['paths'][key]
            except urllib.error.HTTPError as err:
                if err.code == 404:
                    # Group not found in cluster version, skip if simply 404
                    self.logger.info(f"Group '{group}' not found on VxRail Manager API schema")
                    continue
                else:
                    self.logger.error("Non 404 Exception when collecting Swagger info: %s\n", str(err))
                    return -1

        if combo_yml['paths']:
            return combo_yml
        else:
            self.logger.error("No Swagger Schema groups found.\n")
            return -1


''' VxRail Ansible Utility for GET v1/requests/{id} API'''

'''
This method is used to convert the response object from RequestStatusApi into a list of dictionary
parameters:
     - response: response object returned from RequestStatusApi call
returns result_info list
'''


def get_request_info(response):
    statusInfo = {}
    statusInfolist = []
    data = response
    statusInfo['id'] = data.id
    statusInfo['owner'] = data.owner
    statusInfo['state'] = data.state
    if data.error is not None:
        statusInfo['error'] = data.error
    statusInfo['progress'] = data.progress
    statusInfo['start_time'] = data.start_time
    if data.end_time is not None:
        statusInfo['end_time'] = data.end_time
    if data.target is not None:
        statusInfo['target'] = data.target
    if data.step is not None:
        statusInfo['step'] = data.step
    if data.detail is not None:
        statusInfo['detail'] = data.detail
    if data.extension is not None:
        # convert string into a dictoinary
        statusInfo['extension'] = ast.literal_eval(data.extension)
    statusInfolist.append(dict(statusInfo.items()))
    return statusInfolist


'''
This method is used to retrieve status information of any long running operation
parameters:
     - request_id: Long running operation request ID.
returns result_response object
'''


def get_request_status(vxm_ip, vcadmin, vcpasswd, request_id, logger, timeout=60):
    result_response = VxRailRequest(vxm_ip, vcadmin, vcpasswd, logger, timeout).get_request_response(request_id)
    if result_response == 'error':
        logger.error("Call v1/requests/request_id API failed,please see log file /tmp/vxrail_ansible_getrequestinfo_v1.log for more error details.")
    return result_response


class VxrailSystemUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailSystemUrls.cluster_url.format(self.vxm_ip)


class VxRailRequest():
    def __init__(self, vxmip, vcadmin, vcpasswd, logger, timeout=60):
        self.vxm_ip = vxmip
        self.timeout = timeout
        self.vc_admin = vcadmin
        self.vc_password = vcpasswd
        self.logger = logger
        self.system_url = VxrailSystemUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()

    def get_request_response(self, request_id):
        job_id = request_id
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.RequestStatusApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            response = api_instance.v1_request_id_get(job_id)
        except ApiException as e:
            self.logger.error("Exception when calling v1_requests_id_get: %s\n", e)
            return 'error'
        return response
