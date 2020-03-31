'''
mam canvas kde pisem odpocitavanie, 4 tlacidla, kazde ma vlastnu funkciu, podla farby; funkcia judge() porovna
zvolenu farbu z tlacidla s automaticky zvolenou farbou; random.choice vyberie farbu; aby aplikacia bezala hladko
tak refresh interval je zmenseny a na obrazovke sa vyobrazuje zaokruhlene cislo; v cykle to zvykne sekat
'''

from tkinter import *
from random import *

def b():
    judge(str(winner), 'blue')

def r():
    judge(str(winner), 'red')

def y():
    judge(str(winner), 'yellow')

def g():
    judge(str(winner), 'green')

def judge(win, guess):
    global t
    if win == guess:
        current.configure(text='Bomba zneskodnena')
        t = 0


winner = choice(['blue','red','yellow','green'])
master = Tk()
master.title('No bomba...')

t = 3
current = Label(text=t, font=('arial',48), fg='red')
current.pack()
btns = Frame()
btns.pack()
Button(btns, text='Modry kablik', width=20, command=b).pack()
Button(btns, text='Cerveny kablik', width=20, command=r).pack()
Button(btns, text='Zlty kablik', width=20, command=y).pack()
Button(btns, text='Zeleny kablik', width=20, command=g).pack()

while t >= 0:
    if t < 1:
        current.configure(text='Bomba vybuchla')
        break
    else:
        current.configure(text=str(int(round(t,0))))
        current.update()
        current.after(10)
        t -= 0.01


mainloop()