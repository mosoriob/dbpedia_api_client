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


class Drug(object):
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
        'iupac_name': 'list[str]',
        'ch_ebi': 'list[str]',
        'bioavailability': 'list[float]',
        'description': 'list[str]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]',
        'melting_point': 'list[object]',
        'boiling_point': 'list[object]'
    }

    attribute_map = {
        'iupac_name': 'iupacName',
        'ch_ebi': 'chEBI',
        'bioavailability': 'bioavailability',
        'description': 'description',
        'id': 'id',
        'label': 'label',
        'type': 'type',
        'melting_point': 'meltingPoint',
        'boiling_point': 'boilingPoint'
    }

    def __init__(self, iupac_name=None, ch_ebi=None, bioavailability=None, description=None, id=None, label=None, type=None, melting_point=None, boiling_point=None, local_vars_configuration=None):  # noqa: E501
        """Drug - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._iupac_name = None
        self._ch_ebi = None
        self._bioavailability = None
        self._description = None
        self._id = None
        self._label = None
        self._type = None
        self._melting_point = None
        self._boiling_point = None
        self.discriminator = None

        self.iupac_name = iupac_name
        self.ch_ebi = ch_ebi
        self.bioavailability = bioavailability
        self.description = description
        if id is not None:
            self.id = id
        self.label = label
        self.type = type
        self.melting_point = melting_point
        self.boiling_point = boiling_point

    @property
    def iupac_name(self):
        """Gets the iupac_name of this Drug.  # noqa: E501

        Description not available  # noqa: E501

        :return: The iupac_name of this Drug.  # noqa: E501
        :rtype: list[str]
        """
        return self._iupac_name

    @iupac_name.setter
    def iupac_name(self, iupac_name):
        """Sets the iupac_name of this Drug.

        Description not available  # noqa: E501

        :param iupac_name: The iupac_name of this Drug.  # noqa: E501
        :type: list[str]
        """

        self._iupac_name = iupac_name

    @property
    def ch_ebi(self):
        """Gets the ch_ebi of this Drug.  # noqa: E501

        A unique identifier for the drug in the Chemical Entities of Biological Interest (ChEBI) ontology  # noqa: E501

        :return: The ch_ebi of this Drug.  # noqa: E501
        :rtype: list[str]
        """
        return self._ch_ebi

    @ch_ebi.setter
    def ch_ebi(self, ch_ebi):
        """Sets the ch_ebi of this Drug.

        A unique identifier for the drug in the Chemical Entities of Biological Interest (ChEBI) ontology  # noqa: E501

        :param ch_ebi: The ch_ebi of this Drug.  # noqa: E501
        :type: list[str]
        """

        self._ch_ebi = ch_ebi

    @property
    def bioavailability(self):
        """Gets the bioavailability of this Drug.  # noqa: E501

        \"The rate and extent to which the active ingredient or active moiety is absorbed from a drug product and becomes available at the site of action. For drug products that are not intended to be absorbed into the bloodstream, bioavailability may be assessed by measurements intended to reflect the rate and extent to which the active ingredient or active moiety becomes available at the site of action (21CFR320.1).\"  # noqa: E501

        :return: The bioavailability of this Drug.  # noqa: E501
        :rtype: list[float]
        """
        return self._bioavailability

    @bioavailability.setter
    def bioavailability(self, bioavailability):
        """Sets the bioavailability of this Drug.

        \"The rate and extent to which the active ingredient or active moiety is absorbed from a drug product and becomes available at the site of action. For drug products that are not intended to be absorbed into the bloodstream, bioavailability may be assessed by measurements intended to reflect the rate and extent to which the active ingredient or active moiety becomes available at the site of action (21CFR320.1).\"  # noqa: E501

        :param bioavailability: The bioavailability of this Drug.  # noqa: E501
        :type: list[float]
        """

        self._bioavailability = bioavailability

    @property
    def description(self):
        """Gets the description of this Drug.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Drug.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Drug.

        small description  # noqa: E501

        :param description: The description of this Drug.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Drug.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Drug.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Drug.

        identifier  # noqa: E501

        :param id: The id of this Drug.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Drug.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Drug.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Drug.

        short description of the resource  # noqa: E501

        :param label: The label of this Drug.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Drug.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Drug.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Drug.

        type of the resource  # noqa: E501

        :param type: The type of this Drug.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def melting_point(self):
        """Gets the melting_point of this Drug.  # noqa: E501

        Description not available  # noqa: E501

        :return: The melting_point of this Drug.  # noqa: E501
        :rtype: list[object]
        """
        return self._melting_point

    @melting_point.setter
    def melting_point(self, melting_point):
        """Sets the melting_point of this Drug.

        Description not available  # noqa: E501

        :param melting_point: The melting_point of this Drug.  # noqa: E501
        :type: list[object]
        """

        self._melting_point = melting_point

    @property
    def boiling_point(self):
        """Gets the boiling_point of this Drug.  # noqa: E501

        Description not available  # noqa: E501

        :return: The boiling_point of this Drug.  # noqa: E501
        :rtype: list[object]
        """
        return self._boiling_point

    @boiling_point.setter
    def boiling_point(self, boiling_point):
        """Sets the boiling_point of this Drug.

        Description not available  # noqa: E501

        :param boiling_point: The boiling_point of this Drug.  # noqa: E501
        :type: list[object]
        """

        self._boiling_point = boiling_point

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
        if not isinstance(other, Drug):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Drug):
            return True

        return self.to_dict() != other.to_dict()
