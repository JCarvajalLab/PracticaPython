from tkinter import *
from tkinter import filedialog

def guardarArchivo():
    archivo = filedialog.asksaveasfile(initialdir="C:\\Users\\Deo\\Desktop\\CURSO PYTHON\\Dia8\\8GuardarArchivos",
                                        defaultextension='.txt',
                                        filetypes=[("Archivo de texto", ".txt"),
                                                    ("HTML",".html"),
                                                    ("Todos los Archivos", ".*")
                                                    ])
    if archivo is None:
        return
    archivoTexto = texto.get(1.0,END)
    archivo.write(archivoTexto)
    archivo.close()
    print(archivoTexto)

    
windows = Tk()

boton = Button(windows, text="Guardar", command=guardarArchivo)
boton.pack()

texto = Text(windows)
texto.pack()

windows.mainloop()