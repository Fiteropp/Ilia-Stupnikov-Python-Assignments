import sys
from os import getenv

import mysql.connector
from dotenv import load_dotenv
from flask.app import Flask

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


app = Flask(__name__)


@app.route('/kenttä/<user_icao>')
def get_airport_icao(user_icao:str):
    query = "Select airport.name, airport.municipality from airport where airport.ident = %s"
    db_cursor.execute(query, (user_icao,))

    result = db_cursor.fetchall()

    print(result[0])
    if result == []:
        return {"ICAO": "", "Name": "", "Municipality": ""}

    name, municipality = result[0]

    return {"ICAO": user_icao, "Name": name, "Municipality": municipality}



if __name__ == "__main__":
    app.run(port=3000, debug=True)
