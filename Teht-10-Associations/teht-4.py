
from dataclasses import dataclass, field
from random import randrange


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
class Kilpailu:
    kilpailun_nimi: str = field()
    kilpailun_pituus: float = field()
    autojen_lista: dict[str, Auto] = field(default_factory=dict)


    def tunti_kuluu(self):
        for auto in self.autojen_lista.values():
            auto.kiihdyta_auto(randrange(-10, 15))
            auto.kulje(1)


    def tulosta_tilanne(self):
        print("\n Autot:")
        print("Rekisterinro  Kuljettu Matka      Nopeus")

        for auto in self.autojen_lista.values():
            print(f"{auto.rekkari:>8} {auto.kuljettu_matka:>12} km {auto.nopeus:>11}km/h")


    def kilpailu_ohi(self):
        for auto in self.autojen_lista.values():
            if auto.kuljettu_matka > 10000:
                print(f"\n {auto.rekkari} on voittaja")
                return True

        return False



def main():
    autot = {}
    tunnit = 0

    for i in range(1, 10):
        huippunopeus = randrange(100, 200)
        rekisterinumero = str("ABC-" + str(i))
        autot[f"auto{i}"] = Auto(rekkari=rekisterinumero, max_nopeus=huippunopeus)

    suuri_romuralli = Kilpailu(kilpailun_nimi="Suuri Romuralli", kilpailun_pituus=8000, autojen_lista=autot)

    while True:
        suuri_romuralli.tunti_kuluu()
        tunnit += 1

        if tunnit % 10 == 0:
            print(f"\n \n Tunnin määrä: {tunnit} h")
            suuri_romuralli.tulosta_tilanne()

        if suuri_romuralli.kilpailu_ohi() == True:
            print(f"{tunnit} h")
            break




if __name__ == "__main__":
    main()
