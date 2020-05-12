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
from dbpedia.api.library_api import LibraryApi  # noqa: E501
from dbpedia.rest import ApiException


class TestLibraryApi(unittest.TestCase):
    """LibraryApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.library_api.LibraryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_librarys_get(self):
        """Test case for librarys_get

        List all instances of Library  # noqa: E501
        """
        pass

    def test_librarys_id_get(self):
        """Test case for librarys_id_get

        Get a single Library by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()