from os import getenv

import requests
from dotenv.main import load_dotenv

load_dotenv()


def get_weather_forecast():
    city:str = input("Anna kaupungin nimi: ").strip()
    if not city:
        print("Paikkakunnan nimi ei voi olla tyhjä.")
        return

    key = getenv("API_KEY")

    if not key:
        print("Tarkasta API-avainta .env tiedostossa")
        return



    request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

    try:
        response = requests.get(request)
        data = response.json()

        if response.status_code == 200:
            saa_kuvaus = data['weather'][0]['description']
            temp = data['main']['temp']
            temp_c = temp - 273.15
            kaupungin_nimi = data['name']

            print(f"\nSäätiedot paikkakunnalle {kaupungin_nimi}:")
            print(f"Säätila:  {saa_kuvaus.capitalize()}")
            print(f"Lämpötila: {temp_c:.1f} °C")
        elif response.status_code == 404:
            print(f"Paikkakuntaa '{city}' ei löytynyt.")
        elif response.status_code == 401:
            print("API-avain on virheellinen tai puuttuu .env tiedostosta")
        else:
            print(f"Virhe requestissä (Tila koodi: {response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"Yhteysvirhe: {e}")

if __name__ == "__main__":
    get_weather_forecast()
