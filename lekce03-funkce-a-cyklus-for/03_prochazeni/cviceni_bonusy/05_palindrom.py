# Bonus 5 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Palindrom. Uživatel zadá slovo. Zjisti, jestli se čte stejně
#     zepředu i zezadu (třeba "kajak" nebo "radar").
#     Zamysli se, jak si slovo poskládáš pozpátku a jak obě verze porovnáš.

slovo = input("zadej slovo:")
obracene = ""
for znak in slovo:
    obracene =  znak + obracene

# print(obracene)
# print(slovo)
if slovo == obracene:
    print("To je palindrom!", slovo, "=", obracene)
else:
    print("To neni palindrom!", slovo, "ne rovna se", obracene) 



