from player import Player
from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        return_list = []
        for player in self.players:
            if player.nationality == nationality:
                return_list.append(player)
        return_list.sort(key=lambda p: p.points, reverse=True)
        return return_list