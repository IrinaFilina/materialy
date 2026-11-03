# Cvičení 3 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Statistika čísel. Uživatel zadá, kolik čísel bude zadávat, a pak
#    ta čísla postupně napíše. V jednom průchodu cyklem spočítej a vypiš
#    jejich součet, průměr, největší a nejmenší číslo.
#    Nepoužívej funkce sum, max ani min – spočítej vše sama cyklem.

pocet_cisel = int(input("Kolik čísel budeš zadávat? "))
soucet = 0
nejmensi = 0
nejvetsi = 0
for i in range (1, pocet_cisel + 1):
    cislo = int(input("zadej cislo"))
    soucet = soucet + cislo
    if cislo <= nejmensi:
         nejmensi = cislo
    if cislo >= nejvetsi:
         nejvetsi = cislo

print ("soucet cisel je:", soucet)
print ("prumer cisel je:", soucet/pocet_cisel)
print ("nejmensi cislo je:", nejmensi)
print ("nejvetsi cislo je:", nejvetsi)
