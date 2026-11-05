# Cvičení 6 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# V nádrži je 45 litrů vody a každou minutu z ní uteče 3 litry.
#    Po každé minutě vypiš, kolik vody zbývá, a nakonec vypiš,
#    po kolika minutách je nádrž prázdná.

vodapred = 45
pocetminut = 0

while vodapred > 0:
    vodapred =  vodapred - 3
    print ("Zbyva", vodapred, "litru")
    pocetminut = pocetminut + 1
print("Nadoba je prazdna po:", pocetminut, "minutach" )