luokat = ["LUX", "A", "B", "C"]

while True:
    try:
        hyttiluokka = str(input("Syötä hyttiluokkasi (LUX, A, B, C): "))

        if hyttiluokka not in luokat:
            print("Virheellinen hyttiluokka. Syötä laivan hyttiluokan listasta: (LUX, A, B, C)")
        else:
            if hyttiluokka == "A":
                print("A on ikkunallinen hytti autokannen yläpuolella.")
                break
            elif hyttiluokka == "B":
                print("B on ikkunaton hytti autokannen yläpuolella.")
                break
            elif hyttiluokka == "C":
                print("C on ikkunaton hytti autokannen alapuolella.")
                break
            elif hyttiluokka == "LUX":
                print("LUX on parvekkeellinen hytti yläkannella.")
                break

    except ValueError:
        print("Virheellinen syöte. Ole hyvä ja kokeile uudelleen")
