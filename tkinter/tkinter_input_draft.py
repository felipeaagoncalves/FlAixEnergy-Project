from tkinter import *
from tkinter import messagebox


class InputWindow:

    def __init__(self, master):

        global tkvar_pv, tkvar_wind, time, time_display, auto_percentage, auto_percentage_display, steel_percentage
        global steel_percentage_display

        frame = Frame(master, bg="white")
        frame.pack()

        # Input Window

        menubar = Menu(root, title="Menu")
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new)
        filemenu.add_command(label="Open", command=self.open)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Edit", command=self.edit)
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Info", command=self.info)
        helpmenu.add_command(label="License", command=self.license)
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)



        self.WinterWD = Button(frame, text="Winter Weekday", bg="blue", fg="white", command=self.winterwd)
        self.WinterWD.grid(row=0, padx=7, pady=7)

        self.WinterWE = Button(frame, text="Winter Weekend", bg="blue", fg="white", command=self.winterwe)
        self.WinterWE.grid(row=1, padx=7, pady=7)

        self.SummerWD = Button(frame, text="Summer Weekday", bg="blue", fg="white", command=self.summerwd)
        self.SummerWD.grid(row=0, column=1, padx=7, pady=7)

        self.SummerWE = Button(frame, text="Summer Weekend", bg="blue", fg="white", command=self.summerwe)
        self.SummerWE.grid(row=1, column=1, padx=7, pady=7)

        self.LocalPV = Button(frame, text="Local PV", bg="blue", fg="white", command=self.pvFactor)
        self.LocalPV.grid(row=2, columnspan=2, padx=7, pady=7, sticky=W+E)

        self.LocalWind = Button(frame, text="Local Wind", bg="blue", fg="white", command=self.windFactor)
        self.LocalWind.grid(row=3, columnspan=2, padx=7, pady=7, sticky=W+E)

        self.Industy = Label(frame, text="Degree of Flexibility", bg="white")
        self.Industy.grid(row=4, column=2, columnspan=4, padx=2, pady=2, sticky=W+E)

        self.AutoIndustry = Button(frame, text="Automotive industry", bg="blue", fg="white", command=self.autoFlex)
        self.AutoIndustry.grid(row=5, columnspan=2, padx=7, pady=7, sticky=W+E)

        self.SteelIndustry = Button(frame, text="Steel Industry", bg="blue", fg="white", command=self.steelFlex)
        self.SteelIndustry.grid(row=6, columnspan=2, padx=7, pady=7, sticky=W+E)

        auto_percentage.set('0')
        text1 = str(round(float(auto_percentage.get()) * 100)) + '%'
        auto_percentage_display.set(text1)
        self.AutoIndustry_Percentage = Label(frame, textvariable=auto_percentage_display, bg="white", width=1)
        self.AutoIndustry_Percentage.grid(row=5, column=2, padx=2, pady=2, sticky=W + E)
        self.AutoIndustry_Scroll = Scrollbar(frame, orient=HORIZONTAL, command=self.setAuto)
        self.AutoIndustry_Scroll.grid(row=5, column=3, columnspan=3, padx=7, sticky=W + E)

        steel_percentage.set('0')
        text2 = str(round(float(steel_percentage.get()) * 100)) + '%'
        steel_percentage_display.set(text2)
        self.SteelIndustry_Percentage = Label(frame, textvariable=steel_percentage_display, bg="white")
        self.SteelIndustry_Percentage.grid(row=6, column=2, padx=2, pady=2, sticky=W + E)
        self.SteelIndustry_Scroll = Scrollbar(frame, orient=HORIZONTAL, command=self.setSteel)
        self.SteelIndustry_Scroll.grid(row=6, column=3, columnspan=3, padx=7, sticky=W + E)


        tkvar_pv.set('1')
        choices = {'1','2','3','4','5'}
        popupMenu = OptionMenu(frame, tkvar_pv, *sorted(choices))
        self.PV_Factor = Label(frame, text="Factor:", bg="white")
        self.PV_Factor.grid(row=2, column=2, columnspan=2, padx=7, pady=7, sticky=W+E)
        popupMenu.grid(row=2, column=4, columnspan=2, padx=7, sticky=W+E)

        tkvar_wind.set('1')
        choices = {'1', '2', '3', '4', '5'}
        popupMenu = OptionMenu(frame, tkvar_wind, *sorted(choices))
        self.Wind_Factor = Label(frame, text="Factor:", bg="white")
        self.Wind_Factor.grid(row=3, column=2, columnspan=2, padx=7, pady=7, sticky=W+E)
        popupMenu.grid(row=3, column=4, columnspan=2, padx=7, sticky=W+E)

        time.set('0')
        text3 = str(round(float(time.get())*24)) + ':00'
        time_display.set(text3)
        self.Time = Scrollbar(frame, orient=HORIZONTAL, command=self.setTime)
        self.Time.grid(row=1, column=2, columnspan=4, padx=7, sticky=N+W+E)
        self.TimeLabel = Label(frame, textvariable=time_display, width=40, bg="white")
        self.TimeLabel.grid(row=0, column=2, columnspan=4, sticky=S)

        self.Continue = Button(frame, text="Continue", bg="blue", fg="white", command=self.lift)
        self.Continue.grid(row=7, column=4, columnspan=2, padx=7, pady=7, sticky=W+E)


    def raiseitup(event):
        event.WinterWD.config(bg="blue", relief=RAISED)
        event.WinterWE.config(bg="blue", relief=RAISED)
        event.SummerWD.config(bg="blue", relief=RAISED)
        event.SummerWE.config(bg="blue", relief=RAISED)



    def winterwd(event):
        event.raiseitup()
        event.WinterWD.config(bg="green", relief=SUNKEN)
        event.WinterWE.config(bg="blue", relief=RAISED)
        event.SummerWD.config(bg="blue", relief=RAISED)
        event.SummerWE.config(bg="blue", relief=RAISED)
        #print(event.WinterWD['state'])
        #print(event.WinterWE['state'])

    def winterwe(event):
        event.raiseitup()
        event.WinterWD.config(bg="blue", relief=RAISED)
        event.WinterWE.config(bg="green", relief=SUNKEN)
        event.SummerWD.config(bg="blue", relief=RAISED)
        event.SummerWE.config(bg="blue", relief=RAISED)

    def summerwd(event):
        event.raiseitup()
        event.WinterWD.config(bg="blue", relief=RAISED)
        event.WinterWE.config(bg="blue", relief=RAISED)
        event.SummerWD.config(bg="green", relief=SUNKEN)
        event.SummerWE.config(bg="blue", relief=RAISED)

    def summerwe(event):
        event.raiseitup()
        event.WinterWD.config(bg="blue", relief=RAISED)
        event.WinterWE.config(bg="blue", relief=RAISED)
        event.SummerWD.config(bg="blue", relief=RAISED)
        event.SummerWE.config(bg="green", relief=SUNKEN)

    def pvFactor(event):
        global tkvar_pv, count1
        #print(tkvar_pv.get())
        count1 = count1 + 1
        if (count1 % 2) == 1:
            event.LocalPV.config(bg="green", relief=SUNKEN)
        if (count1 % 2) == 0:
            event.LocalPV.config(bg="blue", relief=RAISED)

    def windFactor(event):
        global tkvar_wind, count2
        #print(tkvar_wind.get())
        count2 = count2 + 1
        if (count2 % 2) == 1:
            event.LocalWind.config(bg="green", relief=SUNKEN)
        if (count2 % 2) == 0:
            event.LocalWind.config(bg="blue", relief=RAISED)

    def autoFlex(event):
        global auto_percentage, count3
        #print(auto_percentage.get())
        count3 = count3 + 1
        if (count3 % 2) == 1:
            event.AutoIndustry.config(bg="green", relief=SUNKEN)
        if (count3 % 2) == 0:
            event.AutoIndustry.config(bg="blue", relief=RAISED)

    def steelFlex(event):
        global steel_percentage, count4
        #print(steel_percentage.get())
        count4 = count4 + 1
        if (count4 % 2) == 1:
            event.SteelIndustry.config(bg="green", relief=SUNKEN)
        if (count4 % 2) == 0:
            event.SteelIndustry.config(bg="blue", relief=RAISED)

    def setTime(self, moveto, time_it):
        global time, time_display
        self.Time.set(time_it, time_it)
        time.set(str(time_it))
        text3 = str(round(float(time.get())*24)) + ':00'
        time_display.set(text3)

    def setAuto(self, moveto, auto_it):
        global auto_percentage, auto_percentage_display
        self.AutoIndustry_Scroll.set(auto_it, auto_it)
        auto_percentage.set(str(auto_it))
        text1 = str(round(float(auto_percentage.get()) * 10)*10) + '%'
        auto_percentage_display.set(text1)

    def setSteel(self, moveto, steel_it):
        global steel_percentage, steel_percentage_display
        self.SteelIndustry_Scroll.set(steel_it, steel_it)
        steel_percentage.set(str(steel_it))
        text2 = str(round(float(steel_percentage.get()) * 10)*10) + '%'
        steel_percentage_display.set(text2)

    def lift(self):
        messagebox.showerror(title="Error",message="No continue options yet.")

    def new(self):
        messagebox.showinfo(title="Edit", message="No edit options yet.")

    def open(self):
        messagebox.showinfo(title="Open", message="No open options yet.")

    def save(self):
        messagebox.showinfo(title="Save", message="No save options yet.")

    def edit(self):
        messagebox.showinfo(title="Edit", message="No edit options yet.")

    def info(self):
        messagebox.showinfo(title="Info", message="This program was designed to showcase the impact\nof different parameters on the electric distribution\ngrid of the city of Aachen, Germany.")

    def license(self):
        messagebox.showinfo(title="License", message="FEN Summer 2018 Research Project\nAachen, NW, Germany\nFelipe Goncalves (fagoncal@ualberta.ca)\nversion 1.0")


# class OutputWindow:


root = Tk()

tkvar_pv = StringVar(root)
tkvar_wind = StringVar(root)
time = StringVar(root)
time_display = StringVar(root)
auto_percentage = StringVar(root)
auto_percentage_display = StringVar(root)
steel_percentage = StringVar(root)
steel_percentage_display = StringVar(root)

count1 = 0
count2 = 0
count3 = 0
count4 = 0

obj = InputWindow(root)
root.mainloop()