from random import *

name = input('Deine Name bittschön:')
tips = []
for i in range(7):
    if i == 6:
        t = input('Zusatzliche Zahl jetzt bitte:')
        tips.append(int(t))
    else:
        t = input('Bitte dein Tip:')
        tips.append(int(t))

with open(f'{name}.txt','w') as f:
    for t in tips:
        f.write(f'{t}\n')

final = []
while len(final) != 7:
    x = randint(1,10)
    if x not in final:
        final.append(int(x))

with open(f'final_loterry.txt','w') as f:
    for t in final:
        f.write(f'{t}\n')

score = 0
for i in range(7):
    print(i)
    if i == 6:
        if tips[i] == final[i]:
            if score == 5:
                print('2. Poradie')
            elif score == 6:
                print('Superjackpot')
    if tips[i] in final[:6]:
        score += 1

print(tips)
print(final)
print(f'Mali ste {score} spolocnych.')