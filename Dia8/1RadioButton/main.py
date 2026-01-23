from tkinter import *

comida = ['pizza', 'Hamburguesa','HodDog']

def orden():
    if(x.get() == 0):
        print('Has ordenado una pizza')
    elif(x.get() == 1):
        print('Has ordenado una Hamburguesa')
    elif(x.get() == 2):
        print('Has ordenado una hotDog')
    else:
        print('Error')        

windows = Tk()

# pizzaImagen = PhotoImage(file='')
# hamburguesaImagen = PhotoImage(file='')
# hotDogImagen = PhotoImage(file='')
# foodImage = [pizzaImagen,hamburguesaImagen,hotDogImagen]

x = IntVar()

for index in range(len(comida)):
    radioButton = Radiobutton(windows, 
                                text=comida[index],
                                variable=x,
                                value=index,
                                font=('Arial', 50),
                                # image=foodImage[index],
                                # compound='left',
                                # indicatoron=0
                                # width=500
                                command=orden,
                                bg='blue'
                                )
    radioButton.pack(anchor=W)


windows.mainloop()