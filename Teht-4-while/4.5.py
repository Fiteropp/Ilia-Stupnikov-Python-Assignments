username = "python"
salasana = "rules"

i = 0
usernameGuessed = False

while i < 5:
    try:
        if usernameGuessed == False:
            input_username = str(input("Syötä käyttäjätunnus: "))

            if input_username == username:
                usernameGuessed = True
            else:
                i += 1
                print(f"Väärä käyttäjätunnus, {5 - i} yritystä jäljellä")

        else:
            input_password = str(input("Syötä salasana: "))

            if input_password == salasana:
                print("Tervetuloa")
                break
            else:
                i += 1
                print(f"Väärä salasana, {5 - i} yritystä jäljellä")

    except ValueError:
        print("Virheellinen syöte")
else:
    print("Pääsy evätty")
