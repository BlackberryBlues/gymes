'''
Menej ako 10 minut. Najskor otvoreny subor na citanie, potrebujeme iba krajiny tak si ich dame do zoznamu
ktory potom zoradime podla abecedy. Potom otvorim subor na pisanie a postupne vkladam staty. Premenna sa
vola mesta a mesto, i ked su v nich ulozene staty... az teraz som si vsimol
'''

with open('mesta1.txt', 'r', encoding='utf-8') as f:
    mesta = []
    for line in f.readlines():
        _, mesto = line.split(';')
        mesta.append(mesto.strip('\n'))
    mesta.sort()

with open('krajiny.txt', 'w', encoding='utf-8') as f:
    for mesto in mesta:
        f.write(f'{mesto}\n')