# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import dbpedia
from dbpedia.api.book_api import BookApi  # noqa: E501
from dbpedia.rest import ApiException


class TestBookApi(unittest.TestCase):
    """BookApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.book_api.BookApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_books_get(self):
        """Test case for books_get

        List all instances of Book  # noqa: E501
        """
        pass

    def test_books_id_get(self):
        """Test case for books_id_get

        Get a single Book by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
