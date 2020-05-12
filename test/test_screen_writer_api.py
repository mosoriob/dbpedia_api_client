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
from dbpedia.api.screen_writer_api import ScreenWriterApi  # noqa: E501
from dbpedia.rest import ApiException


class TestScreenWriterApi(unittest.TestCase):
    """ScreenWriterApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.screen_writer_api.ScreenWriterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_screenwriters_get(self):
        """Test case for screenwriters_get

        List all instances of ScreenWriter  # noqa: E501
        """
        pass

    def test_screenwriters_id_get(self):
        """Test case for screenwriters_id_get

        Get a single ScreenWriter by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
