# Cvičení 5 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá číslo. Cyklem vypiš jeho malou násobilku –
#    tedy cislo * 1 až cislo * 10, každý řádek třeba "7 * 3 = 21".

cislo = int(input("Zadej cislo: "))

for i in range (1, 11):
    print(cislo, "*", i, "=", cislo * i)
