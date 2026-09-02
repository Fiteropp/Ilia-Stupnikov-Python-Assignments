
gallons = 0.0
liters = 0.0

def gal_to_liters (gallons: float):
    try:
        return gallons * 3.75
    except ValueError:
        return "Invalid Input"

while True:
    try:
        gallons = float(input("Anna bensamäärä gallonoina: "))
        if gallons <= 0:
           break

        liters = gal_to_liters(gallons)
        print(f"Bensan määrä litroina: {liters}")

    except ValueError:
        print("Invalid Input")
