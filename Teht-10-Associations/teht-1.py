from dataclasses import dataclass


@dataclass(init=True, repr=True)
class Hissi:
    current_kerros: int = 1


    def kerros_ylos(self):
        self.current_kerros += 1

    def kerros_alas(self):
        self.current_kerros -= 1

    def siirry_kerrokseen(self, kerros):
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



h = Hissi()
h.siirry_kerrokseen(5)
print(h)
