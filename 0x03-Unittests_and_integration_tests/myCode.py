import unittest
from unittest.mock import patch
import requests
from utils import access_nested_map, get_json, memoize  # Update this line

class TestUtilities(unittest.TestCase):
    
    def test_access_nested_map(self):
        nested_map = {"a": {"b": {"c": 1}}}
        path = ["a", "b", "c"]
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, 1)

        with self.assertRaises(KeyError):
            access_nested_map(nested_map, ["a", "b", "x"])

    @patch('requests.get')
    def test_get_json(self, mock_get):
        mock_response = unittest.mock.Mock()
        expected_data = {"key": "value"}
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response
        
        url = "https://api.example.com/data"
        result = get_json(url)
        self.assertEqual(result, expected_data)
        mock_get.assert_called_once_with(url)

    def test_memoize(self):
        class MyClass:
            @memoize
            def a_method(self):
                print("a_method called")
                return 42

        my_object = MyClass()

        # First call, should print "a_method called" and return 42
        self.assertEqual(my_object.a_method, 42)

        # Second call, should not print "a_method called" and return cached value 42
        self.assertEqual(my_object.a_method, 42)

if __name__ == '__main__':
    unittest.main()
