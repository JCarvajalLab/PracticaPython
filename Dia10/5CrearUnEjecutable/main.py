from tkinter import *
from time import strftime

def update():
    time_string = strftime("%H:%M:%S %p")
    time_label.config(text=time_string)
    time_label.after(1000, update) # Llama a 'update' de nuevo después de 1000ms (1 segundo)

window = Tk()
window.title("Reloj Digital") # Puedes agregar un título a la ventana

time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

update() # Llama a la función 'update' por primera vez para iniciar el reloj
window.mainloop()