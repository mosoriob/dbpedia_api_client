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
from dbpedia.api.government_type_api import GovernmentTypeApi  # noqa: E501
from dbpedia.rest import ApiException


class TestGovernmentTypeApi(unittest.TestCase):
    """GovernmentTypeApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.government_type_api.GovernmentTypeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_governmenttypes_get(self):
        """Test case for governmenttypes_get

        List all instances of GovernmentType  # noqa: E501
        """
        pass

    def test_governmenttypes_id_get(self):
        """Test case for governmenttypes_id_get

        Get a single GovernmentType by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
