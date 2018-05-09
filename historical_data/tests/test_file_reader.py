import unittest
from file_reader import read_historical_data_file, GeneralError


class TestStringMethods(unittest.TestCase):

    def test_none_file(self):
        with self.assertRaises(GeneralError):
            read_historical_data_file(None)

    # def test_valid_file(self):
    #     try:
    #         read_historical_data_file("(/Users/lizajohn/Documents/Historical_Data_Request_Template_copy.csv")
    #     except Exception:
    #         self.fail("a valid expression had failed")

    # def test_non_csv_file(self):
    #     try:
    #         validate_expression("(())")
    #     except Exception:
    #         self.fail("a valid expression had failed")
    #
    # def test_3_parenthesis_string(self):
    #     try:
    #         validate_expression("((()))")
    #     except Exception:
    #         self.fail("a valid expression had failed")
    #
    # def test_4_parenthesis_string(self):
    #     with self.assertRaises(NotMathematicalLogic):
    #         validate_expression(")(")
    #
    # def test_5_parenthesis_string(self):
    #     with self.assertRaises(NotEqualOpenCloseParentheses):
    #         validate_expression(")()")
    #
    # def test_6_parenthesis_string(self):
    #     with self.assertRaises(NotMathematicalLogic):
    #         validate_expression("())(()")

if __name__ == '__main__':
    unittest.main()