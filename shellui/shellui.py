"""
  shellui.py

  Usage:    Base Library for CLI development
  Records:
      Developers:   Fabian Portilla & Edgar Uribe
      Contact:      rfportilla@yahoo.com & edguribe@cisco.com
      Version:      0.1.1
"""

import argparse
import json
import csv
import xmltodict
import dicttoxml
import logging
import inspect
import getpass
from . import common as c


class SHLog(object):
    """Customizable Logging Class"""

    def __init__(self):
        self.logger = None

    def logging_create(self, **kwargs):
        """Return Logging Object

        **kwargs Valid Keyword Inputs for Logging Details:
          filename :: filemode :: level :: format

          For Additional Keyword pairs consult python docs on logging
        """
        if self.logger is None:
            logging.basicConfig(**kwargs)
            self.logger = logging.getLogger(__name__)

    @staticmethod
    def logging_disable():
        """Disable Logging Temporarily"""
        logging.disable(logging.CRITICAL)

    @staticmethod
    def logging_enable():
        """Enabling Logging Temporarily"""
        logging.disable(logging.NOTSET)

    def logmsg(self, lvl, msg):
        """Log Message to current Logger

        :lvl: 50 - Critical
              40 - Error
              30 - Warning
              20 - Info
              10 - Debug
              0  - NotSet

        :msg: Custom Message to Log
        """
        self.logger.log(lvl, msg)

    def logdebug(self, msg):
        """Log a DEBUG level message

        :msg: Custom Message to Log
        """
        self.logger.debug(msg)

    def loginfo(self, msg):
        """Log an INFO level message

        :msg: Custom Message to Log
        """
        self.logger.info(msg)

    def logwarning(self, msg):
        """Log a WARNING level message

        :msg: Custom Message to Log
        """
        self.logger.warning(msg)

    def logerror(self, msg):
        """Log an Error level message

        :msg: Custom Message to Log
        """
        self.logger.error(msg)

    def logcritical(self, msg):
        """Log a Critical level message

        :msg: Custom Message to Log
        """
        self.logger.critical(msg)

    def setlevel(self, lvl):
        """Set new Logging level

        :lvl: 50 - Critical
              40 - Error
              30 - Warning
              20 - Info
              10 - Debug
              0  - NotSet
        """
        self.logger.setLevel(lvl)



class SHConfig(object):
    """Methods for Exporting and Importing"""

    @staticmethod
    def import_json(conffile):
        '''Base Class For Json Import

        :conffile:  Directory of File To Access
        '''
        with open(conffile, 'rb') as file_desc:
            return json.load(file_desc)

    @staticmethod
    def export_json(conffile, data):
        '''Base Class For Json Export

        :conffile:  Directory of File To Access
        :data:      List of Dictionaries
        '''
        with open(conffile, 'wb') as file_desc:
            file_desc.write(json.dumps(data))

    @staticmethod
    def import_csv(conffile, delimiter=','):
        '''Base Class For CSV Import

        :conffile:  Directory of File To Access
        :delimiter: Delimiter for Seperated Values
        '''
        with open(conffile, 'rb') as file_desc:
            return list(csv.DictReader(file_desc, delimiter=delimiter))

    @staticmethod
    def export_csv(conffile, data, delimiter=',', header=None):
        '''Base Class For CSV Export

        :conffile:  Directory of File To Access
        :data:      List of Dictionaries
        :delimiter: Delimiter for Seperated Values
        :header:    List of headers of prefered order of dict keys
        '''
        with open(conffile, 'wb') as file_desc:
            if header is None:
                header = list(data[0].keys())
            writer = csv.DictWriter(
                file_desc,
                fieldnames=header,
                delimiter=delimiter
            )
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def import_xml(conffile):
        '''Base Class For XML Import

        :conffile:  Directory of File To Access
        '''
        with open(conffile, 'rb') as file_desc:
            return xmltodict.parse(file_desc)

    @staticmethod
    def export_xml(conffile, data):
        '''Base Class For XML Export

        :conffile:  Directory of File To Access
        :data:      List of Dictionaries
        '''
        with open(conffile, 'wb') as file_desc:
            file_desc.write(dicttoxml.dicttoxml(data))



class ShellUI(SHLog, SHConfig):
    '''
    Base class for making CLI tool.  This class offers some of the most
    common base functionality for CLI tools.
    '''

    #This var should be overridden.  Otherwise you will have useless -h options
    helpattr = {
        'argparseattr': {
            'description': ('This is a generic Elevator description that the '
            'programmer neglected to replace')
        },
        'args': [
            [('--ascending', '-a'), {'help': 'Optional: This will cause the '
                'elevator to ascend.'}],
            [('--bescending', '-b'), {'help': 'Required: This will cause the '
                'elevator to bescend.  This is required becase all things that '
                'go up, must come bown'}],
        ]
    }

    def __init__(self):
        SHLog.__init__(self)
        parser = argparse.ArgumentParser(**self.helpattr['argparseattr'])
        for helparg in self.helpattr['args']:
            parser.add_argument(*helparg[0], **helparg[1])
        self.parser = parser

    @c.ReadOnlyCachedProperty
    def args(self):
        return self.parser.parse_args()

    @classmethod
    def scriptpath(cls):
        return inspect.getfile(cls)

    def promptun(self, prompt='Username: '):
        return raw_input(prompt)

    def promptpw(self, prompt='Password: '):
        return getpass.getpass(prompt)

