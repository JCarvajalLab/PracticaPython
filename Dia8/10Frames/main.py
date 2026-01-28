from tkinter import *

windows = Tk()

marco = Frame(windows,bg="pink", bd=5, relief=SUNKEN)
marco.pack()

Button(marco, text="W", font=("Consolas", 25), width=3).pack(side=TOP)
Button(marco, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(marco, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(marco, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)

windows.mainloop()