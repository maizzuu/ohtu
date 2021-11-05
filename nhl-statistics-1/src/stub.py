class StubIO:
    def __init__(self, list_of_players):
        self.players = list_of_players

    def get_players(self):
        return self.players