try:
    vuosiluku = int(input("Syötä vuosiluku: "))

    if vuosiluku % 100 != 0:
        if vuosiluku % 4 == 0:
            print("Annettu vuosi on karkausvuosi")
        else:
            print("Annettu vuosi ei ole karkausvuosi")
    else:
        if vuosiluku % 100 == 0 and vuosiluku % 400 == 0:
            print("Annettu vuosi on karkausvuosi")
        else:
            print("Annettu vuosi ei ole karkausvuosi")
except ValueError:
    print("Virheellinen syöte")
