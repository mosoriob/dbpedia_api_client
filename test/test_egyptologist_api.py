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
from dbpedia.api.egyptologist_api import EgyptologistApi  # noqa: E501
from dbpedia.rest import ApiException


class TestEgyptologistApi(unittest.TestCase):
    """EgyptologistApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.egyptologist_api.EgyptologistApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_egyptologists_get(self):
        """Test case for egyptologists_get

        List all instances of Egyptologist  # noqa: E501
        """
        pass

    def test_egyptologists_id_get(self):
        """Test case for egyptologists_id_get

        Get a single Egyptologist by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
