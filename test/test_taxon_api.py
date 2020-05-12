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
from dbpedia.api.taxon_api import TaxonApi  # noqa: E501
from dbpedia.rest import ApiException


class TestTaxonApi(unittest.TestCase):
    """TaxonApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.taxon_api.TaxonApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_taxons_get(self):
        """Test case for taxons_get

        List all instances of Taxon  # noqa: E501
        """
        pass

    def test_taxons_id_get(self):
        """Test case for taxons_id_get

        Get a single Taxon by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
