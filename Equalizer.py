from tkinter import *
import random as rn

master = Tk()
canvas = Canvas(master, width=1000, height=700)
canvas.pack()

floor = 400

def block(x, y, floor):
    canvas.create_rectangle(x, y, x + 40, floor, fill='green')

def plot():
    canvas.delete('all')
    for i in range(60,600,50):
        block(i, rn.randint(10, 300),floor)
    canvas.update()
    canvas.after(1000)




Button(text='Try me', command=plot).pack()

mainloop()

