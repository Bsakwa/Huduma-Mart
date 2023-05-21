#!/usr/bin/python3

"""Unittests for Huduma Console"""

import console
import unittest
from unittest.mock import patch
from io import StringIO
from console import HUDUMAMARTCommand

class HUDUMAMARTCommandTestCase(unittest.TestCase):
    def setUp(self):
        self.console = HUDUMAMARTCommand()

    def tearDown(self):
        self.console = None

    def test_do_quit(self):
        result = self.console.do_quit("")
        self.assertTrue(result)

    def test_do_EOF(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.do_EOF(""))
            self.assertEqual(fake_out.getvalue(), '\n')

    def test_emptyline(self):
        self.assertFalse(self.console.emptyline())

    @patch('builtins.print')
    def test_do_create(self, mock_print):
        self.console.do_create("User")
        self.assertTrue(mock_print.called)

    @patch('builtins.print')
    def test_do_show(self, mock_print):
        self.console.do_show("User 123")
        self.assertTrue(mock_print.called)

    @patch('builtins.print')
    def test_do_destroy(self, mock_print):
        self.console.do_destroy("User 123")
        self.assertTrue(mock_print.called)

    @patch('builtins.print')
    def test_do_all(self, mock_print):
        self.console.do_all("User")
        self.assertTrue(mock_print.called)

    @patch('builtins.print')
    def test_do_update(self, mock_print):
        self.console.do_update("User 123 name John")
        self.assertTrue(mock_print.called)

if __name__ == '__main__':
    unittest.main()
