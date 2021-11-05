import unittest
from statistics import Statistics
from player import Player
from stub import StubIO


class TestStatistics(unittest.TestCase):
    def setUp(self):
        players = [Player("Connor McDavid", "EDM", 33, 72),Player("Leon Draisaitl", "EDM", 31, 53),Player("Brad Marchand", "BOS", 29, 40),Player("Claude Giroux", "PHI", 16, 27),Player("Justin Braun", "PHI", 1, 5),Player("James van Riemsdyk","PHI", 17, 26)]
        self.statistics = Statistics(StubIO(players))

    def test_konstruktori(self):
        pituus = len(self.statistics._players)
        self.assertAlmostEqual(pituus, 6)

#Connor McDavid EDM 33 + 72 = 105
#Leon Draisaitl EDM 31 + 53 = 84
#Brad Marchand BOS 29 + 40 = 69
#Mitchell Marner TOR 20 + 47 = 67
#Brad Marchand BOS 29 + 40 = 69
#Claude Giroux PHI 16 + 27 = 43
#Justin Braun PHI 1 + 5 = 6
#James van Riemsdyk PHI 17 + 26 = 43