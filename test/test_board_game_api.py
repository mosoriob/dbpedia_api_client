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
from dbpedia.api.board_game_api import BoardGameApi  # noqa: E501
from dbpedia.rest import ApiException


class TestBoardGameApi(unittest.TestCase):
    """BoardGameApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.board_game_api.BoardGameApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_boardgames_get(self):
        """Test case for boardgames_get

        List all instances of BoardGame  # noqa: E501
        """
        pass

    def test_boardgames_id_get(self):
        """Test case for boardgames_id_get

        Get a single BoardGame by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()