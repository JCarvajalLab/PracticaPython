from tkinter import *

def click():
    print('Presionaste el boton!')

windows = Tk()
imagen = PhotoImage(file='8BotonPython\\103869.png')
boton = Button(windows, 
                text='Haz CLICK', 
                command=click, 
                font=('Arial', 20, 'bold'), 
                fg='red', 
                bg='#fff',
                activeforeground='red',
                activebackground='#fff',
                state='active',
                relief='raised',
                bd=10,
                padx=15,
                pady=15,
                image=imagen,
                compound='bottom')
boton.pack()

windows.mainloop()