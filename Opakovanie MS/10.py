'''
z textoveho suboru nacitame data do dvoch listov, ktore sa nam budu lahsie triedit podla poctu bodov. Zip() funkcia umozni
iterovat cez viacero listov naraz co je v spojeni s funkciou sort(list) hlavny dovod preco som si zvolil dva listy a nie slovnik.
Nacitane a zoradene data podla poctu bodov potom v jednom for cykle vypiseme. Enumerate() da listom index a [::-1] ich
zoradi opacne, teda od najvacsieho poctu bodov po najmensi v nasom pripade. Fake ti till you make it.
'''

with open('preteky.txt', 'r') as f:
    names = []
    points = []
    for line in f.readlines():
        name, time = line.split()
        pnts = 1000 - (100*float(time))
        names.append(name)
        points.append(pnts)
    points, names = zip(*sorted(zip(points, names)))
    print('Konecne umiestnenie v slalome:')

    for i, (name, point) in enumerate(zip(names[::-1], points[::-1]), start=1):
        print(f'{i}.miesto\t{name}\t{point} bodov')