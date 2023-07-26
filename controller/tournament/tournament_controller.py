from view.consoleview import ConsoleView


class TournamentController:
    def __init__(self):
        self.view = ConsoleView(self)

    def show_tournaments(self, tournaments):
        self.view.show_tournaments(tournaments)

    def see_specific_tournament(self, tournament):
        self.view.show_tournament(tournament.to_dict())

    def show_tournament_rounds_and_matches(self, tournament):
        self.view.show_all_matches_and_rounds(tournament)
