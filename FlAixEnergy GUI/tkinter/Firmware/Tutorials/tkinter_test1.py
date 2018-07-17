# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:22:03 2018

@author: uoa-student2
"""

import tkinter as tk

u = 0

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, fg="white", bg="blue")
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="white", bg="blue",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        global u
        
#        if (u % 2) == 0:
#            print("hi there, everyone!")
#        if (u % 2) == 1:
#            print("Oh nooooooo!")
        u = u + 1
        print(u)


root = tk.Tk()
app = Application(master=root)
app.mainloop()

