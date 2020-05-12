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
from dbpedia.api.naruto_character_api import NarutoCharacterApi  # noqa: E501
from dbpedia.rest import ApiException


class TestNarutoCharacterApi(unittest.TestCase):
    """NarutoCharacterApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.naruto_character_api.NarutoCharacterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_narutocharacters_get(self):
        """Test case for narutocharacters_get

        List all instances of NarutoCharacter  # noqa: E501
        """
        pass

    def test_narutocharacters_id_get(self):
        """Test case for narutocharacters_id_get

        Get a single NarutoCharacter by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()