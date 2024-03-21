import unittest
from search_algorithms.binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    """
    Test cases for binary_search function.
    """
    def test_binary_search_found(self):
        """
        Test binary_search with a target element that is found in the array.
        """
        arr = [i for i in range(1, 10001)]
        result = binary_search(arr, 5000)
        self.assertEqual(result, 4999)

    def test_binary_search_not_found(self):
        """
        Test binary_search with a target element that is not found in the array.
        """
        arr = [i for i in range(1, 10001)]
        result = binary_search(arr, 15000)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
