
pcs = []
viruses = []
freq_vir = {}
freq_pc = {}

with open('virusy.txt', 'r') as f:
    for line in f.readlines():
        pc, virus = line.split()
        pcs.append(pc.lower())
        viruses.append(virus.strip('\n'))

for pc, virus in zip(pcs, viruses):
    if pc not in freq_vir.keys():
        freq_vir[pc] = 1
    elif pc in freq_vir.keys():
        freq_vir[pc] += 1
    if virus not in freq_pc.keys():
        freq_pc[virus] = 1
    elif virus in freq_pc.keys():
        freq_pc[virus] += 1

for v, c in freq_pc.items():
    print(f'{v} {c} times.')
for pc, n in freq_vir.items():
    if n == max(freq_vir.values()):
        print(f'Najviac napadnuty pc: {pc}')

'''
print(f'Najviac napadnuty pc: {pc for (pc, n) in freq_vir.items() if n == max(freq_vir.values())}')
'''
