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
from dbpedia.models.figure_skater import FigureSkater  # noqa: E501
from dbpedia.rest import ApiException

class TestFigureSkater(unittest.TestCase):
    """FigureSkater unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FigureSkater
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dbpedia.models.figure_skater.FigureSkater()  # noqa: E501
        if include_optional :
            return FigureSkater(
                parent = [
                    None
                    ], 
                viaf_id = [
                    '0'
                    ], 
                competition_title = [
                    None
                    ], 
                art_patron = [
                    None
                    ], 
                hair_colour = [
                    '0'
                    ], 
                tv_show = [
                    None
                    ], 
                sport_country = [
                    None
                    ], 
                expedition = [
                    '0'
                    ], 
                main_domain = [
                    None
                    ], 
                nndb_id = [
                    '0'
                    ], 
                discipline = [
                    None
                    ], 
                consecration = [
                    '0'
                    ], 
                salary = [
                    1.337
                    ], 
                birth_name = [
                    '0'
                    ], 
                spouse = [
                    None
                    ], 
                scene = [
                    '0'
                    ], 
                best_lap = [
                    '0'
                    ], 
                junior_team = [
                    None
                    ], 
                shoe_number = [
                    56
                    ], 
                world_open = [
                    '0'
                    ], 
                european_championship = [
                    '0'
                    ], 
                friend = [
                    None
                    ], 
                world_champion_title_year = [
                    '0'
                    ], 
                full_score = [
                    '0'
                    ], 
                diploma = [
                    None
                    ], 
                active_years_end_year_mgr = [
                    '0'
                    ], 
                abbeychurch_blessing = [
                    '0'
                    ], 
                selection_year = [
                    '0'
                    ], 
                height = [
                    None
                    ], 
                wins = [
                    56
                    ], 
                usopen_wins = [
                    None
                    ], 
                bust_size = [
                    1.337
                    ], 
                cloth_size = [
                    '0'
                    ], 
                handedness = [
                    None
                    ], 
                nfl_season = [
                    '0'
                    ], 
                philosophical_school = [
                    None
                    ], 
                parliamentary_group = [
                    '0'
                    ], 
                date_of_burial = [
                    '0'
                    ], 
                mount = [
                    '0'
                    ], 
                davis_cup = [
                    '0'
                    ], 
                olympic_games_silver = [
                    56
                    ], 
                nationality = [
                    None
                    ], 
                debut_team = [
                    None
                    ], 
                hof = [
                    '0'
                    ], 
                junior_years_start_year = [
                    '0'
                    ], 
                relative = [
                    None
                    ], 
                draft_league = [
                    '0'
                    ], 
                newspaper = [
                    None
                    ], 
                announced_from = [
                    None
                    ], 
                australia_open_mixed = [
                    '0'
                    ], 
                gold_medal_double = [
                    '0'
                    ], 
                military_branch = [
                    None
                    ], 
                activity = [
                    None
                    ], 
                ethnicity = [
                    None
                    ], 
                state_of_origin = [
                    None
                    ], 
                pole_position = [
                    56
                    ], 
                season_manager = [
                    '0'
                    ], 
                killed_by = [
                    '0'
                    ], 
                blood_type = [
                    None
                    ], 
                laterality = [
                    '0'
                    ], 
                draft_position = [
                    56
                    ], 
                continental_tournament = [
                    None
                    ], 
                junior_years_end_year = [
                    '0'
                    ], 
                ithf_date = [
                    '0'
                    ], 
                political_function = [
                    '0'
                    ], 
                honours = [
                    None
                    ], 
                olympic_games = [
                    None
                    ], 
                hair_color = [
                    None
                    ], 
                ncaa_team = [
                    None
                    ], 
                foot = [
                    '0'
                    ], 
                measurements = [
                    '0'
                    ], 
                hand = [
                    None
                    ], 
                federation = [
                    None
                    ], 
                circumcised = [
                    '0'
                    ], 
                sport_specialty = [
                    None
                    ], 
                penis_length = [
                    '0'
                    ], 
                coemperor = [
                    None
                    ], 
                roland_garros_mixed = [
                    '0'
                    ], 
                detractor = [
                    None
                    ], 
                selibr_id = [
                    '0'
                    ], 
                danse_competition = [
                    '0'
                    ], 
                sex = [
                    '0'
                    ], 
                former_team = [
                    None
                    ], 
                sexual_orientation = [
                    None
                    ], 
                partner = [
                    None
                    ], 
                birth_year = [
                    '0'
                    ], 
                sports_function = [
                    '0'
                    ], 
                orcid_id = [
                    '0'
                    ], 
                election_date = [
                    '0'
                    ], 
                sport_discipline = [
                    None
                    ], 
                collaboration = [
                    None
                    ], 
                national_team_year = [
                    '0'
                    ], 
                number_of_run = [
                    56
                    ], 
                spouse_name = [
                    '0'
                    ], 
                roland_garros_double = [
                    '0'
                    ], 
                lah_hof = [
                    '0'
                    ], 
                derived_word = [
                    '0'
                    ], 
                current_team_manager = [
                    None
                    ], 
                little_pool_record = [
                    '0'
                    ], 
                bpn_id = [
                    '0'
                    ], 
                free_danse_score = [
                    '0'
                    ], 
                ncbhof = [
                    '0'
                    ], 
                supplemental_draft_round = [
                    '0'
                    ], 
                project = [
                    None
                    ], 
                active_years = [
                    None
                    ], 
                title_date = [
                    '0'
                    ], 
                blood_group = [
                    '0'
                    ], 
                final_lost = [
                    56
                    ], 
                school = [
                    None
                    ], 
                death_place = [
                    None
                    ], 
                bronze_medal_mixed = [
                    '0'
                    ], 
                silver_medal_single = [
                    '0'
                    ], 
                victory_percentage_as_mgr = [
                    1.337
                    ], 
                club = [
                    None
                    ], 
                imposed_danse_competition = [
                    '0'
                    ], 
                shoot = [
                    '0'
                    ], 
                education_place = [
                    None
                    ], 
                qatar_classic = [
                    '0'
                    ], 
                match_point = [
                    '0'
                    ], 
                reign_name = [
                    '0'
                    ], 
                pro_period = [
                    '0'
                    ], 
                influenced_by = [
                    None
                    ], 
                nla_id = [
                    '0'
                    ], 
                current_team = [
                    None
                    ], 
                cousurper = [
                    None
                    ], 
                race_wins = [
                    56
                    ], 
                world_tournament_bronze = [
                    56
                    ], 
                bronze_medal_single = [
                    '0'
                    ], 
                jutsu = [
                    '0'
                    ], 
                weight = [
                    None
                    ], 
                national_team = [
                    None
                    ], 
                other_media = [
                    None
                    ], 
                alma_mater = [
                    None
                    ], 
                imposed_danse_score = [
                    '0'
                    ], 
                final_lost_single = [
                    '0'
                    ], 
                known_for = [
                    None
                    ], 
                big_pool_record = [
                    '0'
                    ], 
                title_double = [
                    '0'
                    ], 
                olympic_games_wins = [
                    '0'
                    ], 
                eye_colour = [
                    '0'
                    ], 
                world_tournament_silver = [
                    56
                    ], 
                australia_open_double = [
                    '0'
                    ], 
                hopman_cup = [
                    '0'
                    ], 
                architectural_movement = [
                    '0'
                    ], 
                mood = [
                    '0'
                    ], 
                bibsys_id = [
                    '0'
                    ], 
                iihf_hof = [
                    '0'
                    ], 
                fibahof = [
                    '0'
                    ], 
                free_prog_score = [
                    '0'
                    ], 
                description = [
                    '0'
                    ], 
                heisman = [
                    '0'
                    ], 
                nfl_code = [
                    '0'
                    ], 
                particular_sign = [
                    '0'
                    ], 
                us_open_mixed = [
                    '0'
                    ], 
                league_manager = [
                    None
                    ], 
                junior_season = [
                    None
                    ], 
                free_prog_competition = [
                    '0'
                    ], 
                weapon = [
                    None
                    ], 
                kind_of_criminal = [
                    '0'
                    ], 
                notable_idea = [
                    None
                    ], 
                trainer = [
                    None
                    ], 
                state_of_origin_year = [
                    '0'
                    ], 
                player_status = [
                    '0'
                    ], 
                other_function = [
                    None
                    ], 
                continental_tournament_silver = [
                    56
                    ], 
                career_station = [
                    None
                    ], 
                resting_place_position = [
                    None
                    ], 
                original_danse_competition = [
                    '0'
                    ], 
                status_manager = [
                    '0'
                    ], 
                national_tournament = [
                    None
                    ], 
                hometown = [
                    None
                    ], 
                dead_in_fight_place = [
                    '0'
                    ], 
                continental_tournament_bronze = [
                    56
                    ], 
                final_lost_double = [
                    '0'
                    ], 
                victory = [
                    56
                    ], 
                complexion = [
                    None
                    ], 
                citizenship = [
                    None
                    ], 
                start = [
                    56
                    ], 
                british_open = [
                    '0'
                    ], 
                tessitura = [
                    '0'
                    ], 
                start_career = [
                    '0'
                    ], 
                label = [
                    '0'
                    ], 
                birth_date = [
                    '0'
                    ], 
                bronze_medal_double = [
                    '0'
                    ], 
                national_tournament_silver = [
                    56
                    ], 
                other_activity = [
                    '0'
                    ], 
                linguistics_tradition = [
                    None
                    ], 
                national_tournament_bronze = [
                    56
                    ], 
                escalafon = [
                    '0'
                    ], 
                sibling = [
                    None
                    ], 
                title_single = [
                    '0'
                    ], 
                waist_size = [
                    1.337
                    ], 
                olympic_games_gold = [
                    56
                    ], 
                current_partner = [
                    None
                    ], 
                general_council = [
                    None
                    ], 
                australia_open_single = [
                    '0'
                    ], 
                arrest_date = [
                    '0'
                    ], 
                team_manager = [
                    None
                    ], 
                birth_sign = [
                    None
                    ], 
                artistic_function = [
                    '0'
                    ], 
                age = [
                    56
                    ], 
                college = [
                    None
                    ], 
                education = [
                    None
                    ], 
                movie = [
                    None
                    ], 
                team_coached = [
                    None
                    ], 
                achievement = [
                    None
                    ], 
                death_age = [
                    56
                    ], 
                selection_point = [
                    56
                    ], 
                type = [
                    '0'
                    ], 
                approach = [
                    None
                    ], 
                relation = [
                    None
                    ], 
                height_attack = [
                    '0'
                    ], 
                victory_as_mgr = [
                    56
                    ], 
                living_place = [
                    None
                    ], 
                copilote = [
                    None
                    ], 
                season = [
                    None
                    ], 
                start_wct = [
                    '0'
                    ], 
                world_team_cup = [
                    '0'
                    ], 
                catch = [
                    '0'
                    ], 
                id = '0', 
                team_title = [
                    '0'
                    ], 
                feat = [
                    '0'
                    ], 
                decoration = [
                    None
                    ], 
                case = [
                    '0'
                    ], 
                sentence = [
                    '0'
                    ], 
                profession = [
                    None
                    ], 
                roland_garros_single = [
                    '0'
                    ], 
                retirement_date = [
                    '0'
                    ], 
                state_of_origin_team = [
                    None
                    ], 
                nfl_team = [
                    None
                    ], 
                world_tournament = [
                    None
                    ], 
                wife = [
                    None
                    ], 
                allegiance = [
                    '0'
                    ], 
                ncaa_season = [
                    '0'
                    ], 
                old_team_coached = [
                    None
                    ], 
                coach_season = [
                    '0'
                    ], 
                active_years_start_date_mgr = [
                    '0'
                    ], 
                lccn_id = [
                    '0'
                    ], 
                tattoo = [
                    '0'
                    ], 
                british_wins = [
                    None
                    ], 
                gold_medal_single = [
                    '0'
                    ], 
                hip_size = [
                    1.337
                    ], 
                podium = [
                    56
                    ], 
                seiyu = [
                    None
                    ], 
                state_of_origin_point = [
                    56
                    ], 
                player_season = [
                    None
                    ], 
                former_coach = [
                    None
                    ], 
                short_prog_score = [
                    '0'
                    ], 
                regional_council = [
                    None
                    ], 
                homage = [
                    '0'
                    ], 
                shoe_size = [
                    '0'
                    ], 
                national_championship = [
                    '0'
                    ], 
                signature = [
                    '0'
                    ], 
                olympic_games_bronze = [
                    56
                    ], 
                draft_team = [
                    None
                    ], 
                first_pro_match = [
                    '0'
                    ], 
                final_lost_team = [
                    '0'
                    ], 
                danse_score = [
                    '0'
                    ], 
                id_number = [
                    56
                    ], 
                probowl_pick = [
                    '0'
                    ], 
                short_prog_competition = [
                    '0'
                    ], 
                college_hof = [
                    '0'
                    ], 
                active_years_start_year_mgr = [
                    '0'
                    ], 
                wedding_parents_date = [
                    '0'
                    ], 
                birth_place = [
                    None
                    ], 
                silver_medal_double = [
                    '0'
                    ], 
                world = [
                    None
                    ], 
                astrological_sign = [
                    None
                    ], 
                eye_color = [
                    None
                    ], 
                networth = [
                    1.337
                    ], 
                coalition = [
                    '0'
                    ], 
                silver_medal_mixed = [
                    '0'
                    ], 
                racket_catching = [
                    '0'
                    ], 
                national_team_match_point = [
                    '0'
                    ], 
                us_open_double = [
                    '0'
                    ], 
                national_selection = [
                    None
                    ], 
                agency = [
                    None
                    ], 
                start_wqs = [
                    '0'
                    ], 
                coach_club = [
                    None
                    ], 
                defeat_as_mgr = [
                    56
                    ], 
                death_year = [
                    '0'
                    ], 
                tournament_of_champions = [
                    '0'
                    ], 
                horse_riding_discipline = [
                    None
                    ], 
                world_tournament_gold = [
                    56
                    ], 
                former_choreographer = [
                    None
                    ], 
                pga_wins = [
                    None
                    ], 
                board = [
                    None
                    ], 
                rid_id = [
                    '0'
                    ], 
                asia_championship = [
                    '0'
                    ], 
                dead_in_fight_date = [
                    '0'
                    ], 
                team_point = [
                    56
                    ], 
                former_partner = [
                    None
                    ], 
                espn_id = [
                    56
                    ], 
                choreographer = [
                    None
                    ], 
                related_functions = [
                    None
                    ], 
                manager_season = [
                    None
                    ], 
                reign = [
                    '0'
                    ], 
                wimbledon_double = [
                    '0'
                    ], 
                best_rank_single = [
                    '0'
                    ], 
                second = [
                    56
                    ], 
                radio = [
                    None
                    ], 
                full_competition = [
                    '0'
                    ], 
                gold_medal_mixed = [
                    '0'
                    ], 
                free_score_competition = [
                    '0'
                    ], 
                publication = [
                    '0'
                    ], 
                opponent = [
                    None
                    ], 
                us_open_single = [
                    '0'
                    ], 
                employer = [
                    None
                    ], 
                affair = [
                    '0'
                    ], 
                body_discovered = [
                    None
                    ], 
                buried_place = [
                    None
                    ], 
                cash_price = [
                    '0'
                    ], 
                last_pro_match = [
                    '0'
                    ], 
                residence = [
                    None
                    ], 
                usurper = [
                    None
                    ], 
                other_occupation = [
                    None
                    ], 
                contest = [
                    None
                    ], 
                active_years_end_date_mgr = [
                    '0'
                    ], 
                backhand = [
                    '0'
                    ], 
                created = [
                    None
                    ], 
                original_danse_score = [
                    '0'
                    ], 
                end_career = [
                    '0'
                    ], 
                other_sports_experience = [
                    None
                    ], 
                note_on_resting_place = [
                    '0'
                    ], 
                army = [
                    '0'
                    ], 
                fed_cup = [
                    '0'
                    ], 
                active_year = [
                    '0'
                    ], 
                person_function = [
                    None
                    ], 
                superbowl_win = [
                    '0'
                    ], 
                pro_since = [
                    '0'
                    ], 
                cause_of_death = [
                    '0'
                    ], 
                dubber = [
                    None
                    ], 
                non_professional_career = [
                    '0'
                    ], 
                military_function = [
                    '0'
                    ], 
                patent = [
                    None
                    ], 
                creation_christian_bishop = [
                    '0'
                    ], 
                piercing = [
                    '0'
                    ], 
                student = [
                    None
                    ], 
                bad_guy = [
                    '0'
                    ], 
                influenced = [
                    None
                    ], 
                start_reign = [
                    None
                    ], 
                university = [
                    None
                    ], 
                gym_apparatus = [
                    None
                    ], 
                ideology = [
                    None
                    ], 
                conviction_date = [
                    '0'
                    ], 
                media = [
                    None
                    ], 
                bnf_id = [
                    '0'
                    ], 
                pseudonym = [
                    '0'
                    ], 
                temple_year = [
                    '0'
                    ], 
                clothing_size = [
                    '0'
                    ], 
                speciality = [
                    '0'
                    ], 
                award = [
                    None
                    ], 
                kind_of_criminal_action = [
                    '0'
                    ], 
                isni_id = [
                    '0'
                    ], 
                wimbledon_single = [
                    '0'
                    ], 
                significant_project = [
                    None
                    ], 
                youth_club = [
                    None
                    ], 
                leadership = [
                    '0'
                    ], 
                death_date = [
                    '0'
                    ], 
                special_trial = [
                    56
                    ], 
                resting_date = [
                    '0'
                    ], 
                victim = [
                    '0'
                    ], 
                height_against = [
                    '0'
                    ], 
                has_natural_bust = [
                    '0'
                    ], 
                masters_wins = [
                    None
                    ], 
                individualised_pnd = [
                    56
                    ], 
                current_league = [
                    None
                    ], 
                continental_tournament_gold = [
                    56
                    ], 
                orientation = [
                    '0'
                    ], 
                grave = [
                    '0'
                    ], 
                resting_place = [
                    None
                    ], 
                abbeychurch_blessing_charge = [
                    '0'
                    ], 
                mvp = [
                    '0'
                    ], 
                handisport = [
                    '0'
                    ], 
                best_rank_double = [
                    '0'
                    ], 
                external_ornament = [
                    '0'
                    ], 
                third = [
                    56
                    ], 
                film_number = [
                    56
                    ], 
                wimbledon_mixed = [
                    '0'
                    ], 
                temple = [
                    '0'
                    ], 
                end_reign = [
                    None
                    ], 
                national_tournament_gold = [
                    56
                    ], 
                athletics_discipline = [
                    None
                    ], 
                death_cause = [
                    None
                    ]
            )
        else :
            return FigureSkater(
        )

    def testFigureSkater(self):
        """Test FigureSkater"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
