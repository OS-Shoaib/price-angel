from tkinter import *
import math
import pyperclip


def sum_price():
    price = float(first_price.get())
    sp = float(space.get())
    an = int(angel.get())

    new_price = (((math.sqrt(price/sp)) + (an / 180)) ** 2) * sp
    return new_price


def sup_price():
    price = float(first_price.get())
    sp = float(space.get())
    an = int(angel.get())

    new_price = (((math.sqrt(price / sp)) - (an / 180)) ** 2) * sp
    return new_price


def dal():
    output_Label.delete('1.0', END)


def sum_sup():

    var = option_var.get()
    if var == "+":
        output_Label.insert(END, sum_price())
    elif var == "-":
        output_Label.insert(END, sup_price())


def copy_ans():
    var = option_var.get()
    if var == "+":
        pyperclip.copy(sum_price())
    elif var == "-":
        pyperclip.copy(sup_price())


option = ["+", "-"]

root = Tk()
root.title("Price Angel")

first_price = StringVar()
input_text = Label(root, text="Start Price")
input_entry = Entry(root, textvariable=first_price)

input_text.grid(row=0, column=0)
input_entry.grid(row=0, column=1)

angel = StringVar()
angel_text = Label(root, text="Angel")
angel_entry = Entry(root, textvariable=angel)

angel_text.grid(row=1, column=3)
angel_entry.grid(row=1, column=4)

space = StringVar()
space_Lapel = Label(root, text="Space")
space_entry = Entry(root, textvariable=space)

space_Lapel.grid(row=1, column=0)
space_entry.grid(row=1, column=1)

option_var = StringVar(root)
# option_var.set(option[0])

option_lapel = Label(root, text="Option")
option_menu = OptionMenu(root, option_var, *option)

option_lapel.grid(row=0, column=3)
option_menu.grid(row=0, column=4)


output_text = Label(root, text="Output")
output_Label = Text(root, height=1, width=20)

output_text.grid(row=3, column=0)
output_Label.grid(row=3, column=1)

button_frame = Frame(root)
calc_button = Button(button_frame, text="calc", command=sum_sup)
copy_button = Button(button_frame, text="copy", command=copy_ans)
del_button = Button(button_frame, text="del", command=dal)

calc_button.pack(side=LEFT)
del_button.pack(side=RIGHT)
copy_button.pack(side=RIGHT)
button_frame.grid(row=3, column=4)

status = Label(root, text="Created By ** Omar Shoaib ** For Crypto Trader Comunity", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=4, columnspan=20)

root.mainloop()
