# Bonus 2 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá číslo N. Vypiš z hvězdiček trojúhelník vysoký N –
#     první řádek "*", druhý "**", ... N-tý má N hvězdiček.
#     (Nápověda: text se dá opakovat: "*" * 3 je "***")

n = int(input("Zadejte cislo N:"))

for radek in range (1, n+1):
    print ("*" * radek)