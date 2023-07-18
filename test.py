import unittest

from main import jadd


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        result = jadd(4,2)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
