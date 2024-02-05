#!/usr/bin/env python3
""" Tests for utils.py module """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test access_nested_map function for retrieving values.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception, expected_message):
        """
        Test access_nested_map function for raising exceptions.
        """
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_message)


if __name__ == '__main__':
    unittest.main()
