# Jednoduchý textový analyzátor
# Vytvoří statistiku k vybranému textu

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# Grafické oddělení statistik
SLICE = 80 * "="

# Na začátku přivítá uživatele.
print(SLICE)
print("Vítej v mojí aplikaci. Prosím, nejdříve se přihlaš:")

# Seznam registrovaných uživatelů
REGISTR = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
                }
# Vyžádá si od uživatele přihlašovací jméno a heslo.
NAME = input("USERNAME: ")
PASS = input("PASSWORD: ")

# Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
while REGISTR:
    if PASS == REGISTR.get(NAME):
        break
    else:
        print("Špatné uživatelské jméno, nebo heslo. Ukončuji program. Hezký den!")
        exit()

print(SLICE)

# Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS
print("K analýze máš na výběr mezi 3 texty.")
CHOICE = int(input("Prosím, zadej číslo 1-3: "))
print(SLICE)

# Pro vybraný text spočítá statistiky
TEXTIK = TEXTS[CHOICE-1]

# Počet slov
WORDS = TEXTIK.split()
print(f"V textu se nachází dohromady {len(WORDS)} slov.")

CAPITAL = 0     # Počet slov začínajících velkým písmenem
BIG = 0         # Počet slov psaných velkými písmeny
SMALL = 0       # Počet slov psaných malými písmeny
NUM = 0         # Počet čísel (ne cifer!)

while WORDS:
    WORDY = WORDS.pop(0)
    if WORDY.istitle() == True:
        CAPITAL += 1
    elif WORDY.isupper() == True:
        BIG += 1
    elif WORDY.islower() == True:
        SMALL += 1
    elif WORDY.isdigit() == True:
        NUM += 1

print(f"V textu se nachází dohromady {CAPITAL} slov, začínajících velkým písmenem.")
print(f"V textu se nachází dohromady {BIG} slov, psaných velkými písmeny.")
print(f"V textu se nachází dohromady {SMALL} slov, psaných malými písmeny.")
print(f"V textu se nachází dohromady {NUM} číselných řetězců.")
print(SLICE)

# Program zobrazí jednoduchý sloupcový graf,
# který bude reprezentovat četnost různých délek slov v textu.
SPAM = TEXTIK.split()

GRAF = {}

# Smyčka vytvoří slovník kde klíč je počet písmen a hodnota je ukazuje
# kolikrát je v textu
while SPAM:
    EGGS = SPAM.pop(0)
    BACON = len(EGGS.strip(".,"))
    if BACON not in GRAF:
        GRAF.setdefault(BACON, 1)
    else:
        GRAF[BACON] = GRAF[BACON] + 1

# Vytiskne graf
for slovo, opakovani in GRAF.items():
    print(str(slovo), str((opakovani * "*")), str(opakovani))

print(SLICE)

# Program spočítá součet všech čísel (ne cifer!) v textu.
CISLA = TEXTIK.split()

CISILKO = 0

while CISLA:
    NUMB = CISLA.pop(0)
    if NUMB.isdigit() == True:
        CISILKO += int(NUMB)

print(f"Pokud sečteme všechna čísla v textu dostaneme: {CISILKO}.")
print(SLICE)













