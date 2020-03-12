def format_min(minutes):
    return f'{int(minutes)//60}:{int(minutes)%60}'

def format_spd(km, time):
    return f'{round(float(km)/int(time)*60, 2)}'

with open('vylety.txt', 'r', encoding='utf-8') as f:
    print(f'Jednotlive ciele:')
    for line in f.readlines():
        *_, km, time, miesto = line.split()
        print(f'\t{miesto}\t{format_min(time)}\t{format_spd(km,time)}')





