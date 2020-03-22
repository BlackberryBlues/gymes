from tkinter import *

def login():

    if str(n.get()) in db.keys() and str(p.get()) == str(db[n.get()]):
        master2 = Tk()
        master2.title('LOGIN')
        Label(master2, text='Uspesne prihlasenie, mozes pouzivat tento program!').pack()
        Button(master2, text='OK').pack()
    else:
        status.configure(text='Nespravvne meno alebo heslo, zadaj nove!')

with open('hesla.txt', 'r') as f:
    db = {}
    for line in f.readlines():
        name, psw = line.split()
        db[name] = psw.strip('\n')

master = Tk()
master.title('Tester v.1.0')

Label(text='Prihlasovacie meno:').pack()
n = Entry()
n.pack()
Label(text='Prihlasovacei heslo:').pack()
p = Entry(show='*')
p.pack()
Button(text='Potvrd', command=login).pack()
status = Label()
status.pack()

mainloop()