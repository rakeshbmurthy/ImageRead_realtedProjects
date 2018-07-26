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
from Tkinter import *


def select_all(event):
    text_1.tag_add(SEL, "1.0", END)
    text_1.mark_set(INSERT, "1.0")
    text_1.see(INSERT)
    return 'break'


root = Tk()

root.geometry("500x500")

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()

text_1 = Text(root, height = 2, width = 30)
text_1.pack()
text_1.bind("<Control-Key-a>", select_all)

text = Text(root, height = 2, width = 30)
text.pack()
text.insert(END, '-')


def btnpress():
    text.delete('1.1', END)
    text.insert(END, text_1.get("1.0",'end-1c'))


btn = Button(root, text = 'attach', width = 5, command = btnpress)
btn.pack()


root.mainloop()