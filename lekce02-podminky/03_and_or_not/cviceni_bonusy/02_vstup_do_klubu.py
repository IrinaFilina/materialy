# Bonus 2 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Vstup do klubu. Dovnitř smí ten, komu je aspoň 18 let A ZÁROVEŇ
#     je buď členem, NEBO má pozvánku.
#     Kdo má zákaz vstupu, dovnitř nesmí nikdy – ani člen, ani s pozvánkou.
#     Zamysli se, kam patří závorky, aby podmínka fungovala správně.
#     Vypiš "Vítej v klubu." / "Dnes se nedostaneš.".
vek = 17
je_clen = True
ma_pozvanku = False
ma_zakaz = False

if vek >= 18 and (je_clen == True or ma_pozvanku == True) and not (ma_zakaz == True):
    print ("Vítej v klubu.")
else:
    print("Dnes se nedostaneš.")

