import numpy as np
import matplotlib.pyplot as plt

with open('spokojnost.txt', 'r') as f:
    spoko = [line.strip('\n') for line in f.readlines()]

print(f'Celkovy pocet hlasuijucich: {len(spoko)}')
print(f"\tSpokojni:\t{round(spoko.count('ano')/len(spoko)*100, 2)}%")
print(f"\tNespokojni:\t{round(spoko.count('nie')/len(spoko)*100, 2)}%")

obj = ['Spokojni', 'Nespokojni']
y_pos = np.arange(len(obj))
stats = [int(spoko.count('ano')), int(spoko.count('nie'))]

plt.bar(obj, stats, align='center')
plt.title('Spokojnost zakaznikov')
plt.ylabel('Pocet zakaznikov')
plt.show()