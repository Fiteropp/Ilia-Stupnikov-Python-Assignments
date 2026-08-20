sukupuolet = ["M", "N"]
hemoglobiiniarvo = 0

while True:
    try:
        sukupuoli = str(input("Syötä sukupuolesi (M, N): "))

        if sukupuoli not in sukupuolet:
            print("Virheellinen syöte. Kirjoita M tai N")
        else:
            hemoglobiiniarvo = float(input("Syötä hemoglobiiniarvosi: "))
            if sukupuoli == "M":
                if hemoglobiiniarvo < 134:
                    print("hemoglobiiniarvosi on alhainen")
                elif hemoglobiiniarvo > 134 and hemoglobiiniarvo < 195:
                    print("hemoglobiiniarvosi on normaali")
                elif hemoglobiiniarvo > 195:
                    print("hemoglobiiniarvosi on korkea")
                break
            elif sukupuoli == "N":
                if hemoglobiiniarvo < 117:
                    print("hemoglobiiniarvosi on alhainen")
                elif hemoglobiiniarvo > 117 and hemoglobiiniarvo < 175:
                    print("hemoglobiiniarvosi on normaali")
                elif hemoglobiiniarvo > 175:
                    print("hemoglobiiniarvosi on korkea")
                break

    except ValueError:
        print("Virheellinen syöte. Ole hyvä ja kokeile uudelleen")
