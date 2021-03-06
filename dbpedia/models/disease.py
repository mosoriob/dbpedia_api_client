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


class Disease(object):
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
        'genereviewsname': 'list[str]',
        'medlineplus': 'list[str]',
        'description': 'list[str]',
        'label': 'list[str]',
        'type': 'list[str]',
        'mesh_id': 'list[str]',
        'genereviewsid': 'list[str]',
        'emedicine_topic': 'list[str]',
        'icdo': 'list[str]',
        'emedicine_subject': 'list[str]',
        'id': 'str',
        'diseasesdb': 'list[str]',
        'icd9': 'list[str]',
        'icd10': 'list[str]'
    }

    attribute_map = {
        'genereviewsname': 'genereviewsname',
        'medlineplus': 'medlineplus',
        'description': 'description',
        'label': 'label',
        'type': 'type',
        'mesh_id': 'meshId',
        'genereviewsid': 'genereviewsid',
        'emedicine_topic': 'emedicineTopic',
        'icdo': 'icdo',
        'emedicine_subject': 'emedicineSubject',
        'id': 'id',
        'diseasesdb': 'diseasesdb',
        'icd9': 'icd9',
        'icd10': 'icd10'
    }

    def __init__(self, genereviewsname=None, medlineplus=None, description=None, label=None, type=None, mesh_id=None, genereviewsid=None, emedicine_topic=None, icdo=None, emedicine_subject=None, id=None, diseasesdb=None, icd9=None, icd10=None, local_vars_configuration=None):  # noqa: E501
        """Disease - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._genereviewsname = None
        self._medlineplus = None
        self._description = None
        self._label = None
        self._type = None
        self._mesh_id = None
        self._genereviewsid = None
        self._emedicine_topic = None
        self._icdo = None
        self._emedicine_subject = None
        self._id = None
        self._diseasesdb = None
        self._icd9 = None
        self._icd10 = None
        self.discriminator = None

        self.genereviewsname = genereviewsname
        self.medlineplus = medlineplus
        self.description = description
        self.label = label
        self.type = type
        self.mesh_id = mesh_id
        self.genereviewsid = genereviewsid
        self.emedicine_topic = emedicine_topic
        self.icdo = icdo
        self.emedicine_subject = emedicine_subject
        if id is not None:
            self.id = id
        self.diseasesdb = diseasesdb
        self.icd9 = icd9
        self.icd10 = icd10

    @property
    def genereviewsname(self):
        """Gets the genereviewsname of this Disease.  # noqa: E501

        Description not available  # noqa: E501

        :return: The genereviewsname of this Disease.  # noqa: E501
        :rtype: list[str]
        """
        return self._genereviewsname

    @genereviewsname.setter
    def genereviewsname(self, genereviewsname):
        """Sets the genereviewsname of this Disease.

        Description not available  # noqa: E501

        :param genereviewsname: The genereviewsname of this Disease.  # noqa: E501
        :type: list[str]
        """

        self._genereviewsname = genereviewsname

    @property
    def medlineplus(self):
        """Gets the medlineplus of this Disease.  # noqa: E501

        Description not available  # noqa: E501

        :return: The medlineplus of this Disease.  # noqa: E501
        :rtype: list[str]
        """
        return self._medlineplus

    @medlineplus.setter
    def medlineplus(self, medlineplus):
        """Sets the medlineplus of this Disease.

        Description not available  # noqa: E501

        :param medlineplus: The medlineplus of this Disease.  # noqa: E501
        :type: list[str]
        """

        self._medlineplus = medlineplus

    @property
    def description(self):
        """Gets the description of this Disease.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Disease.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Disease.

        small description  # noqa: E501

        :param description: The description of this Disease.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def label(self):
        """Gets the label of this Disease.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Disease.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Disease.

        short description of the resource  # noqa: E501

        :param label: The label of this Disease.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Disease.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Disease.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Disease.

        type of the resource  # noqa: E501

        :param type: The type of this Disease.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def mesh_id(self):
        """Gets the mesh_id of this Disease.  # noqa: E501

        Description not available  # noqa: E501

        :return: The mesh_id of this Disease.  # noqa: E501
        :rtype: list[str]
        """
        return self._mesh_id

    @mesh_id.setter
    def mesh_id(self, mesh_id):
        """Sets the mesh_id of this Disease.

        Description not available  # noqa: E501

        :param mesh_id: The mesh_id of this Disease.  # noqa: E501
        :type: list[str]
        """

        self._mesh_id = mesh_id

    @property
    def genereviewsid(self):
        """Gets the genereviewsid of this Disease.  # noqa: E501

        Description not available  # noqa: E501

        :return: The genereviewsid of this Disease.  # noqa: E501
        :rtype: list[str]
        """
        return self._genereviewsid

    @genereviewsid.setter
    def genereviewsid(self, genereviewsid):
        """Sets the genereviewsid of this Disease.

        Description not available  # noqa: E501

        :param genereviewsid: The genereviewsid of this Disease.  # noqa: E501
        :type: list[str]
        """

        self._genereviewsid = genereviewsid

    @property
    def emedicine_topic(self):
        """Gets the emedicine_topic of this Disease.  # noqa: E501

        Description not available  # noqa: E501

        :return: The emedicine_topic of this Disease.  # noqa: E501
        :rtype: list[str]
        """
        return self._emedicine_topic

    @emedicine_topic.setter
    def emedicine_topic(self, emedicine_topic):
        """Sets the emedicine_topic of this Disease.

        Description not available  # noqa: E501

        :param emedicine_topic: The emedicine_topic of this Disease.  # noqa: E501
        :type: list[str]
        """

        self._emedicine_topic = emedicine_topic

    @property
    def icdo(self):
        """Gets the icdo of this Disease.  # noqa: E501

        Description not available  # noqa: E501

        :return: The icdo of this Disease.  # noqa: E501
        :rtype: list[str]
        """
        return self._icdo

    @icdo.setter
    def icdo(self, icdo):
        """Sets the icdo of this Disease.

        Description not available  # noqa: E501

        :param icdo: The icdo of this Disease.  # noqa: E501
        :type: list[str]
        """

        self._icdo = icdo

    @property
    def emedicine_subject(self):
        """Gets the emedicine_subject of this Disease.  # noqa: E501

        Description not available  # noqa: E501

        :return: The emedicine_subject of this Disease.  # noqa: E501
        :rtype: list[str]
        """
        return self._emedicine_subject

    @emedicine_subject.setter
    def emedicine_subject(self, emedicine_subject):
        """Sets the emedicine_subject of this Disease.

        Description not available  # noqa: E501

        :param emedicine_subject: The emedicine_subject of this Disease.  # noqa: E501
        :type: list[str]
        """

        self._emedicine_subject = emedicine_subject

    @property
    def id(self):
        """Gets the id of this Disease.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Disease.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Disease.

        identifier  # noqa: E501

        :param id: The id of this Disease.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def diseasesdb(self):
        """Gets the diseasesdb of this Disease.  # noqa: E501

        Description not available  # noqa: E501

        :return: The diseasesdb of this Disease.  # noqa: E501
        :rtype: list[str]
        """
        return self._diseasesdb

    @diseasesdb.setter
    def diseasesdb(self, diseasesdb):
        """Sets the diseasesdb of this Disease.

        Description not available  # noqa: E501

        :param diseasesdb: The diseasesdb of this Disease.  # noqa: E501
        :type: list[str]
        """

        self._diseasesdb = diseasesdb

    @property
    def icd9(self):
        """Gets the icd9 of this Disease.  # noqa: E501

        Description not available  # noqa: E501

        :return: The icd9 of this Disease.  # noqa: E501
        :rtype: list[str]
        """
        return self._icd9

    @icd9.setter
    def icd9(self, icd9):
        """Sets the icd9 of this Disease.

        Description not available  # noqa: E501

        :param icd9: The icd9 of this Disease.  # noqa: E501
        :type: list[str]
        """

        self._icd9 = icd9

    @property
    def icd10(self):
        """Gets the icd10 of this Disease.  # noqa: E501

        Description not available  # noqa: E501

        :return: The icd10 of this Disease.  # noqa: E501
        :rtype: list[str]
        """
        return self._icd10

    @icd10.setter
    def icd10(self, icd10):
        """Sets the icd10 of this Disease.

        Description not available  # noqa: E501

        :param icd10: The icd10 of this Disease.  # noqa: E501
        :type: list[str]
        """

        self._icd10 = icd10

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
        if not isinstance(other, Disease):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Disease):
            return True

        return self.to_dict() != other.to_dict()
