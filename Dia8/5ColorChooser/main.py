from tkinter import *
from tkinter import colorchooser

def click():
    # color = colorchooser.askcolor()
    # colorHexa = color[1]
    # print(colorHexa)
    windows.config(bg=colorchooser.askcolor()[1])

windows = Tk()
windows.geometry("420x420")
boton = Button(text="Haz click aqui", command=click)
boton.pack()

windows.mainloop()