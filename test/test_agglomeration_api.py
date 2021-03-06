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
from dbpedia.api.agglomeration_api import AgglomerationApi  # noqa: E501
from dbpedia.rest import ApiException


class TestAgglomerationApi(unittest.TestCase):
    """AgglomerationApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.agglomeration_api.AgglomerationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_agglomerations_get(self):
        """Test case for agglomerations_get

        List all instances of Agglomeration  # noqa: E501
        """
        pass

    def test_agglomerations_id_get(self):
        """Test case for agglomerations_id_get

        Get a single Agglomeration by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
