"""Unit tests for shellui classes"""

import unittest
from mock import patch

from shellui.shellui import ShellUI, SHLog, SHConfig
from . import constants as c
import os


class TestshelluiLogger(unittest.TestCase):
    """Unit test class for shellui classes and methods"""

    def setUp(self):
        self.shutil = ShellUI()
        self.shutil.logging_create(filename='log_one.log', filemode='a', format='%(levelname)s:%(filename)s: %(message)s')

    def tearDown(self):
        self.shutil = None

    def test_logger_is_creatable(self):
        self.assertIsNotNone(self.shutil.logger)

    def test_custom_message(self):
        msg = "custom"
        lvl = 10
        self.shutil.logmsg(lvl, msg)

    @patch.object(SHLog, 'logdebug')
    def test_debug_message(self, mocklogger):
        msg = "debug"
        self.shutil.logdebug(msg)
        mocklogger.assert_called_once_with(msg)

    @patch.object(SHLog, 'loginfo')
    def test_info_message(self, mocklogger):
        msg = "info"
        self.shutil.loginfo(msg)
        mocklogger.assert_called_once_with(msg)
    @patch.object(SHLog, 'logwarning')
    def test_warning_message(self, mocklogger):
        msg = "warning"
        self.shutil.logwarning(msg)
        mocklogger.assert_called_once_with(msg)

    @patch.object(SHLog, 'logerror')
    def test_error_message(self, mocklogger):
        msg = "error"
        self.shutil.logerror(msg)
        mocklogger.assert_called_once_with(msg)

    @patch.object(SHLog, 'logcritical')
    def test_critical_message(self, mocklogger):
        msg = "critical"
        self.shutil.logcritical(msg)
        mocklogger.assert_called_once_with(msg)

    @patch.object(SHLog, 'setlevel')
    def test_level_setting(self, mocklogger):
        self.shutil.setlevel(c.DLEVEL)
        mocklogger.assert_called_once_with(c.DLEVEL)

    @patch.object(SHLog, 'logging_disable')
    def test_disable_logging(self, mocklogger):
        self.shutil.logging_disable()
        mocklogger.assert_called_once_with()

    @patch.object(SHLog, 'logging_enable')
    def test_enable_logging(self, mocklogger):
        self.shutil.logging_enable()
        mocklogger.assert_called_once_with()

class TestshelluiConfigs(unittest.TestCase):
    
    def setUp(self):
        self.shutil = ShellUI()


    def tearDown(self):
        self.shutil = None
        os.system(c.CLEAR_OUT)


    @patch.object(SHConfig, 'import_json')
    def test_import_json(self, mocklogger):
        self.shutil.import_json(c.JSON_SAMPLE)
        mocklogger.assert_called_once_with(c.JSON_SAMPLE)

    @patch.object(SHConfig, 'import_csv')
    def test_import_csv(self, mocklogger):
        self.shutil.import_csv(c.CSV_SAMPLE)
        mocklogger.assert_called_once_with(c.CSV_SAMPLE)

    @patch.object(SHConfig, 'import_csv')
    def test_import_dif_delimiter_sv(self, mocklogger):
        self.shutil.import_csv(c.CSV_SAMPLE, delimiter='\t')
        mocklogger.assert_called_once_with(c.CSV_SAMPLE, delimiter='\t')

    @patch.object(SHConfig, 'import_xml')
    def test_import_xml(self, mocklogger):
        self.shutil.import_xml(c.XML_SAMPLE)
        mocklogger.assert_called_once_with(c.XML_SAMPLE)

    @patch.object(SHConfig, 'export_json')
    def test_export_json(self, mocklogger):
        self.shutil.export_json(c.JSON_OUT, c.LIST_DICTS)
        mocklogger.assert_called_once_with(c.JSON_OUT, c.LIST_DICTS)

    @patch.object(SHConfig, 'export_csv')
    def test_export_csv(self, mocklogger):
        self.shutil.export_csv(c.CSV_OUT, c.LIST_DICTS)
        mocklogger.assert_called_once_with(c.CSV_OUT, c.LIST_DICTS)

    @patch.object(SHConfig, 'export_csv')
    def test_export_dif_delimiter_sv(self, mocklogger):
        self.shutil.export_csv(c.TSV_OUT, c.LIST_DICTS, delimiter='\t')
        mocklogger.assert_called_once_with(c.TSV_OUT, c.LIST_DICTS, delimiter='\t')

    @patch.object(SHConfig, 'export_csv')
    def test_export_dif_header_csv(self, mocklogger):
        self.shutil.export_csv(c.CSV_OUT, c.LIST_DICTS, header=c.HEADER_SAMPLE)
        mocklogger.assert_called_once_with(c.CSV_OUT, c.LIST_DICTS, header=c.HEADER_SAMPLE)

    @patch.object(SHConfig, 'export_xml')
    def test_export_export_xml(self, mocklogger):
        self.shutil.export_xml(c.XML_OUT, c.LIST_DICTS)
        mocklogger.assert_called_once_with(c.XML_OUT, c.LIST_DICTS)

if __name__ == '__main__':
    unittest.main()
