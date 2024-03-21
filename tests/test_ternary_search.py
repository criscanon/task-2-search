import unittest
from search_algorithms.ternary_search import ternary_search

class TestTernarySearch(unittest.TestCase):
    """
    Test cases for ternary_search function.
    """
    def test_ternary_search_found(self):
        """
        Test ternary_search with a target element that is found in the array.
        """
        arr = [i for i in range(1, 10001)]
        result = ternary_search(arr, 5000)
        self.assertEqual(result, 4999)

    def test_ternary_search_not_found(self):
        """
        Test ternary_search with a target element that is not found in the array.
        """
        arr = [i for i in range(1, 10001)]
        result = ternary_search(arr, 15000)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
