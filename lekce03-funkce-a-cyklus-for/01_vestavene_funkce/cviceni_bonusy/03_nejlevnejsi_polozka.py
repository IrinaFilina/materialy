# Bonus 3 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Cíl a rozpočet. Uživatel zadá cenu tří položek. Vypiš nejlevnější
#     a nejdražší z nich a jestli se všechny tři vejdou do rozpočtu 1000 Kč.

cena1 = int(input("Zadej cenu prvni polozky:"))
cena2 = int(input("Zadej cenu druhe polozky:"))
cena3 = int(input("Zadej cenu treti polozky:"))

print("Nejlevnejsi polozka stoji:", min(cena1, cena2, cena3))
print("Nejdrazsi polozka stoji:", max(cena1, cena2, cena3))

if (cena1 + cena2 + cena3) > 1000:
    print("Bohuzel to nevejde do rozpoctu v 1000 Kc:", (cena1 + cena2 + cena3))
else:
    print("Parada, vsechny tri polozky vejdou do rozpoctu v 1000 Kc:", (cena1 + cena2 + cena3))
