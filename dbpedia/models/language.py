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


class Language(object):
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
        'iso6392_code': 'list[object]',
        'number_of_speakers': 'list[int]',
        'language_family': 'list[object]',
        'sil_code': 'list[object]',
        'description': 'list[str]',
        'spoken_in': 'list[object]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]',
        'iso6391_code': 'list[object]',
        'language_code': 'list[object]',
        'iso6393_code': 'list[object]'
    }

    attribute_map = {
        'iso6392_code': 'iso6392Code',
        'number_of_speakers': 'numberOfSpeakers',
        'language_family': 'languageFamily',
        'sil_code': 'silCode',
        'description': 'description',
        'spoken_in': 'spokenIn',
        'id': 'id',
        'label': 'label',
        'type': 'type',
        'iso6391_code': 'iso6391Code',
        'language_code': 'languageCode',
        'iso6393_code': 'iso6393Code'
    }

    def __init__(self, iso6392_code=None, number_of_speakers=None, language_family=None, sil_code=None, description=None, spoken_in=None, id=None, label=None, type=None, iso6391_code=None, language_code=None, iso6393_code=None, local_vars_configuration=None):  # noqa: E501
        """Language - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._iso6392_code = None
        self._number_of_speakers = None
        self._language_family = None
        self._sil_code = None
        self._description = None
        self._spoken_in = None
        self._id = None
        self._label = None
        self._type = None
        self._iso6391_code = None
        self._language_code = None
        self._iso6393_code = None
        self.discriminator = None

        self.iso6392_code = iso6392_code
        self.number_of_speakers = number_of_speakers
        self.language_family = language_family
        self.sil_code = sil_code
        self.description = description
        self.spoken_in = spoken_in
        if id is not None:
            self.id = id
        self.label = label
        self.type = type
        self.iso6391_code = iso6391_code
        self.language_code = language_code
        self.iso6393_code = iso6393_code

    @property
    def iso6392_code(self):
        """Gets the iso6392_code of this Language.  # noqa: E501

        Description not available  # noqa: E501

        :return: The iso6392_code of this Language.  # noqa: E501
        :rtype: list[object]
        """
        return self._iso6392_code

    @iso6392_code.setter
    def iso6392_code(self, iso6392_code):
        """Sets the iso6392_code of this Language.

        Description not available  # noqa: E501

        :param iso6392_code: The iso6392_code of this Language.  # noqa: E501
        :type: list[object]
        """

        self._iso6392_code = iso6392_code

    @property
    def number_of_speakers(self):
        """Gets the number_of_speakers of this Language.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_speakers of this Language.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_speakers

    @number_of_speakers.setter
    def number_of_speakers(self, number_of_speakers):
        """Sets the number_of_speakers of this Language.

        Description not available  # noqa: E501

        :param number_of_speakers: The number_of_speakers of this Language.  # noqa: E501
        :type: list[int]
        """

        self._number_of_speakers = number_of_speakers

    @property
    def language_family(self):
        """Gets the language_family of this Language.  # noqa: E501

        Description not available  # noqa: E501

        :return: The language_family of this Language.  # noqa: E501
        :rtype: list[object]
        """
        return self._language_family

    @language_family.setter
    def language_family(self, language_family):
        """Sets the language_family of this Language.

        Description not available  # noqa: E501

        :param language_family: The language_family of this Language.  # noqa: E501
        :type: list[object]
        """

        self._language_family = language_family

    @property
    def sil_code(self):
        """Gets the sil_code of this Language.  # noqa: E501

        Description not available  # noqa: E501

        :return: The sil_code of this Language.  # noqa: E501
        :rtype: list[object]
        """
        return self._sil_code

    @sil_code.setter
    def sil_code(self, sil_code):
        """Sets the sil_code of this Language.

        Description not available  # noqa: E501

        :param sil_code: The sil_code of this Language.  # noqa: E501
        :type: list[object]
        """

        self._sil_code = sil_code

    @property
    def description(self):
        """Gets the description of this Language.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Language.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Language.

        small description  # noqa: E501

        :param description: The description of this Language.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def spoken_in(self):
        """Gets the spoken_in of this Language.  # noqa: E501

        Description not available  # noqa: E501

        :return: The spoken_in of this Language.  # noqa: E501
        :rtype: list[object]
        """
        return self._spoken_in

    @spoken_in.setter
    def spoken_in(self, spoken_in):
        """Sets the spoken_in of this Language.

        Description not available  # noqa: E501

        :param spoken_in: The spoken_in of this Language.  # noqa: E501
        :type: list[object]
        """

        self._spoken_in = spoken_in

    @property
    def id(self):
        """Gets the id of this Language.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Language.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Language.

        identifier  # noqa: E501

        :param id: The id of this Language.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Language.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Language.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Language.

        short description of the resource  # noqa: E501

        :param label: The label of this Language.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Language.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Language.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Language.

        type of the resource  # noqa: E501

        :param type: The type of this Language.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def iso6391_code(self):
        """Gets the iso6391_code of this Language.  # noqa: E501

        Description not available  # noqa: E501

        :return: The iso6391_code of this Language.  # noqa: E501
        :rtype: list[object]
        """
        return self._iso6391_code

    @iso6391_code.setter
    def iso6391_code(self, iso6391_code):
        """Sets the iso6391_code of this Language.

        Description not available  # noqa: E501

        :param iso6391_code: The iso6391_code of this Language.  # noqa: E501
        :type: list[object]
        """

        self._iso6391_code = iso6391_code

    @property
    def language_code(self):
        """Gets the language_code of this Language.  # noqa: E501

        Description not available  # noqa: E501

        :return: The language_code of this Language.  # noqa: E501
        :rtype: list[object]
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this Language.

        Description not available  # noqa: E501

        :param language_code: The language_code of this Language.  # noqa: E501
        :type: list[object]
        """

        self._language_code = language_code

    @property
    def iso6393_code(self):
        """Gets the iso6393_code of this Language.  # noqa: E501

        Description not available  # noqa: E501

        :return: The iso6393_code of this Language.  # noqa: E501
        :rtype: list[object]
        """
        return self._iso6393_code

    @iso6393_code.setter
    def iso6393_code(self, iso6393_code):
        """Sets the iso6393_code of this Language.

        Description not available  # noqa: E501

        :param iso6393_code: The iso6393_code of this Language.  # noqa: E501
        :type: list[object]
        """

        self._iso6393_code = iso6393_code

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
        if not isinstance(other, Language):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Language):
            return True

        return self.to_dict() != other.to_dict()
