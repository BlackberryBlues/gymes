
mena = []
good = []
bad = []
with open('5a.txt','r', encoding='utf-8') as f:
    for line in f.readlines():
        name, surname, g, b = line.split()
        mena.append(f'{name} {surname}')
        good.append(int(g))
        bad.append(int(b))

print(f'Priemer ospravedlnenych: {round(sum(good)/len(good), 2)}')
print(f'Priemer neospravedlnenych: {round(sum(bad)/len(bad), 2)}')
print('Ziaci s neospravedlnenymi hodinami:')
for m, b in zip(mena, bad):
    if b > 0:
        print(m)