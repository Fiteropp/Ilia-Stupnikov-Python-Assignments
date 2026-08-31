import random

nopan_heitot: list[int] = []
summ = 0

while True:
    try:
        user_input = int(input("arpakuutioiden lukumäärä: "))

        for i in range(user_input):
            nopan_heitto = random.randint(1,6)
            summ += nopan_heitto
            nopan_heitot.append(nopan_heitto)

        print(f"Nopat: {nopan_heitot}")
        print(f"Summa: {summ}")
        break

    except ValueError:
        print("Väärillinen syöte")
