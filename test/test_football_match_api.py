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
from dbpedia.api.football_match_api import FootballMatchApi  # noqa: E501
from dbpedia.rest import ApiException


class TestFootballMatchApi(unittest.TestCase):
    """FootballMatchApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.football_match_api.FootballMatchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_footballmatchs_get(self):
        """Test case for footballmatchs_get

        List all instances of FootballMatch  # noqa: E501
        """
        pass

    def test_footballmatchs_id_get(self):
        """Test case for footballmatchs_id_get

        Get a single FootballMatch by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
