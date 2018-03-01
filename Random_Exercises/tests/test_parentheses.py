
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

    # def test_parenthesis_with_number_string(self):
    #     result = validate_expression("(3)")
    #     self.assertEqual(result, "\nThat is not a valid string.")

    # def test_parenthesis_with_number_string(self):
    #     result = validate_expression("g(bd)")
    #     self.assertEqual(result, "\nThat is not a valid string.")

    def test_4_parenthesis_string(self):
        with self.assertRaises(NotMathematicalLogic):
            validate_expression(")(")

    def test_5_parenthesis_string(self):
        with self.assertRaises(NotEqualOpenCloseParentheses):
            validate_expression(")()")

    def test_6_parenthesis_string(self):
        with self.assertRaises(NotMathematicalLogic):
            validate_expression("())(()")




    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()