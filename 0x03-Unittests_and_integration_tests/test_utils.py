#!/usr/bin/env python3

""" Implement the TestAccessNestedMap.test_access_nested_map method
    to test that the method returns what it is supposed to.
"""

import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Implement the TestAccessNestedMap.test_access_nested_map method
    to test that the method returns what it is supposed to.
"""
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, nested_map, path):
        """ This method test the access_nested_map function in the
            utils module.
        """
        self.assertEqual(access_nested_map(nested_map, path), 1)


if __name__ == '__main__':
    unittest.main()
