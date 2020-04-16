'''
Za 15 minut som stihol iba prevod medzi desiatkovou a dvojkovou.
Uzivatelskemu rozhraniu venujem len tolko, ze na kazdu funkciu je vlastne tlacidlo, ktore cerpa cislo z jedneho vstupneho pola
'''

from tkinter import *

master = Tk()
master.title('Unit converter v.1.0')

def bin_to_dec():
    '''iterujeme zadany binarny vstup odzadu. Ak je hodnota 1 tak pripocitavame k dec hodnote mocninu cisla 2, podla pozicie
    cisla v binarnom vstupe, enumerate()'''
    bin = n.get()
    dec = 0
    for i, ii in enumerate(bin[::-1]):
        if ii == '1':
            dec += int(ii) * 2**i
    answer.configure(text=f'{bin} je v desiatkovej {dec}')

def dec_to_bin():
    '''klasicky hladame zvysok po deleni 2, ktory potom zapisujeme do bin. Bin vypisany odzadu je konecne binarne cislo'''
    dec = int(n.get())
    bin = ''
    while dec != 0:
        bin += str(int(dec)%2)
        dec = dec//2
    answer.configure(text=f'{dec} je v dvojkovej {bin[::-1]}')

def dec_to_hex():
    '''Pismena filtrujem cez ascii kody. ddec je iba aby mi ostala povodna zadana hodnota dec. K retazcu hex pridavame
    postupne zvysky po deleni 16, ktore samozrejme od 10 do 15 su pismena a,b,c,d,e,f. Na konci len upper()
    aby to bolo pekne velke '''
    dec = int(n.get())
    ddec = int(n.get())
    hex = ''
    while dec != 0:
        temp = int(dec) % 16
        if temp < 10:
            hex += str(chr(48 + temp))
        else:
            hex += str(chr(55 + temp))
        dec = dec // 16
    answer.configure(text=f'{ddec} je v sestnastkovej {hex[::-1].upper()}')

def hex_to_dec():
    '''velmi podobne ako pri bin_to_dec, avsak nasobime mocninu 16, a musime zabezpecit ako manipulovat s pismenami.
    ascii kody som si zvolil kvoli ich jednoduchemu pouzivaniu. Podmienkou filtrujem kedy sa jedna o pismeno a kedy o cislo,
    podla toho potom pridavam mocninu 16 k finalnemu vysledku'''
    hex = str(n.get()).upper()
    b = [i for i in str(hex)][::-1]
    dec = 0
    for i, ii in enumerate(b):
        if ord(ii) <= 57:
            dec += (ord(ii) - 48) * (16 ** i)
        elif ord(ii) >= 65 and ord(ii) <= 70:
            dec += (ord(ii) - 55) * (16 ** i)
    answer.configure(text=f'{hex} je v desiatkovej {dec}')


Label(text='Konvertuj medzi jedntkovymi sustavami').pack()
n = Entry()
n.pack()
Button(text='dec na bin', command=dec_to_bin).pack()
Button(text='bin na dec', command=bin_to_dec).pack()
Button(text='dec to hex', command=dec_to_hex).pack()
Button(text='hex na dec', command=hex_to_dec).pack()

answer = Label(text='tu je odpoved')
answer.pack()

mainloop()