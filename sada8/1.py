from tkinter import *

master = Tk()
master.title('Hororezance')

a = {10:100, 60:300, 75:200, 100:255, 150:188, 200:305}
kles = 0
stup = 0
ymax = []
coo = []
profil = []
for x, y in a.items():
    ymax.append(int(y))
    profil.append(y)
strop = int(max(ymax) + 10)
for x, y in a.items():
    coo.append(int(x))
    coo.append(strop - int(y))

for y, i in enumerate(ymax, start=0):
    try:
        if int(y - ymax[i - 1]) < 0:
            kles += int(y - ymax[i - 1])
        elif int(y - ymax[i - 1]) > 0:
            stup += int(y - ymax[i - 1])
    except:
        continue

print(profil)
for i, y in enumerate(profil, start=1):
    try:
        c = profil[i] - y
        if c < 0:
            kles += c
        elif c > 0:
            stup += c
        else:
            pass
    except:
        pass


canvas = Canvas(height=500)
canvas.pack()

canvas.create_line(coo)
Label(text=f'Stupanie: {stup}').pack()
Label(text=f'Klesanie: {kles}').pack()

mainloop()

