# Cvičení 2 – Skládání textu
# Doplň kód pod zadání a soubor spusť (Run).

# Vypiš účtenku tak, aby ceny byly pod sebou: název zarovnaný doleva
#    na dvanáct míst, cenu doprava na osm míst se dvěma desetinnými
#    místy. Na konec přidej řádek se součtem.
#
#    Když je součet vyšší než 150 Kč, přidej ještě řádek se slevou
#    deset procent a řádek s cenou po slevě.

polozka1 = "káva"
cena1 = 59
polozka2 = "dort"
cena2 = 84.5
polozka3 = "čaj"
cena3 = 45
print ()
print (f"{polozka1:15} {cena1:8}")
print (f"{polozka2:15} {cena2:8}")
print (f"{polozka3:15} {cena3:8}")
print("------------------------")
soucet = cena1+cena2+cena3
print(f"Soucet polozek: {soucet:8}")

if  soucet >= 150:
    finalnisoucet = soucet*0.9
    print(f"Cena se slevou: {finalnisoucet:8}")

print ()