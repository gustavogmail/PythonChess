class ConsoleView:
    def __init__(self, controller):
        self.controller = controller

    def show_main_menu(self):
        print("O que você deseja fazer?")
        print("1. Executar uma nova rodada")
        print("2. Ver lista de torneios")
        print("3. Ver lista de jogadores")
        user_choice = input("Digite o número da opção desejada ou 'q' para sair: ")
        if user_choice == '1':
            self.controller.execute_new_round()
        elif user_choice == '2':
            self.controller.show_tournaments()
        elif user_choice == '3':
            self.controller.show_players()
        elif user_choice.lower() == 'q':
            print("Saindo...")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    @staticmethod
    def show_players(players):
        print("Players:")
        for player in players:
            print(f"- {player.name}")

    @staticmethod
    def show_tournaments(tournaments):
        print("Tournaments:")
        for tournament in tournaments:
            print(f"- {tournament.name}")
