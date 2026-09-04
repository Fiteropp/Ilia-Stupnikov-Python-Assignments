while True:
    try:
        user_input = float(input("Tuumat: "))

        if not user_input <= 0:
            print(f"Tulos cm: {user_input * 2.54}")
        else: break

    except ValueError:
        print("Virheellinen syöte")
