from dataclasses import dataclass, field


@dataclass(repr=True, init=True)
class Julkaisu:
    nimi: str = field(init=True)



@dataclass(repr=True, init=True)
class Kirja(Julkaisu):
    kirjoittaja: str = field(init=True)
    sivumäärä: int = field(init=True)

    def tulosta_tiedot(self):
        print(f'''
            {"Julkaisun nimi:":<25} {self.nimi}
            {"Lehden kirjailija:":<25} {self.kirjoittaja}
            {"Sivumäärä:":<25} {self.sivumäärä}
            ''')


@dataclass(repr=True, init=True)
class Lehti(Julkaisu):
    päätoimittaja: str = field(init=True)

    def tulosta_tiedot(self):
        print(f'''
            {"Julkaisun nimi:":<25} {self.nimi}
            {"Lehden päätoimittaja:":<25} {self.päätoimittaja}
            ''')



julkaisu = Lehti(nimi="Aku Ankka", päätoimittaja="Aki Hyyppä")
kirja = Kirja(nimi="Hytti n:o 6", kirjoittaja="Rosa Liksom", sivumäärä=200)

julkaisu.tulosta_tiedot()
kirja.tulosta_tiedot()
