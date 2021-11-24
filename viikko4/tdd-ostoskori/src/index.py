from ostoskori import Ostoskori
from tuote import Tuote
from ostos import Ostos

def main():
    ostoskori = Ostoskori()
    peruna = Tuote("peruna", 3)
    ostoskori.lisaa_tuote(peruna)
    for ostos in ostoskori.kori:
        print(ostos.tuotteen_nimi())
        print(ostos.lukumaara())
    ostoskori.lisaa_tuote(peruna)
    for ostos in ostoskori.kori:
        print(ostos.tuotteen_nimi())
        print(ostos.lukumaara())


if __name__ == "__main__":
    main()