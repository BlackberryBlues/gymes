from tkinter import *

master = Tk()
master.title('Animation version 1.0')

canvas = Canvas(master, width=500, height=400, bg='lightblue')
canvas.pack()

sun = canvas.create_oval(370, 10, 490, 130, fill='yellow')
cloud = canvas.create_oval(0, 70, 180, 140, fill='grey')

def go(event):
    sx, _, sxx, _ = canvas.coords(sun)
    lim = sx + (sxx - sx) / 2
    limm = 0
    while limm <= lim-50:
        cx, _, cxx, _ = canvas.coords(cloud)
        limm = cx + (cxx - cx) / 2
        canvas.move(cloud, +10, 0)
        canvas.update()
        canvas.after(100)

canvas.bind_all('<space>', go)


mainloop()
