from tkinter import *

def odraz(h, p):
    global skoky
    skoky = []
    while h > 0.01:
        h = h * p * 0.01
        skoky.append(round(h, 2))


def start():
    h = float(height.get())
    p = float(percent.get())
    odraz(h, p)
    print(skoky)
    fall(h, skoky)


def fall(h, lst):
    x = 90
    y = 20
    ball = canvas.create_oval(x, y, x + 20, y + 20, fill='red')
    for i in range(len(lst)):
        *_, y = canvas.coords(ball)
        while y < 400.0:
            """falling"""
            *_, y = canvas.coords(ball)
            canvas.move(ball, 0, +5)
            canvas.update()
            canvas.after(10)
        *_, y = canvas.coords(ball)
        while y > 400 - 400 * 0.01 * float(lst[i]) * 100 / h:
            """rising"""
            *_, y = canvas.coords(ball)
            canvas.move(ball, 0, -5)
            canvas.update()
            canvas.after(10)

master = Tk()

Label(master, text='Pociatocna vyska:').pack()
height = Entry()
height.pack()
Label(text='Percento odrazu v %:').pack()
percent = Entry()
percent.pack()
Button(text='Start', command=start).pack()

canvas = Canvas(width=200, height=400)
canvas.pack()




mainloop()

mainloop()