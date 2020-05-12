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


class MusicGenre(object):
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
        'music_fusion_genre': 'list[object]',
        'music_subgenre': 'list[object]',
        'description': 'list[str]',
        'derivative': 'list[object]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]',
        'stylistic_origin': 'list[object]'
    }

    attribute_map = {
        'music_fusion_genre': 'musicFusionGenre',
        'music_subgenre': 'musicSubgenre',
        'description': 'description',
        'derivative': 'derivative',
        'id': 'id',
        'label': 'label',
        'type': 'type',
        'stylistic_origin': 'stylisticOrigin'
    }

    def __init__(self, music_fusion_genre=None, music_subgenre=None, description=None, derivative=None, id=None, label=None, type=None, stylistic_origin=None, local_vars_configuration=None):  # noqa: E501
        """MusicGenre - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._music_fusion_genre = None
        self._music_subgenre = None
        self._description = None
        self._derivative = None
        self._id = None
        self._label = None
        self._type = None
        self._stylistic_origin = None
        self.discriminator = None

        self.music_fusion_genre = music_fusion_genre
        self.music_subgenre = music_subgenre
        self.description = description
        self.derivative = derivative
        if id is not None:
            self.id = id
        self.label = label
        self.type = type
        self.stylistic_origin = stylistic_origin

    @property
    def music_fusion_genre(self):
        """Gets the music_fusion_genre of this MusicGenre.  # noqa: E501

        Description not available  # noqa: E501

        :return: The music_fusion_genre of this MusicGenre.  # noqa: E501
        :rtype: list[object]
        """
        return self._music_fusion_genre

    @music_fusion_genre.setter
    def music_fusion_genre(self, music_fusion_genre):
        """Sets the music_fusion_genre of this MusicGenre.

        Description not available  # noqa: E501

        :param music_fusion_genre: The music_fusion_genre of this MusicGenre.  # noqa: E501
        :type: list[object]
        """

        self._music_fusion_genre = music_fusion_genre

    @property
    def music_subgenre(self):
        """Gets the music_subgenre of this MusicGenre.  # noqa: E501

        Description not available  # noqa: E501

        :return: The music_subgenre of this MusicGenre.  # noqa: E501
        :rtype: list[object]
        """
        return self._music_subgenre

    @music_subgenre.setter
    def music_subgenre(self, music_subgenre):
        """Sets the music_subgenre of this MusicGenre.

        Description not available  # noqa: E501

        :param music_subgenre: The music_subgenre of this MusicGenre.  # noqa: E501
        :type: list[object]
        """

        self._music_subgenre = music_subgenre

    @property
    def description(self):
        """Gets the description of this MusicGenre.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this MusicGenre.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MusicGenre.

        small description  # noqa: E501

        :param description: The description of this MusicGenre.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def derivative(self):
        """Gets the derivative of this MusicGenre.  # noqa: E501

        Description not available  # noqa: E501

        :return: The derivative of this MusicGenre.  # noqa: E501
        :rtype: list[object]
        """
        return self._derivative

    @derivative.setter
    def derivative(self, derivative):
        """Sets the derivative of this MusicGenre.

        Description not available  # noqa: E501

        :param derivative: The derivative of this MusicGenre.  # noqa: E501
        :type: list[object]
        """

        self._derivative = derivative

    @property
    def id(self):
        """Gets the id of this MusicGenre.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this MusicGenre.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MusicGenre.

        identifier  # noqa: E501

        :param id: The id of this MusicGenre.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this MusicGenre.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this MusicGenre.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this MusicGenre.

        short description of the resource  # noqa: E501

        :param label: The label of this MusicGenre.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this MusicGenre.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this MusicGenre.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MusicGenre.

        type of the resource  # noqa: E501

        :param type: The type of this MusicGenre.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def stylistic_origin(self):
        """Gets the stylistic_origin of this MusicGenre.  # noqa: E501

        Description not available  # noqa: E501

        :return: The stylistic_origin of this MusicGenre.  # noqa: E501
        :rtype: list[object]
        """
        return self._stylistic_origin

    @stylistic_origin.setter
    def stylistic_origin(self, stylistic_origin):
        """Sets the stylistic_origin of this MusicGenre.

        Description not available  # noqa: E501

        :param stylistic_origin: The stylistic_origin of this MusicGenre.  # noqa: E501
        :type: list[object]
        """

        self._stylistic_origin = stylistic_origin

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
        if not isinstance(other, MusicGenre):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MusicGenre):
            return True

        return self.to_dict() != other.to_dict()