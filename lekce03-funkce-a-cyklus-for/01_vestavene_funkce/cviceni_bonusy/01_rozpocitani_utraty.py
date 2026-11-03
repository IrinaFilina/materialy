# Bonus 1 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá celkovou cenu útraty a počet lidí. Vypiš, kolik
#     zaplatí každý, zaokrouhleno na dvě desetinná místa.

celkovautrata = int(input("Kolik ste utratili:"))
pocetlidi = int(input("Kolik bylo lidi:"))

print ("Kazdy ma zaplatit:", round(celkovautrata/pocetlidi, 2))
