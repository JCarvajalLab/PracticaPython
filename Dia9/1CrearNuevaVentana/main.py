from tkinter import *

def crearVentana():
    newWindows = Tk()

    windows.destroy()

windows = Tk()

Button(text="Crear nueva ventana!", command=crearVentana).pack()

windows.mainloop()