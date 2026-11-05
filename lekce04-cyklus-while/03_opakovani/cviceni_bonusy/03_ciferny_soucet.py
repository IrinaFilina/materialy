# Bonus 3 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá celé číslo. Sečti jeho číslice a součet vypiš.
#     Například z 253 vyjde 10, protože 2 + 5 + 3 = 10.
#     (Nápověda: cislo % 10 dá poslední číslici, cislo // 10 ji utrhne.)
#     Zkus i záporné číslo. Aby to fungovalo, hodí se abs(cislo) –
#     ta funkce zahodí minus.

cislo = int(input("Zadejte cislo: "))
cislo = abs(cislo)
sumacisel = 0

while cislo > 0:
    sumacisel = sumacisel + (cislo % 10) 
    cislo = cislo // 10

print (sumacisel)