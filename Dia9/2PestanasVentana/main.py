from tkinter import *
from tkinter import ttk

windows = Tk()

notebook = ttk.Notebook(windows)
notebook.pack(expand=TRUE, fill="both")


tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.add(tab3, text="Tab 3")

Label(tab1, text="Pestana 1", width=50,height=50).pack()
Label(tab2, text="Pestana 2", width=50,height=50).pack()
Label(tab3, text="Pestana 3", width=50,height=50).pack()

windows.mainloop()