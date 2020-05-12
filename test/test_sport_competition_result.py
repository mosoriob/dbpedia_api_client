# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import dbpedia
from dbpedia.models.sport_competition_result import SportCompetitionResult  # noqa: E501
from dbpedia.rest import ApiException

class TestSportCompetitionResult(unittest.TestCase):
    """SportCompetitionResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SportCompetitionResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.sport_competition_result.SportCompetitionResult()  # noqa: E501
        if include_optional :
            return SportCompetitionResult(
                number_of_bronze_medals_won = [
                    56
                    ], 
                description = [
                    '0'
                    ], 
                number_of_silver_medals_won = [
                    56
                    ], 
                competition = [
                    None
                    ], 
                id = '0', 
                label = [
                    '0'
                    ], 
                type = [
                    '0'
                    ], 
                number_of_gold_medals_won = [
                    56
                    ]
            )
        else :
            return SportCompetitionResult(
        )

    def testSportCompetitionResult(self):
        """Test SportCompetitionResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
