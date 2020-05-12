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


class Weapon(object):
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
        'diameter': 'list[object]',
        'width': 'list[object]',
        'length': 'list[object]',
        'description': 'list[str]',
        'weight': 'list[object]',
        'used_in_war': 'list[object]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]',
        'height': 'list[object]'
    }

    attribute_map = {
        'diameter': 'diameter',
        'width': 'width',
        'length': 'length',
        'description': 'description',
        'weight': 'weight',
        'used_in_war': 'usedInWar',
        'id': 'id',
        'label': 'label',
        'type': 'type',
        'height': 'height'
    }

    def __init__(self, diameter=None, width=None, length=None, description=None, weight=None, used_in_war=None, id=None, label=None, type=None, height=None, local_vars_configuration=None):  # noqa: E501
        """Weapon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._diameter = None
        self._width = None
        self._length = None
        self._description = None
        self._weight = None
        self._used_in_war = None
        self._id = None
        self._label = None
        self._type = None
        self._height = None
        self.discriminator = None

        self.diameter = diameter
        self.width = width
        self.length = length
        self.description = description
        self.weight = weight
        self.used_in_war = used_in_war
        if id is not None:
            self.id = id
        self.label = label
        self.type = type
        self.height = height

    @property
    def diameter(self):
        """Gets the diameter of this Weapon.  # noqa: E501

        Description not available  # noqa: E501

        :return: The diameter of this Weapon.  # noqa: E501
        :rtype: list[object]
        """
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        """Sets the diameter of this Weapon.

        Description not available  # noqa: E501

        :param diameter: The diameter of this Weapon.  # noqa: E501
        :type: list[object]
        """

        self._diameter = diameter

    @property
    def width(self):
        """Gets the width of this Weapon.  # noqa: E501

        Description not available  # noqa: E501

        :return: The width of this Weapon.  # noqa: E501
        :rtype: list[object]
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Weapon.

        Description not available  # noqa: E501

        :param width: The width of this Weapon.  # noqa: E501
        :type: list[object]
        """

        self._width = width

    @property
    def length(self):
        """Gets the length of this Weapon.  # noqa: E501

        Description not available  # noqa: E501

        :return: The length of this Weapon.  # noqa: E501
        :rtype: list[object]
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Weapon.

        Description not available  # noqa: E501

        :param length: The length of this Weapon.  # noqa: E501
        :type: list[object]
        """

        self._length = length

    @property
    def description(self):
        """Gets the description of this Weapon.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Weapon.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Weapon.

        small description  # noqa: E501

        :param description: The description of this Weapon.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def weight(self):
        """Gets the weight of this Weapon.  # noqa: E501

        Description not available  # noqa: E501

        :return: The weight of this Weapon.  # noqa: E501
        :rtype: list[object]
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Weapon.

        Description not available  # noqa: E501

        :param weight: The weight of this Weapon.  # noqa: E501
        :type: list[object]
        """

        self._weight = weight

    @property
    def used_in_war(self):
        """Gets the used_in_war of this Weapon.  # noqa: E501

        wars that were typical for the usage of a weapon  # noqa: E501

        :return: The used_in_war of this Weapon.  # noqa: E501
        :rtype: list[object]
        """
        return self._used_in_war

    @used_in_war.setter
    def used_in_war(self, used_in_war):
        """Sets the used_in_war of this Weapon.

        wars that were typical for the usage of a weapon  # noqa: E501

        :param used_in_war: The used_in_war of this Weapon.  # noqa: E501
        :type: list[object]
        """

        self._used_in_war = used_in_war

    @property
    def id(self):
        """Gets the id of this Weapon.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Weapon.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Weapon.

        identifier  # noqa: E501

        :param id: The id of this Weapon.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Weapon.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Weapon.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Weapon.

        short description of the resource  # noqa: E501

        :param label: The label of this Weapon.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Weapon.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Weapon.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Weapon.

        type of the resource  # noqa: E501

        :param type: The type of this Weapon.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def height(self):
        """Gets the height of this Weapon.  # noqa: E501

        Description not available  # noqa: E501

        :return: The height of this Weapon.  # noqa: E501
        :rtype: list[object]
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Weapon.

        Description not available  # noqa: E501

        :param height: The height of this Weapon.  # noqa: E501
        :type: list[object]
        """

        self._height = height

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
        if not isinstance(other, Weapon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Weapon):
            return True

        return self.to_dict() != other.to_dict()
