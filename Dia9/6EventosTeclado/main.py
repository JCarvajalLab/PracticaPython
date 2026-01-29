from tkinter import *

def funcion(event):
    # print("Haz presionado: "+ event.keysym)
    label.config(text=event.keysym)

windows = Tk()

windows.bind("<Key>",funcion)

label = Label(windows, font=("Helvetica",100))
label.pack()

windows.mainloop()