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
from dbpedia.api.rocket_api import RocketApi  # noqa: E501
from dbpedia.rest import ApiException


class TestRocketApi(unittest.TestCase):
    """RocketApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.rocket_api.RocketApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_rockets_get(self):
        """Test case for rockets_get

        List all instances of Rocket  # noqa: E501
        """
        pass

    def test_rockets_id_get(self):
        """Test case for rockets_id_get

        Get a single Rocket by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()