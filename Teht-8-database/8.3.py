import sys
from os import getenv

import mysql.connector
from dotenv import load_dotenv
from geopy.distance import geodesic

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
    user_icao_1 = ""
    user_icao_2 = ""
    airport_name_1 = str
    airport_name_2 = str
    airport_1_geodata = tuple
    airport_2_geodata = tuple

    while True:
        user_icao_1 = check_input(
            "Syötä ensimmäisen lentokentan 4-merkkinen ICAO (syötä 'EXIT' lopetaaksesi): ",
            lambda v: len(v) == 4 and v.isupper(),
            "Koodissa voi olla vain 4 isoa kirjainta",
        )

        if user_icao_1 == "EXIT":
            break

        query = "Select airport.name, airport.latitude_deg, airport.longitude_deg from airport where airport.ident = %s"
        db_cursor.execute(query, (user_icao_1,))

        result = db_cursor.fetchall()

        if result == []:
            print("Lentokentää ei löytynyt")
            continue

        airport_name_1, latitude_deg_1, longitude_deg_1 = result[0]
        airport_1_geodata = (latitude_deg_1, longitude_deg_1)
        print(f"\nLentokenttä 1:\nLentokenttän nimi: {airport_name_1} \n ")
        break

    while True:
        user_icao_2 = check_input(
            "Syötä toisen lentokentan 4-merkkinen ICAO (syötä 'EXIT' lopetaaksesi): ",
            lambda v: len(v) == 4 and v.isupper(),
            "Koodissa voi olla vain 4 isoa kirjainta",
        )

        if user_icao_2 == "EXIT":
            break

        query = "Select airport.name, airport.latitude_deg, airport.longitude_deg from airport where airport.ident = %s"
        db_cursor.execute(query, (user_icao_2,))

        result = db_cursor.fetchall()

        if result == []:
            print("Lentokentää ei löytynyt")
            continue

        airport_name_2, latitude_deg_2, longitude_deg_2 = result[0]
        airport_2_geodata = (latitude_deg_2, longitude_deg_2)
        print(f"\nLentokenttä 2:\nLentokenttän nimi: {airport_name_2} \n ")
        break


    if airport_1_geodata and airport_2_geodata:
        print(f"Distance between {airport_name_1} and {airport_name_2} is:")
        print(geodesic(airport_1_geodata, airport_2_geodata).km, "km")



def check_input(prompt, check, error_msg="Virheellinen syöte."):
    while True:
        value = input(prompt)
        if check(value):
            return value
        print(error_msg)


while True:
    print("""
    Valikko:
        1. Lentoasemien välinen etäisyys
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
