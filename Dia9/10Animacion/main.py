from tkinter import * 
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

windows = Tk()

canvas = Canvas(windows, width=WIDTH, height=HEIGHT, bg="#000")
canvas.pack()

photo_imagen =PhotoImage(file='ovni.png')
my_imagen = canvas.create_image(0,0,image=photo_imagen,anchor=NW)

imagen_width = photo_imagen.width()
imagen_height = photo_imagen.height()

while True:
    coordenadas = canvas.coords(my_imagen)
    print(coordenadas)
    if(coordenadas[0]>=WIDTH-imagen_width or coordenadas[0]<0):
        xVelocity = -xVelocity
    if(coordenadas[1]>=HEIGHT-imagen_height or coordenadas[1]<0):
        yVelocity = -yVelocity

    canvas.move(my_imagen,xVelocity,yVelocity)
    windows.update()
    time.sleep(0.01)

windows.mainloop()