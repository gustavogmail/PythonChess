import datetime


class Round:
    def __init__(self, name, start_datetime):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = ""
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def mark_as_finished(self):
        self.end_datetime = datetime.datetime.now()

    def to_dict(self):
        return {
            "name": self.name,
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
            "matches": self.matches
        }
