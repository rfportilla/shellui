"""Unit tests for shellui classes"""

import unittest
from mock import patch

import shellui
import constants
import os


class TestshelluiLogger(unittest.TestCase):
    """Unit test class for shellui classes and methods"""

    def setUp(self):
        self.shutil = shellui.ShellUI()
        self.shutil.logging_create(filename='log_one.log', filemode='a', format='%(levelname)s:%(filename)s: %(message)s')

    def tearDown(self):
        self.shutil = None

    def test_logger_is_creatable(self):
        self.assertIsNotNone(self.shutil.logger)

    def test_custom_message(self):
        msg = "custom"
        lvl = 10
        self.shutil.logmsg(lvl, msg)

    @patch.object(shellui.SHLog, 'logdebug')
    def test_debug_message(self, mocklogger):
        msg = "debug"
        self.shutil.logdebug(msg)
        mocklogger.assert_called_once_with(msg)

    @patch.object(shellui.SHLog, 'loginfo')
    def test_info_message(self, mocklogger):
        msg = "info"
        self.shutil.loginfo(msg)
        mocklogger.assert_called_once_with(msg)
    @patch.object(shellui.SHLog, 'logwarning')
    def test_warning_message(self, mocklogger):
        msg = "warning"
        self.shutil.logwarning(msg)
        mocklogger.assert_called_once_with(msg)

    @patch.object(shellui.SHLog, 'logerror')
    def test_error_message(self, mocklogger):
        msg = "error"
        self.shutil.logerror(msg)
        mocklogger.assert_called_once_with(msg)

    @patch.object(shellui.SHLog, 'logcritical')
    def test_critical_message(self, mocklogger):
        msg = "critical"
        self.shutil.logcritical(msg)
        mocklogger.assert_called_once_with(msg)

    @patch.object(shellui.SHLog, 'setlevel')
    def test_level_setting(self, mocklogger):
        self.shutil.setlevel(constants.DLEVEL)
        mocklogger.assert_called_once_with(constants.DLEVEL)

    @patch.object(shellui.SHLog, 'logging_disable')
    def test_disable_logging(self, mocklogger):
        self.shutil.logging_disable()
        mocklogger.assert_called_once_with()

    @patch.object(shellui.SHLog, 'logging_enable')
    def test_enable_logging(self, mocklogger):
        self.shutil.logging_enable()
        mocklogger.assert_called_once_with()

class TestshelluiConfigs(unittest.TestCase):
    
    def setUp(self):
        self.shutil = shellui.ShellUI()


    def tearDown(self):
        self.shutil = None
        os.system(constants.CLEAR_OUT)


    @patch.object(shellui.SHConfig, 'import_json')
    def test_import_json(self, mocklogger):
        self.shutil.import_json(constants.JSON_SAMPLE)
        mocklogger.assert_called_once_with(constants.JSON_SAMPLE)

    @patch.object(shellui.SHConfig, 'import_csv')
    def test_import_csv(self, mocklogger):
        self.shutil.import_csv(constants.CSV_SAMPLE)
        mocklogger.assert_called_once_with(constants.CSV_SAMPLE)

    @patch.object(shellui.SHConfig, 'import_csv')
    def test_import_dif_delimiter_sv(self, mocklogger):
        self.shutil.import_csv(constants.CSV_SAMPLE, delimiter='\t')
        mocklogger.assert_called_once_with(constants.CSV_SAMPLE, delimiter='\t')

    @patch.object(shellui.SHConfig, 'import_xml')
    def test_import_xml(self, mocklogger):
        self.shutil.import_xml(constants.XML_SAMPLE)
        mocklogger.assert_called_once_with(constants.XML_SAMPLE)

    @patch.object(shellui.SHConfig, 'export_json')
    def test_export_json(self, mocklogger):
        self.shutil.export_json(constants.JSON_OUT, constants.LIST_DICTS)
        mocklogger.assert_called_once_with(constants.JSON_OUT, constants.LIST_DICTS)

    @patch.object(shellui.SHConfig, 'export_csv')
    def test_export_csv(self, mocklogger):
        self.shutil.export_csv(constants.CSV_OUT, constants.LIST_DICTS)
        mocklogger.assert_called_once_with(constants.CSV_OUT, constants.LIST_DICTS)

    @patch.object(shellui.SHConfig, 'export_csv')
    def test_export_dif_delimiter_sv(self, mocklogger):
        self.shutil.export_csv(constants.TSV_OUT, constants.LIST_DICTS, delimiter='\t')
        mocklogger.assert_called_once_with(constants.TSV_OUT, constants.LIST_DICTS, delimiter='\t')

    @patch.object(shellui.SHConfig, 'export_csv')
    def test_export_dif_header_csv(self, mocklogger):
        self.shutil.export_csv(constants.CSV_OUT, constants.LIST_DICTS, header=constants.HEADER_SAMPLE)
        mocklogger.assert_called_once_with(constants.CSV_OUT, constants.LIST_DICTS, header=constants.HEADER_SAMPLE)

    @patch.object(shellui.SHConfig, 'export_xml')
    def test_export_export_xml(self, mocklogger):
        self.shutil.export_xml(constants.XML_OUT, constants.LIST_DICTS)
        mocklogger.assert_called_once_with(constants.XML_OUT, constants.LIST_DICTS)

if __name__ == '__main__':
    unittest.main()
