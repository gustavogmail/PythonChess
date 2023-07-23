from tabulate import tabulate


class ConsoleView:
    def __init__(self, controller):
        self.controller = controller

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

    @staticmethod
    def show_participants(participants):
        tournament_participants = [participant.to_dict() for participant in participants]
        print(tabulate(tournament_participants, headers="keys", tablefmt="pretty"))

    def verify_tournament_option(self, option, tournament):
        if option == "3":
            self.controller.see_specific_tournament(tournament)
        elif option == "4":
            self.controller.see_participants_in_tournament(tournament)
        self.show_main_menu()

    def show_tournament_options(self, option):
        print("Please choose one of the following options:")
        print("1. World Cup")
        print("2. National Cup")
        print("3. Regional Cup")

        user_choice = input("Digite o número da opção desejada: ")
        if user_choice == "1":
            self.verify_tournament_option(option, "World Cup")
        elif user_choice == "2":
            self.verify_tournament_option(option, "National Cup")
        elif user_choice == "3":
            self.verify_tournament_option(option, "Regional Cup")

    def show_main_menu(self):
        print("Please choose one of the following options:")
        print("1. List of all players, sorted alphabetically")
        print("2. List of all tournaments")
        print("3. See name and date of a specific tournament")
        print("4. List of players participating in a tournament, sorted alphabetically")
        print("5. List of all rounds in a tournament and all matches in the round.")

        user_choice = input("Digite o número da opção desejada ou 'q' para sair: ")
        if user_choice == '1':
            self.controller.show_all_players_in_database()
        elif user_choice == '2':
            self.controller.show_all_tournaments_in_database()
        elif user_choice == '3':
            self.show_tournament_options(user_choice)
        elif user_choice == '4':
            self.show_tournament_options(user_choice)
        elif user_choice.lower() == 'q':
            print("Saindo...")
        else:
            print("Invalid optionm. Please, choose a valid option.")
            self.show_main_menu()
