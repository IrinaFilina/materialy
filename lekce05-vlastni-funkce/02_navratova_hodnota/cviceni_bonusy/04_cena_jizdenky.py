# Bonus 4 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci cena_jizdenky, která má na vstupu věk cestujícího
#     a základní cenu jízdenky, a vrátí cenu, kterou cestující zaplatí:
#
#       děti do 10 let včetně       zdarma
#       mládež do 18 let včetně     polovina
#       senioři od 65 let včetně    třetina
#       ostatní                     plná cena
#
#     Vyzkoušej ji pro několik věků a ceny vypiš.

def cena_jizdenky(vek, cena):
    if vek <= 10:
        return 0
    elif vek > 10 and vek <= 18:
        return cena/2
    elif vek > 18 and vek < 65:
        return cena
    elif vek >= 65:
        return cena/3

print(cena_jizdenky(9, 24))
print(cena_jizdenky(18, 24))
print(cena_jizdenky(35, 24))
print(cena_jizdenky(67, 24))