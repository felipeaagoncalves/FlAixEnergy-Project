# from tkinter import *
# from __main__ import *
# from PIL import Image, ImageTk
#
# top = Toplevel(bg="white")
# top.title("EEX Prices")
#
# if count1 == 1:
#     Imagefile = 'Winter Weekday.png'
# if count2 == 1:
#     Imagefile = 'Winter Weekend.png'
# if count3 == 1:
#     Imagefile = 'Summer Weekday.png'
# if count4 == 1:
#     Imagefile = 'Summer Weekend.png'
# Image = Image.open(Imagefile)
# Img = ImageTk.PhotoImage(Image)
#
# Map = Label(top, image=Img)
# Map.grid(padx=7, pady=7)

from tkinter import *
from __main__ import *
import pandas
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np


top = Toplevel(bg="white")
top.title("SMARD Prices")

f = Figure(figsize=(8,5), dpi=100)
a = f.add_subplot(111)
file = pandas.read_csv('Summer-Winter Price Averages (SMARD).csv', sep=',')
x = file.reset_index().values[:, 1]
swd = file.reset_index().values[:, 3]
swe = file.reset_index().values[:, 4]
wwd = file.reset_index().values[:, 5]
wwe = file.reset_index().values[:, 6]
if count1 == 1:
    y = wwd
if count2 == 1:
    y = wwe
if count3 == 1:
    y = swd
if count4 == 1:
    y = swe
a.plot(x, y)
a.set_ylabel('Price [EUR/MWh]')
a.set_xlabel('Time of day [hr]')
a.set_title('')
if count1 == 1:
    a.set_title('Winter Weekday (SMARD)')
if count2 == 1:
    a.set_title('Winter Weekend (SMARD)')
if count3 == 1:
    a.set_title('Summer Weekday (SMARD)')
if count4 == 1:
    a.set_title('Summer Weekend (SMARD)')
a.set_xbound(-1, 24)
a.set_xticks(np.arange(min(x), max(x)+2, 2.0))
a.axvline(x=float(time.get()), color='r', linestyle='-', linewidth=2)

canvas = FigureCanvasTkAgg(f, top)
canvas.show()
canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

toolbar = NavigationToolbar2TkAgg(canvas, top)
toolbar.update()
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)