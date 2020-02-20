from tkinter import *
import random as rn

'''
dict comprehension add please
'''

quest = {}
def vote():
    for i in range(12):
        quest[i + 1] = 0
    for i in range(100000):
        quest[rn.randint(1,12)] += 1
    fld.delete(1.0, END)
    for k, v in quest.items():
        fld.insert(END, f'Cislo {k}     {v} hlasov.\n')
    for k, v in quest.items():
        if v == min(quest.values()):
            fld.insert(END, f'\n\nZo sutaze vypadne sutaziaci s cislom {k}!')

master = Tk()
master.title("Superstar v.1.0")
Button(text='Nove hlasovanie', command=vote).pack()
fld = Text(master)
fld.pack()


mainloop()
