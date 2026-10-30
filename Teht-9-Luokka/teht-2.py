
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




def main():
    auto1 = Auto(rekkari="ABC-123", max_nopeus=142)
    print(auto1)
    auto1.kiihdyta_auto(30)
    auto1.kiihdyta_auto(70)
    auto1.kiihdyta_auto(50)
    print(auto1)
    auto1.kiihdyta_auto(-200)
    print(auto1)




if __name__ == "__main__":
    main()
