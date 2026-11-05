# Cvičení 6 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se na heslo. Když uživatel zadá "pyladies", vypiš "Vítej!"
#    a skonči. Když se splete třikrát, vypiš "Zablokováno." a skonči taky.
#    Z cyklu se v obou případech dostaneš příkazem break.
pocetpokusu = 0
while True:
    heslo = input("Zadej heslo: ")
    pocetpokusu = pocetpokusu + 1
    if heslo == "pyladies":
        print("Vitej!")
        break
    if pocetpokusu == 3:
        print("Zablokováno.")
        break
    print("Spatne ")
