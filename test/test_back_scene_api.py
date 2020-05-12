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
from dbpedia.api.back_scene_api import BackSceneApi  # noqa: E501
from dbpedia.rest import ApiException


class TestBackSceneApi(unittest.TestCase):
    """BackSceneApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.back_scene_api.BackSceneApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_backscenes_get(self):
        """Test case for backscenes_get

        List all instances of BackScene  # noqa: E501
        """
        pass

    def test_backscenes_id_get(self):
        """Test case for backscenes_id_get

        Get a single BackScene by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
