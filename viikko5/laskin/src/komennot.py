class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote
        self.aikaisempi = sovelluslogiikka.tulos

    def suorita(self):
        self.sovelluslogiikka.plus(self.syote)

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.aikaisempi)

class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovelluslogiikka.miinus(self.syote)

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.aikaisempi)

class Nollaus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.nollaa()

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.aikaisempi)

class Kumoa:
    def __init__(self, sovelluslogiikka, syote):
        self.edellinen = sovelluslogiikka.edellinen
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote
        self._komennot = {
            Komento.SUMMA: Summa(self.sovelluslogiikka, self.syote),
            Komento.EROTUS: Erotus(self.sovelluslogiikka, self.syote),
            Komento.NOLLAUS: Nollaus(self.sovelluslogiikka, self.syote),
            Komento.KUMOA: Kumoa(self.sovelluslogiikka, self.syote)
        }

    def suorita(self):
        komento_olio = self._komennot[komento]
        komento_olio.kumoa()