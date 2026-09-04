import sys
from os import getenv

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

try:
    db = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user=getenv("DB_USERNAME"),
        password=getenv("DB_PASSWORD"),
        autocommit=True,
    )
except mysql.connector.Error as e:
    print("Yhteys tietokantaan epäonnistui, tarkasta käyttäjätunnusta ja salasanaa .env tiedostossa")
    print(e)
    sys.exit()



db_cursor = db.cursor()


def hae_lentokentta():
    user_icao = ""

    while True:
        user_icao = check_input(
            "Syötä lentokentan 4-merkkinen ICAO (syötä 'EXIT' lopetaaksesi): ",
            lambda v: len(v) == 4 and v.isupper(),
            "Koodissa voi olla vain 4 isoa kirjainta",
        )

        if user_icao == "EXIT":
            break

        query = "Select airport.name, airport.iso_region from airport where airport.ident = %s"
        db_cursor.execute(query, (user_icao,))

        result = db_cursor.fetchall()

        if result == []:
            print("Lentokentää ei löytynyt")
            continue

        name, iso_region = result[0]
        print(f"\nLentokenttän nimi: {name} \nLentokenttän sijaintikunta: {iso_region} \n ")



def check_input(prompt, check, error_msg="Virheellinen syöte."):
    while True:
        value = input(prompt)
        if check(value):
            return value
        print(error_msg)


while True:
    print("""
    Valikko:
        1. Lentoaseman haku ICAO-koodilla tietokannasta
        2. Lopeta
        """)
    try:
        user_selector = int(input("Valitse 1-3: "))

        match user_selector:
            case 1:
                hae_lentokentta()
            case 2:
                break


    except ValueError:
        print("Virheellinen syöte. Syötä luku 1-2 valittaakseen toiminto")
