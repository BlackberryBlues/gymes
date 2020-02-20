#Hanka a jej jogurtíky

from tkinter import *

master = Tk()
master.title('Jogurtovac')

def jo():
    n = int(amount.get())
    c = float(cena.get())
    if n <= 40:
        vysl = n * c
    elif n <= 100:
        vysl = (40 * c) + ((n - 40) * c * 0.8)
    else:
        vysl = (40 * c) + (60 * c * 0.8) + ((n - 100) * c * 0.6)
    fin.configure(text=f'Cena nakupu je {vysl}€')


Label(text='Pocet Jogurtov:').pack()
amount = Entry()
amount.pack()
Label(text='Jednotkova cena:').pack()
cena = Entry()
cena.pack()
Button(text='Cena nakupu:', command=jo).pack()
fin = Label(text='')
fin.pack()

mainloop()