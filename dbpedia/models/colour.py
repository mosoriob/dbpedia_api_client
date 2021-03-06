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


class Colour(object):
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
        'hsv_coordinate_saturation': 'list[int]',
        'wavelength': 'list[float]',
        'rgb_coordinate_red': 'list[int]',
        'description': 'list[str]',
        'label': 'list[str]',
        'hsv_coordinate_hue': 'list[int]',
        'type': 'list[str]',
        'rgb_coordinate_blue': 'list[int]',
        'cmyk_coordinate_cyanic': 'list[int]',
        'hsv_coordinate_value': 'list[int]',
        'id': 'str',
        'cmyk_coordinate_black': 'list[int]',
        'cmyk_coordinate_yellow': 'list[int]',
        'cmyk_coordinate_magenta': 'list[int]',
        'rgb_coordinate_green': 'list[int]'
    }

    attribute_map = {
        'hsv_coordinate_saturation': 'hsvCoordinateSaturation',
        'wavelength': 'wavelength',
        'rgb_coordinate_red': 'rgbCoordinateRed',
        'description': 'description',
        'label': 'label',
        'hsv_coordinate_hue': 'hsvCoordinateHue',
        'type': 'type',
        'rgb_coordinate_blue': 'rgbCoordinateBlue',
        'cmyk_coordinate_cyanic': 'cmykCoordinateCyanic',
        'hsv_coordinate_value': 'hsvCoordinateValue',
        'id': 'id',
        'cmyk_coordinate_black': 'cmykCoordinateBlack',
        'cmyk_coordinate_yellow': 'cmykCoordinateYellow',
        'cmyk_coordinate_magenta': 'cmykCoordinateMagenta',
        'rgb_coordinate_green': 'rgbCoordinateGreen'
    }

    def __init__(self, hsv_coordinate_saturation=None, wavelength=None, rgb_coordinate_red=None, description=None, label=None, hsv_coordinate_hue=None, type=None, rgb_coordinate_blue=None, cmyk_coordinate_cyanic=None, hsv_coordinate_value=None, id=None, cmyk_coordinate_black=None, cmyk_coordinate_yellow=None, cmyk_coordinate_magenta=None, rgb_coordinate_green=None, local_vars_configuration=None):  # noqa: E501
        """Colour - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hsv_coordinate_saturation = None
        self._wavelength = None
        self._rgb_coordinate_red = None
        self._description = None
        self._label = None
        self._hsv_coordinate_hue = None
        self._type = None
        self._rgb_coordinate_blue = None
        self._cmyk_coordinate_cyanic = None
        self._hsv_coordinate_value = None
        self._id = None
        self._cmyk_coordinate_black = None
        self._cmyk_coordinate_yellow = None
        self._cmyk_coordinate_magenta = None
        self._rgb_coordinate_green = None
        self.discriminator = None

        self.hsv_coordinate_saturation = hsv_coordinate_saturation
        self.wavelength = wavelength
        self.rgb_coordinate_red = rgb_coordinate_red
        self.description = description
        self.label = label
        self.hsv_coordinate_hue = hsv_coordinate_hue
        self.type = type
        self.rgb_coordinate_blue = rgb_coordinate_blue
        self.cmyk_coordinate_cyanic = cmyk_coordinate_cyanic
        self.hsv_coordinate_value = hsv_coordinate_value
        if id is not None:
            self.id = id
        self.cmyk_coordinate_black = cmyk_coordinate_black
        self.cmyk_coordinate_yellow = cmyk_coordinate_yellow
        self.cmyk_coordinate_magenta = cmyk_coordinate_magenta
        self.rgb_coordinate_green = rgb_coordinate_green

    @property
    def hsv_coordinate_saturation(self):
        """Gets the hsv_coordinate_saturation of this Colour.  # noqa: E501

        Description not available  # noqa: E501

        :return: The hsv_coordinate_saturation of this Colour.  # noqa: E501
        :rtype: list[int]
        """
        return self._hsv_coordinate_saturation

    @hsv_coordinate_saturation.setter
    def hsv_coordinate_saturation(self, hsv_coordinate_saturation):
        """Sets the hsv_coordinate_saturation of this Colour.

        Description not available  # noqa: E501

        :param hsv_coordinate_saturation: The hsv_coordinate_saturation of this Colour.  # noqa: E501
        :type: list[int]
        """

        self._hsv_coordinate_saturation = hsv_coordinate_saturation

    @property
    def wavelength(self):
        """Gets the wavelength of this Colour.  # noqa: E501

        Description not available  # noqa: E501

        :return: The wavelength of this Colour.  # noqa: E501
        :rtype: list[float]
        """
        return self._wavelength

    @wavelength.setter
    def wavelength(self, wavelength):
        """Sets the wavelength of this Colour.

        Description not available  # noqa: E501

        :param wavelength: The wavelength of this Colour.  # noqa: E501
        :type: list[float]
        """

        self._wavelength = wavelength

    @property
    def rgb_coordinate_red(self):
        """Gets the rgb_coordinate_red of this Colour.  # noqa: E501

        Description not available  # noqa: E501

        :return: The rgb_coordinate_red of this Colour.  # noqa: E501
        :rtype: list[int]
        """
        return self._rgb_coordinate_red

    @rgb_coordinate_red.setter
    def rgb_coordinate_red(self, rgb_coordinate_red):
        """Sets the rgb_coordinate_red of this Colour.

        Description not available  # noqa: E501

        :param rgb_coordinate_red: The rgb_coordinate_red of this Colour.  # noqa: E501
        :type: list[int]
        """

        self._rgb_coordinate_red = rgb_coordinate_red

    @property
    def description(self):
        """Gets the description of this Colour.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Colour.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Colour.

        small description  # noqa: E501

        :param description: The description of this Colour.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def label(self):
        """Gets the label of this Colour.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Colour.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Colour.

        short description of the resource  # noqa: E501

        :param label: The label of this Colour.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def hsv_coordinate_hue(self):
        """Gets the hsv_coordinate_hue of this Colour.  # noqa: E501

        Description not available  # noqa: E501

        :return: The hsv_coordinate_hue of this Colour.  # noqa: E501
        :rtype: list[int]
        """
        return self._hsv_coordinate_hue

    @hsv_coordinate_hue.setter
    def hsv_coordinate_hue(self, hsv_coordinate_hue):
        """Sets the hsv_coordinate_hue of this Colour.

        Description not available  # noqa: E501

        :param hsv_coordinate_hue: The hsv_coordinate_hue of this Colour.  # noqa: E501
        :type: list[int]
        """

        self._hsv_coordinate_hue = hsv_coordinate_hue

    @property
    def type(self):
        """Gets the type of this Colour.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Colour.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Colour.

        type of the resource  # noqa: E501

        :param type: The type of this Colour.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def rgb_coordinate_blue(self):
        """Gets the rgb_coordinate_blue of this Colour.  # noqa: E501

        Description not available  # noqa: E501

        :return: The rgb_coordinate_blue of this Colour.  # noqa: E501
        :rtype: list[int]
        """
        return self._rgb_coordinate_blue

    @rgb_coordinate_blue.setter
    def rgb_coordinate_blue(self, rgb_coordinate_blue):
        """Sets the rgb_coordinate_blue of this Colour.

        Description not available  # noqa: E501

        :param rgb_coordinate_blue: The rgb_coordinate_blue of this Colour.  # noqa: E501
        :type: list[int]
        """

        self._rgb_coordinate_blue = rgb_coordinate_blue

    @property
    def cmyk_coordinate_cyanic(self):
        """Gets the cmyk_coordinate_cyanic of this Colour.  # noqa: E501

        Description not available  # noqa: E501

        :return: The cmyk_coordinate_cyanic of this Colour.  # noqa: E501
        :rtype: list[int]
        """
        return self._cmyk_coordinate_cyanic

    @cmyk_coordinate_cyanic.setter
    def cmyk_coordinate_cyanic(self, cmyk_coordinate_cyanic):
        """Sets the cmyk_coordinate_cyanic of this Colour.

        Description not available  # noqa: E501

        :param cmyk_coordinate_cyanic: The cmyk_coordinate_cyanic of this Colour.  # noqa: E501
        :type: list[int]
        """

        self._cmyk_coordinate_cyanic = cmyk_coordinate_cyanic

    @property
    def hsv_coordinate_value(self):
        """Gets the hsv_coordinate_value of this Colour.  # noqa: E501

        Description not available  # noqa: E501

        :return: The hsv_coordinate_value of this Colour.  # noqa: E501
        :rtype: list[int]
        """
        return self._hsv_coordinate_value

    @hsv_coordinate_value.setter
    def hsv_coordinate_value(self, hsv_coordinate_value):
        """Sets the hsv_coordinate_value of this Colour.

        Description not available  # noqa: E501

        :param hsv_coordinate_value: The hsv_coordinate_value of this Colour.  # noqa: E501
        :type: list[int]
        """

        self._hsv_coordinate_value = hsv_coordinate_value

    @property
    def id(self):
        """Gets the id of this Colour.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Colour.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Colour.

        identifier  # noqa: E501

        :param id: The id of this Colour.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def cmyk_coordinate_black(self):
        """Gets the cmyk_coordinate_black of this Colour.  # noqa: E501

        Description not available  # noqa: E501

        :return: The cmyk_coordinate_black of this Colour.  # noqa: E501
        :rtype: list[int]
        """
        return self._cmyk_coordinate_black

    @cmyk_coordinate_black.setter
    def cmyk_coordinate_black(self, cmyk_coordinate_black):
        """Sets the cmyk_coordinate_black of this Colour.

        Description not available  # noqa: E501

        :param cmyk_coordinate_black: The cmyk_coordinate_black of this Colour.  # noqa: E501
        :type: list[int]
        """

        self._cmyk_coordinate_black = cmyk_coordinate_black

    @property
    def cmyk_coordinate_yellow(self):
        """Gets the cmyk_coordinate_yellow of this Colour.  # noqa: E501

        Description not available  # noqa: E501

        :return: The cmyk_coordinate_yellow of this Colour.  # noqa: E501
        :rtype: list[int]
        """
        return self._cmyk_coordinate_yellow

    @cmyk_coordinate_yellow.setter
    def cmyk_coordinate_yellow(self, cmyk_coordinate_yellow):
        """Sets the cmyk_coordinate_yellow of this Colour.

        Description not available  # noqa: E501

        :param cmyk_coordinate_yellow: The cmyk_coordinate_yellow of this Colour.  # noqa: E501
        :type: list[int]
        """

        self._cmyk_coordinate_yellow = cmyk_coordinate_yellow

    @property
    def cmyk_coordinate_magenta(self):
        """Gets the cmyk_coordinate_magenta of this Colour.  # noqa: E501

        Description not available  # noqa: E501

        :return: The cmyk_coordinate_magenta of this Colour.  # noqa: E501
        :rtype: list[int]
        """
        return self._cmyk_coordinate_magenta

    @cmyk_coordinate_magenta.setter
    def cmyk_coordinate_magenta(self, cmyk_coordinate_magenta):
        """Sets the cmyk_coordinate_magenta of this Colour.

        Description not available  # noqa: E501

        :param cmyk_coordinate_magenta: The cmyk_coordinate_magenta of this Colour.  # noqa: E501
        :type: list[int]
        """

        self._cmyk_coordinate_magenta = cmyk_coordinate_magenta

    @property
    def rgb_coordinate_green(self):
        """Gets the rgb_coordinate_green of this Colour.  # noqa: E501

        Description not available  # noqa: E501

        :return: The rgb_coordinate_green of this Colour.  # noqa: E501
        :rtype: list[int]
        """
        return self._rgb_coordinate_green

    @rgb_coordinate_green.setter
    def rgb_coordinate_green(self, rgb_coordinate_green):
        """Sets the rgb_coordinate_green of this Colour.

        Description not available  # noqa: E501

        :param rgb_coordinate_green: The rgb_coordinate_green of this Colour.  # noqa: E501
        :type: list[int]
        """

        self._rgb_coordinate_green = rgb_coordinate_green

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
        if not isinstance(other, Colour):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Colour):
            return True

        return self.to_dict() != other.to_dict()
