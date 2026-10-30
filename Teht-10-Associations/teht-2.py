from dataclasses import dataclass, field


@dataclass(init=True, repr=True)
class Hissi:
    current_kerros: int = 1


    def kerros_ylos(self):
        self.current_kerros += 1

    def kerros_alas(self):
        self.current_kerros -= 1

    def siirry_kerrokseen(self, kerros: int):
        if self.current_kerros == kerros:
            pass

        if self.current_kerros > kerros:
            diff = self.current_kerros - kerros
            for i in range(diff):
                self.kerros_alas()

        elif self.current_kerros < kerros:
            diff = kerros -  self.current_kerros
            for i in range(diff):
                self.kerros_ylos()


@dataclass(init=True, repr=True)
class Talo:
    alin_kerros: int = field(init=True)
    ylin_kerros: int = field(init=True)

    hissien_määrä: int = field(default=1, init=True)
    hissit: list[Hissi] = field(default_factory=list, init=False)

    def __post_init__(self):
            for _ in range(self.hissien_määrä):
                self.hissit.append(Hissi())


    def aja_hissia(self, hissin_nro: int, kerros: int):
        self.hissit[hissin_nro - 1].siirry_kerrokseen(kerros)




def main():
    talo1 = Talo(alin_kerros=1, ylin_kerros=5, hissien_määrä=2)
    talo1.aja_hissia(hissin_nro=1, kerros=3)
    talo1.aja_hissia(hissin_nro=2, kerros=2)
    print(talo1)

if __name__ == "__main__":
    main()
