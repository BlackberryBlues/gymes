
with open('sms.txt', 'r') as f:
    """maaan list comprehension"""
    db = [char for char in f.read()]

print(f'Povodna sprava:\n{"".join(i for i in db)}\n')
print(f"Analyza:\n   Pocet znakov: {len(db)}\n   Pocet medzier: {db.count(' ')}\n"
      f"   Pocet sprav pred stlacenim: {(len(db) // 160) + 1}\n")

msg = ''
l = False
for i, znak in enumerate(db, start=1):
    if l == True:
        msg += znak.upper()
        l = False
        continue
    if i == 1 and znak.islower():
        msg += znak.upper()
        continue
    if znak == ' ':
        l = True
        continue
    if znak.islower():
        msg += znak
    else:
        msg += znak

print(f'Vysledna sprava\n{msg}')
