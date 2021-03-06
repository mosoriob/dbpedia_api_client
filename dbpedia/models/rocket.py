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


class Rocket(object):
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
        'mass': 'list[object]',
        'description': 'list[str]',
        'engine_type': 'list[object]',
        'rocket_stages': 'list[int]',
        'type': 'list[str]',
        'introduction_date': 'list[str]',
        'rocket_function': 'list[object]',
        'lower_earth_orbit_payload': 'list[object]',
        'diameter': 'list[object]',
        'design_company': 'list[object]',
        'discharge': 'list[float]',
        'assembly': 'list[object]',
        'id': 'str',
        'rebuilder': 'list[object]',
        '_class': 'list[object]',
        'model_start_date': 'list[str]',
        'height': 'list[object]',
        'model_end_date': 'list[str]',
        'number_of_launches': 'list[int]',
        'model_end_year': 'list[str]',
        'maiden_flight': 'list[str]',
        'length': 'list[object]',
        'final_flight': 'list[str]',
        'weight': 'list[object]',
        'label': 'list[str]',
        'version': 'list[object]',
        'number_of_seats': 'list[int]',
        'model_start_year': 'list[str]',
        'width': 'list[object]',
        'discharge_average': 'list[float]',
        'number_of_crew': 'list[int]',
        'unknown_outcomes': 'list[int]',
        'country_origin': 'list[object]',
        'related_mean_of_transportation': 'list[object]',
        'comparable': 'list[object]',
        'power_type': 'list[object]'
    }

    attribute_map = {
        'mass': 'mass',
        'description': 'description',
        'engine_type': 'engineType',
        'rocket_stages': 'rocketStages',
        'type': 'type',
        'introduction_date': 'introductionDate',
        'rocket_function': 'rocketFunction',
        'lower_earth_orbit_payload': 'lowerEarthOrbitPayload',
        'diameter': 'diameter',
        'design_company': 'designCompany',
        'discharge': 'discharge',
        'assembly': 'assembly',
        'id': 'id',
        'rebuilder': 'rebuilder',
        '_class': 'class',
        'model_start_date': 'modelStartDate',
        'height': 'height',
        'model_end_date': 'modelEndDate',
        'number_of_launches': 'numberOfLaunches',
        'model_end_year': 'modelEndYear',
        'maiden_flight': 'maidenFlight',
        'length': 'length',
        'final_flight': 'finalFlight',
        'weight': 'weight',
        'label': 'label',
        'version': 'version',
        'number_of_seats': 'numberOfSeats',
        'model_start_year': 'modelStartYear',
        'width': 'width',
        'discharge_average': 'dischargeAverage',
        'number_of_crew': 'numberOfCrew',
        'unknown_outcomes': 'unknownOutcomes',
        'country_origin': 'countryOrigin',
        'related_mean_of_transportation': 'relatedMeanOfTransportation',
        'comparable': 'comparable',
        'power_type': 'powerType'
    }

    def __init__(self, mass=None, description=None, engine_type=None, rocket_stages=None, type=None, introduction_date=None, rocket_function=None, lower_earth_orbit_payload=None, diameter=None, design_company=None, discharge=None, assembly=None, id=None, rebuilder=None, _class=None, model_start_date=None, height=None, model_end_date=None, number_of_launches=None, model_end_year=None, maiden_flight=None, length=None, final_flight=None, weight=None, label=None, version=None, number_of_seats=None, model_start_year=None, width=None, discharge_average=None, number_of_crew=None, unknown_outcomes=None, country_origin=None, related_mean_of_transportation=None, comparable=None, power_type=None, local_vars_configuration=None):  # noqa: E501
        """Rocket - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mass = None
        self._description = None
        self._engine_type = None
        self._rocket_stages = None
        self._type = None
        self._introduction_date = None
        self._rocket_function = None
        self._lower_earth_orbit_payload = None
        self._diameter = None
        self._design_company = None
        self._discharge = None
        self._assembly = None
        self._id = None
        self._rebuilder = None
        self.__class = None
        self._model_start_date = None
        self._height = None
        self._model_end_date = None
        self._number_of_launches = None
        self._model_end_year = None
        self._maiden_flight = None
        self._length = None
        self._final_flight = None
        self._weight = None
        self._label = None
        self._version = None
        self._number_of_seats = None
        self._model_start_year = None
        self._width = None
        self._discharge_average = None
        self._number_of_crew = None
        self._unknown_outcomes = None
        self._country_origin = None
        self._related_mean_of_transportation = None
        self._comparable = None
        self._power_type = None
        self.discriminator = None

        self.mass = mass
        self.description = description
        self.engine_type = engine_type
        self.rocket_stages = rocket_stages
        self.type = type
        self.introduction_date = introduction_date
        self.rocket_function = rocket_function
        self.lower_earth_orbit_payload = lower_earth_orbit_payload
        self.diameter = diameter
        self.design_company = design_company
        self.discharge = discharge
        self.assembly = assembly
        if id is not None:
            self.id = id
        self.rebuilder = rebuilder
        self._class = _class
        self.model_start_date = model_start_date
        self.height = height
        self.model_end_date = model_end_date
        self.number_of_launches = number_of_launches
        self.model_end_year = model_end_year
        self.maiden_flight = maiden_flight
        self.length = length
        self.final_flight = final_flight
        self.weight = weight
        self.label = label
        self.version = version
        self.number_of_seats = number_of_seats
        self.model_start_year = model_start_year
        self.width = width
        self.discharge_average = discharge_average
        self.number_of_crew = number_of_crew
        self.unknown_outcomes = unknown_outcomes
        self.country_origin = country_origin
        self.related_mean_of_transportation = related_mean_of_transportation
        self.comparable = comparable
        self.power_type = power_type

    @property
    def mass(self):
        """Gets the mass of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The mass of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._mass

    @mass.setter
    def mass(self, mass):
        """Sets the mass of this Rocket.

        Description not available  # noqa: E501

        :param mass: The mass of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._mass = mass

    @property
    def description(self):
        """Gets the description of this Rocket.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Rocket.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rocket.

        small description  # noqa: E501

        :param description: The description of this Rocket.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def engine_type(self):
        """Gets the engine_type of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The engine_type of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this Rocket.

        Description not available  # noqa: E501

        :param engine_type: The engine_type of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._engine_type = engine_type

    @property
    def rocket_stages(self):
        """Gets the rocket_stages of this Rocket.  # noqa: E501

        number of stages, not including boosters  # noqa: E501

        :return: The rocket_stages of this Rocket.  # noqa: E501
        :rtype: list[int]
        """
        return self._rocket_stages

    @rocket_stages.setter
    def rocket_stages(self, rocket_stages):
        """Sets the rocket_stages of this Rocket.

        number of stages, not including boosters  # noqa: E501

        :param rocket_stages: The rocket_stages of this Rocket.  # noqa: E501
        :type: list[int]
        """

        self._rocket_stages = rocket_stages

    @property
    def type(self):
        """Gets the type of this Rocket.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Rocket.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Rocket.

        type of the resource  # noqa: E501

        :param type: The type of this Rocket.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def introduction_date(self):
        """Gets the introduction_date of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The introduction_date of this Rocket.  # noqa: E501
        :rtype: list[str]
        """
        return self._introduction_date

    @introduction_date.setter
    def introduction_date(self, introduction_date):
        """Sets the introduction_date of this Rocket.

        Description not available  # noqa: E501

        :param introduction_date: The introduction_date of this Rocket.  # noqa: E501
        :type: list[str]
        """

        self._introduction_date = introduction_date

    @property
    def rocket_function(self):
        """Gets the rocket_function of this Rocket.  # noqa: E501

        purpose of the rocket  # noqa: E501

        :return: The rocket_function of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._rocket_function

    @rocket_function.setter
    def rocket_function(self, rocket_function):
        """Sets the rocket_function of this Rocket.

        purpose of the rocket  # noqa: E501

        :param rocket_function: The rocket_function of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._rocket_function = rocket_function

    @property
    def lower_earth_orbit_payload(self):
        """Gets the lower_earth_orbit_payload of this Rocket.  # noqa: E501

        Payload mass in a typical Low Earth orbit  # noqa: E501

        :return: The lower_earth_orbit_payload of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._lower_earth_orbit_payload

    @lower_earth_orbit_payload.setter
    def lower_earth_orbit_payload(self, lower_earth_orbit_payload):
        """Sets the lower_earth_orbit_payload of this Rocket.

        Payload mass in a typical Low Earth orbit  # noqa: E501

        :param lower_earth_orbit_payload: The lower_earth_orbit_payload of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._lower_earth_orbit_payload = lower_earth_orbit_payload

    @property
    def diameter(self):
        """Gets the diameter of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The diameter of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        """Sets the diameter of this Rocket.

        Description not available  # noqa: E501

        :param diameter: The diameter of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._diameter = diameter

    @property
    def design_company(self):
        """Gets the design_company of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The design_company of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._design_company

    @design_company.setter
    def design_company(self, design_company):
        """Sets the design_company of this Rocket.

        Description not available  # noqa: E501

        :param design_company: The design_company of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._design_company = design_company

    @property
    def discharge(self):
        """Gets the discharge of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The discharge of this Rocket.  # noqa: E501
        :rtype: list[float]
        """
        return self._discharge

    @discharge.setter
    def discharge(self, discharge):
        """Sets the discharge of this Rocket.

        Description not available  # noqa: E501

        :param discharge: The discharge of this Rocket.  # noqa: E501
        :type: list[float]
        """

        self._discharge = discharge

    @property
    def assembly(self):
        """Gets the assembly of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The assembly of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._assembly

    @assembly.setter
    def assembly(self, assembly):
        """Sets the assembly of this Rocket.

        Description not available  # noqa: E501

        :param assembly: The assembly of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._assembly = assembly

    @property
    def id(self):
        """Gets the id of this Rocket.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Rocket.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Rocket.

        identifier  # noqa: E501

        :param id: The id of this Rocket.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def rebuilder(self):
        """Gets the rebuilder of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The rebuilder of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._rebuilder

    @rebuilder.setter
    def rebuilder(self, rebuilder):
        """Sets the rebuilder of this Rocket.

        Description not available  # noqa: E501

        :param rebuilder: The rebuilder of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._rebuilder = rebuilder

    @property
    def _class(self):
        """Gets the _class of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The _class of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Rocket.

        Description not available  # noqa: E501

        :param _class: The _class of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self.__class = _class

    @property
    def model_start_date(self):
        """Gets the model_start_date of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The model_start_date of this Rocket.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_start_date

    @model_start_date.setter
    def model_start_date(self, model_start_date):
        """Sets the model_start_date of this Rocket.

        Description not available  # noqa: E501

        :param model_start_date: The model_start_date of this Rocket.  # noqa: E501
        :type: list[str]
        """

        self._model_start_date = model_start_date

    @property
    def height(self):
        """Gets the height of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The height of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Rocket.

        Description not available  # noqa: E501

        :param height: The height of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._height = height

    @property
    def model_end_date(self):
        """Gets the model_end_date of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The model_end_date of this Rocket.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_end_date

    @model_end_date.setter
    def model_end_date(self, model_end_date):
        """Sets the model_end_date of this Rocket.

        Description not available  # noqa: E501

        :param model_end_date: The model_end_date of this Rocket.  # noqa: E501
        :type: list[str]
        """

        self._model_end_date = model_end_date

    @property
    def number_of_launches(self):
        """Gets the number_of_launches of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_launches of this Rocket.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_launches

    @number_of_launches.setter
    def number_of_launches(self, number_of_launches):
        """Sets the number_of_launches of this Rocket.

        Description not available  # noqa: E501

        :param number_of_launches: The number_of_launches of this Rocket.  # noqa: E501
        :type: list[int]
        """

        self._number_of_launches = number_of_launches

    @property
    def model_end_year(self):
        """Gets the model_end_year of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The model_end_year of this Rocket.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_end_year

    @model_end_year.setter
    def model_end_year(self, model_end_year):
        """Sets the model_end_year of this Rocket.

        Description not available  # noqa: E501

        :param model_end_year: The model_end_year of this Rocket.  # noqa: E501
        :type: list[str]
        """

        self._model_end_year = model_end_year

    @property
    def maiden_flight(self):
        """Gets the maiden_flight of this Rocket.  # noqa: E501

        date of maiden flight  # noqa: E501

        :return: The maiden_flight of this Rocket.  # noqa: E501
        :rtype: list[str]
        """
        return self._maiden_flight

    @maiden_flight.setter
    def maiden_flight(self, maiden_flight):
        """Sets the maiden_flight of this Rocket.

        date of maiden flight  # noqa: E501

        :param maiden_flight: The maiden_flight of this Rocket.  # noqa: E501
        :type: list[str]
        """

        self._maiden_flight = maiden_flight

    @property
    def length(self):
        """Gets the length of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The length of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Rocket.

        Description not available  # noqa: E501

        :param length: The length of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._length = length

    @property
    def final_flight(self):
        """Gets the final_flight of this Rocket.  # noqa: E501

        date of final flight  # noqa: E501

        :return: The final_flight of this Rocket.  # noqa: E501
        :rtype: list[str]
        """
        return self._final_flight

    @final_flight.setter
    def final_flight(self, final_flight):
        """Sets the final_flight of this Rocket.

        date of final flight  # noqa: E501

        :param final_flight: The final_flight of this Rocket.  # noqa: E501
        :type: list[str]
        """

        self._final_flight = final_flight

    @property
    def weight(self):
        """Gets the weight of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The weight of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Rocket.

        Description not available  # noqa: E501

        :param weight: The weight of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._weight = weight

    @property
    def label(self):
        """Gets the label of this Rocket.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Rocket.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Rocket.

        short description of the resource  # noqa: E501

        :param label: The label of this Rocket.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def version(self):
        """Gets the version of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The version of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Rocket.

        Description not available  # noqa: E501

        :param version: The version of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._version = version

    @property
    def number_of_seats(self):
        """Gets the number_of_seats of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_seats of this Rocket.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, number_of_seats):
        """Sets the number_of_seats of this Rocket.

        Description not available  # noqa: E501

        :param number_of_seats: The number_of_seats of this Rocket.  # noqa: E501
        :type: list[int]
        """

        self._number_of_seats = number_of_seats

    @property
    def model_start_year(self):
        """Gets the model_start_year of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The model_start_year of this Rocket.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_start_year

    @model_start_year.setter
    def model_start_year(self, model_start_year):
        """Sets the model_start_year of this Rocket.

        Description not available  # noqa: E501

        :param model_start_year: The model_start_year of this Rocket.  # noqa: E501
        :type: list[str]
        """

        self._model_start_year = model_start_year

    @property
    def width(self):
        """Gets the width of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The width of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Rocket.

        Description not available  # noqa: E501

        :param width: The width of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._width = width

    @property
    def discharge_average(self):
        """Gets the discharge_average of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The discharge_average of this Rocket.  # noqa: E501
        :rtype: list[float]
        """
        return self._discharge_average

    @discharge_average.setter
    def discharge_average(self, discharge_average):
        """Sets the discharge_average of this Rocket.

        Description not available  # noqa: E501

        :param discharge_average: The discharge_average of this Rocket.  # noqa: E501
        :type: list[float]
        """

        self._discharge_average = discharge_average

    @property
    def number_of_crew(self):
        """Gets the number_of_crew of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_crew of this Rocket.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_crew

    @number_of_crew.setter
    def number_of_crew(self, number_of_crew):
        """Sets the number_of_crew of this Rocket.

        Description not available  # noqa: E501

        :param number_of_crew: The number_of_crew of this Rocket.  # noqa: E501
        :type: list[int]
        """

        self._number_of_crew = number_of_crew

    @property
    def unknown_outcomes(self):
        """Gets the unknown_outcomes of this Rocket.  # noqa: E501

        number of launches with unknown outcomes (or in progress)  # noqa: E501

        :return: The unknown_outcomes of this Rocket.  # noqa: E501
        :rtype: list[int]
        """
        return self._unknown_outcomes

    @unknown_outcomes.setter
    def unknown_outcomes(self, unknown_outcomes):
        """Sets the unknown_outcomes of this Rocket.

        number of launches with unknown outcomes (or in progress)  # noqa: E501

        :param unknown_outcomes: The unknown_outcomes of this Rocket.  # noqa: E501
        :type: list[int]
        """

        self._unknown_outcomes = unknown_outcomes

    @property
    def country_origin(self):
        """Gets the country_origin of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The country_origin of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._country_origin

    @country_origin.setter
    def country_origin(self, country_origin):
        """Sets the country_origin of this Rocket.

        Description not available  # noqa: E501

        :param country_origin: The country_origin of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._country_origin = country_origin

    @property
    def related_mean_of_transportation(self):
        """Gets the related_mean_of_transportation of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The related_mean_of_transportation of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._related_mean_of_transportation

    @related_mean_of_transportation.setter
    def related_mean_of_transportation(self, related_mean_of_transportation):
        """Sets the related_mean_of_transportation of this Rocket.

        Description not available  # noqa: E501

        :param related_mean_of_transportation: The related_mean_of_transportation of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._related_mean_of_transportation = related_mean_of_transportation

    @property
    def comparable(self):
        """Gets the comparable of this Rocket.  # noqa: E501

        similar, unrelated rockets  # noqa: E501

        :return: The comparable of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._comparable

    @comparable.setter
    def comparable(self, comparable):
        """Sets the comparable of this Rocket.

        similar, unrelated rockets  # noqa: E501

        :param comparable: The comparable of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._comparable = comparable

    @property
    def power_type(self):
        """Gets the power_type of this Rocket.  # noqa: E501

        Description not available  # noqa: E501

        :return: The power_type of this Rocket.  # noqa: E501
        :rtype: list[object]
        """
        return self._power_type

    @power_type.setter
    def power_type(self, power_type):
        """Sets the power_type of this Rocket.

        Description not available  # noqa: E501

        :param power_type: The power_type of this Rocket.  # noqa: E501
        :type: list[object]
        """

        self._power_type = power_type

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
        if not isinstance(other, Rocket):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Rocket):
            return True

        return self.to_dict() != other.to_dict()
