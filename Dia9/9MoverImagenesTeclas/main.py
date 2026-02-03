from tkinter import *

def moveUP(event):
    # label.place(x=label.winfo_x(),y=label.winfo_y()-10)
    canvas.move(miImagen,0,-10)

def moveLeft(event):
    # label.place(x=label.winfo_x()-10,y=label.winfo_y())
    canvas.move(miImagen,-10,0)

def moveRight(event):
    # label.place(x=label.winfo_x()+10,y=label.winfo_y())
    canvas.move(miImagen,10,0)

def moveDown(event):
    # label.place(x=label.winfo_x(),y=label.winfo_y()+10)
    canvas.move(miImagen,0,+10)
    

windows = Tk()

windows.bind("<w>",moveUP)
windows.bind("<a>",moveLeft)
windows.bind("<s>",moveDown)
windows.bind("<d>",moveRight)

windows.bind("<Up>",moveUP)
windows.bind("<Left>",moveLeft)
windows.bind("<Down>",moveDown)
windows.bind("<Right>",moveRight)

canvas = Canvas(windows, width=500,height=500)
canvas.pack()

imagen = PhotoImage(file='C:\\Users\\Deo\\Desktop\\CURSO PYTHON\\Dia9\\9MoverImagenesTeclas\\python.png')
miImagen = canvas.create_image(0,0,image=imagen,anchor=NW)

# label = Label(windows, image=imagen)
# label.place(x=0,y=0)

windows.mainloop()