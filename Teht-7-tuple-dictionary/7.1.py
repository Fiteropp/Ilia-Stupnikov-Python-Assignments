vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät",
              "kesä", "kesä", "kesä", "syksy", "syksy",
              "syksy", "talvi")

user_input_month = 1

try:
    user_input_month = int(input("Anna kuukauden numero: "))

    if 1 <= user_input_month <= 12:
        print(f"Vuodenaika on {vuodenajat[user_input_month - 1]}")
    else:
        print("Syötä luku 1-12.")


except ValueError:
    print("Virheellinen syöte.")
