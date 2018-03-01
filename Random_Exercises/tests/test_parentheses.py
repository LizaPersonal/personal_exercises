
import unittest

from parentheses import validate_expression, GeneralError, NotMathematicalLogic, NotEqualOpenCloseParentheses


class TestStringMethods(unittest.TestCase):

    def test_empty_string(self):
        try:
            validate_expression("")
        except Exception:
            self.fail("a valid expression had failed")

    def test_none_string(self):
        with self.assertRaises(GeneralError):
            validate_expression(None)

    def test_1_parenthesis_string(self):
        try:
            validate_expression("()")
        except Exception:
            self.fail("a valid expression had failed")

    def test_2_parenthesis_string(self):
        try:
            validate_expression("(())")
        except Exception:
            self.fail("a valid expression had failed")

    def test_3_parenthesis_string(self):
        try:
            validate_expression("((()))")
        except Exception:
            self.fail("a valid expression had failed")

    def test_4_parenthesis_string(self):
        with self.assertRaises(NotMathematicalLogic):
            validate_expression(")(")

    def test_5_parenthesis_string(self):
        with self.assertRaises(NotEqualOpenCloseParentheses):
            validate_expression(")()")

    def test_6_parenthesis_string(self):
        with self.assertRaises(NotMathematicalLogic):
            validate_expression("())(()")

if __name__ == '__main__':
    unittest.main()