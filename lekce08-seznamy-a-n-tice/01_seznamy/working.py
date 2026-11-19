organizator = "Karel Gott"

inicialy = ""
for slovo in organizator.split():
    inicialy = inicialy + slovo[0] + "."

print(inicialy)

inicialy = []
for slovo in organizator.split():
    inicialy.append(slovo[0] + ".") 

print("".join(inicialy))


