class Match:
    def __init__(self, player_white, white_score, player_black, black_score):
        self.player_white = player_white
        self.white_score = white_score
        self.player_black = player_black
        self.black_score = black_score

    def to_dict(self):
        return {
            "player_white": self.player_white,
            "white_score": self.white_score,
            "player_black": self.player_black,
            "black_score": self.black_score
        }