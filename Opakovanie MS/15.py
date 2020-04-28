'''
Taxikar tibor. try a except na vymedzenie float a int. If na rozdelenie zaporne a nezaporne. Dalej len jednoducha podmienka a GUI
'''

from tkinter import *

master = Tk()
master.title('Taxikar v1.0')

def rechne():
    try:
        ss = int(s.get())
        if ss >= 0:
            if ss <= 19:
               l.configure(text=f'Cena za jazdu je {round(0.8*ss,1)} €')
            elif ss <= 39:
               l.configure(text=f'Cena za jazdu je {round(0.7*ss,1)} €')
            elif ss <= 59:
               l.configure(text=f'Cena za jazdu je {round(0.65*ss,1)} €')
            else:
               l.configure(text=f'Cena za jazdu je {round(0.6*ss,1)} €')
        else:
            l.configure(text='Zadaj nezaporne cislo, dakujem...')
    except:
        l.configure(text='Zadaj cele cislo, prosim...')


Label(text='Zadaj prejdenu vzdialenost v km:').pack()
s = Entry()
s.pack()
Button(text='vypocitaj cenu', command=rechne).pack()
l = Label()
l.pack()

mainloop()