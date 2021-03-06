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
from dbpedia.api.port_api import PortApi  # noqa: E501
from dbpedia.rest import ApiException


class TestPortApi(unittest.TestCase):
    """PortApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.port_api.PortApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ports_get(self):
        """Test case for ports_get

        List all instances of Port  # noqa: E501
        """
        pass

    def test_ports_id_get(self):
        """Test case for ports_id_get

        Get a single Port by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
