'''
BMI kalkulacka. Niet co vysvetlovat. Vzorec, GUI a rozvinuta podmienka
'''

from tkinter import *

master = Tk()
master.title('BMI v1.0')

def bmi():
    b = round((float(m.get())/(float(h.get())**2)),1)
    if b < 18.5:
        l.configure(text=f'BMI = {b}\n Mas podvahu')
    elif b < 25:
        l.configure(text=f'BMI = {b}\n Mas normalnu hmotnost')
    elif b < 30:
        l.configure(text=f'BMI = {b}\n Mas nadvahu')
    else:
        l.configure(text=f'BMI = {b}\n Si obezny')

Label(text='Zadaj hmotnost v kg:').pack()
m = Entry()
m.pack()
Label(text='Zadaj vysku v m:').pack()
h = Entry()
h.pack()
Button(text='BMI', command=bmi).pack()
l = Label()
l.pack()

mainloop()