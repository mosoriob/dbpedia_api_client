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
from dbpedia.api.office_holder_api import OfficeHolderApi  # noqa: E501
from dbpedia.rest import ApiException


class TestOfficeHolderApi(unittest.TestCase):
    """OfficeHolderApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.office_holder_api.OfficeHolderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_officeholders_get(self):
        """Test case for officeholders_get

        List all instances of OfficeHolder  # noqa: E501
        """
        pass

    def test_officeholders_id_get(self):
        """Test case for officeholders_id_get

        Get a single OfficeHolder by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
