import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.peruna = Tuote("peruna", 3)
        self.makkara = Tuote("makkara", 5)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.peruna)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_oikein(self):
        self.kori.lisaa_tuote(self.peruna)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(self):
        self.kori.lisaa_tuote(self.peruna)
        self.kori.lisaa_tuote(self.makkara)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_oikein(self):
        self.kori.lisaa_tuote(self.peruna)
        self.kori.lisaa_tuote(self.makkara)

        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(self):
        self.kori.lisaa_tuote(self.peruna)
        self.kori.lisaa_tuote(self.peruna)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_2_kertaa_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.peruna)
        self.kori.lisaa_tuote(self.peruna)

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.peruna)
 
        ostokset = self.kori.ostokset()
 
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.peruna)
 
        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "peruna")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.peruna)
        self.kori.lisaa_tuote(self.makkara)

        ostokset = self.kori.ostokset()
 
        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_yhden_ostoksen(self):
        self.kori.lisaa_tuote(self.peruna)
        self.kori.lisaa_tuote(self.peruna)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lukumäärä_2(self):
        self.kori.lisaa_tuote(self.peruna)
        self.kori.lisaa_tuote(self.peruna)
 
        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "peruna")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_jos_korissa_on_kaksi_samaa_tuotetta_ja_toinen_poistetaan_jää_koriin_ostos_jossa_tuotetta_1(self):
        self.kori.lisaa_tuote(self.peruna)
        self.kori.lisaa_tuote(self.peruna)

        self.kori.poista_tuote(self.peruna)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_jos_koriin_on_lisätty_tuote_ja_sama_tuote_poistetaan_on_kori_tämän_jälkeen_tyhjä(self):
        self.kori.lisaa_tuote(self.peruna)
        self.kori.poista_tuote(self.peruna)

        self.assertEqual(self.kori.tavaroita_korissa(),0)
        self.assertEqual(self.kori.hinta(),0)
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_tyhjenna_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(self.peruna)
        self.kori.tyhjenna()

        self.assertEqual(len(self.kori.ostokset()), 0)