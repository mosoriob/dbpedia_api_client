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


class GeneLocation(object):
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
        'gene_location_end': 'list[int]',
        'gene_location_start': 'list[int]',
        'genome_db': 'list[str]',
        'description': 'list[str]',
        'on_chromosome': 'list[int]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]'
    }

    attribute_map = {
        'gene_location_end': 'geneLocationEnd',
        'gene_location_start': 'geneLocationStart',
        'genome_db': 'genomeDB',
        'description': 'description',
        'on_chromosome': 'onChromosome',
        'id': 'id',
        'label': 'label',
        'type': 'type'
    }

    def __init__(self, gene_location_end=None, gene_location_start=None, genome_db=None, description=None, on_chromosome=None, id=None, label=None, type=None, local_vars_configuration=None):  # noqa: E501
        """GeneLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gene_location_end = None
        self._gene_location_start = None
        self._genome_db = None
        self._description = None
        self._on_chromosome = None
        self._id = None
        self._label = None
        self._type = None
        self.discriminator = None

        self.gene_location_end = gene_location_end
        self.gene_location_start = gene_location_start
        self.genome_db = genome_db
        self.description = description
        self.on_chromosome = on_chromosome
        if id is not None:
            self.id = id
        self.label = label
        self.type = type

    @property
    def gene_location_end(self):
        """Gets the gene_location_end of this GeneLocation.  # noqa: E501

        the end of the gene  # noqa: E501

        :return: The gene_location_end of this GeneLocation.  # noqa: E501
        :rtype: list[int]
        """
        return self._gene_location_end

    @gene_location_end.setter
    def gene_location_end(self, gene_location_end):
        """Sets the gene_location_end of this GeneLocation.

        the end of the gene  # noqa: E501

        :param gene_location_end: The gene_location_end of this GeneLocation.  # noqa: E501
        :type: list[int]
        """

        self._gene_location_end = gene_location_end

    @property
    def gene_location_start(self):
        """Gets the gene_location_start of this GeneLocation.  # noqa: E501

        the start of the gene coordinates  # noqa: E501

        :return: The gene_location_start of this GeneLocation.  # noqa: E501
        :rtype: list[int]
        """
        return self._gene_location_start

    @gene_location_start.setter
    def gene_location_start(self, gene_location_start):
        """Sets the gene_location_start of this GeneLocation.

        the start of the gene coordinates  # noqa: E501

        :param gene_location_start: The gene_location_start of this GeneLocation.  # noqa: E501
        :type: list[int]
        """

        self._gene_location_start = gene_location_start

    @property
    def genome_db(self):
        """Gets the genome_db of this GeneLocation.  # noqa: E501

        the edition of the database used (i.e. hg19)  # noqa: E501

        :return: The genome_db of this GeneLocation.  # noqa: E501
        :rtype: list[str]
        """
        return self._genome_db

    @genome_db.setter
    def genome_db(self, genome_db):
        """Sets the genome_db of this GeneLocation.

        the edition of the database used (i.e. hg19)  # noqa: E501

        :param genome_db: The genome_db of this GeneLocation.  # noqa: E501
        :type: list[str]
        """

        self._genome_db = genome_db

    @property
    def description(self):
        """Gets the description of this GeneLocation.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this GeneLocation.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GeneLocation.

        small description  # noqa: E501

        :param description: The description of this GeneLocation.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def on_chromosome(self):
        """Gets the on_chromosome of this GeneLocation.  # noqa: E501

        the number corresponding to the chromosome on which the gene is located  # noqa: E501

        :return: The on_chromosome of this GeneLocation.  # noqa: E501
        :rtype: list[int]
        """
        return self._on_chromosome

    @on_chromosome.setter
    def on_chromosome(self, on_chromosome):
        """Sets the on_chromosome of this GeneLocation.

        the number corresponding to the chromosome on which the gene is located  # noqa: E501

        :param on_chromosome: The on_chromosome of this GeneLocation.  # noqa: E501
        :type: list[int]
        """

        self._on_chromosome = on_chromosome

    @property
    def id(self):
        """Gets the id of this GeneLocation.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this GeneLocation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GeneLocation.

        identifier  # noqa: E501

        :param id: The id of this GeneLocation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this GeneLocation.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this GeneLocation.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this GeneLocation.

        short description of the resource  # noqa: E501

        :param label: The label of this GeneLocation.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this GeneLocation.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this GeneLocation.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GeneLocation.

        type of the resource  # noqa: E501

        :param type: The type of this GeneLocation.  # noqa: E501
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
        if not isinstance(other, GeneLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneLocation):
            return True

        return self.to_dict() != other.to_dict()
