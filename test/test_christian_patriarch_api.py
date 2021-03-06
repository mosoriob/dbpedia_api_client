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
from dbpedia.api.christian_patriarch_api import ChristianPatriarchApi  # noqa: E501
from dbpedia.rest import ApiException


class TestChristianPatriarchApi(unittest.TestCase):
    """ChristianPatriarchApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.christian_patriarch_api.ChristianPatriarchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_christianpatriarchs_get(self):
        """Test case for christianpatriarchs_get

        List all instances of ChristianPatriarch  # noqa: E501
        """
        pass

    def test_christianpatriarchs_id_get(self):
        """Test case for christianpatriarchs_id_get

        Get a single ChristianPatriarch by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
