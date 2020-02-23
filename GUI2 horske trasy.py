from tkinter import *

def read():
    """I dont know how to unpack the values from single line file"""
    global canvas
    filename = route.get()
    with open(f'{filename}.txt', 'r') as f:
        for line in f:
            hs = line.split(',')
            hs = [int(h.strip('\n')) for h in hs]
        print(f'Najnizsi bod: {min(hs)}')
        wid = master.winfo_width()
        canvas = Canvas(height=400, width=wid)
        canvas.pack()
        canvas.delete('all')
        floor = 300
        plt = []
        x = 10
        k = wid/len(hs)
        for h in hs:
            plt.append(x + k)
            plt.append(floor - (h / 10))
            x += k
        canvas.create_line(plt)




master = Tk()
master.title('Turista v1.2')

Label(text='Zadaj trasu, bez ".txt":').pack()
route = Entry()
route.pack()
Button(text='Zobraz trasu!', command=read).pack()
wid = master.winfo_width()



mainloop()
