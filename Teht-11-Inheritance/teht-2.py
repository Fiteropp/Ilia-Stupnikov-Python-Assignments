
from dataclasses import dataclass, field


@dataclass(repr=True, init=True)
class Auto:
    rekkari:str = field(default="")
    max_nopeus:int = field(default=0)
    nopeus:float = 0
    kuljettu_matka:float = 0


    def kiihdyta_auto(self, nopeuden_muutos: float):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus < 0:
            self.nopeus = 0
        elif uusi_nopeus > self.max_nopeus:
            self.nopeus = self.max_nopeus
        else:
            self.nopeus = uusi_nopeus


    def kulje(self, tunteja:float):
        self.kuljettu_matka += tunteja * self.nopeus



@dataclass(repr=True, init=True)
class Polttomoottoriauto(Auto):
    bensatankin_koko: float = field(default=0)



@dataclass(repr=True, init=True)
class Sähköauto(Auto):
    akkukapasiteetti: float = field(default=0)


def main():
    auto1 = Polttomoottoriauto(rekkari="ACD-123", max_nopeus=165, bensatankin_koko=32.3)
    auto2 = Sähköauto(rekkari="ABC-15", max_nopeus=180, akkukapasiteetti=52.5)

    auto1.kiihdyta_auto(150)
    auto2.kiihdyta_auto(120)

    auto1.kulje(3)
    auto2.kulje(3)

    print(auto1)
    print(auto2)



if __name__ == "__main__":
    main()
