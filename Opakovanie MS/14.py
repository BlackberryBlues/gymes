'''
Kontrola palindromu. Porovnavame retazec a jeh oobratenu hodnotu, prectanu odzadu. Vyplyva to z definicie palindromu.
'''

from tkinter import *

master = Tk()
master.title('Palindrom v1.0')

def test():
    if str(slovo.get()) == str(slovo.get())[::-1]:
        l.configure(text='Slovo je palindrom')
    else:
        l.configure(text='Slovo nie je palindrom')

Label(text='Napis slovo:').pack()
slovo = Entry()
slovo.pack()
Button(text='Test na palindrom', command=test).pack()
l = Label()
l.pack()

mainloop()