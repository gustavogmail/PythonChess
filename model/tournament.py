class Tournament:
    def __init__(self, name, venue, start_date,
                 end_date, current_round, players,
                 description, number_of_rounds=4):
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.current_round = current_round
        self.players = players
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.rounds = []

    def add_round(self, round_instance):
        self.rounds.append(round_instance)

    def to_dict(self):
        return {
            "name": self.name,
            "venue": self.venue,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "number_of_rounds": self.number_of_rounds,
            "rounds": self.rounds
        }
