print("Kuha pituus detection software™")
kuha_cm = float(input("Anna the pituus of kuha: "))

if kuha_cm < 37:
    cm_puuttuu = 37 - kuha_cm
    print(f"Put the fih back into järvi, {cm_puuttuu} senttiä alimmasta sallitusta pyyntimitasta puuttuu")
else:
    print("Hyvä saalis!")
