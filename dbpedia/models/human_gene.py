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


class HumanGene(object):
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
        'entrezgene': 'list[str]',
        'symbol': 'list[str]',
        'gene_location': 'list[object]',
        'description': 'list[str]',
        'label': 'list[str]',
        'type': 'list[str]',
        'ensembl': 'list[str]',
        'refseqprotein': 'list[str]',
        'omim': 'list[int]',
        'refseqmrna': 'list[str]',
        'hgncid': 'list[str]',
        'mgiid': 'list[str]',
        'ec_number': 'list[str]',
        'orthologous_gene': 'list[object]',
        'id': 'str',
        'uniprot': 'list[str]'
    }

    attribute_map = {
        'entrezgene': 'entrezgene',
        'symbol': 'symbol',
        'gene_location': 'geneLocation',
        'description': 'description',
        'label': 'label',
        'type': 'type',
        'ensembl': 'ensembl',
        'refseqprotein': 'refseqprotein',
        'omim': 'omim',
        'refseqmrna': 'refseqmrna',
        'hgncid': 'hgncid',
        'mgiid': 'mgiid',
        'ec_number': 'ecNumber',
        'orthologous_gene': 'orthologousGene',
        'id': 'id',
        'uniprot': 'uniprot'
    }

    def __init__(self, entrezgene=None, symbol=None, gene_location=None, description=None, label=None, type=None, ensembl=None, refseqprotein=None, omim=None, refseqmrna=None, hgncid=None, mgiid=None, ec_number=None, orthologous_gene=None, id=None, uniprot=None, local_vars_configuration=None):  # noqa: E501
        """HumanGene - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._entrezgene = None
        self._symbol = None
        self._gene_location = None
        self._description = None
        self._label = None
        self._type = None
        self._ensembl = None
        self._refseqprotein = None
        self._omim = None
        self._refseqmrna = None
        self._hgncid = None
        self._mgiid = None
        self._ec_number = None
        self._orthologous_gene = None
        self._id = None
        self._uniprot = None
        self.discriminator = None

        self.entrezgene = entrezgene
        self.symbol = symbol
        self.gene_location = gene_location
        self.description = description
        self.label = label
        self.type = type
        self.ensembl = ensembl
        self.refseqprotein = refseqprotein
        self.omim = omim
        self.refseqmrna = refseqmrna
        self.hgncid = hgncid
        self.mgiid = mgiid
        self.ec_number = ec_number
        self.orthologous_gene = orthologous_gene
        if id is not None:
            self.id = id
        self.uniprot = uniprot

    @property
    def entrezgene(self):
        """Gets the entrezgene of this HumanGene.  # noqa: E501

        Description not available  # noqa: E501

        :return: The entrezgene of this HumanGene.  # noqa: E501
        :rtype: list[str]
        """
        return self._entrezgene

    @entrezgene.setter
    def entrezgene(self, entrezgene):
        """Sets the entrezgene of this HumanGene.

        Description not available  # noqa: E501

        :param entrezgene: The entrezgene of this HumanGene.  # noqa: E501
        :type: list[str]
        """

        self._entrezgene = entrezgene

    @property
    def symbol(self):
        """Gets the symbol of this HumanGene.  # noqa: E501

        HUGO Gene Symbol  # noqa: E501

        :return: The symbol of this HumanGene.  # noqa: E501
        :rtype: list[str]
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this HumanGene.

        HUGO Gene Symbol  # noqa: E501

        :param symbol: The symbol of this HumanGene.  # noqa: E501
        :type: list[str]
        """

        self._symbol = symbol

    @property
    def gene_location(self):
        """Gets the gene_location of this HumanGene.  # noqa: E501

        Description not available  # noqa: E501

        :return: The gene_location of this HumanGene.  # noqa: E501
        :rtype: list[object]
        """
        return self._gene_location

    @gene_location.setter
    def gene_location(self, gene_location):
        """Sets the gene_location of this HumanGene.

        Description not available  # noqa: E501

        :param gene_location: The gene_location of this HumanGene.  # noqa: E501
        :type: list[object]
        """

        self._gene_location = gene_location

    @property
    def description(self):
        """Gets the description of this HumanGene.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this HumanGene.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HumanGene.

        small description  # noqa: E501

        :param description: The description of this HumanGene.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def label(self):
        """Gets the label of this HumanGene.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this HumanGene.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this HumanGene.

        short description of the resource  # noqa: E501

        :param label: The label of this HumanGene.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this HumanGene.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this HumanGene.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HumanGene.

        type of the resource  # noqa: E501

        :param type: The type of this HumanGene.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def ensembl(self):
        """Gets the ensembl of this HumanGene.  # noqa: E501

        Description not available  # noqa: E501

        :return: The ensembl of this HumanGene.  # noqa: E501
        :rtype: list[str]
        """
        return self._ensembl

    @ensembl.setter
    def ensembl(self, ensembl):
        """Sets the ensembl of this HumanGene.

        Description not available  # noqa: E501

        :param ensembl: The ensembl of this HumanGene.  # noqa: E501
        :type: list[str]
        """

        self._ensembl = ensembl

    @property
    def refseqprotein(self):
        """Gets the refseqprotein of this HumanGene.  # noqa: E501

        Description not available  # noqa: E501

        :return: The refseqprotein of this HumanGene.  # noqa: E501
        :rtype: list[str]
        """
        return self._refseqprotein

    @refseqprotein.setter
    def refseqprotein(self, refseqprotein):
        """Sets the refseqprotein of this HumanGene.

        Description not available  # noqa: E501

        :param refseqprotein: The refseqprotein of this HumanGene.  # noqa: E501
        :type: list[str]
        """

        self._refseqprotein = refseqprotein

    @property
    def omim(self):
        """Gets the omim of this HumanGene.  # noqa: E501

        Description not available  # noqa: E501

        :return: The omim of this HumanGene.  # noqa: E501
        :rtype: list[int]
        """
        return self._omim

    @omim.setter
    def omim(self, omim):
        """Sets the omim of this HumanGene.

        Description not available  # noqa: E501

        :param omim: The omim of this HumanGene.  # noqa: E501
        :type: list[int]
        """

        self._omim = omim

    @property
    def refseqmrna(self):
        """Gets the refseqmrna of this HumanGene.  # noqa: E501

        Description not available  # noqa: E501

        :return: The refseqmrna of this HumanGene.  # noqa: E501
        :rtype: list[str]
        """
        return self._refseqmrna

    @refseqmrna.setter
    def refseqmrna(self, refseqmrna):
        """Sets the refseqmrna of this HumanGene.

        Description not available  # noqa: E501

        :param refseqmrna: The refseqmrna of this HumanGene.  # noqa: E501
        :type: list[str]
        """

        self._refseqmrna = refseqmrna

    @property
    def hgncid(self):
        """Gets the hgncid of this HumanGene.  # noqa: E501

        Description not available  # noqa: E501

        :return: The hgncid of this HumanGene.  # noqa: E501
        :rtype: list[str]
        """
        return self._hgncid

    @hgncid.setter
    def hgncid(self, hgncid):
        """Sets the hgncid of this HumanGene.

        Description not available  # noqa: E501

        :param hgncid: The hgncid of this HumanGene.  # noqa: E501
        :type: list[str]
        """

        self._hgncid = hgncid

    @property
    def mgiid(self):
        """Gets the mgiid of this HumanGene.  # noqa: E501

        Mouse Genomic Informatics ID  # noqa: E501

        :return: The mgiid of this HumanGene.  # noqa: E501
        :rtype: list[str]
        """
        return self._mgiid

    @mgiid.setter
    def mgiid(self, mgiid):
        """Sets the mgiid of this HumanGene.

        Mouse Genomic Informatics ID  # noqa: E501

        :param mgiid: The mgiid of this HumanGene.  # noqa: E501
        :type: list[str]
        """

        self._mgiid = mgiid

    @property
    def ec_number(self):
        """Gets the ec_number of this HumanGene.  # noqa: E501

        Description not available  # noqa: E501

        :return: The ec_number of this HumanGene.  # noqa: E501
        :rtype: list[str]
        """
        return self._ec_number

    @ec_number.setter
    def ec_number(self, ec_number):
        """Sets the ec_number of this HumanGene.

        Description not available  # noqa: E501

        :param ec_number: The ec_number of this HumanGene.  # noqa: E501
        :type: list[str]
        """

        self._ec_number = ec_number

    @property
    def orthologous_gene(self):
        """Gets the orthologous_gene of this HumanGene.  # noqa: E501

        Description not available  # noqa: E501

        :return: The orthologous_gene of this HumanGene.  # noqa: E501
        :rtype: list[object]
        """
        return self._orthologous_gene

    @orthologous_gene.setter
    def orthologous_gene(self, orthologous_gene):
        """Sets the orthologous_gene of this HumanGene.

        Description not available  # noqa: E501

        :param orthologous_gene: The orthologous_gene of this HumanGene.  # noqa: E501
        :type: list[object]
        """

        self._orthologous_gene = orthologous_gene

    @property
    def id(self):
        """Gets the id of this HumanGene.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this HumanGene.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HumanGene.

        identifier  # noqa: E501

        :param id: The id of this HumanGene.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def uniprot(self):
        """Gets the uniprot of this HumanGene.  # noqa: E501

        Description not available  # noqa: E501

        :return: The uniprot of this HumanGene.  # noqa: E501
        :rtype: list[str]
        """
        return self._uniprot

    @uniprot.setter
    def uniprot(self, uniprot):
        """Sets the uniprot of this HumanGene.

        Description not available  # noqa: E501

        :param uniprot: The uniprot of this HumanGene.  # noqa: E501
        :type: list[str]
        """

        self._uniprot = uniprot

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
        if not isinstance(other, HumanGene):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HumanGene):
            return True

        return self.to_dict() != other.to_dict()
