from tkinter import *

def funcion(event):
    print("Has presionado el click: "+ str(event.x) +","+ str(event.y))

windows = Tk()

# windows.bind("<Button-1>", funcion)
# windows.bind("<Button-2>", funcion)
# windows.bind("<Button-3>", funcion)
# windows.bind("<ButtonRelease>", funcion)
# windows.bind("<Enter>",funcion)
# windows.bind("<Leave>",funcion)
# windows.bind("<Motion>",funcion)

windows.mainloop()