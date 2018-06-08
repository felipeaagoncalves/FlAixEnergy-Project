from tkinter import *
from __main__ import *
from PIL import Image, ImageTk
import pandas
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


top = Toplevel(bg="white")
top.title("EEX Prices")

f = Figure(figsize=(8,5), dpi=100)
a = f.add_subplot(111)
file = pandas.read_csv('EEX_prices.csv', header=1, sep=',')
x = file.reset_index().values[:, 1]
y = file.reset_index().values[:, 2]
print('------------------------------')
print(file)
print('------------------------------')
print(x)
print('------------------------------')
print(y)
print('------------------------------')
a.plot(x, y)

canvas = FigureCanvasTkAgg(f, top)
canvas.show()
canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

toolbar = NavigationToolbar2TkAgg(canvas, top)
toolbar.update()
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
