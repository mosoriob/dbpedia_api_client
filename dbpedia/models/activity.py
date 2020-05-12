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


class Activity(object):
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
        'number_of_players': 'list[int]',
        'number_of_professionals': 'list[int]',
        'number_of_clubs': 'list[int]',
        'description': 'list[str]',
        'equipment': 'list[object]',
        'id': 'str',
        'label': 'list[str]',
        'number_of_people_licensed': 'list[int]',
        'type': 'list[str]'
    }

    attribute_map = {
        'number_of_players': 'numberOfPlayers',
        'number_of_professionals': 'numberOfProfessionals',
        'number_of_clubs': 'numberOfClubs',
        'description': 'description',
        'equipment': 'equipment',
        'id': 'id',
        'label': 'label',
        'number_of_people_licensed': 'numberOfPeopleLicensed',
        'type': 'type'
    }

    def __init__(self, number_of_players=None, number_of_professionals=None, number_of_clubs=None, description=None, equipment=None, id=None, label=None, number_of_people_licensed=None, type=None, local_vars_configuration=None):  # noqa: E501
        """Activity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._number_of_players = None
        self._number_of_professionals = None
        self._number_of_clubs = None
        self._description = None
        self._equipment = None
        self._id = None
        self._label = None
        self._number_of_people_licensed = None
        self._type = None
        self.discriminator = None

        self.number_of_players = number_of_players
        self.number_of_professionals = number_of_professionals
        self.number_of_clubs = number_of_clubs
        self.description = description
        self.equipment = equipment
        if id is not None:
            self.id = id
        self.label = label
        self.number_of_people_licensed = number_of_people_licensed
        self.type = type

    @property
    def number_of_players(self):
        """Gets the number_of_players of this Activity.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_players of this Activity.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_players

    @number_of_players.setter
    def number_of_players(self, number_of_players):
        """Sets the number_of_players of this Activity.

        Description not available  # noqa: E501

        :param number_of_players: The number_of_players of this Activity.  # noqa: E501
        :type: list[int]
        """

        self._number_of_players = number_of_players

    @property
    def number_of_professionals(self):
        """Gets the number_of_professionals of this Activity.  # noqa: E501

        number of people who earns his living from a specified activity.  # noqa: E501

        :return: The number_of_professionals of this Activity.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_professionals

    @number_of_professionals.setter
    def number_of_professionals(self, number_of_professionals):
        """Sets the number_of_professionals of this Activity.

        number of people who earns his living from a specified activity.  # noqa: E501

        :param number_of_professionals: The number_of_professionals of this Activity.  # noqa: E501
        :type: list[int]
        """

        self._number_of_professionals = number_of_professionals

    @property
    def number_of_clubs(self):
        """Gets the number_of_clubs of this Activity.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_clubs of this Activity.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_clubs

    @number_of_clubs.setter
    def number_of_clubs(self, number_of_clubs):
        """Sets the number_of_clubs of this Activity.

        Description not available  # noqa: E501

        :param number_of_clubs: The number_of_clubs of this Activity.  # noqa: E501
        :type: list[int]
        """

        self._number_of_clubs = number_of_clubs

    @property
    def description(self):
        """Gets the description of this Activity.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Activity.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Activity.

        small description  # noqa: E501

        :param description: The description of this Activity.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def equipment(self):
        """Gets the equipment of this Activity.  # noqa: E501

        Description not available  # noqa: E501

        :return: The equipment of this Activity.  # noqa: E501
        :rtype: list[object]
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this Activity.

        Description not available  # noqa: E501

        :param equipment: The equipment of this Activity.  # noqa: E501
        :type: list[object]
        """

        self._equipment = equipment

    @property
    def id(self):
        """Gets the id of this Activity.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Activity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Activity.

        identifier  # noqa: E501

        :param id: The id of this Activity.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Activity.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Activity.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Activity.

        short description of the resource  # noqa: E501

        :param label: The label of this Activity.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def number_of_people_licensed(self):
        """Gets the number_of_people_licensed of this Activity.  # noqa: E501

        nombre de personnes ayant une license pour pratiquer cette activité  # noqa: E501

        :return: The number_of_people_licensed of this Activity.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_people_licensed

    @number_of_people_licensed.setter
    def number_of_people_licensed(self, number_of_people_licensed):
        """Sets the number_of_people_licensed of this Activity.

        nombre de personnes ayant une license pour pratiquer cette activité  # noqa: E501

        :param number_of_people_licensed: The number_of_people_licensed of this Activity.  # noqa: E501
        :type: list[int]
        """

        self._number_of_people_licensed = number_of_people_licensed

    @property
    def type(self):
        """Gets the type of this Activity.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Activity.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Activity.

        type of the resource  # noqa: E501

        :param type: The type of this Activity.  # noqa: E501
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
        if not isinstance(other, Activity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Activity):
            return True

        return self.to_dict() != other.to_dict()
