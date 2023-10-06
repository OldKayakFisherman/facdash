import unittest

from facdata import get_connection


class DataTests(unittest.TestCase):
    def test_connection(self):
        cn = get_connection()
        self.assertIsNotNone(cn)

if __name__ == '__main__':
    unittest.main()
