#!/usr/bin/python3
"""
Test Console Documents
"""

import console
import inspect
import pep8
import unittest
HBNBCommand = console.HBNBCommand


class TestConsoleDocuments(unittest.TestCase):
    """A Class for testing documentation of console.py"""
    def test_pep8_console(self):
        """A test that tests the console.py to conform to PEP8(Pycodestyle)"""
        pep8s = pep8.StyleGuide(quiet=True)
        results = pep8s.check_files(['console.py'])
        self.assertEqual(results.total_errors, 0,
                         "Pycodestyle Error (and warnings).")

    def test_pep8_test_console(self):
        """ A Test that tests that the tests/test_console.py conforms to
        PEP8(Pycodestyle
        """
        pep88s = pep8.StyleGuide(quite=True)
        results = pep8s.check_files(['tetst/test_console.py'])
        self.assertEqual(results.total_errors, 0,
                         "Pycodestyle Error (and warnings).")

    def test_console_mod_docstring(self):
        """ A Test for the moduledocstring of the console.py"""
        self.assertIsNot(console.__doc__, None,
                         "console.py has no docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py has no docstring")

    def test_HBNBCommand_class_docstring(self):
        """ A Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class has no docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class has no docstring")
