'''
Postup riesenia ulohy som zvolil nasledovne. Funkcia fall() vykresli vajicko, generuje nahodne pismeno na zaklade ascii
charakterov, a animuje vajicko ako pada. Funkcia run() kontroluje ci vajicko nepadlo na zem. Ak padlo tak sa program zastavi
a vypise game over. programovat s udalostami na klaavesnici mi na mojom pc nefungovalo. Program je responzivny na zmenu
rozmerov hracieho okna.
'''

from tkinter import *
import random as rn

m_width = 200
m_height = 400

canvas = Canvas(width=m_width, height=m_height)
canvas.pack()

def check(event):
    '''Malo by porovnat stlaceny klaves s nahodne generovanym pismenkom, nefungovalo to neviem preco, TypeError: missing 1 required positional argument: event...'''
    global pismenko
    if event.keysym == pismenko:
        return True
    return False

def run():
    '''kontroluje kedy vajco padne na zem'''
    global vajco, m_height
    *_, y = canvas.coords(vajco)
    if y < m_height:
        return True
    return False

def end():
    '''vymaze vajicko pismenko '''
    canvas.delete(vajco)
    canvas.delete(pismenko)
    
def fall():
    '''generuje random pismenko, kresli a animuje vajicko'''
    global vajco, pismenko
    guess_me = chr(rn.randint(97, 122))
    x = rn.randint(0, m_width - 20)
    vajco = canvas.create_oval(x, 10, x + 20, 50)
    pismenko = canvas.create_text(x + 10, 30, text=guess_me, fill='black')

    while run():
        if check():
            end()
            fall()
        canvas.move(vajco, 0, +10)
        canvas.move(pismenko, 0, +10)
        canvas.update()
        canvas.after(100)

    end()
    canvas.destroy()
    print('Game over')

canvas.bind_all('<Key>', check)
fall()