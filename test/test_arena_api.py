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
from dbpedia.api.arena_api import ArenaApi  # noqa: E501
from dbpedia.rest import ApiException


class TestArenaApi(unittest.TestCase):
    """ArenaApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.arena_api.ArenaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_arenas_get(self):
        """Test case for arenas_get

        List all instances of Arena  # noqa: E501
        """
        pass

    def test_arenas_id_get(self):
        """Test case for arenas_id_get

        Get a single Arena by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
