# Bonus 3 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Ciferný součet. Uživatel zadá číslo. Sečti jeho jednotlivé číslice
#     a součet vypiš (třeba z 253 vyjde 2 + 5 + 3 = 10).

cislo = input("Zadej cislo:")
soucet = 0
for znak in cislo:
    soucet = soucet + int(znak)
print (soucet)