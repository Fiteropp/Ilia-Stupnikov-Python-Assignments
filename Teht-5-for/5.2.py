numbers: list[float] = []

ix = 1
user_input_float = 0

while True:
    try:
        user_input = (input("Anna numero: "))

        if user_input == "":
            numbers.sort(reverse=True)
            numbers = numbers[:5]
            print("\n Viisi suurinta lukua:")
            for i in numbers:
                print(f"{ix}. {i}")
                ix += 1
            break

        else:
            try:
                user_input_float = float(user_input)
            except ValueError:
                print("Väärillinen syöte")

            print(f"Numero: {user_input_float}")
            numbers.append(user_input_float)


    except ValueError:
        print("Väärillinen syöte")
