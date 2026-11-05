# Cvičení 4 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel postupně zadává čísla. Sčítej je. Jakmile zadá 0,
#    přestaň se ptát a vypiš celkový součet.
soucet = 0
cislo = "x"
while cislo != 0:
    cislo = int(input("Zadej cislo"))
    soucet = soucet + cislo
print (soucet)

soucet = 0
cislo = int(input("Zadej číslo (0 = konec): "))
while cislo != 0:
    soucet = soucet + cislo
    cislo = int(input("Zadej číslo (0 = konec): "))
print("Součet je", soucet)