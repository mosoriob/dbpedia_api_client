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
from dbpedia.api.public_service_output_api import PublicServiceOutputApi  # noqa: E501
from dbpedia.rest import ApiException


class TestPublicServiceOutputApi(unittest.TestCase):
    """PublicServiceOutputApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.public_service_output_api.PublicServiceOutputApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_publicserviceoutputs_get(self):
        """Test case for publicserviceoutputs_get

        List all instances of PublicServiceOutput  # noqa: E501
        """
        pass

    def test_publicserviceoutputs_id_get(self):
        """Test case for publicserviceoutputs_id_get

        Get a single PublicServiceOutput by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()