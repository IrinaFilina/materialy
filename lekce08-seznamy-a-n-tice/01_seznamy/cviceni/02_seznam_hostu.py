# Cvičení 2 – Seznamy
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na jméno. Když je na seznamu hostů, vypiš "Vítej!".
#    Když není, vypiš "Na seznamu nejsi.".
#    Vstup uprav tak, aby prošlo i " anna " nebo "ANNA".

hoste = ["Anna", "Petra", "Jana", "Eva"]

jmeno = input("Jak se jmenujes?").strip().title()

if jmeno in hoste:
    print ("Vitej")
else:
    print("Na seznamu nejsi.")