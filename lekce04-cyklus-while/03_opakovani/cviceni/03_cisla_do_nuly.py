# Cvičení 3 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadává čísla tak dlouho, dokud nezadá 0. Nakonec vypiš
#    jejich součet, kolik jich bylo a jejich průměr zaokrouhlený
#    na jedno desetinné místo. (Nápověda: round(cislo, 1))

soucet = 0
pocet = 0

while True:
    cislo = int(input("Zadejte cislo: "))
    soucet = soucet + cislo
    pocet = pocet + 1
    if cislo == 0:
        pocet = pocet - 1 # nechci pocitat nulu do vypoctu
        prumer = round(soucet/pocet, 1)
        print ("Soucet vsech cisel je:", soucet)
        print ("Pocet vsech cisel je:", pocet)
        print ("Prumer vsech cisel je:", prumer)
        break

