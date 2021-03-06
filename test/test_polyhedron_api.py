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
from dbpedia.api.polyhedron_api import PolyhedronApi  # noqa: E501
from dbpedia.rest import ApiException


class TestPolyhedronApi(unittest.TestCase):
    """PolyhedronApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.polyhedron_api.PolyhedronApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_polyhedrons_get(self):
        """Test case for polyhedrons_get

        List all instances of Polyhedron  # noqa: E501
        """
        pass

    def test_polyhedrons_id_get(self):
        """Test case for polyhedrons_id_get

        Get a single Polyhedron by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
