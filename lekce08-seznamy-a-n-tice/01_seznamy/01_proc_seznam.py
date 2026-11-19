# ---------------------------------------------
#  Proč seznam
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

# Pořádáš večírek a chceš si zapsat hosty. Zatím umíš tohle:
host1 = "Anna"
host2 = "Petra"
host3 = "Jana"

# Stejně sis v lekci 2 psala známky: znamka1, znamka2, znamka3. Co když
# přijde dalších dvacet lidí? Na každého bys potřebovala novou proměnnou
# a cyklem bys je neprošla.


# Seznam drží víc hodnot v jedné proměnné. Píše se do hranatých závorek
# a hodnoty oddělují čárky:
hoste = ["Anna", "Petra", "Jana", "Shrek"]

print(hoste)            # ['Anna', 'Petra', 'Jana']
print(len(hoste))       # 3 – počet položek v seznamu

pocethostu = len(hoste)

print ("-"* 30)
print ("Pomoci for")

for host in hoste:
    print("Zvu Vas na Vanocni vecirek", host)

print ("Prvni byla pozvana" , hoste[0])

print ("-"* 30)
print ("Pomoci range")

for i in range(pocethostu):
    print("Zvu Vas na Vanocni vecirek", hoste[i])

print ("Prvni byla pozvana" , hoste[0])

blacklist = ["Hegerova", "Vlk"]

prichozi = input("Jak se jmenujes?")

print ("-"* 30)

#for host in hoste:
#    if prichozi == host:
#        print("Pod dal:", prichozi)

def kontrola(prichozi, hoste, blacklist):
    if prichozi in hoste:
        print("pojd dal,", prichozi)
    elif prichozi in blacklist:
        print("zmiz dal,", prichozi)
    else:
        print("Nejsi zvan")

kontrola(prichozi, hoste, blacklist)

def pozvi(jmeno, hoste):
    hoste.append(jmeno)

pozvi("Vojta", hoste)
print (hoste)
hoste [5:5] = ["Tom"]
print (hoste)

def odeber_hosta (jmeno, hoste):
    hoste.remove(jmeno)

print(hoste)

odeber_hosta("Shrek", hoste)
print(hoste)

print ("-"* 30)
fronta = ["Anna", "Petra", "Jana", "Shrek"]
print(fronta)
kontrola(fronta.pop(0), hoste, blacklist)
print(fronta)


# Hodnoty stojí v pořadí, v jakém jsi je napsala, a můžou se opakovat.
# Vejdou se do něj i čísla:
#hlasy = [1, 2, 1, 1]

#print(hlasy)            # [1, 2, 1, 1]


# Do seznamu dáš jakékoli hodnoty: text, celá i desetinná čísla, True
# a False, a dokonce i další seznam:
#ruzne = ["Anna", 34, 1.5, True, ["dort", "víno"]]

#print(ruzne)            # ['Anna', 34, 1.5, True, ['dort', 'víno']]
#print(len(ruzne))       # 5 – vnitřní seznam je jedna položka

# Míchat různé druhy hodnot v jednom seznamu ale nebývá dobrý nápad.
# V cyklu bys u každé položky musela hlídat, co je zač. Obvykle má
# seznam hodnoty jednoho druhu: samá jména, samá čísla.


# Seznam může být i prázdný. Hodí se to, když hodnoty teprve přibudou:
#omluveni = []

#print(omluveni)         # []
#print(len(omluveni))    # 0
