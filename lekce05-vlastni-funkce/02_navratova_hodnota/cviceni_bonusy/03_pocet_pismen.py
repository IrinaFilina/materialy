# Bonus 3 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci spocitej_pismeno(slovo, pismeno), která vrátí,
#     kolikrát se písmeno ve slově objeví.
#     spocitej_pismeno("kolotoč", "o") vrátí 3.
#     Nechej si zadat slovo i písmeno od uživatele a výsledek vypiš.

def spocitej_pismeno(slovo, pismeno):
    pocet = 0
    for i in slovo:
        if i == pismeno:
            pocet = pocet + 1
    print("Písmeno", pismeno, "je ve slově", slovo, pocet, "krát")

spocitej_pismeno("kolotoč", "o")
spocitej_pismeno("oblako", "o")
