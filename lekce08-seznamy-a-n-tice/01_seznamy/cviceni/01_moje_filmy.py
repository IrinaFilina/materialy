# Cvičení 1 – Seznamy
# Doplň kód pod zadání a soubor spusť (Run).

# Vytvoř seznam pěti svých oblíbených filmů. Vypiš:
#    - první film,
#    - poslední film,
#    - první tři filmy jako výřez,
#    - všechny filmy, každý na vlastní řádek s pomlčkou na začátku,
#    - kolik filmů v seznamu je.

filmy = ["Kill Bill", "Forrest Gump", "The Shawshank Redemption", "Schindler's List", "The Dark Knight"]

print("*" * 30)
print("Prvni film:")
print (filmy[0])
# pocetfilmu = len(filmy)
# print (filmy[pocetfilmu-1])
print("*" * 30)
print("Poslední film:")
print(filmy[-1])
print("*" * 30)
print("První tři filmy jako výřez:")
print(filmy[:3])
print("*" * 30)
print("Všechny filmy, každý na vlastní řádek s pomlčkou na začátku:")
for film in filmy:              # položky po jedné
    print(f"{film}")
print("*" * 30)
print("Kolik filmů v seznamu je")
pocetfilmu = len(filmy)
print(pocetfilmu)