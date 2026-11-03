# Cvičení 1 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci nadpis(text), která vypíše text a pod něj čáru
#    z pomlček dlouhou přesně jako ten text.
#    Vyzkoušej ji na dvou různě dlouhých nadpisech.
def nadpis(text):
    pocet_pismen = len(text)
    print(text)
    print (pocet_pismen * "-")

nadpis("Irina Alexandrovna Rastopsina")

