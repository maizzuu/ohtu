import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuote1 = Tuote("peruna", 3)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)

    def test_lisaa_tuote_jota_ei_ole_jo_korissa(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.assertEqual(len(self.kori.kori), 1)