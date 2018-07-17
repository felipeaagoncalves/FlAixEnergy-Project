from tkinter import *

root = Tk()

def callback(event):
    print("clicked at x={}, y={}".format(event.x, event.y))

frame = Frame(root, width=100, height=100, bg="pink")
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()