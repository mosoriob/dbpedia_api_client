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
from dbpedia.api.paintball_league_api import PaintballLeagueApi  # noqa: E501
from dbpedia.rest import ApiException


class TestPaintballLeagueApi(unittest.TestCase):
    """PaintballLeagueApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.paintball_league_api.PaintballLeagueApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_paintballleagues_get(self):
        """Test case for paintballleagues_get

        List all instances of PaintballLeague  # noqa: E501
        """
        pass

    def test_paintballleagues_id_get(self):
        """Test case for paintballleagues_id_get

        Get a single PaintballLeague by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
