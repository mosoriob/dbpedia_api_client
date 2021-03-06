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
from dbpedia.api.pyramid_api import PyramidApi  # noqa: E501
from dbpedia.rest import ApiException


class TestPyramidApi(unittest.TestCase):
    """PyramidApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.pyramid_api.PyramidApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pyramids_get(self):
        """Test case for pyramids_get

        List all instances of Pyramid  # noqa: E501
        """
        pass

    def test_pyramids_id_get(self):
        """Test case for pyramids_id_get

        Get a single Pyramid by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
