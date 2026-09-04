while True:
    try:
        user_input = str(input("Anna numero: "))

        if user_input:
            print(f"Numero: {user_input}")
        else: break

    except ValueError:
        print("Virheellinen syöte")
