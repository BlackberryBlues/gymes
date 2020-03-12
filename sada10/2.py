with open('vylety.txt', 'r', encoding='utf-8') as f:
    loc = []
    l = 0
    t = 0
    for line in f.readlines():
        *_, km, time, miesto = line.split()
        loc.append(miesto)
        l += float(km)
        t += int(time)

    print('Jednotlive ciele:')
    for m in loc:
        print(f'\t{m}')

    print(f'Trvanie cesty: {t//60} hod. {t%60} min.')
    print(f'Priemerna rychlost: {round(l/t*60, 2)} km/h')





