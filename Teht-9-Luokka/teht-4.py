
from dataclasses import dataclass, field
from random import randrange


@dataclass(repr=True, init=True)
class Auto:
    rekkari:str = field(default="")
    max_nopeus:int = field(default=0)
    nopeus:float = 0
    kuljettu_matka:float = 0


    def kiihdyta_auto(self, nopeuden_muutos:float):

        match self.nopeus + nopeuden_muutos:

            case n if n + nopeuden_muutos < 0:
                self.nopeus = 0

            case n if n + nopeuden_muutos > self.max_nopeus:
                self.nopeus = self.max_nopeus

            case _:
                self.nopeus = nopeuden_muutos


    def kulje(self, tunteja:float):
        self.kuljettu_matka += tunteja * self.nopeus


def main():
    autot = {}

    for i in range(1, 10):
        huippunopeus = randrange(100, 200)
        rekisterinumero = str("ABC-" + str(i))
        autot[f"auto{i}"] = Auto(rekkari=rekisterinumero, max_nopeus=huippunopeus)


    while True:
        voittaja = None

        for auto in autot.values():
            auto.kiihdyta_auto(randrange(-10, 15))
            auto.kulje(1)

            if auto.kuljettu_matka > 10000:
                voittaja = auto
                print(f"\n {auto.rekkari} on voittaja")
                break

        if voittaja:
            break



    print("\n Autot:")
    print("\n Rekisterinro  Kuljettu Matka      Nopeus")

    for auto in autot.values():
        print(f"{" " * 3} {auto.rekkari} {" " * 7} {auto.kuljettu_matka:<5} km {" " * 7} {auto.nopeus:<3}km/h")





if __name__ == "__main__":
    main()
