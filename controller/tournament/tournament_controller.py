import json
from model.tournament import Tournament
from model.player import Player
from view.consoleview import ConsoleView


class TournamentController:
    def __init__(self):
        self.tournaments = self.read_tournaments_from_database()
        self.view = ConsoleView(self)

    def show_tournaments(self):
        self.view.show_tournaments(self.tournaments)

    def see_specific_tournament(self, tournament_name):
        tournament = self.find_specific_tournament(tournament_name)
        self.view.show_tournament(tournament.to_dict())

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
                    rounds=tournament["rounds"],
                    current_round=tournament["current_round"],
                    players=players,
                    description=tournament["description"]
                )
                tournaments_on_database.append(current_tournament)

        return tournaments_on_database
