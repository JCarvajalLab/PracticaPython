from tkinter import * 
windows = Tk()

label = Label(windows, 
                text='Hola mundo quieres aprender a programar', 
                font=('Arial', 40, 'bold'), 
                fg='#00FFFF', 
                bg='Black',
                relief='raised',
                bd=10,
                padx=50,
                pady=50)
label.pack(padx=150, pady=150)
label.pack()
# label.place(x=100, y=100)

windows.mainloop()