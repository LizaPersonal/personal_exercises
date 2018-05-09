import unittest
from data_cleanup.check_airline_vendors import _search_airline_database


class TestStringMethods(unittest.TestCase):

    def test_airline_in_database(self):
        self.assertEqual(_search_airline_database(cursor, "Delta"), "DL")

    def test_airline_not_in_database(self):
        self.assertEqual(_search_airline_database(cursor, "Not Airline"), None)


if __name__ == '__main__':
    unittest.main()