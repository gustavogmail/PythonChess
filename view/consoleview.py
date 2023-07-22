import json
from tabulate import tabulate


class ConsoleView:
    def __init__(self, controller):
        self.controller = controller

    def show_main_menu(self):
        print("Please choose one of the following options:")
        print("1. List of all players, sorted alphabetically")
        print("2. List of all tournaments")
        print("3. See name and date of a specific tournament")
        print("4. List of players participating in a tournament, sorted alphabetically")
        print("5. List of all rounds in a tournament and all matches in the round.")

        user_choice = input("Digite o número da opção desejada ou 'q' para sair: ")
        if user_choice == '1':
            self.controller.show_players()
        elif user_choice == '2':
            self.controller.show_tournaments()
        elif user_choice == '3':
            self.controller.see_specific_tournament("World Cup")
        elif user_choice.lower() == 'q':
            print("Saindo...")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    @staticmethod
    def show_players(players):
        table = [player.to_dict() for player in players]
        print(tabulate(table, headers="keys", tablefmt="pretty"))

    @staticmethod
    def show_tournaments(tournaments):
        table = [tournament.to_dict() for tournament in tournaments]
        print(tabulate(table, headers="keys", tablefmt="pretty"))

    @staticmethod
    def show_tournament(tournament):
        table = []
        info_tournament = {
            "Name": tournament["name"],
            "Start Date": tournament["start_date"],
            "End Date": tournament["end_date"]
        }
        table.append(info_tournament)
        print(tabulate(table, headers="keys", tablefmt="pretty"))
