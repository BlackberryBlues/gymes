from random import *

priklady = []
este = []
ev = []
vysl = []

def generate():
    for i in range(10):
        x = randint(1, 10)
        y = randint(1, 10)
        z = x * y
        priklady.append(f'{x} * {y} =')
        vysl.append(int(z))

generate()
points = 0
for item, v in zip(priklady, vysl):
    n = input(item)
    if int(n) == int(v):
        print('Spravne')
        points += 1
    else:
        este.append(item)
        ev.append(v)

for item, v in zip(este, ev):
    n = input(item)
    if int(n) == int(v):
        print('Spravne')

print(f'Ziskali ste {points} bodov.')

with open('nasobilka_vystup.txt', 'w') as f:
    for item, v in zip(priklady, vysl):
        f.write(f'{item} {v}\n')