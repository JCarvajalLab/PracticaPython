from tkinter import *
from time import *
import locale 

locale.setlocale(locale.LC_TIME, 'es_ES')

def update():
    horaLocal = strftime("%H:%M:%S")
    timeLabel.config(text=horaLocal)

    diaLocal = strftime("%A")
    dayLabel.config(text=diaLocal)

    fechaLocal = strftime("%B %d, %Y")
    dateLabel.config(text=fechaLocal)

    timeLabel.after(1000,update)

windows = Tk()

timeLabel = Label(windows,font=("Arial", 50), fg="red", bg="#000")
timeLabel.pack()

dayLabel = Label(windows,font=("Ink Free",25))
dayLabel.pack()

dateLabel = Label(windows,font=("Ink Free",25))
dateLabel.pack()


update()

windows.mainloop()