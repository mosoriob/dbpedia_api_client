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
from dbpedia.api.guitarist_api import GuitaristApi  # noqa: E501
from dbpedia.rest import ApiException


class TestGuitaristApi(unittest.TestCase):
    """GuitaristApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.guitarist_api.GuitaristApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_guitarists_get(self):
        """Test case for guitarists_get

        List all instances of Guitarist  # noqa: E501
        """
        pass

    def test_guitarists_id_get(self):
        """Test case for guitarists_id_get

        Get a single Guitarist by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
