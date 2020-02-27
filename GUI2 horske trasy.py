from tkinter import *

def plot():
    try:
        with open(f'{fname.get()}.txt', 'r') as f:
            try:
                h = [int(i) for i in f.read().split(',')]
            except:
                print('Chyba pri nacitani suboru')               
        h_min = min(h)
        h_max = max(h)
        print(f'Najmensia nadmorska vyska na useku trasy je: {h_min} m.n.m.')

        k = 5
        lauf = []
        floor = 400
        span = round(550 / len(h), 2)
        for i in range(len(h)):
            lauf.append(span * (i + 1))
            lauf.append(floor - (h[i] / 10))
            if h[i] == h_min:
                mi = [span * (i + 1) - k, floor - (h[i] / 10) - k, span * (i + 1) + k,floor - (h[i] / 10) + k]
            if h[i] == h_max:
                mx = [span * (i + 1) - k, floor - (h[i] / 10) - k, span * (i + 1) + k,floor - (h[i] / 10) + k]
        canvas.delete(ALL)
        canvas.create_line(lauf)
        canvas.create_oval(mi, fill='blue')
        canvas.create_oval(mx, fill='red')
        Label(text=f'Minimum (blue): {h_min}, Maximum (red): {h_max}').pack()
        
    except:
                print('Neplatny nazov suboru')




master = Tk()
master.title('Turista v1.0')
Label(text='Zadaj nazov suboru s trasou [bez ".txt"; idealne csv]:').pack()
fname = Entry()
fname.pack()
Button(text='Zobraz trasu', command=plot).pack()
canvas = Canvas(height=500, width=600)
canvas.pack()

mainloop()
