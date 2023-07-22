import json
from model.player import Player
from model.tournament import Tournament
from view.consoleview import ConsoleView


class ChessController:
    def __init__(self):
        self.players = []
        self.tournaments = []
        self.view = ConsoleView(self)

    def show_players(self):
        self.read_players_from_database()
        self.view.show_players(self.players)

    def show_tournaments(self):
        self.read_tournaments_from_database()
        self.view.show_tournaments(self.tournaments)

    def generate_menu(self):
        self.view.show_main_menu()

    @staticmethod
    def execute_new_round():
        print("Método para executar nova rodada")

    def read_players_from_database(self):
        with open("./database/players.json", "r") as file:
            data = json.load(file)

            for player in data:
                current_player = Player(player["name"])
                self.players.append(current_player)

    def read_tournaments_from_database(self):
        with open("./database/tournament.json", "r") as file:
            data = json.load(file)

            for tournament in data:
                current_tournament = Tournament(tournament["name"])
                self.tournaments.append(current_tournament)
