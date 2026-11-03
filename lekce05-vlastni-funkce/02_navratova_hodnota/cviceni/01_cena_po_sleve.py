# Cvičení 1 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci cena_po_sleve(cena, sleva), která vrátí cenu
#    sníženou o slevu v procentech. cena_po_sleve(200, 25) vrátí 150.0.
#    Vypiš cenu 200 Kč se slevou 25 % a cenu 1200 Kč se slevou 10 %.

def cena_po_sleve(cena, sleva):
    print(cena*(100 - sleva)/100)


cena_po_sleve("200 Kč se slevou 25 %:", 200, 25)
cena_po_sleve("1200 Kč se slevou 10 %:",1200, 10)