# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import dbpedia
from dbpedia.models.research_project import ResearchProject  # noqa: E501
from dbpedia.rest import ApiException

class TestResearchProject(unittest.TestCase):
    """ResearchProject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResearchProject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.research_project.ResearchProject()  # noqa: E501
        if include_optional :
            return ResearchProject(
                project_reference_id = [
                    '0'
                    ], 
                project_end_date = [
                    '0'
                    ], 
                project_objective = [
                    '0'
                    ], 
                project_type = [
                    '0'
                    ], 
                description = [
                    '0'
                    ], 
                label = [
                    '0'
                    ], 
                type = [
                    '0'
                    ], 
                funded_by = [
                    None
                    ], 
                project_coordinator = [
                    None
                    ], 
                project_keyword = [
                    '0'
                    ], 
                project_budget_total = [
                    1.337
                    ], 
                project_start_date = [
                    '0'
                    ], 
                project_participant = [
                    None
                    ], 
                project_budget_funding = [
                    1.337
                    ], 
                developer = [
                    None
                    ], 
                id = '0'
            )
        else :
            return ResearchProject(
        )

    def testResearchProject(self):
        """Test ResearchProject"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
