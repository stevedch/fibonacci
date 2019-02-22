import unittest

from utils import nth_succession
import urllib.request


class TestFibonacciMethods(unittest.TestCase):

    def test_status(self):
        status = urllib.request.urlopen('http://127.0.0.1:8080/').getcode()
        print(status)
        self.assertEqual(status, 200)

    def test_sussecion(self):
        self.assertEqual(nth_succession(5), [0, 1, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
