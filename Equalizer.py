from tkinter import *
import random as rn

master = Tk()
canvas = Canvas(master, width=700, height=500, bg='black')
canvas.pack()
vals = ['31', '62', '125', '250', '500', '1K', '2K', '4K', '8K', '16K', '[Hz]']
floor = 400


def block(x, y, floor):
    if y < 100:
        canvas.create_rectangle(x, 200, x + 40, floor, fill='green')
        canvas.create_rectangle(x, 100, x + 40, 200, fill='yellow')
        canvas.create_rectangle(x, y, x + 40, 100, fill='red')
    elif y < 200:
        canvas.create_rectangle(x, 200, x + 40, floor, fill='green')
        canvas.create_rectangle(x, y, x + 40, 200, fill='yellow')
    else:
        canvas.create_rectangle(x, y, x + 40, floor, fill='green')


def plot():
    canvas.delete('all')
    for i in range(60,600,50):
        if i != 560:
            block(i, rn.randint(10, 300),floor)
        canvas.create_text(i + 20, 420, text=vals[i//50 - 1], font=(20), fill='green')
    canvas.update()
    canvas.after(50)

for i in range(20):
    plot()

'''
Button(text='Try me', command=plot).pack()
'''

mainloop()
