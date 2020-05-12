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
from dbpedia.api.depth_api import DepthApi  # noqa: E501
from dbpedia.rest import ApiException


class TestDepthApi(unittest.TestCase):
    """DepthApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.depth_api.DepthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_depths_get(self):
        """Test case for depths_get

        List all instances of Depth  # noqa: E501
        """
        pass

    def test_depths_id_get(self):
        """Test case for depths_id_get

        Get a single Depth by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
