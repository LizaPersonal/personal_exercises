import unittest
from file_reader import read_historical_data_file, GeneralError


class TestStringMethods(unittest.TestCase):

    def test_none_file(self):
        with self.assertRaises(GeneralError):
            read_historical_data_file(None)