# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import dbpedia
from dbpedia.models.place import Place  # noqa: E501
from dbpedia.rest import ApiException

class TestPlace(unittest.TestCase):
    """Place unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Place
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.place.Place()  # noqa: E501
        if include_optional :
            return Place(
                daylight_saving_time_zone = [
                    None
                    ], 
                long_distance_piste_number = [
                    56
                    ], 
                rank_agreement = [
                    56
                    ], 
                political_leader = [
                    None
                    ], 
                red_long_distance_piste_number = [
                    56
                    ], 
                type = [
                    '0'
                    ], 
                parliament = [
                    None
                    ], 
                linked_space = [
                    '0'
                    ], 
                area_water = [
                    1.337
                    ], 
                supply = [
                    None
                    ], 
                green_ski_piste_number = [
                    56
                    ], 
                output = [
                    1.337
                    ], 
                quote = [
                    '0'
                    ], 
                province = [
                    None
                    ], 
                region_type = [
                    '0'
                    ], 
                number_of_island = [
                    '0'
                    ], 
                id = '0', 
                piscicultural_population = [
                    '0'
                    ], 
                land_percentage = [
                    1.337
                    ], 
                water_percentage = [
                    1.337
                    ], 
                geoloc_dual = [
                    '0'
                    ], 
                subregion = [
                    None
                    ], 
                time_zone = [
                    None
                    ], 
                lowest = [
                    '0'
                    ], 
                minimum_elevation = [
                    1.337
                    ], 
                human_development_index_rank = [
                    '0'
                    ], 
                route = [
                    '0'
                    ], 
                map_caption = [
                    '0'
                    ], 
                plant = [
                    None
                    ], 
                green_long_distance_piste_number = [
                    56
                    ], 
                coast_length = [
                    1.337
                    ], 
                cannon_number = [
                    56
                    ], 
                grid_reference = [
                    '0'
                    ], 
                blue_long_distance_piste_number = [
                    56
                    ], 
                bioclimate = [
                    '0'
                    ], 
                city_link = [
                    '0'
                    ], 
                date_agreement = [
                    '0'
                    ], 
                mayor_article = [
                    '0'
                    ], 
                area_of_catchment_quote = [
                    '0'
                    ], 
                iso31661_code = [
                    '0'
                    ], 
                sea = [
                    None
                    ], 
                settlement = [
                    None
                    ], 
                ski_lift = [
                    56
                    ], 
                maximum_depth = [
                    1.337
                    ], 
                unesco = [
                    None
                    ], 
                gross_domestic_product_rank = [
                    '0'
                    ], 
                region_link = [
                    '0'
                    ], 
                artificial_snow_area = [
                    1.337
                    ], 
                located_in_area = [
                    None
                    ], 
                map = [
                    None
                    ], 
                type_coordinate = [
                    '0'
                    ], 
                code_provincial_monument = [
                    '0'
                    ], 
                coordinates = [
                    '0'
                    ], 
                map_description = [
                    '0'
                    ], 
                climate = [
                    None
                    ], 
                flower = [
                    None
                    ], 
                law_country = [
                    '0'
                    ], 
                area_date = [
                    '0'
                    ], 
                information_name = [
                    '0'
                    ], 
                depth = [
                    1.337
                    ], 
                kind_of_coordinate = [
                    '0'
                    ], 
                black_long_distance_piste_number = [
                    56
                    ], 
                water_area = [
                    1.337
                    ], 
                frontier_length = [
                    1.337
                    ], 
                depths = [
                    None
                    ], 
                information = [
                    '0'
                    ], 
                governing_body = [
                    None
                    ], 
                black_ski_piste_number = [
                    56
                    ], 
                river = [
                    None
                    ], 
                heritage_register = [
                    None
                    ], 
                currency_code = [
                    '0'
                    ], 
                related_places = [
                    None
                    ], 
                subdivisions = [
                    56
                    ], 
                refcul = [
                    '0'
                    ], 
                tu = [
                    '0'
                    ], 
                climb_up_number = [
                    56
                    ], 
                fauna = [
                    '0'
                    ], 
                land_area = [
                    1.337
                    ], 
                code_national_monument = [
                    '0'
                    ], 
                flora = [
                    '0'
                    ], 
                year_of_construction = [
                    '0'
                    ], 
                subsystem = [
                    '0'
                    ], 
                president_regional_council_mandate = [
                    '0'
                    ], 
                retention_time = [
                    '0'
                    ], 
                maximum_elevation = [
                    1.337
                    ], 
                reference = [
                    '0'
                    ], 
                code_land_registry = [
                    '0'
                    ], 
                forester_district = [
                    None
                    ], 
                named_by_language = [
                    None
                    ], 
                volume_quote = [
                    '0'
                    ], 
                population_date = [
                    '0'
                    ], 
                province_link = [
                    None
                    ], 
                gross_domestic_product_per_people = [
                    '0'
                    ], 
                kind_of_rock = [
                    '0'
                    ], 
                bird = [
                    None
                    ], 
                president_general_council_mandate = [
                    '0'
                    ], 
                limit = [
                    '0'
                    ], 
                refgeo = [
                    '0'
                    ], 
                protection_status = [
                    '0'
                    ], 
                regional_prefecture = [
                    '0'
                    ], 
                refgen = [
                    '0'
                    ], 
                different = [
                    '0'
                    ], 
                representative = [
                    56
                    ], 
                refpol = [
                    '0'
                    ], 
                maximum_area_quote = [
                    '0'
                    ], 
                population_quote = [
                    '0'
                    ], 
                utc_offset = [
                    '0'
                    ], 
                per_capita_income_rank = [
                    '0'
                    ], 
                ski_piste_kilometre = [
                    1.337
                    ], 
                biggest_city = [
                    None
                    ], 
                tree = [
                    None
                    ], 
                vehicle_code = [
                    '0'
                    ], 
                minimum_area = [
                    '0'
                    ], 
                municipality_code = [
                    '0'
                    ], 
                water = [
                    '0'
                    ], 
                elevation_quote = [
                    '0'
                    ], 
                average_depth_quote = [
                    '0'
                    ], 
                geologic_period = [
                    '0'
                    ], 
                area_land = [
                    1.337
                    ], 
                red_ski_piste_number = [
                    56
                    ], 
                unlo_code = [
                    '0'
                    ], 
                district = [
                    None
                    ], 
                main_island = [
                    None
                    ], 
                parliament_type = [
                    '0'
                    ], 
                previous_entity = [
                    None
                    ], 
                maximum_area = [
                    '0'
                    ], 
                lake = [
                    None
                    ], 
                neighbour_region = [
                    '0'
                    ], 
                event_date = [
                    '0'
                    ], 
                minimum_area_quote = [
                    '0'
                    ], 
                altitude = [
                    None
                    ], 
                sovereign_country = [
                    None
                    ], 
                national_topographic_system_map_number = [
                    '0'
                    ], 
                budget_year = [
                    '0'
                    ], 
                historical_map = [
                    '0'
                    ], 
                next_entity = [
                    None
                    ], 
                annual_temperature = [
                    1.337
                    ], 
                scale = [
                    '0'
                    ], 
                description = [
                    '0'
                    ], 
                regency = [
                    None
                    ], 
                long_distance_piste_kilometre = [
                    1.337
                    ], 
                code_municipal_monument = [
                    '0'
                    ], 
                average_depth = [
                    '0'
                    ], 
                sub_prefecture = [
                    '0'
                    ], 
                ski_piste_number = [
                    56
                    ], 
                subdivision = [
                    None
                    ], 
                snow_park_number = [
                    56
                    ], 
                depth_quote = [
                    '0'
                    ], 
                area_quote = [
                    '0'
                    ], 
                area_total = [
                    1.337
                    ], 
                avifauna_population = [
                    '0'
                    ], 
                ski_tow = [
                    56
                    ], 
                capital_coordinates = [
                    '0'
                    ], 
                land = [
                    None
                    ], 
                length_quote = [
                    '0'
                    ], 
                relief = [
                    '0'
                    ], 
                elevation = [
                    1.337
                    ], 
                endangered_since = [
                    '0'
                    ], 
                subdivision_link = [
                    '0'
                    ], 
                merger_date = [
                    '0'
                    ], 
                blue_ski_piste_number = [
                    56
                    ], 
                label = [
                    '0'
                    ], 
                historical_name = [
                    '0'
                    ], 
                nearest_city = [
                    None
                    ], 
                subsystem_link = [
                    '0'
                    ], 
                nuts_code = [
                    '0'
                    ], 
                authority_mandate = [
                    '0'
                    ], 
                whole_area = [
                    None
                    ], 
                iso_code = [
                    '0'
                    ], 
                area_rank = [
                    '0'
                    ], 
                width_quote = [
                    '0'
                    ], 
                maximum_depth_quote = [
                    '0'
                    ], 
                cable_car = [
                    56
                    ]
            )
        else :
            return Place(
        )

    def testPlace(self):
        """Test Place"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
