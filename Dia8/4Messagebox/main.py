from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="Hola mundo", message="Suscrito")
    # messagebox.showwarning(title="Hola mundo", message="PELIGRO PELIGRO")
    # messagebox.showerror(title="ERROR!", message="Tienes un Error")
    
    # messagebox.askokcancel()
    # if(messagebox.askretrycancel()):
    #     print("Reintenta")
    # else:
    #     print("Has Cancelado")

    # messagebox.askyesno()
    # messagebox.askquestion()

    # pregunta = messagebox.askquestion(title="Pregunta: ", message="Te gusta el helado")
    # if(pregunta == 'yes'):
    #     print("Si le gusta el helado")
    # else:
    #     print("No me gusta el helado")

    var = (messagebox.askyesnocancel(title="Advertencia!", message="Estas seguro de salir?"))
    print(var)

    messagebox.askyesnocancel(title="Advertencia!", message="Estas seguro de salir?", icon="warning")

windows = Tk()

button = Button(windows, text="Click", command=click)
button.pack()

windows.mainloop()