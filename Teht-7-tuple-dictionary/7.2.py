
nimet: list[str] = []


while True:
    try:
        user_input = str(input("Anna nimi: "))

        if user_input == "":
            for index, nimi in enumerate(nimet):
                print(f"{index + 1}. {nimi}")
            break

        if user_input in nimet:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            nimet.append(user_input)


    except ValueError:
        print("Virheellinen syöte")
