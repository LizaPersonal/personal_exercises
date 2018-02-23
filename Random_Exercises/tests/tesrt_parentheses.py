
import unittest

from parentheses import validate_expression


class TestStringMethods(unittest.TestCase):

    def test_empty_string(self):
        result = validate_expression("")
        self.assertEqual(result, "This string has accurate mathematical logic.\nIt passes this test.\n")

    def test_none_string(self):
        result = validate_expression(None)
        self.assertEqual(result, "error")

    def test_1_parenthesis_string(self):
        result = validate_expression("()")
        self.assertEqual(result, "This string has accurate mathematical logic.\nIt passes this test.\n")

    def test_2_parenthesis_string(self):
        result = validate_expression("(())")
        self.assertEqual(result, "This string has accurate mathematical logic.\nIt passes this test.\n")

    def test_3_parenthesis_string(self):
        result = validate_expression("((()))")
        self.assertEqual(result, "This string has accurate mathematical logic.\nIt passes this test.\n")

    # def test_parenthesis_with_number_string(self):
    #     result = validate_expression("(3)")
    #     self.assertEqual(result, "\nThat is not a valid string.")

    # def test_parenthesis_with_number_string(self):
    #     result = validate_expression("g(bd)")
    #     self.assertEqual(result, "\nThat is not a valid string.")

    def test_4_parenthesis_string(self):
        result = validate_expression(")(")
        self.assertEqual(result, "This string does NOT follow mathematical logic.\nIt does not pass this test.\n")

    def test_5_parenthesis_string(self):
        result = validate_expression(")()")
        self.assertEqual(result, "\nThis string does NOT have equal open and close parentheses.\nIt does not pass this test.\n")

    def test_6_parenthesis_string(self):
        result = validate_expression("())(((")
        self.assertEqual(result, "\nThis string does NOT have equal open and close parentheses.\nIt does not pass this test.\n")




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