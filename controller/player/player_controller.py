import json
from model.player import Player
from view.consoleview import ConsoleView


class PlayerController:
    def __init__(self):
        self.players = self.read_players_from_database()
        self.view = ConsoleView(self)

    def show_players(self):
        self.view.show_players(self.sort_players_alphabetically(self.players))

    @staticmethod
    def sort_players_alphabetically(players) -> list[Player]:
        return sorted(players, key=lambda player: player.name)

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
    def write_players_on_database():
        data = [{
            "name": "Gustavo"
        }]
        with open("./database/players.json", "w") as file:
            json.dump(data, file, indent=2)
