import json

from model.player import Player
from model.tournament import Tournament
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
        tournament = self.tournament_controller.build_rounds(tournament)
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

    # TODO: Create the logic to a new turn
    @staticmethod
    def execute_new_round():
        print("Method to execute new turn")
