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
from dbpedia.api.legislature_api import LegislatureApi  # noqa: E501
from dbpedia.rest import ApiException


class TestLegislatureApi(unittest.TestCase):
    """LegislatureApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.legislature_api.LegislatureApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_legislatures_get(self):
        """Test case for legislatures_get

        List all instances of Legislature  # noqa: E501
        """
        pass

    def test_legislatures_id_get(self):
        """Test case for legislatures_id_get

        Get a single Legislature by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
