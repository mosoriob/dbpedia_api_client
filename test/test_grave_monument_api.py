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
from dbpedia.api.grave_monument_api import GraveMonumentApi  # noqa: E501
from dbpedia.rest import ApiException


class TestGraveMonumentApi(unittest.TestCase):
    """GraveMonumentApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.grave_monument_api.GraveMonumentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_gravemonuments_get(self):
        """Test case for gravemonuments_get

        List all instances of GraveMonument  # noqa: E501
        """
        pass

    def test_gravemonuments_id_get(self):
        """Test case for gravemonuments_id_get

        Get a single GraveMonument by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
