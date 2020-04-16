'''
nacitame data, rozdelime cez split, ulozime do slovnika {skok:[meno]}, druhy slovnik pre
krajiny iba s menami {krajina:[meno, meno, meno, meno...]}. Z prvej vieme urcit uplneho vitaza, ked ich je viac tak
rovnako bez problemov, z druheho slovnika vyberieme sutaziace krajiny a pocet sutaziacich.
*perf nam vrati list vsetkych skokov, z ktoreho potom vyberieme uz len ten najlepsi...
'''

db = {}
dbb = {}

with open('skok_do_dialky.txt', 'r') as f:
    for line in f.readlines():
        name, ccode, *perf = line.split()
        if max(perf) not in db.keys():
            db[max(perf)] = []
        db[max(perf)].append(name)
        if ccode not in dbb.keys():
            dbb[ccode] = []
        dbb[ccode].append(name)
    print(db)
    print(dbb)
    print('Sutaziaci boli z nasledujucich krajin:')
    [print(f'\t{c}', end=' ') for c in dbb.keys()]
    print('\nV poctoch:')
    [print(f'\t{c}: {len(n)}') for c,n in dbb.items()]
    for v,name in db.items():
        if v == max(db.keys()):
            print(f'Vitaz celkovo: ')
            [print(f'\t{n}') for n in name]
