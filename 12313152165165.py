from tkinter import *
import random


c = 0
o = 0
m = 0
def rock():
    global c, o
    b = 1
    a = random.randint(1, 3)
    if a == 1:
        print('Камень')
    elif a == 2:
        print('Ножницы')
    elif a == 3:
        print('Бумага')
    if a == 1 and b == 1:
        lbl.configure(text="Draw")
    if a == 2 and b == 1:
        lbl.configure(text="You win")
        c = c + 1
    if a == 3 and b == 1:
        lbl.configure(text="You lose")
        o = o + 1
def scissors():
    global c, o
    b = 2
    a = random.randint(1, 3)
    if a == 1:
        print('Камень')
    elif a == 2:
        print('Ножницы')
    elif a == 3:
        print('Бумага')
    if a == 1 and b == 2:
        lbl.configure(text="You lose")
        o = o + 1
    if a == 2 and b == 2:
        lbl.configure(text="Draw")
    if a == 3 and b == 2:
        lbl.configure(text="You win")
        c = c + 1
def paper():
    global c, o
    b = 3
    a = random.randint(1, 3)
    if a == 1:
        print('Камень')
    elif a == 2:
        print('Ножницы')
    elif a == 3:
        print('Бумага')
    if a == 1 and b == 3:
        lbl.configure(text="You win")
        c = c + 1
    if a == 2 and b == 3:
        lbl.configure(text="You lose")
        o = o + 1
    if a == 3 and b == 3:
        lbl.configure(text="Draw")
    
def po():
    global m
    
    lbl1 = Label(window, text=o, font=("Arial Bold", 20)) 
    lbl2 = Label(window, text=c, font=("Arial Bold", 20))
    if m > 0:
        lbl1.destroy()
        lbl2.destroy()
        m=0
    lbl1.pack(side=LEFT)
    lbl2.pack(side=RIGHT)
    m +=1
    
window = Tk()
window.title("Выбери")
window.geometry('400x400')
lbl = Label(window, text='Выбери', font=("Arial Bold", 50)) 
btn = Button(window, text='Камень', command=rock) 
btn1 = Button(window, text='Ножницы', command=scissors) 
btn2 = Button(window, text='Бумага', command=paper)
#btn3 = Button(window, text='Посмотреть счет', command=po)
lbl.pack()
btn.pack()
btn1.pack()
btn2.pack()
#btn3.pack()
window.mainloop()







