# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:04:35 2018

@author: uoa-student2
"""

from tkinter import *

root = Tk()

one = Label(root, text="One", bg="blue", fg="white")
one.pack()
two = Label(root, text="Two", bg="blue", fg="white")
two.pack(fill=X)
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(fill=Y)

root.mainloop()