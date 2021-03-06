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
from dbpedia.api.mammal_api import MammalApi  # noqa: E501
from dbpedia.rest import ApiException


class TestMammalApi(unittest.TestCase):
    """MammalApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.mammal_api.MammalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_mammals_get(self):
        """Test case for mammals_get

        List all instances of Mammal  # noqa: E501
        """
        pass

    def test_mammals_id_get(self):
        """Test case for mammals_id_get

        Get a single Mammal by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
