# Cvičení 4 – Definice funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci odpocet(od), která odpočítá od zadaného čísla
#    dolů k 1 a nakonec vypíše "Teď!".
#    Zavolej ji pro 3 a pro 5.
#    Krok v range jde nastavit i tak, aby se počítalo dolů.

cislo =int(input("Zadej cislo:"))

def odpocet (cislo):
    print (cislo)
    while cislo > 1:
        cislo = cislo - 1
        print (cislo)
    print("Ted!")

odpocet(cislo)

def odpocet2(od):
    for i in range(od, 0, -1):
        print(i)
    print("Teď!")


odpocet2(3)
odpocet2(5)