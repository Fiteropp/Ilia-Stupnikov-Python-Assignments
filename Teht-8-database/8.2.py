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
    while True:
        user_iso_country = check_input(
            "Syötä lentokentan 2-merkkinen maakoodi (esim 'FI') (syötä 'EX' lopetaaksesi): ",
            lambda v: len(v) == 2 and v.isupper(),
            "Koodissa voi olla vain 2 isoa kirjainta",
        )
        if user_iso_country == "EX":
            break

        query = "SELECT type, COUNT(*) as count FROM airport WHERE airport.iso_country = %s GROUP BY type"
        db_cursor.execute(query, (user_iso_country,))
        result = db_cursor.fetchall()

        if not result:
            print("Mitään ei löytynyt")
            continue

        for rivi in result:
            print(f"{rivi[0]} : {rivi[1]}") #type: ignore[index] # mysql.connector's type stubs are loose and basedpyright is complaining



def check_input(prompt, check, error_msg="Virheellinen syöte."):
    while True:
        value = input(prompt)
        if check(value):
            return value
        print(error_msg)


while True:
    print("""
    Valikko:
        1. Lentokenttien lukumäärän haku maakoodilla
        2. Lopeta
        """)
    try:
        user_selector = int(input("Valitse 1-2: "))

        match user_selector:
            case 1:
                hae_lentokentta()
            case 2:
                break


    except ValueError:
        print("Virheellinen syöte. Syötä luku 1-2 valittaakseen toiminto")
