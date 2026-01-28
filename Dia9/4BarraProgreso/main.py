from tkinter import *
from tkinter.ttk import *
import time

def star():
    GB = 100
    download = 0
    speed = 0.5
    while(download < GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+= speed
        porcentaje.set(str(int((download/GB)*100))+"%")
        texto.set(str(download)+"/"+str(GB)+" GB Completados")
        windows.update_idletasks()
    # print("Descargando...")

windows = Tk()

porcentaje = StringVar()
texto = StringVar()

bar = Progressbar(windows, orient=HORIZONTAL,length=300)
bar.pack(pady=10)

textoLabel = Label(windows, textvariable=porcentaje).pack()
comLabel = Label(windows, textvariable=texto).pack()

boton = Button(windows, text="Descargar", command=star).pack()

windows.mainloop()