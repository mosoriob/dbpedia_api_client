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
from dbpedia.api.municipality_api import MunicipalityApi  # noqa: E501
from dbpedia.rest import ApiException


class TestMunicipalityApi(unittest.TestCase):
    """MunicipalityApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.municipality_api.MunicipalityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_municipalitys_get(self):
        """Test case for municipalitys_get

        List all instances of Municipality  # noqa: E501
        """
        pass

    def test_municipalitys_id_get(self):
        """Test case for municipalitys_id_get

        Get a single Municipality by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
