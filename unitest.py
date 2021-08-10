import unittest
from tasks import get_coins , check_palindrome


class TestTask2(unittest.TestCase):
    def test_get_all_coins(self):
        """
        Test  all possible coins variants
        """
        result = get_coins(186)
        self.assertEqual(result, {1: 1, 5: 1, 10: 1, 20: 1, 50: 1, 100: 1})

    def test_zero_coins(self):
        """
        Test  zero coins
        """
        result = get_coins(0)
        self.assertEqual(result, {1: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0})

    def test_bad_type(self):
        with self.assertRaises(TypeError):
            result = get_coins(1.1)

class TestTask1(unittest.TestCase):
    def test_palindrome(self):
        """
        Test  palindrome
        """
        result = check_palindrome("Abba")
        self.assertTrue(result)

    def test_not_palindrome(self):
        """
        Test  not_palindrome
        """
        result = check_palindrome("aaoaa")
        self.assertFalse(result)

    def test_bad_type(self):
        with self.assertRaises(TypeError):
            result = check_palindrome(1001)

if __name__ == '__main__':
    unittest.main()
