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
from dbpedia.api.deity_api import DeityApi  # noqa: E501
from dbpedia.rest import ApiException


class TestDeityApi(unittest.TestCase):
    """DeityApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.deity_api.DeityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deitys_get(self):
        """Test case for deitys_get

        List all instances of Deity  # noqa: E501
        """
        pass

    def test_deitys_id_get(self):
        """Test case for deitys_id_get

        Get a single Deity by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
