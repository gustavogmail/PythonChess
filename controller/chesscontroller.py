import json

from model.round import Round
from model.player import Player
from model.tournament import Tournament
from model.match import Match
from controller.player.player_controller import PlayerController
from controller.tournament.tournament_controller import TournamentController
from view.consoleview import ConsoleView


class ChessController:
    def __init__(self):
        self.tournaments = self.read_tournaments_from_database()
        self.view = ConsoleView(self)
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def generate_menu(self):
        self.view.show_main_menu()

    def show_all_players_in_database(self):
        self.player_controller.show_players()

    def show_all_tournaments_in_database(self):
        self.tournament_controller.show_tournaments(self.tournaments)

    def see_specific_tournament(self, tournament_name):
        tournament = self.find_specific_tournament(tournament_name)
        self.tournament_controller.see_specific_tournament(tournament)

    def see_participants_in_tournament(self, tournament_name):
        tournament = self.find_specific_tournament(tournament_name)
        self.view.show_participants(self.player_controller.sort_players_alphabetically(tournament.players))

    def show_tournament_rounds_and_matches(self, tournament_name):
        tournament = self.find_specific_tournament(tournament_name)
        match1 = Match(tournament.players[0].name, 1, tournament.players[1].name, 0)
        match2 = Match(tournament.players[2].name, 1, tournament.players[3].name, 0)
        round1 = Round(name="Round1", start_datetime="2023-06-06")
        round1.add_match(match1)
        round1.add_match(match2)
        round1.mark_as_finished()
        tournament.add_round(round1)
        self.tournament_controller.show_tournament_rounds_and_matches(tournament)

    def find_specific_tournament(self, name):
        for tournament in self.tournaments:
            if tournament.name == name:
                return tournament
        return None

    @staticmethod
    def instantiate_players(players_json) -> list[Player]:
        players = []
        for player in players_json:
            current_player = Player(
                name=player["name"],
                last_name=player["last_name"],
                date_of_birth=player["date_of_birth"],
                national_chess_id=player["national_chess_id"]
            )
            players.append(current_player)

        return players

    def instantiate_rounds(self, rounds_json) -> list[Round]:
        rounds = []
        for single_round in rounds_json:
            matches = self.instantiate_matches(single_round["matches"])
            current_round = Round(
                name=single_round["name"],
                matches=matches,
                start_datetime=single_round["start_datetime"],
                end_datetime=single_round["end_datetime"]
            )
            rounds.append(current_round)

        return rounds

    def read_tournaments_from_database(self) -> list[Tournament]:
        tournaments_on_database = []
        with open("./database/tournament.json", "r") as file:
            data = json.load(file)
            for tournament in data:
                players = self.instantiate_players(tournament["players"])
                current_tournament = Tournament(
                    name=tournament["name"],
                    venue=tournament["venue"],
                    start_date=tournament["start_date"],
                    end_date=tournament["end_date"],
                    current_round=tournament["current_round"],
                    players=players,
                    description=tournament["description"],
                    number_of_rounds=tournament["number_of_rounds"]
                )
                tournaments_on_database.append(current_tournament)

        return tournaments_on_database

    @staticmethod
    def execute_new_round():
        print("Método para executar nova rodada")
