# Cvičení 4 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadává naměřené teploty. Po každé se zeptej
#    "Další? (ano/ne) ". Až odpoví "ne", vypiš nejvyšší teplotu.

maxteplota = int(input("Zadej teplotu: "))
while True:
    otazka = input("Další? (ano/ne) ")
    if otazka == "ano":
        teplota = int(input("Zadej teplotu: "))
        if teplota > maxteplota:
            maxteplota = teplota
    elif otazka == "ne":
        print("Maximalni teplota co uzivatel zadal je:", maxteplota)
        break


