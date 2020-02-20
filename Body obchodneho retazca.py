from tkinter import *


def load():
    fld.delete(1.0, END)
    try:
        with open(f'{filename.get()}.txt','r') as f:
            for line in f.readlines():
                name, points = line.split()
                if name not in db.keys():
                    db[name] = int(points)
                else:
                    db[name] += int(points)
            for name, points in db.items():
                fld.insert(END, f'{name}\t\t{points}\n')
    except:
        fld.insert(END, f'Nespravne meno suboru')

def verni():
    fld.delete(1.0,END)
    if submit.get() == 'ano':
        with open('verni.txt', 'w') as f:
            for name, points in db.items():
                if points >= 20:
                    f.write(f'{name}\n')
            ls = [name for name in db.keys()]
            ls.sort()
            for name in ls:
                fld.insert(END, f'{name}\t\t{db[name]}\n')
    else:
        fld.insert(END, f'Napis ano alebo nie')




master = Tk()
master.title('Punkte')

db = {}
Label(text='Nazov textoveho suboru:').pack()
filename = Entry()
filename.pack()
Button(text='Nacitaj', command=load).pack()
fld = Text()
fld.pack()
Label(text='Chces abecedny vypis vernych zakaznikov? ano/nie').pack()
submit = Entry()
submit.pack()
Button(text='Nacitaj', command=verni).pack()


mainloop()
