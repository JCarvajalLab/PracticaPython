from tkinter import * 

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("Su orden es: ")
    # print(listbox.get(listbox.curselection()))
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    # listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

windows = Tk()

listbox = Listbox(windows,
                    bg="#f7ffde",
                    font=("Arial",30),
                    width=20,
                    selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, 'Pizza margarita')
listbox.insert(2, 'Pizza napolitana')
listbox.insert(3, 'Pizza de peperoni')
listbox.insert(4, 'Pizza marinara')
listbox.insert(5, 'Pizza champinion')

listbox.config(height=listbox.size())

entryBox = Entry(windows)
entryBox.pack()

submitButton = Button(windows, text=("Enviar"), command=submit)
submitButton.pack()

addButton = Button(windows, text=("Agregar"), command=add)
addButton.pack()

deleteButton = Button(windows, text=("Eliminar"), command=delete)
deleteButton.pack()


windows.mainloop()