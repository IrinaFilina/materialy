# Cvičení 6 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Zabezpečení domu. Dům je zabezpečený, jen když jsou zavřené dveře,
#    zavřená okna a zároveň zapnutý alarm.
#    Zeptej se na všechny tři věci (ano/ne). Pomocí not (…) vypiš
#    "Pozor, dům není zabezpečený!", když zabezpečený NENÍ,
#    jinak vypiš "Zabezpečeno.".

dvere = input("Dvere jsou zavreny?")
okna = input("Okna jsou zavreny?")
alarm = input("Alarm je zapnuty?")

if not(dvere == "ano" and okna == "ano" and alarm == "ano"):
    print("Pozor, dům není zabezpečený!")
else:
    print("Zabezpečeno.")
