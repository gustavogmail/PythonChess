from controller.player.player_controller import PlayerController
from controller.tournament.tournament_controller import TournamentController
from view.consoleview import ConsoleView


class ChessController:
    def __init__(self):
        self.view = ConsoleView(self)
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def generate_menu(self):
        self.view.show_main_menu()

    def show_all_players_in_database(self):
        self.player_controller.show_players()

    def show_all_tournaments_in_database(self):
        self.tournament_controller.show_tournaments()

    def see_specific_tournament(self, tournament):
        self.tournament_controller.see_specific_tournament(tournament)

    def see_participants_in_tournament(self, tournament_name):
        tournament = self.tournament_controller.find_specific_tournament(tournament_name)
        self.view.show_participants(self.player_controller.sort_players_alphabetically(tournament.players))

    @staticmethod
    def execute_new_round():
        print("Método para executar nova rodada")
