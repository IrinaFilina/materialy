# Bonus 1 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá číslo N. Spočítej cyklem jeho faktoriál –
#     tedy 1 * 2 * 3 * ... * N – a výsledek vypiš.
#     (Faktoriál z 5 je 120.)

N = int(input("Zadej cislo N:"))
factorial = 1
for i in range (1, N+1):
    factorial = factorial * i
print (factorial)
