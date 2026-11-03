# Bonus 4 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Teplotní skok. Uživatel postupně zadá sedm denních teplot
#     (klidně i záporných). Najdi a vypiš největší skok mezi dvěma
#     sousedními dny – tedy největší rozdíl teplot ze dne na den
#     (bez ohledu na to, jestli teplota stoupla, nebo klesla).

predchozi = int(input("Zadej teplotu:"))
nejvetsirozdil=0

for den in range (1,7):
    teplota = int(input("Zadej teplotu:"))  
    rozdil = abs (teplota - predchozi)
    if rozdil > nejvetsirozdil:
        nejvetsirozdil = rozdil
    predchozi = teplota

print("Největší skok:", nejvetsirozdil)

