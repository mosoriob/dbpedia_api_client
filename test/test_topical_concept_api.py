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
from dbpedia.api.topical_concept_api import TopicalConceptApi  # noqa: E501
from dbpedia.rest import ApiException


class TestTopicalConceptApi(unittest.TestCase):
    """TopicalConceptApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.topical_concept_api.TopicalConceptApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_topicalconcepts_get(self):
        """Test case for topicalconcepts_get

        List all instances of TopicalConcept  # noqa: E501
        """
        pass

    def test_topicalconcepts_id_get(self):
        """Test case for topicalconcepts_id_get

        Get a single TopicalConcept by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
