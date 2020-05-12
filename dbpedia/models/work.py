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


class Work(object):
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
        'previous_work': 'list[object]',
        'translator': 'list[object]',
        'alternative_title': 'list[str]',
        'description': 'list[str]',
        'subsequent_work': 'list[object]',
        'chief_editor': 'list[object]',
        'music_composer': 'list[object]',
        'type': 'list[str]',
        'main_character': 'list[object]',
        'id': 'str',
        'based_on': 'list[object]',
        'release_date': 'list[str]',
        'composer': 'list[object]',
        'author': 'list[object]',
        'runtime': 'list[object]',
        'production_company': 'list[object]',
        'label': 'list[str]',
        'original_language': 'list[object]',
        'license': 'list[object]',
        'subject_term': 'list[str]',
        'original_title': 'list[str]',
        'producer': 'list[object]',
        'starring': 'list[object]',
        'completion_date': 'list[str]',
        'writer': 'list[object]'
    }

    attribute_map = {
        'previous_work': 'previousWork',
        'translator': 'translator',
        'alternative_title': 'alternativeTitle',
        'description': 'description',
        'subsequent_work': 'subsequentWork',
        'chief_editor': 'chiefEditor',
        'music_composer': 'musicComposer',
        'type': 'type',
        'main_character': 'mainCharacter',
        'id': 'id',
        'based_on': 'basedOn',
        'release_date': 'releaseDate',
        'composer': 'composer',
        'author': 'author',
        'runtime': 'runtime',
        'production_company': 'productionCompany',
        'label': 'label',
        'original_language': 'originalLanguage',
        'license': 'license',
        'subject_term': 'subjectTerm',
        'original_title': 'originalTitle',
        'producer': 'producer',
        'starring': 'starring',
        'completion_date': 'completionDate',
        'writer': 'writer'
    }

    def __init__(self, previous_work=None, translator=None, alternative_title=None, description=None, subsequent_work=None, chief_editor=None, music_composer=None, type=None, main_character=None, id=None, based_on=None, release_date=None, composer=None, author=None, runtime=None, production_company=None, label=None, original_language=None, license=None, subject_term=None, original_title=None, producer=None, starring=None, completion_date=None, writer=None, local_vars_configuration=None):  # noqa: E501
        """Work - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._previous_work = None
        self._translator = None
        self._alternative_title = None
        self._description = None
        self._subsequent_work = None
        self._chief_editor = None
        self._music_composer = None
        self._type = None
        self._main_character = None
        self._id = None
        self._based_on = None
        self._release_date = None
        self._composer = None
        self._author = None
        self._runtime = None
        self._production_company = None
        self._label = None
        self._original_language = None
        self._license = None
        self._subject_term = None
        self._original_title = None
        self._producer = None
        self._starring = None
        self._completion_date = None
        self._writer = None
        self.discriminator = None

        self.previous_work = previous_work
        self.translator = translator
        self.alternative_title = alternative_title
        self.description = description
        self.subsequent_work = subsequent_work
        self.chief_editor = chief_editor
        self.music_composer = music_composer
        self.type = type
        self.main_character = main_character
        if id is not None:
            self.id = id
        self.based_on = based_on
        self.release_date = release_date
        self.composer = composer
        self.author = author
        self.runtime = runtime
        self.production_company = production_company
        self.label = label
        self.original_language = original_language
        self.license = license
        self.subject_term = subject_term
        self.original_title = original_title
        self.producer = producer
        self.starring = starring
        self.completion_date = completion_date
        self.writer = writer

    @property
    def previous_work(self):
        """Gets the previous_work of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The previous_work of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._previous_work

    @previous_work.setter
    def previous_work(self, previous_work):
        """Sets the previous_work of this Work.

        Description not available  # noqa: E501

        :param previous_work: The previous_work of this Work.  # noqa: E501
        :type: list[object]
        """

        self._previous_work = previous_work

    @property
    def translator(self):
        """Gets the translator of this Work.  # noqa: E501

        Translator(s), if original not in English  # noqa: E501

        :return: The translator of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._translator

    @translator.setter
    def translator(self, translator):
        """Sets the translator of this Work.

        Translator(s), if original not in English  # noqa: E501

        :param translator: The translator of this Work.  # noqa: E501
        :type: list[object]
        """

        self._translator = translator

    @property
    def alternative_title(self):
        """Gets the alternative_title of this Work.  # noqa: E501

        The alternative title attributed to a work  # noqa: E501

        :return: The alternative_title of this Work.  # noqa: E501
        :rtype: list[str]
        """
        return self._alternative_title

    @alternative_title.setter
    def alternative_title(self, alternative_title):
        """Sets the alternative_title of this Work.

        The alternative title attributed to a work  # noqa: E501

        :param alternative_title: The alternative_title of this Work.  # noqa: E501
        :type: list[str]
        """

        self._alternative_title = alternative_title

    @property
    def description(self):
        """Gets the description of this Work.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Work.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Work.

        small description  # noqa: E501

        :param description: The description of this Work.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def subsequent_work(self):
        """Gets the subsequent_work of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The subsequent_work of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._subsequent_work

    @subsequent_work.setter
    def subsequent_work(self, subsequent_work):
        """Sets the subsequent_work of this Work.

        Description not available  # noqa: E501

        :param subsequent_work: The subsequent_work of this Work.  # noqa: E501
        :type: list[object]
        """

        self._subsequent_work = subsequent_work

    @property
    def chief_editor(self):
        """Gets the chief_editor of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The chief_editor of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._chief_editor

    @chief_editor.setter
    def chief_editor(self, chief_editor):
        """Sets the chief_editor of this Work.

        Description not available  # noqa: E501

        :param chief_editor: The chief_editor of this Work.  # noqa: E501
        :type: list[object]
        """

        self._chief_editor = chief_editor

    @property
    def music_composer(self):
        """Gets the music_composer of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The music_composer of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._music_composer

    @music_composer.setter
    def music_composer(self, music_composer):
        """Sets the music_composer of this Work.

        Description not available  # noqa: E501

        :param music_composer: The music_composer of this Work.  # noqa: E501
        :type: list[object]
        """

        self._music_composer = music_composer

    @property
    def type(self):
        """Gets the type of this Work.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Work.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Work.

        type of the resource  # noqa: E501

        :param type: The type of this Work.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def main_character(self):
        """Gets the main_character of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The main_character of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._main_character

    @main_character.setter
    def main_character(self, main_character):
        """Sets the main_character of this Work.

        Description not available  # noqa: E501

        :param main_character: The main_character of this Work.  # noqa: E501
        :type: list[object]
        """

        self._main_character = main_character

    @property
    def id(self):
        """Gets the id of this Work.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Work.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Work.

        identifier  # noqa: E501

        :param id: The id of this Work.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def based_on(self):
        """Gets the based_on of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The based_on of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._based_on

    @based_on.setter
    def based_on(self, based_on):
        """Sets the based_on of this Work.

        Description not available  # noqa: E501

        :param based_on: The based_on of this Work.  # noqa: E501
        :type: list[object]
        """

        self._based_on = based_on

    @property
    def release_date(self):
        """Gets the release_date of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The release_date of this Work.  # noqa: E501
        :rtype: list[str]
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this Work.

        Description not available  # noqa: E501

        :param release_date: The release_date of this Work.  # noqa: E501
        :type: list[str]
        """

        self._release_date = release_date

    @property
    def composer(self):
        """Gets the composer of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The composer of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._composer

    @composer.setter
    def composer(self, composer):
        """Sets the composer of this Work.

        Description not available  # noqa: E501

        :param composer: The composer of this Work.  # noqa: E501
        :type: list[object]
        """

        self._composer = composer

    @property
    def author(self):
        """Gets the author of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The author of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Work.

        Description not available  # noqa: E501

        :param author: The author of this Work.  # noqa: E501
        :type: list[object]
        """

        self._author = author

    @property
    def runtime(self):
        """Gets the runtime of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The runtime of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this Work.

        Description not available  # noqa: E501

        :param runtime: The runtime of this Work.  # noqa: E501
        :type: list[object]
        """

        self._runtime = runtime

    @property
    def production_company(self):
        """Gets the production_company of this Work.  # noqa: E501

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :return: The production_company of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._production_company

    @production_company.setter
    def production_company(self, production_company):
        """Sets the production_company of this Work.

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :param production_company: The production_company of this Work.  # noqa: E501
        :type: list[object]
        """

        self._production_company = production_company

    @property
    def label(self):
        """Gets the label of this Work.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Work.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Work.

        short description of the resource  # noqa: E501

        :param label: The label of this Work.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def original_language(self):
        """Gets the original_language of this Work.  # noqa: E501

        The original language of the work.  # noqa: E501

        :return: The original_language of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._original_language

    @original_language.setter
    def original_language(self, original_language):
        """Sets the original_language of this Work.

        The original language of the work.  # noqa: E501

        :param original_language: The original_language of this Work.  # noqa: E501
        :type: list[object]
        """

        self._original_language = original_language

    @property
    def license(self):
        """Gets the license of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The license of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Work.

        Description not available  # noqa: E501

        :param license: The license of this Work.  # noqa: E501
        :type: list[object]
        """

        self._license = license

    @property
    def subject_term(self):
        """Gets the subject_term of this Work.  # noqa: E501

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :return: The subject_term of this Work.  # noqa: E501
        :rtype: list[str]
        """
        return self._subject_term

    @subject_term.setter
    def subject_term(self, subject_term):
        """Sets the subject_term of this Work.

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :param subject_term: The subject_term of this Work.  # noqa: E501
        :type: list[str]
        """

        self._subject_term = subject_term

    @property
    def original_title(self):
        """Gets the original_title of this Work.  # noqa: E501

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :return: The original_title of this Work.  # noqa: E501
        :rtype: list[str]
        """
        return self._original_title

    @original_title.setter
    def original_title(self, original_title):
        """Sets the original_title of this Work.

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :param original_title: The original_title of this Work.  # noqa: E501
        :type: list[str]
        """

        self._original_title = original_title

    @property
    def producer(self):
        """Gets the producer of this Work.  # noqa: E501

        The producer of the creative work.  # noqa: E501

        :return: The producer of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """Sets the producer of this Work.

        The producer of the creative work.  # noqa: E501

        :param producer: The producer of this Work.  # noqa: E501
        :type: list[object]
        """

        self._producer = producer

    @property
    def starring(self):
        """Gets the starring of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The starring of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._starring

    @starring.setter
    def starring(self, starring):
        """Sets the starring of this Work.

        Description not available  # noqa: E501

        :param starring: The starring of this Work.  # noqa: E501
        :type: list[object]
        """

        self._starring = starring

    @property
    def completion_date(self):
        """Gets the completion_date of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The completion_date of this Work.  # noqa: E501
        :rtype: list[str]
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this Work.

        Description not available  # noqa: E501

        :param completion_date: The completion_date of this Work.  # noqa: E501
        :type: list[str]
        """

        self._completion_date = completion_date

    @property
    def writer(self):
        """Gets the writer of this Work.  # noqa: E501

        Description not available  # noqa: E501

        :return: The writer of this Work.  # noqa: E501
        :rtype: list[object]
        """
        return self._writer

    @writer.setter
    def writer(self, writer):
        """Sets the writer of this Work.

        Description not available  # noqa: E501

        :param writer: The writer of this Work.  # noqa: E501
        :type: list[object]
        """

        self._writer = writer

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
        if not isinstance(other, Work):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Work):
            return True

        return self.to_dict() != other.to_dict()
