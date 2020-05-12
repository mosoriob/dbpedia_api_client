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
from dbpedia.api.lacrosse_player_api import LacrossePlayerApi  # noqa: E501
from dbpedia.rest import ApiException


class TestLacrossePlayerApi(unittest.TestCase):
    """LacrossePlayerApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.lacrosse_player_api.LacrossePlayerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_lacrosseplayers_get(self):
        """Test case for lacrosseplayers_get

        List all instances of LacrossePlayer  # noqa: E501
        """
        pass

    def test_lacrosseplayers_id_get(self):
        """Test case for lacrosseplayers_id_get

        Get a single LacrossePlayer by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
