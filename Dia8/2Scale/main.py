from tkinter import *

def submit():
    print('La temperatura es: '+str(scale.get()) + ' grados.')

windows = Tk()

# hotImage = PhotoImage(file='calor.png')
# hotImage = Label(image=hotImage)
# hotImage.pack()

scale = Scale(windows,
                from_=100, 
                to=0,
                length=600,
                orient=VERTICAL,
                font=('Arial', 20),
                tickinterval=10,
                resolution=5,
                troughcolor='#ff6600',
                fg='#ff1c00',
                bg='#111111')

scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

# coldImage = PhotoImage(file='calor.png')
# coldImage = Label(image=coldImage)
# coldImage.pack()

boton = Button(windows, text="Enviar", command=submit)
boton.pack()

windows.mainloop()