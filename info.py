#!/usr/bin/python
import unittest
import info
class Testinfo(unittest.TestCase):
        def test_register(self):
                self.assertEqual(info.firstname('Fi'), 'kate')
                self.assertEqual(info.lastnam('owuor'), 'owuor')
                self.assertEqual(info.username('fk'), 'fk')
