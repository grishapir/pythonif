from tkinter import *



def jak():
    btn.configure(text= ent.get())
    lbl.configure(text= "Не нажимать!")
window = Tk()
window.title("Привет")
window.geometry('400x400')
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
btn = Button(window, text= "Не нажимать!", command=jak)
ent = Entry(window, width = 10)
ent.focus()
newText = ent.get()






lbl.pack()
ent.pack()
btn.pack()
window.mainloop()