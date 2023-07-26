import random
from view.consoleview import ConsoleView
from model.tournament import Tournament
from model.round import Round
from model.match import Match


class TournamentController:
    def __init__(self):
        self.view = ConsoleView(self)

    def show_tournaments(self, tournaments):
        self.view.show_tournaments(tournaments)

    def see_specific_tournament(self, tournament):
        self.view.show_tournament(tournament.to_dict())

    def show_tournament_rounds_and_matches(self, tournament):
        self.view.show_all_matches_and_rounds(tournament)

    @staticmethod
    def add_matches_to_round(tournament, matches) -> Tournament:
        # TODO: Handle the second round
        for i in range(tournament.number_of_rounds):
            round1 = Round(
                name=f"Round{i + 1}",
                start_datetime="2023-06-06"
            )
            for match in matches:
                round1.add_match(match)
                round1.mark_as_finished()
            tournament.add_round(round1)

        return tournament

    def build_rounds(self, tournament) -> Tournament:
        # Shuffle the array of players (optional step)
        random.shuffle(tournament.players)

        matches = []
        for i in range(0, len(tournament.players), 2):
            player1 = tournament.players[i]
            player2 = tournament.players[i + 1]
            match = Match(player_white=player1.name, white_score=1, player_black=player2.name, black_score=0)
            matches.append(match)

        tournament = self.add_matches_to_round(tournament, matches)

        return tournament
