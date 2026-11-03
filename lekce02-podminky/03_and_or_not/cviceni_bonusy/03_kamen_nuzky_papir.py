# Bonus 3 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Kámen, nůžky, papír. Zeptej se obou hráčů na tah – ať zadají
#     "kamen", "nuzky" nebo "papir". Vypiš, kdo vyhrál:
#       - "Remíza.", když mají oba stejně,
#       - jinak urči vítěze podle pravidel:
#           kámen tupí nůžky, nůžky stříhají papír, papír balí kámen.
#     Vypiš "Vyhrál hráč 1." / "Vyhrál hráč 2.".

tahhrace1 = input("Zadej kamen, nuzky nebo papir:")

tahhrace2 = input("Zadej kamen, nuzky nebo papir:")

if tahhrace1 == tahhrace2:
    print ("Remíza.")
else:
    if (tahhrace1 == "kamen" and tahhrace2 == "nuzky") or (tahhrace1 == "nuzky" and tahhrace2 == "papir") or (tahhrace1 == "papir" and tahhrace2 == "kamen"):
        print("Vyhrál hráč 1." )  
    else:
        print("Vyhrál hráč 2." ) 
        
