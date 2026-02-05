from tkinter import *
from pelota import *
import time

WIDTH =500
HEIGHT =500

windows = Tk()

canvas = Canvas(windows,width=WIDTH,height=HEIGHT)
canvas.pack()

volleyBall = Ball(canvas,0,0,100,1,1,"white")
tennisBall = Ball(canvas,0,0,40,4,3,"yellow")
backetBall = Ball(canvas,0,0,120,8,7,"orange")

while True:
    volleyBall.move()
    tennisBall.move()
    backetBall.move()
    windows.update()
    time.sleep(0.01)

windows.mainloop()