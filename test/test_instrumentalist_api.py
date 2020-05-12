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
from dbpedia.api.instrumentalist_api import InstrumentalistApi  # noqa: E501
from dbpedia.rest import ApiException


class TestInstrumentalistApi(unittest.TestCase):
    """InstrumentalistApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.instrumentalist_api.InstrumentalistApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_instrumentalists_get(self):
        """Test case for instrumentalists_get

        List all instances of Instrumentalist  # noqa: E501
        """
        pass

    def test_instrumentalists_id_get(self):
        """Test case for instrumentalists_id_get

        Get a single Instrumentalist by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
