# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dbpedia.configuration import Configuration


class ResearchProject(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'project_reference_id': 'list[str]',
        'project_end_date': 'list[str]',
        'project_objective': 'list[str]',
        'project_type': 'list[str]',
        'description': 'list[str]',
        'label': 'list[str]',
        'type': 'list[str]',
        'funded_by': 'list[object]',
        'project_coordinator': 'list[object]',
        'project_keyword': 'list[str]',
        'project_budget_total': 'list[float]',
        'project_start_date': 'list[str]',
        'project_participant': 'list[object]',
        'project_budget_funding': 'list[float]',
        'developer': 'list[object]',
        'id': 'str'
    }

    attribute_map = {
        'project_reference_id': 'projectReferenceID',
        'project_end_date': 'projectEndDate',
        'project_objective': 'projectObjective',
        'project_type': 'projectType',
        'description': 'description',
        'label': 'label',
        'type': 'type',
        'funded_by': 'fundedBy',
        'project_coordinator': 'projectCoordinator',
        'project_keyword': 'projectKeyword',
        'project_budget_total': 'projectBudgetTotal',
        'project_start_date': 'projectStartDate',
        'project_participant': 'projectParticipant',
        'project_budget_funding': 'projectBudgetFunding',
        'developer': 'developer',
        'id': 'id'
    }

    def __init__(self, project_reference_id=None, project_end_date=None, project_objective=None, project_type=None, description=None, label=None, type=None, funded_by=None, project_coordinator=None, project_keyword=None, project_budget_total=None, project_start_date=None, project_participant=None, project_budget_funding=None, developer=None, id=None, local_vars_configuration=None):  # noqa: E501
        """ResearchProject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project_reference_id = None
        self._project_end_date = None
        self._project_objective = None
        self._project_type = None
        self._description = None
        self._label = None
        self._type = None
        self._funded_by = None
        self._project_coordinator = None
        self._project_keyword = None
        self._project_budget_total = None
        self._project_start_date = None
        self._project_participant = None
        self._project_budget_funding = None
        self._developer = None
        self._id = None
        self.discriminator = None

        self.project_reference_id = project_reference_id
        self.project_end_date = project_end_date
        self.project_objective = project_objective
        self.project_type = project_type
        self.description = description
        self.label = label
        self.type = type
        self.funded_by = funded_by
        self.project_coordinator = project_coordinator
        self.project_keyword = project_keyword
        self.project_budget_total = project_budget_total
        self.project_start_date = project_start_date
        self.project_participant = project_participant
        self.project_budget_funding = project_budget_funding
        self.developer = developer
        if id is not None:
            self.id = id

    @property
    def project_reference_id(self):
        """Gets the project_reference_id of this ResearchProject.  # noqa: E501

        The reference identification of the project.  # noqa: E501

        :return: The project_reference_id of this ResearchProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._project_reference_id

    @project_reference_id.setter
    def project_reference_id(self, project_reference_id):
        """Sets the project_reference_id of this ResearchProject.

        The reference identification of the project.  # noqa: E501

        :param project_reference_id: The project_reference_id of this ResearchProject.  # noqa: E501
        :type: list[str]
        """

        self._project_reference_id = project_reference_id

    @property
    def project_end_date(self):
        """Gets the project_end_date of this ResearchProject.  # noqa: E501

        The end date of the project.  # noqa: E501

        :return: The project_end_date of this ResearchProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._project_end_date

    @project_end_date.setter
    def project_end_date(self, project_end_date):
        """Sets the project_end_date of this ResearchProject.

        The end date of the project.  # noqa: E501

        :param project_end_date: The project_end_date of this ResearchProject.  # noqa: E501
        :type: list[str]
        """

        self._project_end_date = project_end_date

    @property
    def project_objective(self):
        """Gets the project_objective of this ResearchProject.  # noqa: E501

        A defined objective of the project.  # noqa: E501

        :return: The project_objective of this ResearchProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._project_objective

    @project_objective.setter
    def project_objective(self, project_objective):
        """Sets the project_objective of this ResearchProject.

        A defined objective of the project.  # noqa: E501

        :param project_objective: The project_objective of this ResearchProject.  # noqa: E501
        :type: list[str]
        """

        self._project_objective = project_objective

    @property
    def project_type(self):
        """Gets the project_type of this ResearchProject.  # noqa: E501

        The type of the research project. Mostly used for the funding schemes of the European Union, for instance: Specific Targeted Research Projects (STREP), Network of Excellence (NoE) or Integrated Project.  # noqa: E501

        :return: The project_type of this ResearchProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        """Sets the project_type of this ResearchProject.

        The type of the research project. Mostly used for the funding schemes of the European Union, for instance: Specific Targeted Research Projects (STREP), Network of Excellence (NoE) or Integrated Project.  # noqa: E501

        :param project_type: The project_type of this ResearchProject.  # noqa: E501
        :type: list[str]
        """

        self._project_type = project_type

    @property
    def description(self):
        """Gets the description of this ResearchProject.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this ResearchProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResearchProject.

        small description  # noqa: E501

        :param description: The description of this ResearchProject.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def label(self):
        """Gets the label of this ResearchProject.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this ResearchProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ResearchProject.

        short description of the resource  # noqa: E501

        :param label: The label of this ResearchProject.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this ResearchProject.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this ResearchProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResearchProject.

        type of the resource  # noqa: E501

        :param type: The type of this ResearchProject.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def funded_by(self):
        """Gets the funded_by of this ResearchProject.  # noqa: E501

        A organisation financing the research project.  # noqa: E501

        :return: The funded_by of this ResearchProject.  # noqa: E501
        :rtype: list[object]
        """
        return self._funded_by

    @funded_by.setter
    def funded_by(self, funded_by):
        """Sets the funded_by of this ResearchProject.

        A organisation financing the research project.  # noqa: E501

        :param funded_by: The funded_by of this ResearchProject.  # noqa: E501
        :type: list[object]
        """

        self._funded_by = funded_by

    @property
    def project_coordinator(self):
        """Gets the project_coordinator of this ResearchProject.  # noqa: E501

        The coordinating organisation of the project.  # noqa: E501

        :return: The project_coordinator of this ResearchProject.  # noqa: E501
        :rtype: list[object]
        """
        return self._project_coordinator

    @project_coordinator.setter
    def project_coordinator(self, project_coordinator):
        """Sets the project_coordinator of this ResearchProject.

        The coordinating organisation of the project.  # noqa: E501

        :param project_coordinator: The project_coordinator of this ResearchProject.  # noqa: E501
        :type: list[object]
        """

        self._project_coordinator = project_coordinator

    @property
    def project_keyword(self):
        """Gets the project_keyword of this ResearchProject.  # noqa: E501

        A key word of the project.  # noqa: E501

        :return: The project_keyword of this ResearchProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._project_keyword

    @project_keyword.setter
    def project_keyword(self, project_keyword):
        """Sets the project_keyword of this ResearchProject.

        A key word of the project.  # noqa: E501

        :param project_keyword: The project_keyword of this ResearchProject.  # noqa: E501
        :type: list[str]
        """

        self._project_keyword = project_keyword

    @property
    def project_budget_total(self):
        """Gets the project_budget_total of this ResearchProject.  # noqa: E501

        The total budget of the research project.  # noqa: E501

        :return: The project_budget_total of this ResearchProject.  # noqa: E501
        :rtype: list[float]
        """
        return self._project_budget_total

    @project_budget_total.setter
    def project_budget_total(self, project_budget_total):
        """Sets the project_budget_total of this ResearchProject.

        The total budget of the research project.  # noqa: E501

        :param project_budget_total: The project_budget_total of this ResearchProject.  # noqa: E501
        :type: list[float]
        """

        self._project_budget_total = project_budget_total

    @property
    def project_start_date(self):
        """Gets the project_start_date of this ResearchProject.  # noqa: E501

        The start date of the project.  # noqa: E501

        :return: The project_start_date of this ResearchProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._project_start_date

    @project_start_date.setter
    def project_start_date(self, project_start_date):
        """Sets the project_start_date of this ResearchProject.

        The start date of the project.  # noqa: E501

        :param project_start_date: The project_start_date of this ResearchProject.  # noqa: E501
        :type: list[str]
        """

        self._project_start_date = project_start_date

    @property
    def project_participant(self):
        """Gets the project_participant of this ResearchProject.  # noqa: E501

        A participating organisation of the project.  # noqa: E501

        :return: The project_participant of this ResearchProject.  # noqa: E501
        :rtype: list[object]
        """
        return self._project_participant

    @project_participant.setter
    def project_participant(self, project_participant):
        """Sets the project_participant of this ResearchProject.

        A participating organisation of the project.  # noqa: E501

        :param project_participant: The project_participant of this ResearchProject.  # noqa: E501
        :type: list[object]
        """

        self._project_participant = project_participant

    @property
    def project_budget_funding(self):
        """Gets the project_budget_funding of this ResearchProject.  # noqa: E501

        The part of the project budget that is funded by the Organistaions given in the \"FundedBy\" property.  # noqa: E501

        :return: The project_budget_funding of this ResearchProject.  # noqa: E501
        :rtype: list[float]
        """
        return self._project_budget_funding

    @project_budget_funding.setter
    def project_budget_funding(self, project_budget_funding):
        """Sets the project_budget_funding of this ResearchProject.

        The part of the project budget that is funded by the Organistaions given in the \"FundedBy\" property.  # noqa: E501

        :param project_budget_funding: The project_budget_funding of this ResearchProject.  # noqa: E501
        :type: list[float]
        """

        self._project_budget_funding = project_budget_funding

    @property
    def developer(self):
        """Gets the developer of this ResearchProject.  # noqa: E501

        Description not available  # noqa: E501

        :return: The developer of this ResearchProject.  # noqa: E501
        :rtype: list[object]
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        """Sets the developer of this ResearchProject.

        Description not available  # noqa: E501

        :param developer: The developer of this ResearchProject.  # noqa: E501
        :type: list[object]
        """

        self._developer = developer

    @property
    def id(self):
        """Gets the id of this ResearchProject.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this ResearchProject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResearchProject.

        identifier  # noqa: E501

        :param id: The id of this ResearchProject.  # noqa: E501
        :type: str
        """

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResearchProject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResearchProject):
            return True

        return self.to_dict() != other.to_dict()
