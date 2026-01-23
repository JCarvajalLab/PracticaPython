from tkinter import *

def enviar():
    nombreUsuario = entrada.get()
    print('Hola '+ nombreUsuario)
    # entrada.config(state=DISABLED)

def resetear():
    entrada.delete(0, END)

def eliminar():
    entrada.delete(len(entrada.get()) - 1, END)

window = Tk()

entrada = Entry(window, font=('Arial', 50,), fg='red', bg='black' )
# entrada.insert(0, 'Hola')
entrada.pack(side=LEFT)

botonEnviar = Button(window, text='Enviar', command=enviar)
botonEnviar.pack(side=RIGHT)

botonReset = Button(window, text='Resetear', command=resetear)
botonReset.pack(side=RIGHT)

botonEliminar = Button(window, text='Eliminar', command=eliminar)
botonEliminar.pack(side=RIGHT)



window.mainloop()
