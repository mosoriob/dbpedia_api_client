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
from dbpedia.api.gymnast_api import GymnastApi  # noqa: E501
from dbpedia.rest import ApiException


class TestGymnastApi(unittest.TestCase):
    """GymnastApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.gymnast_api.GymnastApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_gymnasts_get(self):
        """Test case for gymnasts_get

        List all instances of Gymnast  # noqa: E501
        """
        pass

    def test_gymnasts_id_get(self):
        """Test case for gymnasts_id_get

        Get a single Gymnast by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
