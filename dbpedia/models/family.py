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


class Family(object):
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
        'family_member': 'list[object]',
        'viaf_id': 'list[str]',
        'hometown': 'list[object]',
        'last_family_member': 'list[object]',
        'national_selection': 'list[object]',
        'art_patron': 'list[object]',
        'manager_season': 'list[object]',
        'ideology': 'list[object]',
        'description': 'list[str]',
        'label': 'list[str]',
        'discipline': 'list[object]',
        'type': 'list[str]',
        'junior_season': 'list[object]',
        'head_of_family': 'list[object]',
        'general_council': 'list[object]',
        'player_season': 'list[object]',
        'season': 'list[object]',
        'honours': 'list[object]',
        'primogenitor': 'list[object]',
        'id': 'str',
        'regional_council': 'list[object]',
        'age': 'list[int]',
        'nla_id': 'list[str]'
    }

    attribute_map = {
        'family_member': 'familyMember',
        'viaf_id': 'viafId',
        'hometown': 'hometown',
        'last_family_member': 'lastFamilyMember',
        'national_selection': 'nationalSelection',
        'art_patron': 'artPatron',
        'manager_season': 'managerSeason',
        'ideology': 'ideology',
        'description': 'description',
        'label': 'label',
        'discipline': 'discipline',
        'type': 'type',
        'junior_season': 'juniorSeason',
        'head_of_family': 'headOfFamily',
        'general_council': 'generalCouncil',
        'player_season': 'playerSeason',
        'season': 'season',
        'honours': 'honours',
        'primogenitor': 'primogenitor',
        'id': 'id',
        'regional_council': 'regionalCouncil',
        'age': 'age',
        'nla_id': 'nlaId'
    }

    def __init__(self, family_member=None, viaf_id=None, hometown=None, last_family_member=None, national_selection=None, art_patron=None, manager_season=None, ideology=None, description=None, label=None, discipline=None, type=None, junior_season=None, head_of_family=None, general_council=None, player_season=None, season=None, honours=None, primogenitor=None, id=None, regional_council=None, age=None, nla_id=None, local_vars_configuration=None):  # noqa: E501
        """Family - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._family_member = None
        self._viaf_id = None
        self._hometown = None
        self._last_family_member = None
        self._national_selection = None
        self._art_patron = None
        self._manager_season = None
        self._ideology = None
        self._description = None
        self._label = None
        self._discipline = None
        self._type = None
        self._junior_season = None
        self._head_of_family = None
        self._general_council = None
        self._player_season = None
        self._season = None
        self._honours = None
        self._primogenitor = None
        self._id = None
        self._regional_council = None
        self._age = None
        self._nla_id = None
        self.discriminator = None

        self.family_member = family_member
        self.viaf_id = viaf_id
        self.hometown = hometown
        self.last_family_member = last_family_member
        self.national_selection = national_selection
        self.art_patron = art_patron
        self.manager_season = manager_season
        self.ideology = ideology
        self.description = description
        self.label = label
        self.discipline = discipline
        self.type = type
        self.junior_season = junior_season
        self.head_of_family = head_of_family
        self.general_council = general_council
        self.player_season = player_season
        self.season = season
        self.honours = honours
        self.primogenitor = primogenitor
        if id is not None:
            self.id = id
        self.regional_council = regional_council
        self.age = age
        self.nla_id = nla_id

    @property
    def family_member(self):
        """Gets the family_member of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The family_member of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._family_member

    @family_member.setter
    def family_member(self, family_member):
        """Sets the family_member of this Family.

        Description not available  # noqa: E501

        :param family_member: The family_member of this Family.  # noqa: E501
        :type: list[object]
        """

        self._family_member = family_member

    @property
    def viaf_id(self):
        """Gets the viaf_id of this Family.  # noqa: E501

        International authority data from the Online Computer Library Center (OCLC)  # noqa: E501

        :return: The viaf_id of this Family.  # noqa: E501
        :rtype: list[str]
        """
        return self._viaf_id

    @viaf_id.setter
    def viaf_id(self, viaf_id):
        """Sets the viaf_id of this Family.

        International authority data from the Online Computer Library Center (OCLC)  # noqa: E501

        :param viaf_id: The viaf_id of this Family.  # noqa: E501
        :type: list[str]
        """

        self._viaf_id = viaf_id

    @property
    def hometown(self):
        """Gets the hometown of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The hometown of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._hometown

    @hometown.setter
    def hometown(self, hometown):
        """Sets the hometown of this Family.

        Description not available  # noqa: E501

        :param hometown: The hometown of this Family.  # noqa: E501
        :type: list[object]
        """

        self._hometown = hometown

    @property
    def last_family_member(self):
        """Gets the last_family_member of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The last_family_member of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._last_family_member

    @last_family_member.setter
    def last_family_member(self, last_family_member):
        """Sets the last_family_member of this Family.

        Description not available  # noqa: E501

        :param last_family_member: The last_family_member of this Family.  # noqa: E501
        :type: list[object]
        """

        self._last_family_member = last_family_member

    @property
    def national_selection(self):
        """Gets the national_selection of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The national_selection of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._national_selection

    @national_selection.setter
    def national_selection(self, national_selection):
        """Sets the national_selection of this Family.

        Description not available  # noqa: E501

        :param national_selection: The national_selection of this Family.  # noqa: E501
        :type: list[object]
        """

        self._national_selection = national_selection

    @property
    def art_patron(self):
        """Gets the art_patron of this Family.  # noqa: E501

        An influential, wealthy person who supported an artist, craftsman, a scholar or a noble.. See also  # noqa: E501

        :return: The art_patron of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._art_patron

    @art_patron.setter
    def art_patron(self, art_patron):
        """Sets the art_patron of this Family.

        An influential, wealthy person who supported an artist, craftsman, a scholar or a noble.. See also  # noqa: E501

        :param art_patron: The art_patron of this Family.  # noqa: E501
        :type: list[object]
        """

        self._art_patron = art_patron

    @property
    def manager_season(self):
        """Gets the manager_season of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The manager_season of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._manager_season

    @manager_season.setter
    def manager_season(self, manager_season):
        """Sets the manager_season of this Family.

        Description not available  # noqa: E501

        :param manager_season: The manager_season of this Family.  # noqa: E501
        :type: list[object]
        """

        self._manager_season = manager_season

    @property
    def ideology(self):
        """Gets the ideology of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The ideology of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._ideology

    @ideology.setter
    def ideology(self, ideology):
        """Sets the ideology of this Family.

        Description not available  # noqa: E501

        :param ideology: The ideology of this Family.  # noqa: E501
        :type: list[object]
        """

        self._ideology = ideology

    @property
    def description(self):
        """Gets the description of this Family.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Family.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Family.

        small description  # noqa: E501

        :param description: The description of this Family.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def label(self):
        """Gets the label of this Family.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Family.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Family.

        short description of the resource  # noqa: E501

        :param label: The label of this Family.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def discipline(self):
        """Gets the discipline of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The discipline of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._discipline

    @discipline.setter
    def discipline(self, discipline):
        """Sets the discipline of this Family.

        Description not available  # noqa: E501

        :param discipline: The discipline of this Family.  # noqa: E501
        :type: list[object]
        """

        self._discipline = discipline

    @property
    def type(self):
        """Gets the type of this Family.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Family.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Family.

        type of the resource  # noqa: E501

        :param type: The type of this Family.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def junior_season(self):
        """Gets the junior_season of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The junior_season of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._junior_season

    @junior_season.setter
    def junior_season(self, junior_season):
        """Sets the junior_season of this Family.

        Description not available  # noqa: E501

        :param junior_season: The junior_season of this Family.  # noqa: E501
        :type: list[object]
        """

        self._junior_season = junior_season

    @property
    def head_of_family(self):
        """Gets the head_of_family of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The head_of_family of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._head_of_family

    @head_of_family.setter
    def head_of_family(self, head_of_family):
        """Sets the head_of_family of this Family.

        Description not available  # noqa: E501

        :param head_of_family: The head_of_family of this Family.  # noqa: E501
        :type: list[object]
        """

        self._head_of_family = head_of_family

    @property
    def general_council(self):
        """Gets the general_council of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The general_council of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._general_council

    @general_council.setter
    def general_council(self, general_council):
        """Sets the general_council of this Family.

        Description not available  # noqa: E501

        :param general_council: The general_council of this Family.  # noqa: E501
        :type: list[object]
        """

        self._general_council = general_council

    @property
    def player_season(self):
        """Gets the player_season of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The player_season of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._player_season

    @player_season.setter
    def player_season(self, player_season):
        """Sets the player_season of this Family.

        Description not available  # noqa: E501

        :param player_season: The player_season of this Family.  # noqa: E501
        :type: list[object]
        """

        self._player_season = player_season

    @property
    def season(self):
        """Gets the season of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The season of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this Family.

        Description not available  # noqa: E501

        :param season: The season of this Family.  # noqa: E501
        :type: list[object]
        """

        self._season = season

    @property
    def honours(self):
        """Gets the honours of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The honours of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._honours

    @honours.setter
    def honours(self, honours):
        """Sets the honours of this Family.

        Description not available  # noqa: E501

        :param honours: The honours of this Family.  # noqa: E501
        :type: list[object]
        """

        self._honours = honours

    @property
    def primogenitor(self):
        """Gets the primogenitor of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The primogenitor of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._primogenitor

    @primogenitor.setter
    def primogenitor(self, primogenitor):
        """Sets the primogenitor of this Family.

        Description not available  # noqa: E501

        :param primogenitor: The primogenitor of this Family.  # noqa: E501
        :type: list[object]
        """

        self._primogenitor = primogenitor

    @property
    def id(self):
        """Gets the id of this Family.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Family.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Family.

        identifier  # noqa: E501

        :param id: The id of this Family.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def regional_council(self):
        """Gets the regional_council of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The regional_council of this Family.  # noqa: E501
        :rtype: list[object]
        """
        return self._regional_council

    @regional_council.setter
    def regional_council(self, regional_council):
        """Sets the regional_council of this Family.

        Description not available  # noqa: E501

        :param regional_council: The regional_council of this Family.  # noqa: E501
        :type: list[object]
        """

        self._regional_council = regional_council

    @property
    def age(self):
        """Gets the age of this Family.  # noqa: E501

        Description not available  # noqa: E501

        :return: The age of this Family.  # noqa: E501
        :rtype: list[int]
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this Family.

        Description not available  # noqa: E501

        :param age: The age of this Family.  # noqa: E501
        :type: list[int]
        """

        self._age = age

    @property
    def nla_id(self):
        """Gets the nla_id of this Family.  # noqa: E501

        NLA Trove’s People and Organisation view allows the discovery of biographical and other contextual information about people and organisations. Search also available via VIAF.  # noqa: E501

        :return: The nla_id of this Family.  # noqa: E501
        :rtype: list[str]
        """
        return self._nla_id

    @nla_id.setter
    def nla_id(self, nla_id):
        """Sets the nla_id of this Family.

        NLA Trove’s People and Organisation view allows the discovery of biographical and other contextual information about people and organisations. Search also available via VIAF.  # noqa: E501

        :param nla_id: The nla_id of this Family.  # noqa: E501
        :type: list[str]
        """

        self._nla_id = nla_id

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
        if not isinstance(other, Family):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Family):
            return True

        return self.to_dict() != other.to_dict()
