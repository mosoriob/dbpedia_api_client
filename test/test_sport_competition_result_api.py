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
from dbpedia.api.sport_competition_result_api import SportCompetitionResultApi  # noqa: E501
from dbpedia.rest import ApiException


class TestSportCompetitionResultApi(unittest.TestCase):
    """SportCompetitionResultApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.sport_competition_result_api.SportCompetitionResultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sportcompetitionresults_get(self):
        """Test case for sportcompetitionresults_get

        List all instances of SportCompetitionResult  # noqa: E501
        """
        pass

    def test_sportcompetitionresults_id_get(self):
        """Test case for sportcompetitionresults_id_get

        Get a single SportCompetitionResult by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
