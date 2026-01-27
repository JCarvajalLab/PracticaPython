from tkinter import *
from tkinter import filedialog

def abrirArchivo():
    filepath = filedialog.askopenfilename(initialdir='C:\\Users\\tuUSUARIO\\Desktop\\CURSO PYTHON\\Dia8\\7AbrirArchivos',
                                            title="ABRIR ARCHIVOS",
                                            filetypes=(('Archivos de texto','.txt'),("Todos los archivos","*.*")))
    # print(filepath)
    archivo = open(filepath,'r')
    print(archivo.read())
    archivo.close()

windows = Tk()

boton = Button(windows, text="Abrir", command=abrirArchivo)
boton.pack()

windows.mainloop()