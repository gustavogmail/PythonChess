import json
from model.player import Player
from model.tournament import Tournament
from view.consoleview import ConsoleView


class ChessController:
    def __init__(self):
        self.players = self.read_players_from_database()
        self.tournaments = self.read_tournaments_from_database()
        self.view = ConsoleView(self)

    def show_players(self):
        self.view.show_players(self.sort_players_alphabetically(self.players))

    def show_tournaments(self):
        self.view.show_tournaments(self.tournaments)

    def see_specific_tournament(self, name):
        tournament = self.find_specific_tournament(name)
        self.view.show_tournament(tournament.to_dict())

    def find_specific_tournament(self, name):
        for tournament in self.tournaments:
            if tournament.name == name:
                return tournament
        return None

    def generate_menu(self):
        self.view.show_main_menu()

    @staticmethod
    def sort_players_alphabetically(players) -> list[Player]:
        return sorted(players, key=lambda player: player.name)

    @staticmethod
    def execute_new_round():
        print("Método para executar nova rodada")

    @staticmethod
    def read_players_from_database() -> list[Player]:
        players_on_database = []
        with open("./database/players.json", "r") as file:
            data = json.load(file)
            for player in data:
                current_player = Player(
                    name=player["name"],
                    last_name=player["last_name"],
                    date_of_birth=player["date_of_birth"],
                    national_chess_id=player["national_chess_id"]
                )
                players_on_database.append(current_player)

        return players_on_database

    @staticmethod
    def read_tournaments_from_database():
        tournaments_on_database = []
        with open("./database/tournament.json", "r") as file:
            data = json.load(file)
            for tournament in data:
                current_tournament = Tournament(
                    name=tournament["name"],
                    venue=tournament["venue"],
                    start_date=tournament["start_date"],
                    end_date=tournament["end_date"],
                    rounds=tournament["rounds"],
                    current_round=tournament["current_round"],
                    players=tournament["players"],
                    description=tournament["description"]
                )
                tournaments_on_database.append(current_tournament)

        return tournaments_on_database

    @staticmethod
    def write_players_on_database():
        data = [{
            "name": "Gustavo"
        }]
        with open("./database/players.json", "w") as file:
            json.dump(data, file, indent=2)
