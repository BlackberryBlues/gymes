'''
na ulozenie dat pouzijeme slovnik, kde kluc je farebne oznacenie jedla a atribut je zoznam id cisel jednotlivych stravnikov.
je to najefektivnejsi sposob zistenia poctu stravnikov jednotlivych jedal.
jednoducha konstanta nam pomoze pri zisteni poctu stravnikov, dlzky zoznamov v slovniku udaju pocet stravnikov jednotlivych
jedal.
'''

with open('objednane_jedla.txt', 'r') as f:
    data = {}
    c = 0
    for line in f.readlines():
        c += 1
        id, food = line.split()
        if food not in data.keys():
            data[food] = [id]
        else:
            data[food].append(id)

    print(f'Pocet stravnikov:\n\t{c}')
    print(f'''Jednotlive jedla:
    Zelena: {len(data["z"])}
    Cervena: {len(data["c"])}
    Modra: {len(data["m"])}
    Oranzova: {len(data["o"])}''')

    for key in data.keys():
        if len(data[key]) > 20:
            if key == 'o':
                print('Kazde jedlo si objednal dostatok stravnikov')
            continue
        print(f'Jedlo farby |{key}| si objednalo menej ako 20 zakaznikov')
