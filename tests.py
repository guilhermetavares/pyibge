import unittest

from pyibge import geografos


class PyIbgeTest(unittest.TestCase):

    def test_01_not_found(self):
    	assert geografos('sem municipio') == None

    def test_02_valid_test(self):
    	assert geografos('sao-paulo') == '3550308'


if __name__ == '__main__':
    unittest.main()
