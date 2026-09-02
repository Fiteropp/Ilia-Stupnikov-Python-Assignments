import math


def calculate_pizza_m2(halkaisija: float):
    sade = halkaisija / 2
    pinta_ala = math.pi * (sade**2)
    pinta_ala /= 10000
    return pinta_ala


def calculate_price_per_area(halkaisija: float, hinta: float):
    pinta_ala = calculate_pizza_m2(halkaisija)
    return hinta / pinta_ala


def main():
    pizza1_price = float(input("Anna ensimmäisen pizzan hinta: "))
    pizza1_diameter = float(input("Anna ensimmäisen pizzan halkaisija: "))
    pizza2_price = float(input("Anna toisen pizzan hinta: "))
    pizza2_diameter = float(input("Anna toisen pizzan halkaisija: "))

    pizza1_price_per_area = calculate_price_per_area(pizza1_diameter, pizza1_price)
    pizza2_price_per_area = calculate_price_per_area(pizza2_diameter, pizza2_price)

    print(f"\nPizza 1: {pizza1_price_per_area:.2f} €/m2")
    print(f"Pizza 2: {pizza2_price_per_area:.2f} €/m2\n")

    if pizza1_price_per_area < pizza2_price_per_area:
        print("Ensimmäinen pizza on edullisempi.")
    elif pizza2_price_per_area < pizza1_price_per_area:
        print("Toinen pizza on edullisempi.")
    else:
        print("Pizzat ovat saman hintaisia neliömetriä kohden.")



if __name__ == "__main__":
    main()
