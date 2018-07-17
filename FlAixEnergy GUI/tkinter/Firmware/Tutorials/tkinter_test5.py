# -*- coding: utf-8 -*-
"""
Created on Wed May 23 09:34:12 2018

@author: uoa-student2
"""

from tkinter import *

root = Tk()

label = Label(root, text="This is too easy", fg="black")
label.pack()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", bg ="blue", fg="white")
button2 = Button(topFrame, text="Button 2", bg ="blue", fg="white")
button3 = Button(topFrame, text="Button 3", bg ="blue", fg="white")
button4 = Button(bottomFrame, text="Button 4", bg ="blue", fg="white")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()