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
from dbpedia.models.archipelago import Archipelago  # noqa: E501
from dbpedia.rest import ApiException

class TestArchipelago(unittest.TestCase):
    """Archipelago unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Archipelago
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.archipelago.Archipelago()  # noqa: E501
        if include_optional :
            return Archipelago(
                city_type = [
                    '0'
                    ], 
                irish_name = [
                    '0'
                    ], 
                reff_bourgmestre = [
                    None
                    ], 
                community_iso_code = [
                    '0'
                    ], 
                anthem = [
                    None
                    ], 
                rank_agreement = [
                    56
                    ], 
                wilaya = [
                    None
                    ], 
                parliament = [
                    None
                    ], 
                moldavian_name = [
                    '0'
                    ], 
                rank_population = [
                    56
                    ], 
                quote = [
                    '0'
                    ], 
                commissioner_date = [
                    '0'
                    ], 
                demographics_as_of = [
                    '0'
                    ], 
                largest_settlement = [
                    None
                    ], 
                distance_to_london = [
                    1.337
                    ], 
                geoloc_dual = [
                    '0'
                    ], 
                distance_to_capital = [
                    1.337
                    ], 
                subregion = [
                    None
                    ], 
                sharing_out_area = [
                    '0'
                    ], 
                phone_prefix_name = [
                    '0'
                    ], 
                time_zone = [
                    None
                    ], 
                gross_domestic_product_as_of = [
                    '0'
                    ], 
                population = [
                    None
                    ], 
                senior = [
                    '0'
                    ], 
                human_development_index_rank = [
                    '0'
                    ], 
                population_rural = [
                    56
                    ], 
                gaelic_name = [
                    '0'
                    ], 
                area_total_ranking = [
                    56
                    ], 
                route = [
                    '0'
                    ], 
                leader_name = [
                    None
                    ], 
                principal_area = [
                    None
                    ], 
                plant = [
                    None
                    ], 
                green_long_distance_piste_number = [
                    56
                    ], 
                cannon_number = [
                    56
                    ], 
                purchasing_power_parity = [
                    '0'
                    ], 
                grid_reference = [
                    '0'
                    ], 
                barangays = [
                    '0'
                    ], 
                bioclimate = [
                    '0'
                    ], 
                dissolution_year = [
                    '0'
                    ], 
                patron_saint = [
                    None
                    ], 
                apskritis = [
                    '0'
                    ], 
                area_of_catchment_quote = [
                    '0'
                    ], 
                sea = [
                    None
                    ], 
                life_expectancy = [
                    '0'
                    ], 
                tamazight_name = [
                    '0'
                    ], 
                ski_lift = [
                    56
                    ], 
                insee_code = [
                    56
                    ], 
                governorate = [
                    '0'
                    ], 
                region_link = [
                    '0'
                    ], 
                vice_leader_party = [
                    None
                    ], 
                political_seats = [
                    56
                    ], 
                artificial_snow_area = [
                    1.337
                    ], 
                located_in_area = [
                    None
                    ], 
                saint = [
                    None
                    ], 
                gnl = [
                    '0'
                    ], 
                licence_number = [
                    '0'
                    ], 
                map_description = [
                    '0'
                    ], 
                infant_mortality = [
                    1.337
                    ], 
                area_metro = [
                    None
                    ], 
                number_of_cantons = [
                    56
                    ], 
                information_name = [
                    '0'
                    ], 
                information = [
                    '0'
                    ], 
                river = [
                    None
                    ], 
                ethnic_group = [
                    None
                    ], 
                heritage_register = [
                    None
                    ], 
                subdivisions = [
                    56
                    ], 
                refcul = [
                    '0'
                    ], 
                italian_name = [
                    '0'
                    ], 
                dissolution_date = [
                    '0'
                    ], 
                ist = [
                    '0'
                    ], 
                geoloc_department = [
                    None
                    ], 
                borough = [
                    None
                    ], 
                official_name = [
                    '0'
                    ], 
                maximum_elevation = [
                    1.337
                    ], 
                colonial_name = [
                    '0'
                    ], 
                named_by_language = [
                    None
                    ], 
                volume_quote = [
                    '0'
                    ], 
                province_link = [
                    None
                    ], 
                parish = [
                    None
                    ], 
                old_name = [
                    '0'
                    ], 
                bird = [
                    None
                    ], 
                president_general_council_mandate = [
                    '0'
                    ], 
                regional_prefecture = [
                    '0'
                    ], 
                term_of_office = [
                    '0'
                    ], 
                code_settlement = [
                    '0'
                    ], 
                winter_temperature = [
                    1.337
                    ], 
                commissioner = [
                    '0'
                    ], 
                refpol = [
                    '0'
                    ], 
                number_of_counties = [
                    56
                    ], 
                area = [
                    None
                    ], 
                population_quote = [
                    '0'
                    ], 
                biggest_city = [
                    None
                    ], 
                nis_code = [
                    None
                    ], 
                other_information = [
                    '0'
                    ], 
                area_code = [
                    '0'
                    ], 
                average_depth_quote = [
                    '0'
                    ], 
                geologic_period = [
                    '0'
                    ], 
                coast_line = [
                    1.337
                    ], 
                unitary_authority = [
                    None
                    ], 
                area_land = [
                    1.337
                    ], 
                population_metro_density = [
                    None
                    ], 
                previous_population = [
                    None
                    ], 
                iso_code_region = [
                    None
                    ], 
                gini_coefficient = [
                    1.337
                    ], 
                neighbour_region = [
                    '0'
                    ], 
                event_date = [
                    '0'
                    ], 
                income = [
                    '0'
                    ], 
                touristic_site = [
                    None
                    ], 
                next_entity = [
                    None
                    ], 
                political_majority = [
                    None
                    ], 
                area_quote = [
                    '0'
                    ], 
                ski_tow = [
                    56
                    ], 
                international_phone_prefix = [
                    '0'
                    ], 
                largest_metro = [
                    None
                    ], 
                gagaouze = [
                    '0'
                    ], 
                label = [
                    '0'
                    ], 
                iso_code = [
                    '0'
                    ], 
                finnish_name = [
                    '0'
                    ], 
                width_quote = [
                    '0'
                    ], 
                agglomeration_population_year = [
                    '0'
                    ], 
                daylight_saving_time_zone = [
                    None
                    ], 
                long_distance_piste_number = [
                    56
                    ], 
                political_leader = [
                    None
                    ], 
                same_name = [
                    '0'
                    ], 
                agglomeration = [
                    None
                    ], 
                red_long_distance_piste_number = [
                    56
                    ], 
                area_water = [
                    1.337
                    ], 
                output = [
                    1.337
                    ], 
                previous_demographics = [
                    None
                    ], 
                region_type = [
                    '0'
                    ], 
                police_name = [
                    '0'
                    ], 
                neighboring_municipality = [
                    None
                    ], 
                population_pct_children = [
                    56
                    ], 
                id = '0', 
                distance_to_charing_cross = [
                    1.337
                    ], 
                lieutenancy = [
                    '0'
                    ], 
                delegate_mayor = [
                    None
                    ], 
                minimum_elevation = [
                    1.337
                    ], 
                number_of_capital_deputies = [
                    56
                    ], 
                ceremonial_county = [
                    None
                    ], 
                scotish_name = [
                    '0'
                    ], 
                watercourse = [
                    '0'
                    ], 
                metropolitan_borough = [
                    None
                    ], 
                coast_length = [
                    1.337
                    ], 
                joint_community = [
                    None
                    ], 
                ekatte_code = [
                    '0'
                    ], 
                per_capita_income = [
                    1.337
                    ], 
                settlement = [
                    None
                    ], 
                sharing_out_population_year = [
                    '0'
                    ], 
                foundation_date = [
                    '0'
                    ], 
                maximum_depth = [
                    1.337
                    ], 
                teryt_code = [
                    None
                    ], 
                smallest_country = [
                    None
                    ], 
                algerian_name = [
                    '0'
                    ], 
                map = [
                    None
                    ], 
                localization_thumbnail_caption = [
                    '0'
                    ], 
                unlc_code = [
                    '0'
                    ], 
                sicilian_name = [
                    '0'
                    ], 
                department_position = [
                    '0'
                    ], 
                population_pct_men = [
                    56
                    ], 
                law_country = [
                    '0'
                    ], 
                major_volcano = [
                    None
                    ], 
                summer_temperature = [
                    1.337
                    ], 
                area_date = [
                    '0'
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
                tamazight_settlement_name = [
                    '0'
                    ], 
                okato_code = [
                    '0'
                    ], 
                disappearance_date = [
                    '0'
                    ], 
                population_urban_density = [
                    None
                    ], 
                largest_country = [
                    None
                    ], 
                phone_prefix = [
                    56
                    ], 
                capital = [
                    None
                    ], 
                status_year = [
                    '0'
                    ], 
                flora = [
                    '0'
                    ], 
                agglomeration_area = [
                    None
                    ], 
                cornish_name = [
                    '0'
                    ], 
                largest_city = [
                    None
                    ], 
                licence_number_label = [
                    '0'
                    ], 
                limit = [
                    '0'
                    ], 
                scots_name = [
                    '0'
                    ], 
                refgeo = [
                    '0'
                    ], 
                refgen = [
                    '0'
                    ], 
                population_as_of = [
                    '0'
                    ], 
                different = [
                    '0'
                    ], 
                emblem = [
                    '0'
                    ], 
                representative = [
                    56
                    ], 
                maximum_area_quote = [
                    '0'
                    ], 
                utc_offset = [
                    '0'
                    ], 
                pluviometry = [
                    '0'
                    ], 
                german_name = [
                    '0'
                    ], 
                per_capita_income_rank = [
                    '0'
                    ], 
                ski_piste_kilometre = [
                    1.337
                    ], 
                distance_to_edinburgh = [
                    1.337
                    ], 
                minimum_area = [
                    '0'
                    ], 
                municipality_code = [
                    '0'
                    ], 
                population_rural_density = [
                    1.337
                    ], 
                kabyle_name = [
                    '0'
                    ], 
                red_ski_piste_number = [
                    56
                    ], 
                other_name = [
                    '0'
                    ], 
                welsh_name = [
                    '0'
                    ], 
                lake = [
                    None
                    ], 
                collectivity_minority = [
                    None
                    ], 
                regional_language = [
                    None
                    ], 
                chaoui_name = [
                    '0'
                    ], 
                english_name = [
                    '0'
                    ], 
                county_seat = [
                    None
                    ], 
                purchasing_power_parity_year = [
                    '0'
                    ], 
                lieutenancy_area = [
                    None
                    ], 
                historical_map = [
                    '0'
                    ], 
                people_name = [
                    '0'
                    ], 
                regency = [
                    None
                    ], 
                code_municipal_monument = [
                    '0'
                    ], 
                purchasing_power_parity_rank = [
                    '0'
                    ], 
                depth_quote = [
                    '0'
                    ], 
                avifauna_population = [
                    '0'
                    ], 
                land = [
                    None
                    ], 
                sharing_out = [
                    '0'
                    ], 
                department = [
                    None
                    ], 
                other_language = [
                    '0'
                    ], 
                ofs_code = [
                    '0'
                    ], 
                elevation = [
                    1.337
                    ], 
                endangered_since = [
                    '0'
                    ], 
                rank_area = [
                    56
                    ], 
                prov_code = [
                    '0'
                    ], 
                merger_date = [
                    '0'
                    ], 
                seniunija = [
                    '0'
                    ], 
                city_since = [
                    '0'
                    ], 
                nuts_code = [
                    '0'
                    ], 
                authority_mandate = [
                    '0'
                    ], 
                gnis_code = [
                    '0'
                    ], 
                deme = [
                    '0'
                    ], 
                maximum_depth_quote = [
                    '0'
                    ], 
                canton = [
                    None
                    ], 
                province_iso_code = [
                    '0'
                    ], 
                human_development_index_ranking_category = [
                    None
                    ], 
                nation = [
                    '0'
                    ], 
                arrondissement = [
                    None
                    ], 
                french_name = [
                    '0'
                    ], 
                supply = [
                    None
                    ], 
                agglomeration_population = [
                    None
                    ], 
                green_ski_piste_number = [
                    56
                    ], 
                province = [
                    None
                    ], 
                meaning = [
                    '0'
                    ], 
                leader_party = [
                    None
                    ], 
                population_total_ranking = [
                    56
                    ], 
                twin_city = [
                    None
                    ], 
                sharing_out_population = [
                    56
                    ], 
                piscicultural_population = [
                    '0'
                    ], 
                distance_to_dublin = [
                    1.337
                    ], 
                sharing_out_name = [
                    None
                    ], 
                land_percentage = [
                    1.337
                    ], 
                population_year = [
                    '0'
                    ], 
                administrative_collectivity = [
                    None
                    ], 
                per_capita_income_as_of = [
                    '0'
                    ], 
                circle = [
                    '0'
                    ], 
                occitan_name = [
                    '0'
                    ], 
                blue_long_distance_piste_number = [
                    56
                    ], 
                algerian_settlement_name = [
                    '0'
                    ], 
                gross_domestic_product_purchasing_power_parity_per_capita = [
                    None
                    ], 
                date_agreement = [
                    '0'
                    ], 
                frazioni = [
                    None
                    ], 
                mayor_article = [
                    '0'
                    ], 
                iso31661_code = [
                    '0'
                    ], 
                simc_code = [
                    None
                    ], 
                council_area = [
                    None
                    ], 
                unesco = [
                    None
                    ], 
                gross_domestic_product = [
                    None
                    ], 
                gross_domestic_product_rank = [
                    '0'
                    ], 
                distance_to_douglas = [
                    1.337
                    ], 
                number_of_municipalities = [
                    56
                    ], 
                coordinates = [
                    '0'
                    ], 
                gini_coefficient_ranking = [
                    56
                    ], 
                highest_point = [
                    None
                    ], 
                flower = [
                    None
                    ], 
                hra_state = [
                    '0'
                    ], 
                major_lake = [
                    None
                    ], 
                depths = [
                    None
                    ], 
                cca_state = [
                    '0'
                    ], 
                politic_government_department = [
                    None
                    ], 
                currency_code = [
                    '0'
                    ], 
                tu = [
                    '0'
                    ], 
                population_metro = [
                    56
                    ], 
                climb_up_number = [
                    56
                    ], 
                founding_person = [
                    None
                    ], 
                postal_code = [
                    '0'
                    ], 
                land_area = [
                    1.337
                    ], 
                code_national_monument = [
                    '0'
                    ], 
                president_regional_council_mandate = [
                    '0'
                    ], 
                retention_time = [
                    '0'
                    ], 
                gini_coefficient_category = [
                    None
                    ], 
                sardinian_name = [
                    '0'
                    ], 
                forester_district = [
                    None
                    ], 
                illiteracy = [
                    1.337
                    ], 
                gross_domestic_product_per_people = [
                    '0'
                    ], 
                kind_of_rock = [
                    '0'
                    ], 
                arberisht_name = [
                    '0'
                    ], 
                manx_name = [
                    '0'
                    ], 
                protection_status = [
                    '0'
                    ], 
                fips_code = [
                    '0'
                    ], 
                greek_name = [
                    '0'
                    ], 
                population_density = [
                    None
                    ], 
                elevation_quote = [
                    '0'
                    ], 
                outskirts = [
                    '0'
                    ], 
                area_urban = [
                    None
                    ], 
                unlo_code = [
                    '0'
                    ], 
                district = [
                    None
                    ], 
                merged_settlement = [
                    None
                    ], 
                parliament_type = [
                    '0'
                    ], 
                previous_entity = [
                    None
                    ], 
                federal_state = [
                    None
                    ], 
                maximum_area = [
                    '0'
                    ], 
                population_urban = [
                    56
                    ], 
                scottish_name = [
                    '0'
                    ], 
                sovereign_country = [
                    None
                    ], 
                phone_prefix_label = [
                    '0'
                    ], 
                official_language = [
                    None
                    ], 
                previous_population_total = [
                    56
                    ], 
                commune = [
                    None
                    ], 
                annual_temperature = [
                    1.337
                    ], 
                description = [
                    '0'
                    ], 
                number_of_state_deputies = [
                    56
                    ], 
                average_depth = [
                    '0'
                    ], 
                arabic_name = [
                    '0'
                    ], 
                ski_piste_number = [
                    56
                    ], 
                subdivision = [
                    None
                    ], 
                human_development_index = [
                    None
                    ], 
                alemmanic_name = [
                    '0'
                    ], 
                human_development_index_as_of = [
                    '0'
                    ], 
                capital_coordinates = [
                    '0'
                    ], 
                touareg_name = [
                    '0'
                    ], 
                administrative_head_city = [
                    None
                    ], 
                kanji_name = [
                    '0'
                    ], 
                blue_ski_piste_number = [
                    56
                    ], 
                historical_name = [
                    '0'
                    ], 
                area_rank = [
                    '0'
                    ], 
                first_mention = [
                    '0'
                    ], 
                localization_thumbnail = [
                    None
                    ], 
                cable_car = [
                    56
                    ], 
                administrative_district = [
                    None
                    ], 
                type = [
                    '0'
                    ], 
                linked_space = [
                    '0'
                    ], 
                lowest_point = [
                    None
                    ], 
                daira = [
                    None
                    ], 
                number_of_island = [
                    '0'
                    ], 
                cyrillique_name = [
                    '0'
                    ], 
                catholic_percentage = [
                    '0'
                    ], 
                old_district = [
                    None
                    ], 
                area_rural = [
                    1.337
                    ], 
                water_percentage = [
                    1.337
                    ], 
                lowest = [
                    '0'
                    ], 
                sharing_out_population_name = [
                    '0'
                    ], 
                number_of_federal_deputies = [
                    56
                    ], 
                map_caption = [
                    '0'
                    ], 
                previous_name = [
                    '0'
                    ], 
                city_link = [
                    '0'
                    ], 
                leader_title = [
                    '0'
                    ], 
                foundation = [
                    '0'
                    ], 
                agglomeration_demographics = [
                    None
                    ], 
                calabrian_name = [
                    '0'
                    ], 
                type_coordinate = [
                    '0'
                    ], 
                touareg_settlement_name = [
                    '0'
                    ], 
                distance_to_belfast = [
                    1.337
                    ], 
                code_provincial_monument = [
                    '0'
                    ], 
                climate = [
                    None
                    ], 
                bourgmestre = [
                    None
                    ], 
                depth = [
                    1.337
                    ], 
                governing_body = [
                    None
                    ], 
                black_ski_piste_number = [
                    56
                    ], 
                protestant_percentage = [
                    '0'
                    ], 
                related_places = [
                    None
                    ], 
                zip_code = [
                    '0'
                    ], 
                fauna = [
                    '0'
                    ], 
                year_of_construction = [
                    '0'
                    ], 
                subsystem = [
                    '0'
                    ], 
                historical_region = [
                    '0'
                    ], 
                international_phone_prefix_label = [
                    '0'
                    ], 
                minority = [
                    None
                    ], 
                frioulan_name = [
                    '0'
                    ], 
                reference = [
                    '0'
                    ], 
                code_land_registry = [
                    '0'
                    ], 
                distance_to_cardiff = [
                    1.337
                    ], 
                population_date = [
                    '0'
                    ], 
                dutch_name = [
                    '0'
                    ], 
                day = [
                    '0'
                    ], 
                sheading = [
                    None
                    ], 
                local_phone_prefix = [
                    56
                    ], 
                population_pct_women = [
                    56
                    ], 
                tree = [
                    None
                    ], 
                old_province = [
                    None
                    ], 
                vehicle_code = [
                    '0'
                    ], 
                water = [
                    '0'
                    ], 
                gross_domestic_product_nominal_per_capita = [
                    None
                    ], 
                association_of_local_government = [
                    None
                    ], 
                topic = [
                    '0'
                    ], 
                main_island = [
                    None
                    ], 
                maori_name = [
                    '0'
                    ], 
                istat = [
                    '0'
                    ], 
                minimum_area_quote = [
                    '0'
                    ], 
                altitude = [
                    None
                    ], 
                national_topographic_system_map_number = [
                    '0'
                    ], 
                budget_year = [
                    '0'
                    ], 
                gini_coefficient_as_of = [
                    '0'
                    ], 
                scale = [
                    '0'
                    ], 
                long_distance_piste_kilometre = [
                    1.337
                    ], 
                sub_prefecture = [
                    '0'
                    ], 
                snow_park_number = [
                    56
                    ], 
                luxembourgish_name = [
                    '0'
                    ], 
                area_total = [
                    None
                    ], 
                population_total_reference = [
                    None
                    ], 
                length_quote = [
                    '0'
                    ], 
                relief = [
                    '0'
                    ], 
                census_year = [
                    '0'
                    ], 
                ladin_name = [
                    '0'
                    ], 
                subdivision_link = [
                    '0'
                    ], 
                mozabite_name = [
                    '0'
                    ], 
                nearest_city = [
                    None
                    ], 
                subsystem_link = [
                    '0'
                    ], 
                whole_area = [
                    None
                    ], 
                delegation = [
                    '0'
                    ], 
                vice_leader = [
                    None
                    ], 
                demographics = [
                    None
                    ]
            )
        else :
            return Archipelago(
        )

    def testArchipelago(self):
        """Test Archipelago"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
