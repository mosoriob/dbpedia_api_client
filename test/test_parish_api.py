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
from dbpedia.api.parish_api import ParishApi  # noqa: E501
from dbpedia.rest import ApiException


class TestParishApi(unittest.TestCase):
    """ParishApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.parish_api.ParishApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_parishs_get(self):
        """Test case for parishs_get

        List all instances of Parish  # noqa: E501
        """
        pass

    def test_parishs_id_get(self):
        """Test case for parishs_id_get

        Get a single Parish by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
