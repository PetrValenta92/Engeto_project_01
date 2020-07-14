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
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
# Vyžádá si od uživatele přihlašovací jméno a heslo.
NAME = input("USERNAME: ")
PASS = input("PASSWORD: ")

# Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
if PASS != REGISTR.get(NAME):
    print("Špatné uživatelské jméno, nebo heslo. Ukončuji program. Hezký den!")
    exit()

print(SLICE)

# Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS
print(f"K analýze máš na výběr mezi {len(TEXTS)} texty.")
CHOICE = int(input("Prosím, zadej číslo textu: "))
print(SLICE)

# Pro vybraný text spočítá statistiky
chosen_text = TEXTS[CHOICE - 1]

# Počet slov
WORDS = chosen_text.split()

capital = 0  # Počet slov začínajících velkým písmenem
big = 0  # Počet slov psaných velkými písmeny
small = 0  # Počet slov psaných malými písmeny
num = 0  # Počet čísel (ne cifer!)
GRAF = {}  # Slovník ke grafu, klíč je počet písmen a hodnota ukazu kolikrát je v textu
final_number = 0  # Použiji v závěru programu

for single_word in WORDS:
    clean_word = len(single_word.strip(",."))
    GRAF.setdefault(clean_word, 1)
    GRAF[clean_word] += 1
    if single_word.istitle():
        capital += 1
    elif single_word.isupper():
        big += 1
    elif single_word.islower():
        small += 1
    elif single_word.isdigit():
        num += 1
        final_number += int(single_word)

print(f"V textu se nachází dohromady {len(WORDS)} slov.")
print(f"V textu se nachází dohromady {capital} slov, začínajících velkým písmenem.")
print(f"V textu se nachází dohromady {big} slov, psaných velkými písmeny.")
print(f"V textu se nachází dohromady {small} slov, psaných malými písmeny.")
print(f"V textu se nachází dohromady {num} číselných řetězců.")
print(SLICE)

# Program zobrazí jednoduchý sloupcový graf,
# který bude reprezentovat četnost různých délek slov v textu.

list_from_graf = sorted(GRAF.keys())

# Vytiskne graf
for word in list_from_graf:
    print(f' {word} {GRAF.get(word) * "*"} {GRAF.get(word)}')

print(SLICE)

# Program spočítá součet všech čísel (ne cifer!) v textu.
print(f"Pokud sečteme všechna čísla v textu dostaneme: {final_number}.")
print()
