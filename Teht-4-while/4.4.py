import random

secret_num = random.randint(1,10)

while True:
    try:
        user_input = int(input("Anna arvaus: "))

        if user_input != secret_num:

            if user_input < secret_num:
                print("Liian pieni arvaus")

            elif user_input > secret_num:
                print("Liian suuri arvaus")

            else: break
        else:
            print("Oikein")
            break

    except ValueError:
        print("Virheellinen syöte")
