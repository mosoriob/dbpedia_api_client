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
from dbpedia.api.national_anthem_api import NationalAnthemApi  # noqa: E501
from dbpedia.rest import ApiException


class TestNationalAnthemApi(unittest.TestCase):
    """NationalAnthemApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.national_anthem_api.NationalAnthemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_nationalanthems_get(self):
        """Test case for nationalanthems_get

        List all instances of NationalAnthem  # noqa: E501
        """
        pass

    def test_nationalanthems_id_get(self):
        """Test case for nationalanthems_id_get

        Get a single NationalAnthem by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
