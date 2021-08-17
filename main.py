


from Tkinter import *
from Tkinter.ttk import *


from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S %P')
    lable.config(text=string)
    lable.after(1000,time)

lable = lable(root, font=("ds-digital",80),background = "black",foreground = "cyan")
lable.pack(anchor='center')
time()

mainloop()