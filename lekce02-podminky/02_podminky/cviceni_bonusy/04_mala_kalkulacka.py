# Bonus 4 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Malá kalkulačka.
#     Zeptej se na dvě čísla a na znaménko (+, -, *, /).
#     Podle znaménka vypiš výsledek správné operace.
#     Bonus v bonusu: ošetři dělení nulou vlastní hláškou.

cislo1 = int(input("zvol si nejake cislo:"))
cislo2 = int(input("zvol si dalsi cislo:"))
znamenko = input("zvol znamenko (+, -, *, /):")


if znamenko == "+":
    print (cislo1 + cislo2)
elif znamenko == "-":
    print (cislo1 - cislo2)
elif znamenko == "*":
    print (cislo1 * cislo2)
elif znamenko == "/":
    if cislo2 == 0:
        print ("Zakaz deleni nulou")
    else:
        print (cislo1 / cislo2)
else:
    print ("neznama kombinace")