# Cvičení 5 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# Načítej od uživatele čísla tak dlouho, dokud nezadá záporné číslo.
#    Pak vypiš, kolik čísel stihl zadat.
pocetcisel = 0

while True:
    cislo = int(input("Zadej cislo: "))
    pocetcisel = pocetcisel + 1
    if cislo <= 0:
        print ("zadal ste ", pocetcisel, "cisel")
        break
