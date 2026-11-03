# Cvičení 2 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš dvě funkce:
#    je_sude(cislo) vrátí True, nebo False,
#    popis(cislo) vrátí text "4 je sudé" nebo "7 je liché" a uvnitř
#    se na je_sude zeptá.
#    Pak v cyklu for vypiš popis čísel od 1 do 6.

def je_sude(cislo):
    if cislo%2==0:
        return True
    else:
        return False
    
def popis(cislo):
    if je_sude(cislo) == True:
        print (cislo, "je sude")
    else:
       print (cislo, "je liche") 

popis(7)
popis(4)
popis(16)
popis(133)