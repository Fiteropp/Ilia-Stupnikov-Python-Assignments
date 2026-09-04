lentokentat = {}


def luo_lentokentta(icao: str, nimi: str):
    try:
        lentokentat[icao] = nimi
    except ValueError:
        print("Virheellinen syöte")


def hae_lentokentta():
    user_icao = check_input("Syötä lentokentan 4-merkkinen ICAO-koodi: ", lambda v: len(v) == 4 and str.isupper, "Koodissa voi olla vain 4 isoa kirjainta")

    result = lentokentat.get(user_icao, "Annetulla koodilla ei löytynyt lentokenttää")

    print(f"\nTulos: {result} \n")


def check_input(prompt, check, error_msg="Virheellinen syöte."):
    while True:
        value = input(prompt)
        if check(value):
            return value
        print(error_msg)

def handle_lentokentan_luominen():
    user_icao = check_input("Syötä lentokentan 4-merkkinen ICAO-koodi: ", lambda v: len(v) == 4 and str.isupper, "Koodissa voi olla vain 4 isoa kirjainta")
    user_airport_name = check_input("Syötä lentokentan nimi: ", str.isascii)

    luo_lentokentta(user_icao, user_airport_name)



while True:
    print("""
    Valikko:
        1. Uuden lentoaseman luominen
        2. Lentoaseman haku ICAO-koodilla
        3. Lopeta
        """)
    try:
        user_selector = int(input("Valitse 1-3: "))

        match user_selector:
            case 1:
                handle_lentokentan_luominen()
            case 2:
                hae_lentokentta()
            case 3:
                break

    except ValueError:
        print("Virheellinen syöte. Syötä luku 1-3 valittaakseen toiminto")
