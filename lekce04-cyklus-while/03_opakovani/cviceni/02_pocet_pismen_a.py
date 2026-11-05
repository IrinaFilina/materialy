# Cvičení 2 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá slovo. Spočítej, kolikrát se v něm objeví
#    písmeno "a", a výsledek vypiš.

slovo = input("Zadejte slovo: ")
pocetpismen = 0
for pismeno in slovo:
    if pismeno == "a":
        pocetpismen = pocetpismen + 1
print ("slovo", slovo, "obsahuje", pocetpismen, "pismen a")
