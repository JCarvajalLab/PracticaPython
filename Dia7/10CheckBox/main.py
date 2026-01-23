from tkinter import *

def mostrar():
    if(x.get()==1):
        print('Estas de Acuerdo')
    else:
        print('Estas en desAcuerdo')

window = Tk()
x = IntVar()

checkButton = Checkbutton(window, 
                            text= 'Acepto',
                            variable=x,
                            onvalue= 1,
                            offvalue= 0,
                            command=mostrar,
                            font=('Arial', 20),
                            fg='red',
                            bg='black',
                            activebackground='black',
                            activeforeground='red',
                            padx=25,
                            pady=25)
checkButton.pack()

window.mainloop()