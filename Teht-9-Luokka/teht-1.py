
from dataclasses import dataclass, field


@dataclass(repr=True, init=True)
class Auto:
    rekkari:str = field(default="")
    max_nopeus:int = field(default=0)
    nopeus:float = 0
    kuljettu_matka:float = 0





def main():
    auto1 = Auto(rekkari="ABC-123", max_nopeus=142)
    print(auto1)


if __name__ == "__main__":
    main()
