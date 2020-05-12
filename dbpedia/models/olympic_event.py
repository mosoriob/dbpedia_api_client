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


class OlympicEvent(object):
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
        'number_of_people_attending': 'list[int]',
        'end_date': 'list[str]',
        'description': 'list[str]',
        'type': 'list[str]',
        'silver_medalist': 'list[object]',
        'olympic_oath_sworn_by_athlete': 'list[object]',
        'participant': 'list[str]',
        'number_of_participating_athletes': 'list[int]',
        'duration': 'list[float]',
        'medalist': 'list[object]',
        'previous_event': 'list[object]',
        'champion_in_single_female': 'list[object]',
        'olympic_oath_sworn_by_judge': 'list[object]',
        'torch_bearer': 'list[object]',
        'champion_in_double_male': 'list[object]',
        'id': 'str',
        'following_event': 'list[object]',
        'champion_in_single_male': 'list[object]',
        'official_opened_by': 'list[object]',
        'bronze_medalist': 'list[object]',
        'champion_in_mixed_double': 'list[object]',
        'number_of_participating_male_athletes': 'list[int]',
        'caused_by': 'list[object]',
        'label': 'list[str]',
        'gold_medalist': 'list[object]',
        'champion_in_single': 'list[object]',
        'olympic_oath_sworn_by': 'list[object]',
        'number_of_newly_introduced_sports': 'list[int]',
        'race_track': 'list[object]',
        'next_event': 'list[object]',
        'number_of_participating_nations': 'list[int]',
        'champion_in_double_female': 'list[object]',
        'champion_in_double': 'list[object]',
        'number_of_participating_female_athletes': 'list[int]',
        'start_date': 'list[str]',
        'champion': 'list[object]'
    }

    attribute_map = {
        'number_of_people_attending': 'numberOfPeopleAttending',
        'end_date': 'endDate',
        'description': 'description',
        'type': 'type',
        'silver_medalist': 'silverMedalist',
        'olympic_oath_sworn_by_athlete': 'olympicOathSwornByAthlete',
        'participant': 'participant',
        'number_of_participating_athletes': 'numberOfParticipatingAthletes',
        'duration': 'duration',
        'medalist': 'medalist',
        'previous_event': 'previousEvent',
        'champion_in_single_female': 'championInSingleFemale',
        'olympic_oath_sworn_by_judge': 'olympicOathSwornByJudge',
        'torch_bearer': 'torchBearer',
        'champion_in_double_male': 'championInDoubleMale',
        'id': 'id',
        'following_event': 'followingEvent',
        'champion_in_single_male': 'championInSingleMale',
        'official_opened_by': 'officialOpenedBy',
        'bronze_medalist': 'bronzeMedalist',
        'champion_in_mixed_double': 'championInMixedDouble',
        'number_of_participating_male_athletes': 'numberOfParticipatingMaleAthletes',
        'caused_by': 'causedBy',
        'label': 'label',
        'gold_medalist': 'goldMedalist',
        'champion_in_single': 'championInSingle',
        'olympic_oath_sworn_by': 'olympicOathSwornBy',
        'number_of_newly_introduced_sports': 'numberOfNewlyIntroducedSports',
        'race_track': 'raceTrack',
        'next_event': 'nextEvent',
        'number_of_participating_nations': 'numberOfParticipatingNations',
        'champion_in_double_female': 'championInDoubleFemale',
        'champion_in_double': 'championInDouble',
        'number_of_participating_female_athletes': 'numberOfParticipatingFemaleAthletes',
        'start_date': 'startDate',
        'champion': 'champion'
    }

    def __init__(self, number_of_people_attending=None, end_date=None, description=None, type=None, silver_medalist=None, olympic_oath_sworn_by_athlete=None, participant=None, number_of_participating_athletes=None, duration=None, medalist=None, previous_event=None, champion_in_single_female=None, olympic_oath_sworn_by_judge=None, torch_bearer=None, champion_in_double_male=None, id=None, following_event=None, champion_in_single_male=None, official_opened_by=None, bronze_medalist=None, champion_in_mixed_double=None, number_of_participating_male_athletes=None, caused_by=None, label=None, gold_medalist=None, champion_in_single=None, olympic_oath_sworn_by=None, number_of_newly_introduced_sports=None, race_track=None, next_event=None, number_of_participating_nations=None, champion_in_double_female=None, champion_in_double=None, number_of_participating_female_athletes=None, start_date=None, champion=None, local_vars_configuration=None):  # noqa: E501
        """OlympicEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._number_of_people_attending = None
        self._end_date = None
        self._description = None
        self._type = None
        self._silver_medalist = None
        self._olympic_oath_sworn_by_athlete = None
        self._participant = None
        self._number_of_participating_athletes = None
        self._duration = None
        self._medalist = None
        self._previous_event = None
        self._champion_in_single_female = None
        self._olympic_oath_sworn_by_judge = None
        self._torch_bearer = None
        self._champion_in_double_male = None
        self._id = None
        self._following_event = None
        self._champion_in_single_male = None
        self._official_opened_by = None
        self._bronze_medalist = None
        self._champion_in_mixed_double = None
        self._number_of_participating_male_athletes = None
        self._caused_by = None
        self._label = None
        self._gold_medalist = None
        self._champion_in_single = None
        self._olympic_oath_sworn_by = None
        self._number_of_newly_introduced_sports = None
        self._race_track = None
        self._next_event = None
        self._number_of_participating_nations = None
        self._champion_in_double_female = None
        self._champion_in_double = None
        self._number_of_participating_female_athletes = None
        self._start_date = None
        self._champion = None
        self.discriminator = None

        self.number_of_people_attending = number_of_people_attending
        self.end_date = end_date
        self.description = description
        self.type = type
        self.silver_medalist = silver_medalist
        self.olympic_oath_sworn_by_athlete = olympic_oath_sworn_by_athlete
        self.participant = participant
        self.number_of_participating_athletes = number_of_participating_athletes
        self.duration = duration
        self.medalist = medalist
        self.previous_event = previous_event
        self.champion_in_single_female = champion_in_single_female
        self.olympic_oath_sworn_by_judge = olympic_oath_sworn_by_judge
        self.torch_bearer = torch_bearer
        self.champion_in_double_male = champion_in_double_male
        if id is not None:
            self.id = id
        self.following_event = following_event
        self.champion_in_single_male = champion_in_single_male
        self.official_opened_by = official_opened_by
        self.bronze_medalist = bronze_medalist
        self.champion_in_mixed_double = champion_in_mixed_double
        self.number_of_participating_male_athletes = number_of_participating_male_athletes
        self.caused_by = caused_by
        self.label = label
        self.gold_medalist = gold_medalist
        self.champion_in_single = champion_in_single
        self.olympic_oath_sworn_by = olympic_oath_sworn_by
        self.number_of_newly_introduced_sports = number_of_newly_introduced_sports
        self.race_track = race_track
        self.next_event = next_event
        self.number_of_participating_nations = number_of_participating_nations
        self.champion_in_double_female = champion_in_double_female
        self.champion_in_double = champion_in_double
        self.number_of_participating_female_athletes = number_of_participating_female_athletes
        self.start_date = start_date
        self.champion = champion

    @property
    def number_of_people_attending(self):
        """Gets the number_of_people_attending of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_people_attending of this OlympicEvent.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_people_attending

    @number_of_people_attending.setter
    def number_of_people_attending(self, number_of_people_attending):
        """Sets the number_of_people_attending of this OlympicEvent.

        Description not available  # noqa: E501

        :param number_of_people_attending: The number_of_people_attending of this OlympicEvent.  # noqa: E501
        :type: list[int]
        """

        self._number_of_people_attending = number_of_people_attending

    @property
    def end_date(self):
        """Gets the end_date of this OlympicEvent.  # noqa: E501

        The end date of the event.  # noqa: E501

        :return: The end_date of this OlympicEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this OlympicEvent.

        The end date of the event.  # noqa: E501

        :param end_date: The end_date of this OlympicEvent.  # noqa: E501
        :type: list[str]
        """

        self._end_date = end_date

    @property
    def description(self):
        """Gets the description of this OlympicEvent.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this OlympicEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OlympicEvent.

        small description  # noqa: E501

        :param description: The description of this OlympicEvent.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this OlympicEvent.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this OlympicEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OlympicEvent.

        type of the resource  # noqa: E501

        :param type: The type of this OlympicEvent.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def silver_medalist(self):
        """Gets the silver_medalist of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The silver_medalist of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._silver_medalist

    @silver_medalist.setter
    def silver_medalist(self, silver_medalist):
        """Sets the silver_medalist of this OlympicEvent.

        Description not available  # noqa: E501

        :param silver_medalist: The silver_medalist of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._silver_medalist = silver_medalist

    @property
    def olympic_oath_sworn_by_athlete(self):
        """Gets the olympic_oath_sworn_by_athlete of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The olympic_oath_sworn_by_athlete of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._olympic_oath_sworn_by_athlete

    @olympic_oath_sworn_by_athlete.setter
    def olympic_oath_sworn_by_athlete(self, olympic_oath_sworn_by_athlete):
        """Sets the olympic_oath_sworn_by_athlete of this OlympicEvent.

        Description not available  # noqa: E501

        :param olympic_oath_sworn_by_athlete: The olympic_oath_sworn_by_athlete of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._olympic_oath_sworn_by_athlete = olympic_oath_sworn_by_athlete

    @property
    def participant(self):
        """Gets the participant of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The participant of this OlympicEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this OlympicEvent.

        Description not available  # noqa: E501

        :param participant: The participant of this OlympicEvent.  # noqa: E501
        :type: list[str]
        """

        self._participant = participant

    @property
    def number_of_participating_athletes(self):
        """Gets the number_of_participating_athletes of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_participating_athletes of this OlympicEvent.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_participating_athletes

    @number_of_participating_athletes.setter
    def number_of_participating_athletes(self, number_of_participating_athletes):
        """Sets the number_of_participating_athletes of this OlympicEvent.

        Description not available  # noqa: E501

        :param number_of_participating_athletes: The number_of_participating_athletes of this OlympicEvent.  # noqa: E501
        :type: list[int]
        """

        self._number_of_participating_athletes = number_of_participating_athletes

    @property
    def duration(self):
        """Gets the duration of this OlympicEvent.  # noqa: E501

        The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format  # noqa: E501

        :return: The duration of this OlympicEvent.  # noqa: E501
        :rtype: list[float]
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this OlympicEvent.

        The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format  # noqa: E501

        :param duration: The duration of this OlympicEvent.  # noqa: E501
        :type: list[float]
        """

        self._duration = duration

    @property
    def medalist(self):
        """Gets the medalist of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The medalist of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._medalist

    @medalist.setter
    def medalist(self, medalist):
        """Sets the medalist of this OlympicEvent.

        Description not available  # noqa: E501

        :param medalist: The medalist of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._medalist = medalist

    @property
    def previous_event(self):
        """Gets the previous_event of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The previous_event of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._previous_event

    @previous_event.setter
    def previous_event(self, previous_event):
        """Sets the previous_event of this OlympicEvent.

        Description not available  # noqa: E501

        :param previous_event: The previous_event of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._previous_event = previous_event

    @property
    def champion_in_single_female(self):
        """Gets the champion_in_single_female of this OlympicEvent.  # noqa: E501

        winner of a competition in the single female session, to distinguish from the double session (as in tennis)  # noqa: E501

        :return: The champion_in_single_female of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._champion_in_single_female

    @champion_in_single_female.setter
    def champion_in_single_female(self, champion_in_single_female):
        """Sets the champion_in_single_female of this OlympicEvent.

        winner of a competition in the single female session, to distinguish from the double session (as in tennis)  # noqa: E501

        :param champion_in_single_female: The champion_in_single_female of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._champion_in_single_female = champion_in_single_female

    @property
    def olympic_oath_sworn_by_judge(self):
        """Gets the olympic_oath_sworn_by_judge of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The olympic_oath_sworn_by_judge of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._olympic_oath_sworn_by_judge

    @olympic_oath_sworn_by_judge.setter
    def olympic_oath_sworn_by_judge(self, olympic_oath_sworn_by_judge):
        """Sets the olympic_oath_sworn_by_judge of this OlympicEvent.

        Description not available  # noqa: E501

        :param olympic_oath_sworn_by_judge: The olympic_oath_sworn_by_judge of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._olympic_oath_sworn_by_judge = olympic_oath_sworn_by_judge

    @property
    def torch_bearer(self):
        """Gets the torch_bearer of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The torch_bearer of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._torch_bearer

    @torch_bearer.setter
    def torch_bearer(self, torch_bearer):
        """Sets the torch_bearer of this OlympicEvent.

        Description not available  # noqa: E501

        :param torch_bearer: The torch_bearer of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._torch_bearer = torch_bearer

    @property
    def champion_in_double_male(self):
        """Gets the champion_in_double_male of this OlympicEvent.  # noqa: E501

        winner of a competition in the male double session (as in tennis)  # noqa: E501

        :return: The champion_in_double_male of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._champion_in_double_male

    @champion_in_double_male.setter
    def champion_in_double_male(self, champion_in_double_male):
        """Sets the champion_in_double_male of this OlympicEvent.

        winner of a competition in the male double session (as in tennis)  # noqa: E501

        :param champion_in_double_male: The champion_in_double_male of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._champion_in_double_male = champion_in_double_male

    @property
    def id(self):
        """Gets the id of this OlympicEvent.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this OlympicEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OlympicEvent.

        identifier  # noqa: E501

        :param id: The id of this OlympicEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def following_event(self):
        """Gets the following_event of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The following_event of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._following_event

    @following_event.setter
    def following_event(self, following_event):
        """Sets the following_event of this OlympicEvent.

        Description not available  # noqa: E501

        :param following_event: The following_event of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._following_event = following_event

    @property
    def champion_in_single_male(self):
        """Gets the champion_in_single_male of this OlympicEvent.  # noqa: E501

        winner of a competition in the single male session, to distinguish from the double session (as in tennis)  # noqa: E501

        :return: The champion_in_single_male of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._champion_in_single_male

    @champion_in_single_male.setter
    def champion_in_single_male(self, champion_in_single_male):
        """Sets the champion_in_single_male of this OlympicEvent.

        winner of a competition in the single male session, to distinguish from the double session (as in tennis)  # noqa: E501

        :param champion_in_single_male: The champion_in_single_male of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._champion_in_single_male = champion_in_single_male

    @property
    def official_opened_by(self):
        """Gets the official_opened_by of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The official_opened_by of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._official_opened_by

    @official_opened_by.setter
    def official_opened_by(self, official_opened_by):
        """Sets the official_opened_by of this OlympicEvent.

        Description not available  # noqa: E501

        :param official_opened_by: The official_opened_by of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._official_opened_by = official_opened_by

    @property
    def bronze_medalist(self):
        """Gets the bronze_medalist of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The bronze_medalist of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._bronze_medalist

    @bronze_medalist.setter
    def bronze_medalist(self, bronze_medalist):
        """Sets the bronze_medalist of this OlympicEvent.

        Description not available  # noqa: E501

        :param bronze_medalist: The bronze_medalist of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._bronze_medalist = bronze_medalist

    @property
    def champion_in_mixed_double(self):
        """Gets the champion_in_mixed_double of this OlympicEvent.  # noqa: E501

        winner of a competition in the mixed double session (as in tennis)  # noqa: E501

        :return: The champion_in_mixed_double of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._champion_in_mixed_double

    @champion_in_mixed_double.setter
    def champion_in_mixed_double(self, champion_in_mixed_double):
        """Sets the champion_in_mixed_double of this OlympicEvent.

        winner of a competition in the mixed double session (as in tennis)  # noqa: E501

        :param champion_in_mixed_double: The champion_in_mixed_double of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._champion_in_mixed_double = champion_in_mixed_double

    @property
    def number_of_participating_male_athletes(self):
        """Gets the number_of_participating_male_athletes of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_participating_male_athletes of this OlympicEvent.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_participating_male_athletes

    @number_of_participating_male_athletes.setter
    def number_of_participating_male_athletes(self, number_of_participating_male_athletes):
        """Sets the number_of_participating_male_athletes of this OlympicEvent.

        Description not available  # noqa: E501

        :param number_of_participating_male_athletes: The number_of_participating_male_athletes of this OlympicEvent.  # noqa: E501
        :type: list[int]
        """

        self._number_of_participating_male_athletes = number_of_participating_male_athletes

    @property
    def caused_by(self):
        """Gets the caused_by of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The caused_by of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._caused_by

    @caused_by.setter
    def caused_by(self, caused_by):
        """Sets the caused_by of this OlympicEvent.

        Description not available  # noqa: E501

        :param caused_by: The caused_by of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._caused_by = caused_by

    @property
    def label(self):
        """Gets the label of this OlympicEvent.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this OlympicEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this OlympicEvent.

        short description of the resource  # noqa: E501

        :param label: The label of this OlympicEvent.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def gold_medalist(self):
        """Gets the gold_medalist of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The gold_medalist of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._gold_medalist

    @gold_medalist.setter
    def gold_medalist(self, gold_medalist):
        """Sets the gold_medalist of this OlympicEvent.

        Description not available  # noqa: E501

        :param gold_medalist: The gold_medalist of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._gold_medalist = gold_medalist

    @property
    def champion_in_single(self):
        """Gets the champion_in_single of this OlympicEvent.  # noqa: E501

        winner of a competition in the single session, to distinguish from the double session (as in tennis)  # noqa: E501

        :return: The champion_in_single of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._champion_in_single

    @champion_in_single.setter
    def champion_in_single(self, champion_in_single):
        """Sets the champion_in_single of this OlympicEvent.

        winner of a competition in the single session, to distinguish from the double session (as in tennis)  # noqa: E501

        :param champion_in_single: The champion_in_single of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._champion_in_single = champion_in_single

    @property
    def olympic_oath_sworn_by(self):
        """Gets the olympic_oath_sworn_by of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The olympic_oath_sworn_by of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._olympic_oath_sworn_by

    @olympic_oath_sworn_by.setter
    def olympic_oath_sworn_by(self, olympic_oath_sworn_by):
        """Sets the olympic_oath_sworn_by of this OlympicEvent.

        Description not available  # noqa: E501

        :param olympic_oath_sworn_by: The olympic_oath_sworn_by of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._olympic_oath_sworn_by = olympic_oath_sworn_by

    @property
    def number_of_newly_introduced_sports(self):
        """Gets the number_of_newly_introduced_sports of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_newly_introduced_sports of this OlympicEvent.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_newly_introduced_sports

    @number_of_newly_introduced_sports.setter
    def number_of_newly_introduced_sports(self, number_of_newly_introduced_sports):
        """Sets the number_of_newly_introduced_sports of this OlympicEvent.

        Description not available  # noqa: E501

        :param number_of_newly_introduced_sports: The number_of_newly_introduced_sports of this OlympicEvent.  # noqa: E501
        :type: list[int]
        """

        self._number_of_newly_introduced_sports = number_of_newly_introduced_sports

    @property
    def race_track(self):
        """Gets the race_track of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The race_track of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._race_track

    @race_track.setter
    def race_track(self, race_track):
        """Sets the race_track of this OlympicEvent.

        Description not available  # noqa: E501

        :param race_track: The race_track of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._race_track = race_track

    @property
    def next_event(self):
        """Gets the next_event of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The next_event of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._next_event

    @next_event.setter
    def next_event(self, next_event):
        """Sets the next_event of this OlympicEvent.

        Description not available  # noqa: E501

        :param next_event: The next_event of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._next_event = next_event

    @property
    def number_of_participating_nations(self):
        """Gets the number_of_participating_nations of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_participating_nations of this OlympicEvent.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_participating_nations

    @number_of_participating_nations.setter
    def number_of_participating_nations(self, number_of_participating_nations):
        """Sets the number_of_participating_nations of this OlympicEvent.

        Description not available  # noqa: E501

        :param number_of_participating_nations: The number_of_participating_nations of this OlympicEvent.  # noqa: E501
        :type: list[int]
        """

        self._number_of_participating_nations = number_of_participating_nations

    @property
    def champion_in_double_female(self):
        """Gets the champion_in_double_female of this OlympicEvent.  # noqa: E501

        winner of a competition in the female double session (as in tennis)  # noqa: E501

        :return: The champion_in_double_female of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._champion_in_double_female

    @champion_in_double_female.setter
    def champion_in_double_female(self, champion_in_double_female):
        """Sets the champion_in_double_female of this OlympicEvent.

        winner of a competition in the female double session (as in tennis)  # noqa: E501

        :param champion_in_double_female: The champion_in_double_female of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._champion_in_double_female = champion_in_double_female

    @property
    def champion_in_double(self):
        """Gets the champion_in_double of this OlympicEvent.  # noqa: E501

        winner of a competition in the double session (as in tennis)  # noqa: E501

        :return: The champion_in_double of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._champion_in_double

    @champion_in_double.setter
    def champion_in_double(self, champion_in_double):
        """Sets the champion_in_double of this OlympicEvent.

        winner of a competition in the double session (as in tennis)  # noqa: E501

        :param champion_in_double: The champion_in_double of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._champion_in_double = champion_in_double

    @property
    def number_of_participating_female_athletes(self):
        """Gets the number_of_participating_female_athletes of this OlympicEvent.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_participating_female_athletes of this OlympicEvent.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_participating_female_athletes

    @number_of_participating_female_athletes.setter
    def number_of_participating_female_athletes(self, number_of_participating_female_athletes):
        """Sets the number_of_participating_female_athletes of this OlympicEvent.

        Description not available  # noqa: E501

        :param number_of_participating_female_athletes: The number_of_participating_female_athletes of this OlympicEvent.  # noqa: E501
        :type: list[int]
        """

        self._number_of_participating_female_athletes = number_of_participating_female_athletes

    @property
    def start_date(self):
        """Gets the start_date of this OlympicEvent.  # noqa: E501

        The start date of the event.  # noqa: E501

        :return: The start_date of this OlympicEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this OlympicEvent.

        The start date of the event.  # noqa: E501

        :param start_date: The start_date of this OlympicEvent.  # noqa: E501
        :type: list[str]
        """

        self._start_date = start_date

    @property
    def champion(self):
        """Gets the champion of this OlympicEvent.  # noqa: E501

        winner of a competition  # noqa: E501

        :return: The champion of this OlympicEvent.  # noqa: E501
        :rtype: list[object]
        """
        return self._champion

    @champion.setter
    def champion(self, champion):
        """Sets the champion of this OlympicEvent.

        winner of a competition  # noqa: E501

        :param champion: The champion of this OlympicEvent.  # noqa: E501
        :type: list[object]
        """

        self._champion = champion

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
        if not isinstance(other, OlympicEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OlympicEvent):
            return True

        return self.to_dict() != other.to_dict()
