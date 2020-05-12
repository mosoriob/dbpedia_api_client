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
from dbpedia.models.board_game import BoardGame  # noqa: E501
from dbpedia.rest import ApiException

class TestBoardGame(unittest.TestCase):
    """BoardGame unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BoardGame
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.board_game.BoardGame()  # noqa: E501
        if include_optional :
            return BoardGame(
                number_of_players = [
                    56
                    ], 
                number_of_professionals = [
                    56
                    ], 
                number_of_clubs = [
                    56
                    ], 
                description = [
                    '0'
                    ], 
                equipment = [
                    None
                    ], 
                id = '0', 
                label = [
                    '0'
                    ], 
                number_of_people_licensed = [
                    56
                    ], 
                type = [
                    '0'
                    ]
            )
        else :
            return BoardGame(
        )

    def testBoardGame(self):
        """Test BoardGame"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
