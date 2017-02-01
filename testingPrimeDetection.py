import unittest

from PrimeDetection import is_prime

class checkPrime(unittest.TestCase):
    def test_for_0asPrime(self):
        self.assertFalse(is_prime(0))

    def test_for_1asPrime(self):
        self.assertFalse(is_prime(1))

    def test_for_prime(self):
        self.assertTrue(is_prime(5))

if __name__=="__main__":
    unittest.main()