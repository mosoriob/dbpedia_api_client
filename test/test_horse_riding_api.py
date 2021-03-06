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
from dbpedia.api.horse_riding_api import HorseRidingApi  # noqa: E501
from dbpedia.rest import ApiException


class TestHorseRidingApi(unittest.TestCase):
    """HorseRidingApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.horse_riding_api.HorseRidingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_horseridings_get(self):
        """Test case for horseridings_get

        List all instances of HorseRiding  # noqa: E501
        """
        pass

    def test_horseridings_id_get(self):
        """Test case for horseridings_id_get

        Get a single HorseRiding by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
