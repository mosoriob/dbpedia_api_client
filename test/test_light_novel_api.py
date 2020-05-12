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
from dbpedia.api.light_novel_api import LightNovelApi  # noqa: E501
from dbpedia.rest import ApiException


class TestLightNovelApi(unittest.TestCase):
    """LightNovelApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.light_novel_api.LightNovelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_lightnovels_get(self):
        """Test case for lightnovels_get

        List all instances of LightNovel  # noqa: E501
        """
        pass

    def test_lightnovels_id_get(self):
        """Test case for lightnovels_id_get

        Get a single LightNovel by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()