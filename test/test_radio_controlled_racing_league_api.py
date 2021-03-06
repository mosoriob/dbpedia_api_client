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
from dbpedia.api.radio_controlled_racing_league_api import RadioControlledRacingLeagueApi  # noqa: E501
from dbpedia.rest import ApiException


class TestRadioControlledRacingLeagueApi(unittest.TestCase):
    """RadioControlledRacingLeagueApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.radio_controlled_racing_league_api.RadioControlledRacingLeagueApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_radiocontrolledracingleagues_get(self):
        """Test case for radiocontrolledracingleagues_get

        List all instances of RadioControlledRacingLeague  # noqa: E501
        """
        pass

    def test_radiocontrolledracingleagues_id_get(self):
        """Test case for radiocontrolledracingleagues_id_get

        Get a single RadioControlledRacingLeague by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
