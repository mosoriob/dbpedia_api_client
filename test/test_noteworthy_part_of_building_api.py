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
from dbpedia.api.noteworthy_part_of_building_api import NoteworthyPartOfBuildingApi  # noqa: E501
from dbpedia.rest import ApiException


class TestNoteworthyPartOfBuildingApi(unittest.TestCase):
    """NoteworthyPartOfBuildingApi unit test stubs"""

    def setUp(self):
        self.api = dbpedia.api.noteworthy_part_of_building_api.NoteworthyPartOfBuildingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_noteworthypartofbuildings_get(self):
        """Test case for noteworthypartofbuildings_get

        List all instances of NoteworthyPartOfBuilding  # noqa: E501
        """
        pass

    def test_noteworthypartofbuildings_id_get(self):
        """Test case for noteworthypartofbuildings_id_get

        Get a single NoteworthyPartOfBuilding by its id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
