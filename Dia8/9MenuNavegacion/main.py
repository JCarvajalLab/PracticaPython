from tkinter import *


# openImage = PhotoImage(file='img1.png')
# saveImage = PhotoImage (file='img2.png') 
# exitImage = PhotoImage (file='img3.png')

def abrirArchivo():
    print("Abrindo Archivo")
def guardarArchivo():
    print("Guardando Archivo")
def modificarArchivo():
    print("Modificar Archivo")

def copiarArchivo():
    print("Copiando Archivo")
def cortarArchivo():
    print("Cortando Archivo")
def pegarARchivo():
    print("Pegando Archivo")

windows = Tk()

menuBar = Menu(windows)
windows.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Archivos", menu=fileMenu)
# fileMenu.add_command(label="Abrir", command=abrirArchivo, image=openImage, compound="left")
fileMenu.add_command(label="Abrir", command=abrirArchivo)
fileMenu.add_command(label="Modificar", command=guardarArchivo)
fileMenu.add_command(label="Editar", command=modificarArchivo)
fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=quit)

editMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Editar", menu=editMenu)
fileMenu.add_command(label="copiar", command=copiarArchivo)
fileMenu.add_command(label="Cortar", command=cortarArchivo)
fileMenu.add_command(label="Pegar", command=pegarARchivo)

windows.mainloop()