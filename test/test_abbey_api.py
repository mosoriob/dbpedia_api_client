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
from dbpedia.api.abbey_api import AbbeyApi  # noqa: E501
from dbpedia.rest import ApiException


class TestAbbeyApi(unittest.TestCase):
    """AbbeyApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.abbey_api.AbbeyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_abbeys_get(self):
        """Test case for abbeys_get

        List all instances of Abbey  # noqa: E501
        """
        pass

    def test_abbeys_id_get(self):
        """Test case for abbeys_id_get

        Get a single Abbey by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
