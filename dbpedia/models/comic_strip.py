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


class ComicStrip(object):
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
        'coden': 'list[str]',
        'translator': 'list[object]',
        'alternative_title': 'list[str]',
        'description': 'list[str]',
        'subsequent_work': 'list[object]',
        'chief_editor': 'list[object]',
        'music_composer': 'list[object]',
        'last_publication_date': 'list[str]',
        'type': 'list[str]',
        'lcc': 'list[str]',
        'lccn': 'list[str]',
        'main_character': 'list[object]',
        'id': 'str',
        'literary_genre': 'list[object]',
        'based_on': 'list[object]',
        'first_publisher': 'list[object]',
        'first_publication_date': 'list[str]',
        'film_version': 'list[object]',
        'release_date': 'list[str]',
        'number_of_volumes': 'list[int]',
        'composer': 'list[object]',
        'author': 'list[object]',
        'preface_by': 'list[object]',
        'runtime': 'list[object]',
        'production_company': 'list[object]',
        'label': 'list[str]',
        'original_language': 'list[object]',
        'license': 'list[object]',
        'subject_term': 'list[str]',
        'original_title': 'list[str]',
        'circulation': 'list[int]',
        'oclc': 'list[str]',
        'producer': 'list[object]',
        'starring': 'list[object]',
        'completion_date': 'list[str]',
        'writer': 'list[object]',
        'magazine': 'list[object]'
    }

    attribute_map = {
        'previous_work': 'previousWork',
        'coden': 'coden',
        'translator': 'translator',
        'alternative_title': 'alternativeTitle',
        'description': 'description',
        'subsequent_work': 'subsequentWork',
        'chief_editor': 'chiefEditor',
        'music_composer': 'musicComposer',
        'last_publication_date': 'lastPublicationDate',
        'type': 'type',
        'lcc': 'lcc',
        'lccn': 'lccn',
        'main_character': 'mainCharacter',
        'id': 'id',
        'literary_genre': 'literaryGenre',
        'based_on': 'basedOn',
        'first_publisher': 'firstPublisher',
        'first_publication_date': 'firstPublicationDate',
        'film_version': 'filmVersion',
        'release_date': 'releaseDate',
        'number_of_volumes': 'numberOfVolumes',
        'composer': 'composer',
        'author': 'author',
        'preface_by': 'prefaceBy',
        'runtime': 'runtime',
        'production_company': 'productionCompany',
        'label': 'label',
        'original_language': 'originalLanguage',
        'license': 'license',
        'subject_term': 'subjectTerm',
        'original_title': 'originalTitle',
        'circulation': 'circulation',
        'oclc': 'oclc',
        'producer': 'producer',
        'starring': 'starring',
        'completion_date': 'completionDate',
        'writer': 'writer',
        'magazine': 'magazine'
    }

    def __init__(self, previous_work=None, coden=None, translator=None, alternative_title=None, description=None, subsequent_work=None, chief_editor=None, music_composer=None, last_publication_date=None, type=None, lcc=None, lccn=None, main_character=None, id=None, literary_genre=None, based_on=None, first_publisher=None, first_publication_date=None, film_version=None, release_date=None, number_of_volumes=None, composer=None, author=None, preface_by=None, runtime=None, production_company=None, label=None, original_language=None, license=None, subject_term=None, original_title=None, circulation=None, oclc=None, producer=None, starring=None, completion_date=None, writer=None, magazine=None, local_vars_configuration=None):  # noqa: E501
        """ComicStrip - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._previous_work = None
        self._coden = None
        self._translator = None
        self._alternative_title = None
        self._description = None
        self._subsequent_work = None
        self._chief_editor = None
        self._music_composer = None
        self._last_publication_date = None
        self._type = None
        self._lcc = None
        self._lccn = None
        self._main_character = None
        self._id = None
        self._literary_genre = None
        self._based_on = None
        self._first_publisher = None
        self._first_publication_date = None
        self._film_version = None
        self._release_date = None
        self._number_of_volumes = None
        self._composer = None
        self._author = None
        self._preface_by = None
        self._runtime = None
        self._production_company = None
        self._label = None
        self._original_language = None
        self._license = None
        self._subject_term = None
        self._original_title = None
        self._circulation = None
        self._oclc = None
        self._producer = None
        self._starring = None
        self._completion_date = None
        self._writer = None
        self._magazine = None
        self.discriminator = None

        self.previous_work = previous_work
        self.coden = coden
        self.translator = translator
        self.alternative_title = alternative_title
        self.description = description
        self.subsequent_work = subsequent_work
        self.chief_editor = chief_editor
        self.music_composer = music_composer
        self.last_publication_date = last_publication_date
        self.type = type
        self.lcc = lcc
        self.lccn = lccn
        self.main_character = main_character
        if id is not None:
            self.id = id
        self.literary_genre = literary_genre
        self.based_on = based_on
        self.first_publisher = first_publisher
        self.first_publication_date = first_publication_date
        self.film_version = film_version
        self.release_date = release_date
        self.number_of_volumes = number_of_volumes
        self.composer = composer
        self.author = author
        self.preface_by = preface_by
        self.runtime = runtime
        self.production_company = production_company
        self.label = label
        self.original_language = original_language
        self.license = license
        self.subject_term = subject_term
        self.original_title = original_title
        self.circulation = circulation
        self.oclc = oclc
        self.producer = producer
        self.starring = starring
        self.completion_date = completion_date
        self.writer = writer
        self.magazine = magazine

    @property
    def previous_work(self):
        """Gets the previous_work of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The previous_work of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._previous_work

    @previous_work.setter
    def previous_work(self, previous_work):
        """Sets the previous_work of this ComicStrip.

        Description not available  # noqa: E501

        :param previous_work: The previous_work of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._previous_work = previous_work

    @property
    def coden(self):
        """Gets the coden of this ComicStrip.  # noqa: E501

        CODEN is a six character, alphanumeric bibliographic code, that provides concise, unique and unambiguous identification of the titles of serials and non-serial publications from all subject areas.  # noqa: E501

        :return: The coden of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._coden

    @coden.setter
    def coden(self, coden):
        """Sets the coden of this ComicStrip.

        CODEN is a six character, alphanumeric bibliographic code, that provides concise, unique and unambiguous identification of the titles of serials and non-serial publications from all subject areas.  # noqa: E501

        :param coden: The coden of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._coden = coden

    @property
    def translator(self):
        """Gets the translator of this ComicStrip.  # noqa: E501

        Translator(s), if original not in English  # noqa: E501

        :return: The translator of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._translator

    @translator.setter
    def translator(self, translator):
        """Sets the translator of this ComicStrip.

        Translator(s), if original not in English  # noqa: E501

        :param translator: The translator of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._translator = translator

    @property
    def alternative_title(self):
        """Gets the alternative_title of this ComicStrip.  # noqa: E501

        The alternative title attributed to a work  # noqa: E501

        :return: The alternative_title of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._alternative_title

    @alternative_title.setter
    def alternative_title(self, alternative_title):
        """Sets the alternative_title of this ComicStrip.

        The alternative title attributed to a work  # noqa: E501

        :param alternative_title: The alternative_title of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._alternative_title = alternative_title

    @property
    def description(self):
        """Gets the description of this ComicStrip.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComicStrip.

        small description  # noqa: E501

        :param description: The description of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def subsequent_work(self):
        """Gets the subsequent_work of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The subsequent_work of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._subsequent_work

    @subsequent_work.setter
    def subsequent_work(self, subsequent_work):
        """Sets the subsequent_work of this ComicStrip.

        Description not available  # noqa: E501

        :param subsequent_work: The subsequent_work of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._subsequent_work = subsequent_work

    @property
    def chief_editor(self):
        """Gets the chief_editor of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The chief_editor of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._chief_editor

    @chief_editor.setter
    def chief_editor(self, chief_editor):
        """Sets the chief_editor of this ComicStrip.

        Description not available  # noqa: E501

        :param chief_editor: The chief_editor of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._chief_editor = chief_editor

    @property
    def music_composer(self):
        """Gets the music_composer of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The music_composer of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._music_composer

    @music_composer.setter
    def music_composer(self, music_composer):
        """Sets the music_composer of this ComicStrip.

        Description not available  # noqa: E501

        :param music_composer: The music_composer of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._music_composer = music_composer

    @property
    def last_publication_date(self):
        """Gets the last_publication_date of this ComicStrip.  # noqa: E501

        Date of the last publication.  # noqa: E501

        :return: The last_publication_date of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._last_publication_date

    @last_publication_date.setter
    def last_publication_date(self, last_publication_date):
        """Sets the last_publication_date of this ComicStrip.

        Date of the last publication.  # noqa: E501

        :param last_publication_date: The last_publication_date of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._last_publication_date = last_publication_date

    @property
    def type(self):
        """Gets the type of this ComicStrip.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComicStrip.

        type of the resource  # noqa: E501

        :param type: The type of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def lcc(self):
        """Gets the lcc of this ComicStrip.  # noqa: E501

        The Library of Congress Classification (LCC) is a system of library classification developed by the Library of Congress.  # noqa: E501

        :return: The lcc of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._lcc

    @lcc.setter
    def lcc(self, lcc):
        """Sets the lcc of this ComicStrip.

        The Library of Congress Classification (LCC) is a system of library classification developed by the Library of Congress.  # noqa: E501

        :param lcc: The lcc of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._lcc = lcc

    @property
    def lccn(self):
        """Gets the lccn of this ComicStrip.  # noqa: E501

        The Library of Congress Control Number or LCCN is a serially based system of numbering cataloging records in the Library of Congress in the United States. It has nothing to do with the contents of any book, and should not be confused with Library of Congress Classification.  # noqa: E501

        :return: The lccn of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._lccn

    @lccn.setter
    def lccn(self, lccn):
        """Sets the lccn of this ComicStrip.

        The Library of Congress Control Number or LCCN is a serially based system of numbering cataloging records in the Library of Congress in the United States. It has nothing to do with the contents of any book, and should not be confused with Library of Congress Classification.  # noqa: E501

        :param lccn: The lccn of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._lccn = lccn

    @property
    def main_character(self):
        """Gets the main_character of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The main_character of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._main_character

    @main_character.setter
    def main_character(self, main_character):
        """Sets the main_character of this ComicStrip.

        Description not available  # noqa: E501

        :param main_character: The main_character of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._main_character = main_character

    @property
    def id(self):
        """Gets the id of this ComicStrip.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this ComicStrip.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComicStrip.

        identifier  # noqa: E501

        :param id: The id of this ComicStrip.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def literary_genre(self):
        """Gets the literary_genre of this ComicStrip.  # noqa: E501

        A literary genre is a category of literary composition. Genres may be determined by literary technique, tone, content, or even (as in the case of fiction) length.  # noqa: E501

        :return: The literary_genre of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._literary_genre

    @literary_genre.setter
    def literary_genre(self, literary_genre):
        """Sets the literary_genre of this ComicStrip.

        A literary genre is a category of literary composition. Genres may be determined by literary technique, tone, content, or even (as in the case of fiction) length.  # noqa: E501

        :param literary_genre: The literary_genre of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._literary_genre = literary_genre

    @property
    def based_on(self):
        """Gets the based_on of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The based_on of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._based_on

    @based_on.setter
    def based_on(self, based_on):
        """Sets the based_on of this ComicStrip.

        Description not available  # noqa: E501

        :param based_on: The based_on of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._based_on = based_on

    @property
    def first_publisher(self):
        """Gets the first_publisher of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The first_publisher of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._first_publisher

    @first_publisher.setter
    def first_publisher(self, first_publisher):
        """Sets the first_publisher of this ComicStrip.

        Description not available  # noqa: E501

        :param first_publisher: The first_publisher of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._first_publisher = first_publisher

    @property
    def first_publication_date(self):
        """Gets the first_publication_date of this ComicStrip.  # noqa: E501

        Date of the first publication.  # noqa: E501

        :return: The first_publication_date of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._first_publication_date

    @first_publication_date.setter
    def first_publication_date(self, first_publication_date):
        """Sets the first_publication_date of this ComicStrip.

        Date of the first publication.  # noqa: E501

        :param first_publication_date: The first_publication_date of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._first_publication_date = first_publication_date

    @property
    def film_version(self):
        """Gets the film_version of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The film_version of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._film_version

    @film_version.setter
    def film_version(self, film_version):
        """Sets the film_version of this ComicStrip.

        Description not available  # noqa: E501

        :param film_version: The film_version of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._film_version = film_version

    @property
    def release_date(self):
        """Gets the release_date of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The release_date of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this ComicStrip.

        Description not available  # noqa: E501

        :param release_date: The release_date of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._release_date = release_date

    @property
    def number_of_volumes(self):
        """Gets the number_of_volumes of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_volumes of this ComicStrip.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_volumes

    @number_of_volumes.setter
    def number_of_volumes(self, number_of_volumes):
        """Sets the number_of_volumes of this ComicStrip.

        Description not available  # noqa: E501

        :param number_of_volumes: The number_of_volumes of this ComicStrip.  # noqa: E501
        :type: list[int]
        """

        self._number_of_volumes = number_of_volumes

    @property
    def composer(self):
        """Gets the composer of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The composer of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._composer

    @composer.setter
    def composer(self, composer):
        """Sets the composer of this ComicStrip.

        Description not available  # noqa: E501

        :param composer: The composer of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._composer = composer

    @property
    def author(self):
        """Gets the author of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The author of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ComicStrip.

        Description not available  # noqa: E501

        :param author: The author of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._author = author

    @property
    def preface_by(self):
        """Gets the preface_by of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The preface_by of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._preface_by

    @preface_by.setter
    def preface_by(self, preface_by):
        """Sets the preface_by of this ComicStrip.

        Description not available  # noqa: E501

        :param preface_by: The preface_by of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._preface_by = preface_by

    @property
    def runtime(self):
        """Gets the runtime of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The runtime of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this ComicStrip.

        Description not available  # noqa: E501

        :param runtime: The runtime of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._runtime = runtime

    @property
    def production_company(self):
        """Gets the production_company of this ComicStrip.  # noqa: E501

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :return: The production_company of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._production_company

    @production_company.setter
    def production_company(self, production_company):
        """Sets the production_company of this ComicStrip.

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :param production_company: The production_company of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._production_company = production_company

    @property
    def label(self):
        """Gets the label of this ComicStrip.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ComicStrip.

        short description of the resource  # noqa: E501

        :param label: The label of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def original_language(self):
        """Gets the original_language of this ComicStrip.  # noqa: E501

        The original language of the work.  # noqa: E501

        :return: The original_language of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._original_language

    @original_language.setter
    def original_language(self, original_language):
        """Sets the original_language of this ComicStrip.

        The original language of the work.  # noqa: E501

        :param original_language: The original_language of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._original_language = original_language

    @property
    def license(self):
        """Gets the license of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The license of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this ComicStrip.

        Description not available  # noqa: E501

        :param license: The license of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._license = license

    @property
    def subject_term(self):
        """Gets the subject_term of this ComicStrip.  # noqa: E501

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :return: The subject_term of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._subject_term

    @subject_term.setter
    def subject_term(self, subject_term):
        """Sets the subject_term of this ComicStrip.

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :param subject_term: The subject_term of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._subject_term = subject_term

    @property
    def original_title(self):
        """Gets the original_title of this ComicStrip.  # noqa: E501

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :return: The original_title of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._original_title

    @original_title.setter
    def original_title(self, original_title):
        """Sets the original_title of this ComicStrip.

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :param original_title: The original_title of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._original_title = original_title

    @property
    def circulation(self):
        """Gets the circulation of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The circulation of this ComicStrip.  # noqa: E501
        :rtype: list[int]
        """
        return self._circulation

    @circulation.setter
    def circulation(self, circulation):
        """Sets the circulation of this ComicStrip.

        Description not available  # noqa: E501

        :param circulation: The circulation of this ComicStrip.  # noqa: E501
        :type: list[int]
        """

        self._circulation = circulation

    @property
    def oclc(self):
        """Gets the oclc of this ComicStrip.  # noqa: E501

        Online Computer Library Center number  # noqa: E501

        :return: The oclc of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._oclc

    @oclc.setter
    def oclc(self, oclc):
        """Sets the oclc of this ComicStrip.

        Online Computer Library Center number  # noqa: E501

        :param oclc: The oclc of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._oclc = oclc

    @property
    def producer(self):
        """Gets the producer of this ComicStrip.  # noqa: E501

        The producer of the creative work.  # noqa: E501

        :return: The producer of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """Sets the producer of this ComicStrip.

        The producer of the creative work.  # noqa: E501

        :param producer: The producer of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._producer = producer

    @property
    def starring(self):
        """Gets the starring of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The starring of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._starring

    @starring.setter
    def starring(self, starring):
        """Sets the starring of this ComicStrip.

        Description not available  # noqa: E501

        :param starring: The starring of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._starring = starring

    @property
    def completion_date(self):
        """Gets the completion_date of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The completion_date of this ComicStrip.  # noqa: E501
        :rtype: list[str]
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this ComicStrip.

        Description not available  # noqa: E501

        :param completion_date: The completion_date of this ComicStrip.  # noqa: E501
        :type: list[str]
        """

        self._completion_date = completion_date

    @property
    def writer(self):
        """Gets the writer of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The writer of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._writer

    @writer.setter
    def writer(self, writer):
        """Sets the writer of this ComicStrip.

        Description not available  # noqa: E501

        :param writer: The writer of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._writer = writer

    @property
    def magazine(self):
        """Gets the magazine of this ComicStrip.  # noqa: E501

        Description not available  # noqa: E501

        :return: The magazine of this ComicStrip.  # noqa: E501
        :rtype: list[object]
        """
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        """Sets the magazine of this ComicStrip.

        Description not available  # noqa: E501

        :param magazine: The magazine of this ComicStrip.  # noqa: E501
        :type: list[object]
        """

        self._magazine = magazine

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
        if not isinstance(other, ComicStrip):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComicStrip):
            return True

        return self.to_dict() != other.to_dict()
