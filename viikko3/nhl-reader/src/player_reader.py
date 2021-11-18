import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._url = url
        self.players = []
        self.get_players()

    def get_players(self):
        players_json = requests.get(self._url).json()
        for player_dict in players_json:
            player = Player(
                player_dict['name'],
                player_dict["nationality"],
                player_dict["assists"],
                player_dict["goals"],
                player_dict["penalties"],
                player_dict["team"],
                player_dict["games"]
            )

            self.players.append(player)