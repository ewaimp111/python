#!/usr/bin/env python3
from tkinter import *
from cmd import *

root=Tk()
root.title("hello world")
root.geometry()


def print_item(event):
    print(lb.get(lb.curselection()))

var=StringVar()

lb=Listbox(root,listvariable=var)
l =[1,2,3,4]

for item in l:
    lb.insert(END,item)
print(var.get())

var.set(('a','b','c','d','e'))
print (var.get())

lb.bind('<ButtonRelease-1>',print_item)
lb.pack()

root.mainloop()