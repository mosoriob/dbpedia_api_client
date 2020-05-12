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


class Death(object):
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
        'caused_by': 'list[object]',
        'label': 'list[str]',
        'type': 'list[str]',
        'participant': 'list[str]',
        'duration': 'list[float]',
        'previous_event': 'list[object]',
        'next_event': 'list[object]',
        'id': 'str',
        'following_event': 'list[object]',
        'start_date': 'list[str]'
    }

    attribute_map = {
        'number_of_people_attending': 'numberOfPeopleAttending',
        'end_date': 'endDate',
        'description': 'description',
        'caused_by': 'causedBy',
        'label': 'label',
        'type': 'type',
        'participant': 'participant',
        'duration': 'duration',
        'previous_event': 'previousEvent',
        'next_event': 'nextEvent',
        'id': 'id',
        'following_event': 'followingEvent',
        'start_date': 'startDate'
    }

    def __init__(self, number_of_people_attending=None, end_date=None, description=None, caused_by=None, label=None, type=None, participant=None, duration=None, previous_event=None, next_event=None, id=None, following_event=None, start_date=None, local_vars_configuration=None):  # noqa: E501
        """Death - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._number_of_people_attending = None
        self._end_date = None
        self._description = None
        self._caused_by = None
        self._label = None
        self._type = None
        self._participant = None
        self._duration = None
        self._previous_event = None
        self._next_event = None
        self._id = None
        self._following_event = None
        self._start_date = None
        self.discriminator = None

        self.number_of_people_attending = number_of_people_attending
        self.end_date = end_date
        self.description = description
        self.caused_by = caused_by
        self.label = label
        self.type = type
        self.participant = participant
        self.duration = duration
        self.previous_event = previous_event
        self.next_event = next_event
        if id is not None:
            self.id = id
        self.following_event = following_event
        self.start_date = start_date

    @property
    def number_of_people_attending(self):
        """Gets the number_of_people_attending of this Death.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_people_attending of this Death.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_people_attending

    @number_of_people_attending.setter
    def number_of_people_attending(self, number_of_people_attending):
        """Sets the number_of_people_attending of this Death.

        Description not available  # noqa: E501

        :param number_of_people_attending: The number_of_people_attending of this Death.  # noqa: E501
        :type: list[int]
        """

        self._number_of_people_attending = number_of_people_attending

    @property
    def end_date(self):
        """Gets the end_date of this Death.  # noqa: E501

        The end date of the event.  # noqa: E501

        :return: The end_date of this Death.  # noqa: E501
        :rtype: list[str]
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Death.

        The end date of the event.  # noqa: E501

        :param end_date: The end_date of this Death.  # noqa: E501
        :type: list[str]
        """

        self._end_date = end_date

    @property
    def description(self):
        """Gets the description of this Death.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Death.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Death.

        small description  # noqa: E501

        :param description: The description of this Death.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def caused_by(self):
        """Gets the caused_by of this Death.  # noqa: E501

        Description not available  # noqa: E501

        :return: The caused_by of this Death.  # noqa: E501
        :rtype: list[object]
        """
        return self._caused_by

    @caused_by.setter
    def caused_by(self, caused_by):
        """Sets the caused_by of this Death.

        Description not available  # noqa: E501

        :param caused_by: The caused_by of this Death.  # noqa: E501
        :type: list[object]
        """

        self._caused_by = caused_by

    @property
    def label(self):
        """Gets the label of this Death.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Death.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Death.

        short description of the resource  # noqa: E501

        :param label: The label of this Death.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Death.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Death.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Death.

        type of the resource  # noqa: E501

        :param type: The type of this Death.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def participant(self):
        """Gets the participant of this Death.  # noqa: E501

        Description not available  # noqa: E501

        :return: The participant of this Death.  # noqa: E501
        :rtype: list[str]
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this Death.

        Description not available  # noqa: E501

        :param participant: The participant of this Death.  # noqa: E501
        :type: list[str]
        """

        self._participant = participant

    @property
    def duration(self):
        """Gets the duration of this Death.  # noqa: E501

        The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format  # noqa: E501

        :return: The duration of this Death.  # noqa: E501
        :rtype: list[float]
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Death.

        The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format  # noqa: E501

        :param duration: The duration of this Death.  # noqa: E501
        :type: list[float]
        """

        self._duration = duration

    @property
    def previous_event(self):
        """Gets the previous_event of this Death.  # noqa: E501

        Description not available  # noqa: E501

        :return: The previous_event of this Death.  # noqa: E501
        :rtype: list[object]
        """
        return self._previous_event

    @previous_event.setter
    def previous_event(self, previous_event):
        """Sets the previous_event of this Death.

        Description not available  # noqa: E501

        :param previous_event: The previous_event of this Death.  # noqa: E501
        :type: list[object]
        """

        self._previous_event = previous_event

    @property
    def next_event(self):
        """Gets the next_event of this Death.  # noqa: E501

        Description not available  # noqa: E501

        :return: The next_event of this Death.  # noqa: E501
        :rtype: list[object]
        """
        return self._next_event

    @next_event.setter
    def next_event(self, next_event):
        """Sets the next_event of this Death.

        Description not available  # noqa: E501

        :param next_event: The next_event of this Death.  # noqa: E501
        :type: list[object]
        """

        self._next_event = next_event

    @property
    def id(self):
        """Gets the id of this Death.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Death.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Death.

        identifier  # noqa: E501

        :param id: The id of this Death.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def following_event(self):
        """Gets the following_event of this Death.  # noqa: E501

        Description not available  # noqa: E501

        :return: The following_event of this Death.  # noqa: E501
        :rtype: list[object]
        """
        return self._following_event

    @following_event.setter
    def following_event(self, following_event):
        """Sets the following_event of this Death.

        Description not available  # noqa: E501

        :param following_event: The following_event of this Death.  # noqa: E501
        :type: list[object]
        """

        self._following_event = following_event

    @property
    def start_date(self):
        """Gets the start_date of this Death.  # noqa: E501

        The start date of the event.  # noqa: E501

        :return: The start_date of this Death.  # noqa: E501
        :rtype: list[str]
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Death.

        The start date of the event.  # noqa: E501

        :param start_date: The start_date of this Death.  # noqa: E501
        :type: list[str]
        """

        self._start_date = start_date

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
        if not isinstance(other, Death):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Death):
            return True

        return self.to_dict() != other.to_dict()
