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


class Project(object):
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
        'project_keyword': 'list[str]',
        'project_end_date': 'list[str]',
        'project_start_date': 'list[str]',
        'project_objective': 'list[str]',
        'description': 'list[str]',
        'developer': 'list[object]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]'
    }

    attribute_map = {
        'project_keyword': 'projectKeyword',
        'project_end_date': 'projectEndDate',
        'project_start_date': 'projectStartDate',
        'project_objective': 'projectObjective',
        'description': 'description',
        'developer': 'developer',
        'id': 'id',
        'label': 'label',
        'type': 'type'
    }

    def __init__(self, project_keyword=None, project_end_date=None, project_start_date=None, project_objective=None, description=None, developer=None, id=None, label=None, type=None, local_vars_configuration=None):  # noqa: E501
        """Project - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project_keyword = None
        self._project_end_date = None
        self._project_start_date = None
        self._project_objective = None
        self._description = None
        self._developer = None
        self._id = None
        self._label = None
        self._type = None
        self.discriminator = None

        self.project_keyword = project_keyword
        self.project_end_date = project_end_date
        self.project_start_date = project_start_date
        self.project_objective = project_objective
        self.description = description
        self.developer = developer
        if id is not None:
            self.id = id
        self.label = label
        self.type = type

    @property
    def project_keyword(self):
        """Gets the project_keyword of this Project.  # noqa: E501

        A key word of the project.  # noqa: E501

        :return: The project_keyword of this Project.  # noqa: E501
        :rtype: list[str]
        """
        return self._project_keyword

    @project_keyword.setter
    def project_keyword(self, project_keyword):
        """Sets the project_keyword of this Project.

        A key word of the project.  # noqa: E501

        :param project_keyword: The project_keyword of this Project.  # noqa: E501
        :type: list[str]
        """

        self._project_keyword = project_keyword

    @property
    def project_end_date(self):
        """Gets the project_end_date of this Project.  # noqa: E501

        The end date of the project.  # noqa: E501

        :return: The project_end_date of this Project.  # noqa: E501
        :rtype: list[str]
        """
        return self._project_end_date

    @project_end_date.setter
    def project_end_date(self, project_end_date):
        """Sets the project_end_date of this Project.

        The end date of the project.  # noqa: E501

        :param project_end_date: The project_end_date of this Project.  # noqa: E501
        :type: list[str]
        """

        self._project_end_date = project_end_date

    @property
    def project_start_date(self):
        """Gets the project_start_date of this Project.  # noqa: E501

        The start date of the project.  # noqa: E501

        :return: The project_start_date of this Project.  # noqa: E501
        :rtype: list[str]
        """
        return self._project_start_date

    @project_start_date.setter
    def project_start_date(self, project_start_date):
        """Sets the project_start_date of this Project.

        The start date of the project.  # noqa: E501

        :param project_start_date: The project_start_date of this Project.  # noqa: E501
        :type: list[str]
        """

        self._project_start_date = project_start_date

    @property
    def project_objective(self):
        """Gets the project_objective of this Project.  # noqa: E501

        A defined objective of the project.  # noqa: E501

        :return: The project_objective of this Project.  # noqa: E501
        :rtype: list[str]
        """
        return self._project_objective

    @project_objective.setter
    def project_objective(self, project_objective):
        """Sets the project_objective of this Project.

        A defined objective of the project.  # noqa: E501

        :param project_objective: The project_objective of this Project.  # noqa: E501
        :type: list[str]
        """

        self._project_objective = project_objective

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Project.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.

        small description  # noqa: E501

        :param description: The description of this Project.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def developer(self):
        """Gets the developer of this Project.  # noqa: E501

        Description not available  # noqa: E501

        :return: The developer of this Project.  # noqa: E501
        :rtype: list[object]
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        """Sets the developer of this Project.

        Description not available  # noqa: E501

        :param developer: The developer of this Project.  # noqa: E501
        :type: list[object]
        """

        self._developer = developer

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.

        identifier  # noqa: E501

        :param id: The id of this Project.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Project.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Project.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Project.

        short description of the resource  # noqa: E501

        :param label: The label of this Project.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Project.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Project.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Project.

        type of the resource  # noqa: E501

        :param type: The type of this Project.  # noqa: E501
        :type: list[str]
        """

        self._type = type

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
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()
