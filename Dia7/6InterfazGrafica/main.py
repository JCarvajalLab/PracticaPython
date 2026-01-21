from tkinter import *

windows = Tk()
windows.geometry('500x500')

windows.title('Programando la primera interfaz grafica')

icono = PhotoImage(file='6InterfazGrafica\\3030224.png')
windows.iconphoto(True, icono)
windows.config(background='black')

windows.mainloop()