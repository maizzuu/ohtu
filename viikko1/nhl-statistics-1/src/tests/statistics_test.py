import unittest
from statistics import Statistics
from player import Player
from stub import StubIO


class TestStatistics(unittest.TestCase):
    def setUp(self):
        players = [Player("Connor McDavid", "EDM", 33, 72),Player("Leon Draisaitl", "EDM", 31, 53),Player("Brad Marchand", "BOS", 29, 40),Player("Claude Giroux", "PHI", 16, 27),Player("Justin Braun", "PHI", 1, 5),Player("James van Riemsdyk","PHI", 17, 26)]
        self.statistics = Statistics(StubIO(players))

    def test_constructor(self):
        pituus = len(self.statistics._players)
        self.assertAlmostEqual(pituus, 6)

    def test_search_returns_player(self):
        self.assertAlmostEqual(str(self.statistics.search("Connor McDavid")), str(Player("Connor McDavid", "EDM", 33, 72)))

    def test_search_returns_none(self):
        self.assertAlmostEqual(self.statistics.search("Daniel Harper"), None)

    def test_team_returns_list(self):
        philly = [Player("Claude Giroux", "PHI", 16, 27),Player("Justin Braun", "PHI", 1, 5),Player("James van Riemsdyk","PHI", 17, 26)]
        team_list = self.statistics.team("PHI")
        self.assertAlmostEqual(len(philly), len(team_list))
        self.assertAlmostEqual(str(team_list[0]), str(Player("Claude Giroux", "PHI", 16, 27)))

    def test_top_scorers(self):
        top = self.statistics.top_scorers(3)
        self.assertAlmostEqual(len(top), 4)
        self.assertAlmostEqual(str(top[0]),str(Player("Connor McDavid", "EDM", 33, 72)))


#Connor McDavid EDM 33 + 72 = 105
#Leon Draisaitl EDM 31 + 53 = 84
#Brad Marchand BOS 29 + 40 = 69
#Claude Giroux PHI 16 + 27 = 43
#Justin Braun PHI 1 + 5 = 6
#James van Riemsdyk PHI 17 + 26 = 43