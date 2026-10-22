# Bonus 2 – Vstup od uživatelky
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na částku a na počet lidí.
#     Vypiš, kolik zaplatí každý a kolik korun zbyde.

castka = input("Kolik stalo vecere?")
cislo = input("Kolik bylo lidi?")
print("Kazdy ma zaplatit:", int(castka) // int (cislo), ". Zbyde:", int(castka) % int (cislo), ".")
