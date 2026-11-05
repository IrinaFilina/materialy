# Bonus 1 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Kámen, nůžky, papír – znáš z bonusu v lekci 2, kde hráli
#     dva lidé. Teď to rozšíříme: hraješ proti počítači a na víc kol.
#     - Zeptej se na svůj tah: "kamen", "nuzky" nebo "papir".
#     - Počítač si tah vylosuje: randrange(1, 4) vrátí 1, 2 nebo 3,
#       tak si to číslo přelož na tah (1 = kamen, 2 = nuzky, 3 = papir).
#     - Vypiš, co hrál počítač, a kdo kolo vyhrál.
#     - Pak se zeptej "Hrát znovu? (ano/ne) " a podle odpovědi
#       buď pokračuj, nebo skonči.
#     Kdo koho poráží: kámen tupí nůžky, nůžky stříhají papír,
#     papír balí kámen.
#     Nahoru na první řádek nezapomeň:  from random import randrange

from random import randrange

while True:
    tahhrace = input("Zadej kamen, nuzky nebo papir:")

# tah pocitace a prelozeni tahu z cisel do nazvu
    tahpocitace = randrange(1, 4)

    if tahpocitace == 1:
        tahpocitace = 'kamen'
    elif tahpocitace == 2:
        tahpocitace = 'nuzky'
    else: 
        tahpocitace = 'papir'

    print("Pocitac zahral:", tahpocitace)
    print("Zahral(a) ste:", tahhrace)

    if tahhrace == tahpocitace:
        print ("Remíza.")
    else:
        if (tahhrace == "kamen" and tahpocitace == "nuzky") or (tahhrace == "nuzky" and tahpocitace == "papir") or (tahhrace == "papir" and tahpocitace == "kamen"):    
            print("Vyhrál jsi." )  
        else:
            print("Vyhrál PC." ) 

    znovu = input("Hrát znovu? (ano/ne) ")
    if znovu == "ne":
        break
    
    print("Díky za hru!")
    
        