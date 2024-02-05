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
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str],
                               expected: Union[int, Dict]):
        """
        Test access_nested_map function for retrieving values.
        """
        self.assertEqual(expected, access_nested_map(nested_map, path))

    def test_access_nested_map_exception(self, nested_map: Dict, path:
                                         Tuple[str]) -> None:
        """
        Test access_nested_map function for raising exceptions.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Defines tests for get_json utility"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload:
                      Dict[str, bool]) -> None:
        """
        Test that it returns a valid json payload
        Args:
            test_url (str): url to make a request to
            test_payload (Dict): expected payload from the response
        Returns:
            None
        """
        config = {'return_value.json.return_value': test_payload}
        with patch('requests.get', autospec=True, **config) as mockRequestGet:
            self.assertEqual(get_json(test_url), test_payload)
            mockRequestGet.assert_called_once_with(test_url)
