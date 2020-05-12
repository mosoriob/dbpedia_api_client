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
from dbpedia.api.comic_strip_api import ComicStripApi  # noqa: E501
from dbpedia.rest import ApiException


class TestComicStripApi(unittest.TestCase):
    """ComicStripApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.comic_strip_api.ComicStripApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_comicstrips_get(self):
        """Test case for comicstrips_get

        List all instances of ComicStrip  # noqa: E501
        """
        pass

    def test_comicstrips_id_get(self):
        """Test case for comicstrips_id_get

        Get a single ComicStrip by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
