from copy import copy

from file_reader import compare_headers


def test_comparing_headers_with_matching_headers():
    """
    method name: compare_headers
    scenario: when the headers from the file match the headers needed from the template
    expected: the template headers did not change
    """

    file_header = ["header 1", "header 2"]
    original_template = {"h1": "header 1", "h2": "header 2"}
    template_parameter = copy(original_template)
    compare_headers(file_header, template_parameter)
    assert template_parameter == original_template


def test_comparing_headers_with_missing_header_from_file():
    """
    method name: compare_headers
    scenario: when the headers from the file have fewer than the headers needed from the template
    expected: the template headers update the additional expected headers
    """

    file_header = ["header 1", "header 2"]
    original_template = {"h1": "header 1", "h2": "header 2", "h3": ""}
    final_template = {"h1": "header 1", "h2": "header 2", "h3": "h3"}
    compare_headers(file_header, original_template)
    assert final_template == original_template


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

