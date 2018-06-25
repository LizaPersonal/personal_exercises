from copy import copy
from unittest import TestCase
from unittest.mock import create_autospec

from file_reader import compare_headers, HeaderProvider


class ComparerTests(TestCase):

    def setUp(self):
        self.headers_provider_mock = create_autospec(HeaderProvider)

    def test_comparing_headers_with_matching_headers(self):
        """
        method name: compare_headers
        scenario: when the headers from the file match the headers needed from the template
        expected: the template headers did not change
        """

        self.headers_provider_mock.get_headers.return_value = ["h1", "h2"]

        original_file_headers = ["header 1", "header 2"]
        original_template_headers = {"h1": "header 1", "h2": "header 2"}
        updated_file_headers = copy(original_file_headers)
        updated_template_headers = copy(original_template_headers)
        compare_headers(updated_file_headers, updated_template_headers, self.headers_provider_mock)
        assert updated_template_headers == original_template_headers
        assert updated_file_headers == original_file_headers

    def test_comparing_headers_with_missing_header_from_file(self):
        """
        method name: compare_headers
        scenario: when the headers from the file have fewer than the headers needed from the template
        expected: the template headers update the additional expected headers
        """

        self.headers_provider_mock.get_headers.return_value = ["h1", "h2", "h3"]

        original_file_headers = ["header 1", "header 2"]
        original_template_headers = {"h1": "header 1", "h2": "header 2", "h3": ""}
        updated_file_headers = ["header 1", "header 2", "h3"]
        updated_template_headers = {"h1": "header 1", "h2": "header 2", "h3": "h3"}
        compare_headers(original_file_headers, original_template_headers, self.headers_provider_mock)
        assert updated_template_headers == original_template_headers
        assert original_file_headers == updated_file_headers

    def test_comparing_headers_with_extra_header_in_file(self):
        """
        method name: compare_headers
        scenario: when the headers from the file have fewer than the headers needed from the template
        expected: the template headers update the additional expected headers
        """

        self.headers_provider_mock.get_headers.return_value = ["h1", "h2"]

        original_file_headers = ["header 1", "header 2", "header 3"]
        original_template_headers = {"h1": "header 1", "h2": "header 2"}
        updated_file_headers = copy(original_file_headers)
        updated_template_headers = copy(original_template_headers)
        compare_headers(original_file_headers, original_template_headers, self.headers_provider_mock)
        assert updated_template_headers == original_template_headers
        assert original_file_headers == updated_file_headers

