from tkinter import *

master = Tk()
master.title('Spokojnost')

def jej():
    with open('spokojnost.txt', 'a') as f:
        f.write(f'Ano\n')

def joj():
    with open('spokojnost.txt', 'a') as f:
        f.write(f'Nie\n')

f = Frame(bg='grey')
f.pack()
Label(f, text='Boli ste spokojni \n s nasimi sluzbami ?', font=('arial', 50), bg='grey', highlightcolor='white').pack()
Button(f, text='Ano :)', bg='yellow', command=jej).pack(side=LEFT, pady=80, padx=100)
Button(f, text='Nie :(', bg='yellow', command=joj).pack(side=RIGHT, pady=80, padx=100)




mainloop()