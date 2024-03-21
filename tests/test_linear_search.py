import unittest
from search_algorithms.linear_search import linear_search

class TestLinearSearch(unittest.TestCase):
    """
    Test cases for linear_search function.
    """
    def test_linear_search_found(self):
        """
        Test linear_search with a target element that is found in the array.
        """
        arr = [i for i in range(1, 10001)]
        result = linear_search(arr, 5000)
        self.assertEqual(result, 4999)

    def test_linear_search_not_found(self):
        """
        Test linear_search with a target element that is not found in the array.
        """
        arr = [i for i in range(1, 10001)]
        result = linear_search(arr, 15000)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
