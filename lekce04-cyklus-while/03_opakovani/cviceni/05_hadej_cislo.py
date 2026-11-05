# Cvičení 5 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Hra "hádej číslo":
#    - Počítač si vylosuje číslo od 1 do 20: randrange(1, 21)
#    - Uživatel hádá. Po každém tipu vypiš "Moc velké." nebo "Moc malé.".
#    - Když trefí, vypiš "Trefa!" a skonči.
#    - Když se netrefí ani na pátý pokus, prozraď číslo a skonči.
#    Nahoru na první řádek nezapomeň:  from random import randrange

from random import randrange
cislo = randrange(1, 21)
pokus = 0

while True:
    mojecislo = int(input("Hadej cislo od 1 do 20: "))
    pokus = pokus + 1
    if mojecislo < 1 or mojecislo > 20:
        print("Cislo neni v uvedenem rozsahu")
        continue
    if pokus == 5:
        print ("Cislo bylo:", cislo)
        break
    if mojecislo == cislo:
        print("Trefa!")
        break
    if mojecislo > cislo:
        print("Moc velké.")
    if mojecislo < cislo:
        print("Moc malé.")
