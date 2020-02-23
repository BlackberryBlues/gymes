
from tkinter import *

def read():
    """I dont know how to unpack the values from single line file"""
    try:
        filename = city.get()
        with open(f'{filename}.txt', 'r') as f:
            ts = f.readlines()
            ts = [int(t.strip('\n')) for t in ts]
            print(ts)
            canvas = Canvas(width=300, height=80)
            canvas.pack()
            canvas.create_line(10, 5, 10, 75, fill='black')
            canvas.create_line(5, 70, 295, 70, fill='black')
            x = 15
            avg = round(sum(ts) / len(ts), 0)
            for i in range(len(ts)):
                y = 70
                y = y - ts[i]
                if ts[i] < avg:
                    canvas.create_oval(x, y, x + 4, y + 4, fill='blue', outline='blue')
                elif ts[i] > avg:
                    canvas.create_oval(x, y, x + 4, y + 4, fill='red', outline='red')
                elif ts[i] == avg:
                    canvas.create_oval(x, y, x + 4, y + 4, fill='green', outline='green')
                x += 9
        Label(text=f'Priemerna teplota\n{avg}').pack()
        Label(text=f'Najnizsia teplota\n{min(ts)}').pack()
        Label(text=f'Najvyssia teplota\n{max(ts)}').pack()

    except FileNotFoundError:
        with open(f'{filename}.txt', 'w') as f:
            pass


master = Tk()
master.title('Ze Temperaturen verzion 1.0')

Label(text='Vyber si mesto, bez ".txt":').pack()
city = Entry()
city.pack()
Button(text='Vykresli!', command=read).pack()








mainloop()
