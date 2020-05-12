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
from dbpedia.api.inline_hockey_league_api import InlineHockeyLeagueApi  # noqa: E501
from dbpedia.rest import ApiException


class TestInlineHockeyLeagueApi(unittest.TestCase):
    """InlineHockeyLeagueApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.inline_hockey_league_api.InlineHockeyLeagueApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_inlinehockeyleagues_get(self):
        """Test case for inlinehockeyleagues_get

        List all instances of InlineHockeyLeague  # noqa: E501
        """
        pass

    def test_inlinehockeyleagues_id_get(self):
        """Test case for inlinehockeyleagues_id_get

        Get a single InlineHockeyLeague by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()