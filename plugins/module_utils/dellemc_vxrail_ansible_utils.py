# #!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

from __future__ import (absolute_import, division, print_function)
import logging
__metaclass__ = type

'''
This method is to initialize logger and return the logger object
parameters:
     - module_name: Name of module to be part of log message.
     - log_file_name: name of the file in which the log meessages get
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
