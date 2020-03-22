
def conversion(date):
    y = date[:4]
    m = date[4:6]
    d = date[6:8]
    return f'{d}.{m}.{y}'

with open('zamestnanci.txt', 'r', encoding='utf-8') as f:
    dates = []
    names = []
    for line in f.readlines():
        date, *name = line.split()
        dates.append(date)
        names.append(name)
    print(f'Pocet zamestnancov v zozname: {len(names)} \nNastupili:')
    for date, name in zip(dates, names):
        print(f'\n{conversion(date)}', end='\t')
        for n in name:
            print(n, end='   ')

