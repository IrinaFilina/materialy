# Bonus 1 – Definice funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci obdelnik(sirka, vyska), která z hvězdiček vypíše
#     obdélník zadané velikosti. obdelnik(5, 3) vypíše tři řádky
#     po pěti hvězdičkách.

def obdelnik(sirka, vyska):
    print("*" * sirka)
    for i in range (2, vyska):
     print("*" + (" " * (sirka - 2)) + "*" )
    print("*" * sirka)

obdelnik(5, 3)

print ("                                ")

def obdelnik2(sirka, vyska):
    for radek in range(vyska):
        print("*" * sirka)


obdelnik2(5, 3)