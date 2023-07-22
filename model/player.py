class Player:
    def __init__(self, name, last_name, date_of_birth, national_chess_id):
        self.name = name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.national_chess_id = national_chess_id

    def to_dict(self):
        return {
            "name": self.name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "national_chess_id": self.national_chess_id
        }
