# Cvičení 2 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci je_plnoleta(vek), která vrátí True, nebo False.
#    Zeptej se uživatele na věk a podle výsledku vypiš
#    "Můžeš dál." nebo "Ještě ne.".


vek = int(input("Kolik je tobe let?"))
def je_plnoleta(vek):
    if vek >= 18:
        print ("Můžeš dál.")
    else:
        print("Ještě ne.")
    
je_plnoleta(vek)