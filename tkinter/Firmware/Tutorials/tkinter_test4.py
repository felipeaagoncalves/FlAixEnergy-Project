# -*- coding: utf-8 -*-
"""
Created on Tue May 22 17:29:40 2018

@author: uoa-student2
"""

from tkinter import *

master = Tk()

Label(text="one").pack()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Label(text="two").pack()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Label(text="three").pack()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Label(text="four").pack()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Label(text="five").pack()

frame = Frame(width=768, height=576, bg="white", colormap="new", )
frame.pack()

mainloop()