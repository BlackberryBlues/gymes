'''
zo subora nacitame data, ako datovu strukturu pouzijeme slovnik s jednotlivymi mesiacmi
ku kazdemu mesiacu priradime do listu mena oslavencov
potom pracujeme so slovnikom a vypisujeme data
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
