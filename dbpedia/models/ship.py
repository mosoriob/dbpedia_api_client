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


class Ship(object):
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
        'laying_down': 'list[str]',
        'mass': 'list[object]',
        'description': 'list[str]',
        'engine_type': 'list[object]',
        'type': 'list[str]',
        'introduction_date': 'list[str]',
        'ship_launch': 'list[str]',
        'diameter': 'list[object]',
        'design_company': 'list[object]',
        'christening_date': 'list[str]',
        'discharge': 'list[float]',
        'assembly': 'list[object]',
        'id': 'str',
        'ship_crew': 'list[object]',
        'rebuilder': 'list[object]',
        '_class': 'list[object]',
        'model_start_date': 'list[str]',
        'acquirement_date': 'list[str]',
        'height': 'list[object]',
        'model_end_date': 'list[str]',
        'number_of_launches': 'list[int]',
        'model_end_year': 'list[str]',
        'maiden_voyage': 'list[str]',
        'length': 'list[object]',
        'weight': 'list[object]',
        'commissioning_date': 'list[str]',
        'label': 'list[str]',
        'version': 'list[object]',
        'decommissioning_date': 'list[str]',
        'recommissioning_date': 'list[str]',
        'ship_beam': 'list[float]',
        'number_of_seats': 'list[int]',
        'homeport': 'list[object]',
        'model_start_year': 'list[str]',
        'width': 'list[object]',
        'discharge_average': 'list[float]',
        'number_of_crew': 'list[int]',
        'capture_date': 'list[str]',
        'ship_draft': 'list[float]',
        'order_date': 'list[str]',
        'related_mean_of_transportation': 'list[object]',
        'ship_displacement': 'list[float]',
        'power_type': 'list[object]'
    }

    attribute_map = {
        'laying_down': 'layingDown',
        'mass': 'mass',
        'description': 'description',
        'engine_type': 'engineType',
        'type': 'type',
        'introduction_date': 'introductionDate',
        'ship_launch': 'shipLaunch',
        'diameter': 'diameter',
        'design_company': 'designCompany',
        'christening_date': 'christeningDate',
        'discharge': 'discharge',
        'assembly': 'assembly',
        'id': 'id',
        'ship_crew': 'shipCrew',
        'rebuilder': 'rebuilder',
        '_class': 'class',
        'model_start_date': 'modelStartDate',
        'acquirement_date': 'acquirementDate',
        'height': 'height',
        'model_end_date': 'modelEndDate',
        'number_of_launches': 'numberOfLaunches',
        'model_end_year': 'modelEndYear',
        'maiden_voyage': 'maidenVoyage',
        'length': 'length',
        'weight': 'weight',
        'commissioning_date': 'commissioningDate',
        'label': 'label',
        'version': 'version',
        'decommissioning_date': 'decommissioningDate',
        'recommissioning_date': 'recommissioningDate',
        'ship_beam': 'shipBeam',
        'number_of_seats': 'numberOfSeats',
        'homeport': 'homeport',
        'model_start_year': 'modelStartYear',
        'width': 'width',
        'discharge_average': 'dischargeAverage',
        'number_of_crew': 'numberOfCrew',
        'capture_date': 'captureDate',
        'ship_draft': 'shipDraft',
        'order_date': 'orderDate',
        'related_mean_of_transportation': 'relatedMeanOfTransportation',
        'ship_displacement': 'shipDisplacement',
        'power_type': 'powerType'
    }

    def __init__(self, laying_down=None, mass=None, description=None, engine_type=None, type=None, introduction_date=None, ship_launch=None, diameter=None, design_company=None, christening_date=None, discharge=None, assembly=None, id=None, ship_crew=None, rebuilder=None, _class=None, model_start_date=None, acquirement_date=None, height=None, model_end_date=None, number_of_launches=None, model_end_year=None, maiden_voyage=None, length=None, weight=None, commissioning_date=None, label=None, version=None, decommissioning_date=None, recommissioning_date=None, ship_beam=None, number_of_seats=None, homeport=None, model_start_year=None, width=None, discharge_average=None, number_of_crew=None, capture_date=None, ship_draft=None, order_date=None, related_mean_of_transportation=None, ship_displacement=None, power_type=None, local_vars_configuration=None):  # noqa: E501
        """Ship - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._laying_down = None
        self._mass = None
        self._description = None
        self._engine_type = None
        self._type = None
        self._introduction_date = None
        self._ship_launch = None
        self._diameter = None
        self._design_company = None
        self._christening_date = None
        self._discharge = None
        self._assembly = None
        self._id = None
        self._ship_crew = None
        self._rebuilder = None
        self.__class = None
        self._model_start_date = None
        self._acquirement_date = None
        self._height = None
        self._model_end_date = None
        self._number_of_launches = None
        self._model_end_year = None
        self._maiden_voyage = None
        self._length = None
        self._weight = None
        self._commissioning_date = None
        self._label = None
        self._version = None
        self._decommissioning_date = None
        self._recommissioning_date = None
        self._ship_beam = None
        self._number_of_seats = None
        self._homeport = None
        self._model_start_year = None
        self._width = None
        self._discharge_average = None
        self._number_of_crew = None
        self._capture_date = None
        self._ship_draft = None
        self._order_date = None
        self._related_mean_of_transportation = None
        self._ship_displacement = None
        self._power_type = None
        self.discriminator = None

        self.laying_down = laying_down
        self.mass = mass
        self.description = description
        self.engine_type = engine_type
        self.type = type
        self.introduction_date = introduction_date
        self.ship_launch = ship_launch
        self.diameter = diameter
        self.design_company = design_company
        self.christening_date = christening_date
        self.discharge = discharge
        self.assembly = assembly
        if id is not None:
            self.id = id
        self.ship_crew = ship_crew
        self.rebuilder = rebuilder
        self._class = _class
        self.model_start_date = model_start_date
        self.acquirement_date = acquirement_date
        self.height = height
        self.model_end_date = model_end_date
        self.number_of_launches = number_of_launches
        self.model_end_year = model_end_year
        self.maiden_voyage = maiden_voyage
        self.length = length
        self.weight = weight
        self.commissioning_date = commissioning_date
        self.label = label
        self.version = version
        self.decommissioning_date = decommissioning_date
        self.recommissioning_date = recommissioning_date
        self.ship_beam = ship_beam
        self.number_of_seats = number_of_seats
        self.homeport = homeport
        self.model_start_year = model_start_year
        self.width = width
        self.discharge_average = discharge_average
        self.number_of_crew = number_of_crew
        self.capture_date = capture_date
        self.ship_draft = ship_draft
        self.order_date = order_date
        self.related_mean_of_transportation = related_mean_of_transportation
        self.ship_displacement = ship_displacement
        self.power_type = power_type

    @property
    def laying_down(self):
        """Gets the laying_down of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The laying_down of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._laying_down

    @laying_down.setter
    def laying_down(self, laying_down):
        """Sets the laying_down of this Ship.

        Description not available  # noqa: E501

        :param laying_down: The laying_down of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._laying_down = laying_down

    @property
    def mass(self):
        """Gets the mass of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The mass of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._mass

    @mass.setter
    def mass(self, mass):
        """Sets the mass of this Ship.

        Description not available  # noqa: E501

        :param mass: The mass of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._mass = mass

    @property
    def description(self):
        """Gets the description of this Ship.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Ship.

        small description  # noqa: E501

        :param description: The description of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def engine_type(self):
        """Gets the engine_type of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The engine_type of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this Ship.

        Description not available  # noqa: E501

        :param engine_type: The engine_type of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._engine_type = engine_type

    @property
    def type(self):
        """Gets the type of this Ship.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Ship.

        type of the resource  # noqa: E501

        :param type: The type of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def introduction_date(self):
        """Gets the introduction_date of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The introduction_date of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._introduction_date

    @introduction_date.setter
    def introduction_date(self, introduction_date):
        """Sets the introduction_date of this Ship.

        Description not available  # noqa: E501

        :param introduction_date: The introduction_date of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._introduction_date = introduction_date

    @property
    def ship_launch(self):
        """Gets the ship_launch of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The ship_launch of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._ship_launch

    @ship_launch.setter
    def ship_launch(self, ship_launch):
        """Sets the ship_launch of this Ship.

        Description not available  # noqa: E501

        :param ship_launch: The ship_launch of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._ship_launch = ship_launch

    @property
    def diameter(self):
        """Gets the diameter of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The diameter of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        """Sets the diameter of this Ship.

        Description not available  # noqa: E501

        :param diameter: The diameter of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._diameter = diameter

    @property
    def design_company(self):
        """Gets the design_company of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The design_company of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._design_company

    @design_company.setter
    def design_company(self, design_company):
        """Sets the design_company of this Ship.

        Description not available  # noqa: E501

        :param design_company: The design_company of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._design_company = design_company

    @property
    def christening_date(self):
        """Gets the christening_date of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The christening_date of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._christening_date

    @christening_date.setter
    def christening_date(self, christening_date):
        """Sets the christening_date of this Ship.

        Description not available  # noqa: E501

        :param christening_date: The christening_date of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._christening_date = christening_date

    @property
    def discharge(self):
        """Gets the discharge of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The discharge of this Ship.  # noqa: E501
        :rtype: list[float]
        """
        return self._discharge

    @discharge.setter
    def discharge(self, discharge):
        """Sets the discharge of this Ship.

        Description not available  # noqa: E501

        :param discharge: The discharge of this Ship.  # noqa: E501
        :type: list[float]
        """

        self._discharge = discharge

    @property
    def assembly(self):
        """Gets the assembly of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The assembly of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._assembly

    @assembly.setter
    def assembly(self, assembly):
        """Sets the assembly of this Ship.

        Description not available  # noqa: E501

        :param assembly: The assembly of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._assembly = assembly

    @property
    def id(self):
        """Gets the id of this Ship.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Ship.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Ship.

        identifier  # noqa: E501

        :param id: The id of this Ship.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ship_crew(self):
        """Gets the ship_crew of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The ship_crew of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._ship_crew

    @ship_crew.setter
    def ship_crew(self, ship_crew):
        """Sets the ship_crew of this Ship.

        Description not available  # noqa: E501

        :param ship_crew: The ship_crew of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._ship_crew = ship_crew

    @property
    def rebuilder(self):
        """Gets the rebuilder of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The rebuilder of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._rebuilder

    @rebuilder.setter
    def rebuilder(self, rebuilder):
        """Sets the rebuilder of this Ship.

        Description not available  # noqa: E501

        :param rebuilder: The rebuilder of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._rebuilder = rebuilder

    @property
    def _class(self):
        """Gets the _class of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The _class of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Ship.

        Description not available  # noqa: E501

        :param _class: The _class of this Ship.  # noqa: E501
        :type: list[object]
        """

        self.__class = _class

    @property
    def model_start_date(self):
        """Gets the model_start_date of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The model_start_date of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_start_date

    @model_start_date.setter
    def model_start_date(self, model_start_date):
        """Sets the model_start_date of this Ship.

        Description not available  # noqa: E501

        :param model_start_date: The model_start_date of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._model_start_date = model_start_date

    @property
    def acquirement_date(self):
        """Gets the acquirement_date of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The acquirement_date of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._acquirement_date

    @acquirement_date.setter
    def acquirement_date(self, acquirement_date):
        """Sets the acquirement_date of this Ship.

        Description not available  # noqa: E501

        :param acquirement_date: The acquirement_date of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._acquirement_date = acquirement_date

    @property
    def height(self):
        """Gets the height of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The height of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Ship.

        Description not available  # noqa: E501

        :param height: The height of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._height = height

    @property
    def model_end_date(self):
        """Gets the model_end_date of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The model_end_date of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_end_date

    @model_end_date.setter
    def model_end_date(self, model_end_date):
        """Sets the model_end_date of this Ship.

        Description not available  # noqa: E501

        :param model_end_date: The model_end_date of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._model_end_date = model_end_date

    @property
    def number_of_launches(self):
        """Gets the number_of_launches of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_launches of this Ship.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_launches

    @number_of_launches.setter
    def number_of_launches(self, number_of_launches):
        """Sets the number_of_launches of this Ship.

        Description not available  # noqa: E501

        :param number_of_launches: The number_of_launches of this Ship.  # noqa: E501
        :type: list[int]
        """

        self._number_of_launches = number_of_launches

    @property
    def model_end_year(self):
        """Gets the model_end_year of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The model_end_year of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_end_year

    @model_end_year.setter
    def model_end_year(self, model_end_year):
        """Sets the model_end_year of this Ship.

        Description not available  # noqa: E501

        :param model_end_year: The model_end_year of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._model_end_year = model_end_year

    @property
    def maiden_voyage(self):
        """Gets the maiden_voyage of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The maiden_voyage of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._maiden_voyage

    @maiden_voyage.setter
    def maiden_voyage(self, maiden_voyage):
        """Sets the maiden_voyage of this Ship.

        Description not available  # noqa: E501

        :param maiden_voyage: The maiden_voyage of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._maiden_voyage = maiden_voyage

    @property
    def length(self):
        """Gets the length of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The length of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Ship.

        Description not available  # noqa: E501

        :param length: The length of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._length = length

    @property
    def weight(self):
        """Gets the weight of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The weight of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Ship.

        Description not available  # noqa: E501

        :param weight: The weight of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._weight = weight

    @property
    def commissioning_date(self):
        """Gets the commissioning_date of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The commissioning_date of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._commissioning_date

    @commissioning_date.setter
    def commissioning_date(self, commissioning_date):
        """Sets the commissioning_date of this Ship.

        Description not available  # noqa: E501

        :param commissioning_date: The commissioning_date of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._commissioning_date = commissioning_date

    @property
    def label(self):
        """Gets the label of this Ship.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Ship.

        short description of the resource  # noqa: E501

        :param label: The label of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def version(self):
        """Gets the version of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The version of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Ship.

        Description not available  # noqa: E501

        :param version: The version of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._version = version

    @property
    def decommissioning_date(self):
        """Gets the decommissioning_date of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The decommissioning_date of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._decommissioning_date

    @decommissioning_date.setter
    def decommissioning_date(self, decommissioning_date):
        """Sets the decommissioning_date of this Ship.

        Description not available  # noqa: E501

        :param decommissioning_date: The decommissioning_date of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._decommissioning_date = decommissioning_date

    @property
    def recommissioning_date(self):
        """Gets the recommissioning_date of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The recommissioning_date of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._recommissioning_date

    @recommissioning_date.setter
    def recommissioning_date(self, recommissioning_date):
        """Sets the recommissioning_date of this Ship.

        Description not available  # noqa: E501

        :param recommissioning_date: The recommissioning_date of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._recommissioning_date = recommissioning_date

    @property
    def ship_beam(self):
        """Gets the ship_beam of this Ship.  # noqa: E501

        The beam of a ship is its width at the widest point.  # noqa: E501

        :return: The ship_beam of this Ship.  # noqa: E501
        :rtype: list[float]
        """
        return self._ship_beam

    @ship_beam.setter
    def ship_beam(self, ship_beam):
        """Sets the ship_beam of this Ship.

        The beam of a ship is its width at the widest point.  # noqa: E501

        :param ship_beam: The ship_beam of this Ship.  # noqa: E501
        :type: list[float]
        """

        self._ship_beam = ship_beam

    @property
    def number_of_seats(self):
        """Gets the number_of_seats of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_seats of this Ship.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, number_of_seats):
        """Sets the number_of_seats of this Ship.

        Description not available  # noqa: E501

        :param number_of_seats: The number_of_seats of this Ship.  # noqa: E501
        :type: list[int]
        """

        self._number_of_seats = number_of_seats

    @property
    def homeport(self):
        """Gets the homeport of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The homeport of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._homeport

    @homeport.setter
    def homeport(self, homeport):
        """Sets the homeport of this Ship.

        Description not available  # noqa: E501

        :param homeport: The homeport of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._homeport = homeport

    @property
    def model_start_year(self):
        """Gets the model_start_year of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The model_start_year of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_start_year

    @model_start_year.setter
    def model_start_year(self, model_start_year):
        """Sets the model_start_year of this Ship.

        Description not available  # noqa: E501

        :param model_start_year: The model_start_year of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._model_start_year = model_start_year

    @property
    def width(self):
        """Gets the width of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The width of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Ship.

        Description not available  # noqa: E501

        :param width: The width of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._width = width

    @property
    def discharge_average(self):
        """Gets the discharge_average of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The discharge_average of this Ship.  # noqa: E501
        :rtype: list[float]
        """
        return self._discharge_average

    @discharge_average.setter
    def discharge_average(self, discharge_average):
        """Sets the discharge_average of this Ship.

        Description not available  # noqa: E501

        :param discharge_average: The discharge_average of this Ship.  # noqa: E501
        :type: list[float]
        """

        self._discharge_average = discharge_average

    @property
    def number_of_crew(self):
        """Gets the number_of_crew of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_crew of this Ship.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_crew

    @number_of_crew.setter
    def number_of_crew(self, number_of_crew):
        """Sets the number_of_crew of this Ship.

        Description not available  # noqa: E501

        :param number_of_crew: The number_of_crew of this Ship.  # noqa: E501
        :type: list[int]
        """

        self._number_of_crew = number_of_crew

    @property
    def capture_date(self):
        """Gets the capture_date of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The capture_date of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._capture_date

    @capture_date.setter
    def capture_date(self, capture_date):
        """Sets the capture_date of this Ship.

        Description not available  # noqa: E501

        :param capture_date: The capture_date of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._capture_date = capture_date

    @property
    def ship_draft(self):
        """Gets the ship_draft of this Ship.  # noqa: E501

        The draft (or draught) of a ship's hull is the vertical distance between the waterline and the bottom of the hull (keel), with the thickness of the hull included; in the case of not being included the draft outline would be obtained.  # noqa: E501

        :return: The ship_draft of this Ship.  # noqa: E501
        :rtype: list[float]
        """
        return self._ship_draft

    @ship_draft.setter
    def ship_draft(self, ship_draft):
        """Sets the ship_draft of this Ship.

        The draft (or draught) of a ship's hull is the vertical distance between the waterline and the bottom of the hull (keel), with the thickness of the hull included; in the case of not being included the draft outline would be obtained.  # noqa: E501

        :param ship_draft: The ship_draft of this Ship.  # noqa: E501
        :type: list[float]
        """

        self._ship_draft = ship_draft

    @property
    def order_date(self):
        """Gets the order_date of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The order_date of this Ship.  # noqa: E501
        :rtype: list[str]
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this Ship.

        Description not available  # noqa: E501

        :param order_date: The order_date of this Ship.  # noqa: E501
        :type: list[str]
        """

        self._order_date = order_date

    @property
    def related_mean_of_transportation(self):
        """Gets the related_mean_of_transportation of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The related_mean_of_transportation of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._related_mean_of_transportation

    @related_mean_of_transportation.setter
    def related_mean_of_transportation(self, related_mean_of_transportation):
        """Sets the related_mean_of_transportation of this Ship.

        Description not available  # noqa: E501

        :param related_mean_of_transportation: The related_mean_of_transportation of this Ship.  # noqa: E501
        :type: list[object]
        """

        self._related_mean_of_transportation = related_mean_of_transportation

    @property
    def ship_displacement(self):
        """Gets the ship_displacement of this Ship.  # noqa: E501

        A ship's displacement is its mass at any given time.  # noqa: E501

        :return: The ship_displacement of this Ship.  # noqa: E501
        :rtype: list[float]
        """
        return self._ship_displacement

    @ship_displacement.setter
    def ship_displacement(self, ship_displacement):
        """Sets the ship_displacement of this Ship.

        A ship's displacement is its mass at any given time.  # noqa: E501

        :param ship_displacement: The ship_displacement of this Ship.  # noqa: E501
        :type: list[float]
        """

        self._ship_displacement = ship_displacement

    @property
    def power_type(self):
        """Gets the power_type of this Ship.  # noqa: E501

        Description not available  # noqa: E501

        :return: The power_type of this Ship.  # noqa: E501
        :rtype: list[object]
        """
        return self._power_type

    @power_type.setter
    def power_type(self, power_type):
        """Sets the power_type of this Ship.

        Description not available  # noqa: E501

        :param power_type: The power_type of this Ship.  # noqa: E501
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
        if not isinstance(other, Ship):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Ship):
            return True

        return self.to_dict() != other.to_dict()
