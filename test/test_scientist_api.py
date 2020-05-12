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
from dbpedia.api.scientist_api import ScientistApi  # noqa: E501
from dbpedia.rest import ApiException


class TestScientistApi(unittest.TestCase):
    """ScientistApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.scientist_api.ScientistApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_scientists_get(self):
        """Test case for scientists_get

        List all instances of Scientist  # noqa: E501
        """
        pass

    def test_scientists_id_get(self):
        """Test case for scientists_id_get

        Get a single Scientist by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
