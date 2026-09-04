
def onko_alkuluku(number: float):

    if number <= 1:
        return False

    ix = 2

    while ix * ix <= number:
        if number % ix == 0:
            return False
        ix += 1

    return True


while True:
    try:
        user_input = float(input("Anna numero (kirjoita 0 lopetaaksesi): "))

        if user_input == 0:
            break

        if onko_alkuluku(user_input):
            print("Numero on alkuluku")

        else:
            print("Numero ei ole alkuluku")


    except ValueError:
        print("Virheellinen syöte")
