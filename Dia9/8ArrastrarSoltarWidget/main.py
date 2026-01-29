from tkinter import *

def mover(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def mover1(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

windows = Tk()

label = Label(windows, bg="red", width=10, height=5)
label.place(x=0,y=0)

label1 = Label(windows, bg="green", width=10, height=5)
label1.place(x=100,y=100)

label.bind("<Button-1>",mover )
label.bind("<B1-Motion>",mover1)

label1.bind("<Button-1>",mover )
label1.bind("<B1-Motion>",mover1)

windows.mainloop()