# from tkinter import *

# def main():
#     w1 = Tk()
#     w1.title("Finestra 1")
#     f1 = Frame(w1)
#     b = Button(f1, text='asldkf')
#     b.pack()
#     f1.pack()
#     w1.mainloop()
#
#
# main()
from tkinter import *


# variable_1 = StringVar()


def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    # variable_1.get()
    e1.delete(0, END)
    e2.delete(0, END)


master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop()
