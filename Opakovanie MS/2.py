'''
potrebne su len mesiace tak si ich hned pri vstupe vyberieme, slovnik s mesiacmi a jednoduchy print
'''

def oslavenci():
    n = int(input('Zadajte poradove cislo mesiaca (1-12):'))
    print('Zoznam oslavencov v kruzku:')
    for names in db[n]:
        print(names)

with open('kruzok.txt', 'r', encoding='utf-8') as f:
    db = {x:[] for x in range(1,13)}
    for line in f.readlines():
        name, date = line.split()
        _, month, _ = date.split('.')
        db[int(month.lstrip('0'))].append(name)
    print(db)

while True:
    oslavenci()
