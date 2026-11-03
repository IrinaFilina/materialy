def cena_mhd(vek):
    if vek < 6:
        print ("Cena je 0!")
        return 0
    elif vek < 18:
        print ("Cena je 39!")
        return 39
    elif vek < 65:
        print ("Cena je 50!")
        return 50
    else:
        print ("Cena je 0!")
        return 0


zustatek_uctu = 150
cena_jizdenky = cena_mhd(30)
print("Vysledna cena je", cena_jizdenky)
zustatek_uctu = zustatek_uctu - cena_jizdenky
print("Zustatek na uctu je ", zustatek_uctu)
