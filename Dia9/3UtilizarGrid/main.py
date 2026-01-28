from tkinter import *

windows = Tk()

tituloLabel = Label(windows, text="Ingresa tu informacion", font=("Arial", 25)).grid(row=0,column=0,columnspan=2)

nombreLabel = Label(windows, text="Nombre: ", width=20, bg="red").grid(row=1,column=0)
nombreEntry = Entry(windows).grid(row=1,column=1)

apellidoLabel = Label(windows, text="Apellido: ",bg="green").grid(row=2,column=0)
apellidoEntry = Entry(windows).grid(row=2,column=1)

emailLabel = Label(windows, text="Email: ",bg="blue").grid(row=3,column=0)
emailEntry = Entry(windows).grid(row=3,column=1)

enviarButton = Button(windows, text="Enviar").grid(row=4,column=0, columnspan=2)

windows.mainloop()