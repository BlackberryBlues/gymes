'''
jednoduchy Tkinter interfejs; uzivatelske rozhranie; zabezpecenie aby bol vstup cele cislo; potom porovname
hodnoty jednotlivych stran a postupne vypiseme co je potrebne
'''

from tkinter import *

def istriangle():
    s.configure(text='')
    ss.configure(text='')
    try:
        a = int(aa.get())
        b = int(bb.get())
        c = int(cc.get())
        if a+b>=c and a+c>=b and b+c>=a:
            s.configure(text='Cisla su stranami trojuholnika')
            if a==b and b==c:
                ss.configure(text='Rovnostranny trojuholnik')
            if a==b or a==c or c==b:
                ss.configure(text='Rovnoramenny trojuholnik')
        else:
            s.configure(text='Cisla nie su stranami trojuholnika')
    except:
        s.configure(text='Zadajte prosim cele cisla...')


master = Tk()
master.title('Trojuhoolnik v.1.0')

Label(text='Zadaj strany trojuholnika:').pack()
Label(text='strana a:').pack()
aa = Entry()
aa.pack()
Label(text='strana b:').pack()
bb = Entry()
bb.pack()
Label(text='strana c:').pack()
cc = Entry()
cc.pack()
Button(text='Otestuj trojuholnik', command=istriangle).pack()
s = Label()
s.pack()
ss = Label()
ss.pack()


mainloop()
