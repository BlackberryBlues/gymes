'''
budeme používať dva súbory, použijeme metódu with ktorá zabezpečí krajšiu syntax a lepší exeption handling. na šifrovanie
máme vytvorenú funkciu, berie text, kľúč a informáciu či zašifrovať alebo odšifrovať. Vracia výsledný text. Texty sú
reťazce cez ktoré prechádzame for loop-om, aby sme sa dostali ku každému znaku. Ascii kód každého znaku je potom posunutý
o hodnotu kódu...
'''

def ccipher(text, key, action):
    new = ''
    if str(action).lower() == 'z':
        for letter in text:
            try:
                new += chr(ord(letter) + int(key))
            except UnicodeEncodeError:
                pass
    elif str(action).lower() == 'o':
        for letter in text:
            try:
                new += chr(ord(letter) - int(key))
            except UnicodeEncodeError:
                pass
    return new

first = input('Zadajte nazov vstupneho suboru:')
last = input('Zadajte nazov vystupneho suboru:')
key = int(input('Zadaj kluc (1-9):'))
action = str(input('Z pre zasifrovanie, O pre odsifrovanie:'))

with open(f'{first}', 'r', encoding='utf-8') as f:
    content = f.read()

with open(f'{last}', 'w', encoding='utf-8') as f:
    f.write(ccipher(content, key, action))
