# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:41:44 2018

@author: uoa-student2
"""

import tkinter as tk
import time

start = time.time()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.widget1 = tk.Button(self, fg="white", bg="blue")
        self.widget1["text"] = "Print 1"
        self.widget1["command"] = self.printing1
        self.widget1.pack(side="left")
        
        self.widget2 = tk.Button(self, fg="white", bg="blue")
        self.widget2["text"] = "Print 2"
        self.widget2["command"] = self.printing2
        self.widget2.pack(side="left")
        
        self.quit = tk.Button(self, text="QUIT", fg="white", bg="blue", command=root.destroy)
        self.quit.pack(side="right")
        
        self.widget3 = tk.Button(self, fg="white", bg="blue")
        self.widget3["text"] = "time"
        self.widget3["command"] = self.time
        self.widget3.pack(side="right")
        

    def printing1(self):
        print(1)

    def printing2(self):
        print(2)
        
    def time(self):
        global start
        print(time.time()-start)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
