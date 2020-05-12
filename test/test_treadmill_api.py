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
from dbpedia.api.treadmill_api import TreadmillApi  # noqa: E501
from dbpedia.rest import ApiException


class TestTreadmillApi(unittest.TestCase):
    """TreadmillApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.treadmill_api.TreadmillApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_treadmills_get(self):
        """Test case for treadmills_get

        List all instances of Treadmill  # noqa: E501
        """
        pass

    def test_treadmills_id_get(self):
        """Test case for treadmills_id_get

        Get a single Treadmill by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
