from tkinter import *
from tkinter import messagebox
import webbrowser
import PIL
from PIL import Image, ImageTk
import importlib
import datetime as dt


class WindowController(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(root)
        container.grid()

        self.frames = {}

        for F in (InputWindow, OutputWindow):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(InputWindow)

        self.destroy()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class InputWindow(Frame):

    def __init__(self, parent, controller):
        global tkvar_pv, tkvar_wind, time, time_display, auto_percentage, auto_percentage_display, steel_percentage
        global steel_percentage_display

        self.controller = controller
        self.parent = parent

        Frame.__init__(self, parent, bg="white", padx=4, pady=4)

        menubar = Menu(self, title="Menu")
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
        helpmenu.add_command(label="GitHub Repo", command=self.gitHub)
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)

        self.WinterWD = Button(self, text="Winter Weekday", bg="blue", fg="white", command=self.winterwd)
        self.WinterWD.grid(row=0, padx=7, pady=7)

        self.WinterWE = Button(self, text="Winter Weekend", bg="blue", fg="white", command=self.winterwe)
        self.WinterWE.grid(row=1, padx=7, pady=7)

        self.SummerWD = Button(self, text="Summer Weekday", bg="blue", fg="white", command=self.summerwd)
        self.SummerWD.grid(row=0, column=1, padx=7, pady=7)

        self.SummerWE = Button(self, text="Summer Weekend", bg="blue", fg="white", command=self.summerwe)
        self.SummerWE.grid(row=1, column=1, padx=7, pady=7)

        self.LocalPV = Button(self, text="Local PV", bg="blue", fg="white", command=self.pvFactor)
        self.LocalPV.grid(row=2, columnspan=2, padx=7, pady=(20,7), sticky=W + E)

        self.LocalWind = Button(self, text="Local Wind", bg="blue", fg="white", command=self.windFactor)
        self.LocalWind.grid(row=3, columnspan=2, padx=7, pady=7, sticky=W + E)

        self.Industy = Label(self, text="Degree of Flexibility", bg="white")
        self.Industy.grid(row=4, column=2, columnspan=4, padx=2, pady=2, sticky=W + E)

        self.AutoIndustry = Button(self, text="Automotive industry", bg="blue", fg="white", command=self.autoFlex)
        self.AutoIndustry.grid(row=5, columnspan=2, padx=7, pady=7, sticky=W + E)

        self.SteelIndustry = Button(self, text="Steel Industry", bg="blue", fg="white", command=self.steelFlex)
        self.SteelIndustry.grid(row=6, columnspan=2, padx=7, pady=7, sticky=W + E)


        text1 = str(round(float(auto_percentage.get()) * 100)) + '%'
        auto_percentage_display.set(text1)
        self.AutoIndustry_Percentage = Label(self, textvariable=auto_percentage_display, bg="white", width=1)
        self.AutoIndustry_Percentage.grid(row=5, column=2, padx=2, pady=2, sticky=W + E)
        self.AutoIndustry_Scroll = Scrollbar(self, orient=HORIZONTAL, command=self.setAuto)
        self.AutoIndustry_Scroll.grid(row=5, column=3, columnspan=3, padx=7, sticky=W + E)


        text2 = str(round(float(steel_percentage.get()) * 100)) + '%'
        steel_percentage_display.set(text2)
        self.SteelIndustry_Percentage = Label(self, textvariable=steel_percentage_display, bg="white")
        self.SteelIndustry_Percentage.grid(row=6, column=2, padx=2, pady=2, sticky=W + E)
        self.SteelIndustry_Scroll = Scrollbar(self, orient=HORIZONTAL, command=self.setSteel)
        self.SteelIndustry_Scroll.grid(row=6, column=3, columnspan=3, padx=7, sticky=W + E)


        choices = {'1', '2', '3', '4', '5'}
        popupMenu = OptionMenu(self, tkvar_pv, *sorted(choices))
        self.PV_Factor = Label(self, text="Factor:", bg="white")
        self.PV_Factor.grid(row=2, column=2, columnspan=2, padx=7, pady=(20,7), sticky=W + E)
        popupMenu.grid(row=2, column=4, columnspan=2, padx=7, pady=(20,0), sticky=W + E)


        choices = {'1', '2', '3', '4', '5'}
        popupMenu = OptionMenu(self, tkvar_wind, *sorted(choices))
        self.Wind_Factor = Label(self, text="Factor:", bg="white")
        self.Wind_Factor.grid(row=3, column=2, columnspan=2, padx=7, pady=7, sticky=W + E)
        popupMenu.grid(row=3, column=4, columnspan=2, padx=7, sticky=W + E)

        self.Time = Scrollbar(self, orient=HORIZONTAL, command=self.setTime)
        self.Time.grid(row=1, column=2, columnspan=4, padx=7, sticky=N + W + E)
        self.TimeLabel = Label(self, textvariable=time_display, width=40, bg="white")
        self.TimeLabel.grid(row=0, column=2, columnspan=4, sticky=S)

        self.Continue = Button(self, text="Continue", bg="blue", fg="white",
                               command=self.next_page)
        self.Continue.grid(row=7, column=4, columnspan=2, padx=7, pady=7, sticky=W + E)


    def raiseitup(event):
        global count, count1, count2, count3, count4
        event.WinterWD.config(bg="blue", relief=RAISED)
        event.WinterWE.config(bg="blue", relief=RAISED)
        event.SummerWD.config(bg="blue", relief=RAISED)
        event.SummerWE.config(bg="blue", relief=RAISED)
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count = [count1, count2, count3, count4]

    def winterwd(event):
        global count, count1, count2, count3, count4
        event.raiseitup()
        event.WinterWD.config(bg="green", relief=SUNKEN)
        event.WinterWE.config(bg="blue", relief=RAISED)
        event.SummerWD.config(bg="blue", relief=RAISED)
        event.SummerWE.config(bg="blue", relief=RAISED)
        count1 = 1
        count = [count1, count2, count3, count4]

    def winterwe(event):
        global count, count1, count2, count3, count4
        event.raiseitup()
        event.WinterWD.config(bg="blue", relief=RAISED)
        event.WinterWE.config(bg="green", relief=SUNKEN)
        event.SummerWD.config(bg="blue", relief=RAISED)
        event.SummerWE.config(bg="blue", relief=RAISED)
        count2 = 1
        count = [count1, count2, count3, count4]

    def summerwd(event):
        global count, count1, count2, count3, count4
        event.raiseitup()
        event.WinterWD.config(bg="blue", relief=RAISED)
        event.WinterWE.config(bg="blue", relief=RAISED)
        event.SummerWD.config(bg="green", relief=SUNKEN)
        event.SummerWE.config(bg="blue", relief=RAISED)
        count3 = 1
        count = [count1, count2, count3, count4]

    def summerwe(event):
        global count, count1, count2, count3, count4
        event.raiseitup()
        event.WinterWD.config(bg="blue", relief=RAISED)
        event.WinterWE.config(bg="blue", relief=RAISED)
        event.SummerWD.config(bg="blue", relief=RAISED)
        event.SummerWE.config(bg="green", relief=SUNKEN)
        count4 = 1
        count = [count1, count2, count3, count4]

    def pvFactor(event):
        global tkvar_pv, count5
        count5 += 1
        if (count5 % 2) == 1:
            event.LocalPV.config(bg="green", relief=SUNKEN)
        if (count5 % 2) == 0:
            event.LocalPV.config(bg="blue", relief=RAISED)

    def windFactor(event):
        global tkvar_wind, count6
        count6 += 1
        if (count6 % 2) == 1:
            event.LocalWind.config(bg="green", relief=SUNKEN)
        if (count6 % 2) == 0:
            event.LocalWind.config(bg="blue", relief=RAISED)

    def autoFlex(event):
        global auto_percentage, count7
        # print(auto_percentage_display.get())
        count7 += 1
        if (count7 % 2) == 1:
            event.AutoIndustry.config(bg="green", relief=SUNKEN)
        if (count7 % 2) == 0:
            event.AutoIndustry.config(bg="blue", relief=RAISED)

    def steelFlex(event):
        global steel_percentage, count8
        # print(steel_percentage.get())
        count8 += 1
        if (count8 % 2) == 1:
            event.SteelIndustry.config(bg="green", relief=SUNKEN)
        if (count8 % 2) == 0:
            event.SteelIndustry.config(bg="blue", relief=RAISED)

    def setTime(self, moveto, time_it):
        global time, time_display, time_dt
        self.Time.set(time_it, time_it)
        time.set(str(round(96*float(time_it))/4))
        if float(time.get()) == 24.:
            time.set(str(95/4))
        time_dt = dt.time(hour=int(float(time.get())//1), minute=int((float(time.get())%1)*60)).__format__("%H:%M")
        time_display.set(time_dt)

    def setAuto(self, moveto, auto_it):
        global auto_percentage, auto_percentage_display
        self.AutoIndustry_Scroll.set(auto_it, auto_it)
        auto_percentage.set(str(auto_it))
        text1 = str(round(float(auto_percentage.get()) * 10) * 10) + '%'
        auto_percentage_display.set(text1)

    def setSteel(self, moveto, steel_it):
        global steel_percentage, steel_percentage_display
        self.SteelIndustry_Scroll.set(steel_it, steel_it)
        steel_percentage.set(str(steel_it))
        text2 = str(round(float(steel_percentage.get()) * 10) * 10) + '%'
        steel_percentage_display.set(text2)

    def next_page(self):
        global count, count5, count6, count7, count8
        if count != [0,0,0,0] and (count5 % 2 == 1 or count6 % 2 == 1 or count7 % 2 == 1 or count8 % 2 == 1):
            self.controller.show_frame(OutputWindow)

    def new(self):
        messagebox.showinfo(title="Edit", message="No edit options yet.")

    def open(self):
        messagebox.showinfo(title="Open", message="No open options yet.")

    def save(self):
        messagebox.showinfo(title="Save", message="No save options yet.")

    def edit(self):
        messagebox.showinfo(title="Edit", message="No edit options yet.")

    def info(self):
        messagebox.showinfo(title="Info",
                            message="This program was designed to showcase"
                                    " the impact of different parameters on"
                                    " the electric distribution grid of the"
                                    " city of Aachen, Germany.")

    def license(self):
        messagebox.showinfo(title="License",
                            message="FEN Summer 2018 Research Project\nAachen,"
                                    " NW, Germany\nFelipe Goncalves"
                                    " (fagoncal@ualberta.ca)\nversion 1.0.")

    def gitHub(self):
        webbrowser.open_new("https://github.com/felipeaagoncalves/Forschungscampus"
                            "_Flexible_Elektrische_Netze_FEN")


class OutputWindow(Frame):

    def __init__(self, parent, controller):
        global date, date_time, time, time_display

        self.controller = controller
        self.parent = parent

        Frame.__init__(self, parent, bg="white", padx=4, pady=4)

        self.Container_output = Frame(self, bg="blue")
        self.Container_output.grid(row=0, column=0, rowspan=4, columnspan=3, padx=7, pady=7)

        self.Resulting_cluster = Label(self.Container_output, bg="blue", fg="white", text="Resulting Cluster",
                                       font=("Helvetica", 11, "bold"))
        self.Resulting_cluster.grid(row=0, column=0, padx=7, pady=(2,0), sticky=S)

        self.getMap()
        self.Map = Label(self.Container_output, image=self.Img)
        self.Map.grid(row=1, column=0, padx=7, pady=(0,7), sticky=N)

        self.TotalLineLoading = Button(self, text="Total Line Loading", bg="white", fg="blue", command=self.loading,
                                       relief=GROOVE)
        self.TotalLineLoading.grid(row=4, column=1, pady=(0,7), sticky=W+E)

        self.TotalLineLosses = Button(self, text="Total Line Losses", bg="white", fg="blue", command=self.losses,
                                       relief=GROOVE)
        self.TotalLineLosses.grid(row=5, column=1, sticky=W+E)

        root.bind("<Button-1>", self.setDate)
        self.setDate()
        self.Date_time = Label(self, textvariable=date_time, bg="white")
        self.Date_time.grid(row=0, column=3, padx=7, pady=(7,0))

        self.EEX_Price_Curve = Button(self, text="SMARD Price Curve", bg="blue", fg="white", command=self.eex,
                                       relief=GROOVE)
        self.EEX_Price_Curve.grid(row=1, column=3, rowspan=2, sticky=N+S+W+E)

        self.OPF_Result = Button(self, text="OPF Result", bg="white", fg="green", command=self.opf,
                                       relief=GROOVE)
        self.OPF_Result.grid(row=4, column=3, rowspan=2, sticky=N+S+W+E)

        self.Return = Button(self, text="Back to Input Window", bg="blue", fg="white",
                             command=self.previous_page)
        self.Return.grid(row=6, column=3, pady=(7,7), sticky=N+S+W+E)


    def getMap(self):
        self.Imagefile = 'Aachen_Map_Draft.png'
        self.Image = Image.open(self.Imagefile).resize((256, 256), resample=PIL.Image.LANCZOS)
        self.Img = ImageTk.PhotoImage(self.Image)

    def loading(self):
        messagebox.showerror(title="Error", message="No data yet.")

    def losses(self):
        messagebox.showerror(title="Error", message="No data yet.")

    def eex(self):
        global count1, count10
        import EEX_prices
        if count10 == 1:
            self.EEX_prices = importlib.reload(EEX_prices)
        count10 = 1

    def opf(self):
        global count9
        import OPF_test1
        if count9 == 1:
            self.OPF_test1 = importlib.reload(OPF_test1)
        count9 = 1

    def setDate(evet, *args):
        global time_display, date_time, date
        global count1, count2, count3, count4
        # date.set('1/5/2017')
        if count1 == 1:
            date.set('Winter Weekday')
        if count2 == 1:
            date.set('Winter Weekend')
        if count3 == 1:
            date.set('Summer Weekday')
        if count4 == 1:
            date.set('Summer Weekend')
        if count == [0,0,0,0]:
            date.set('???????')
        text4 = 'Date & Time:\n' + date.get() + '\n' + time_display.get()
        date_time.set(text4)

    def previous_page(self):
        self.controller.show_frame(InputWindow)


root = Tk()

tkvar_pv = StringVar(root)
tkvar_wind = StringVar(root)
time = StringVar(root)
time_display = StringVar(root)
date = StringVar(root)
date_time = StringVar(root)
auto_percentage = StringVar(root)
auto_percentage_display = StringVar(root)
steel_percentage = StringVar(root)
steel_percentage_display = StringVar(root)

time.set('0')
time_display.set('00:00')
auto_percentage.set('0')
steel_percentage.set('0')
tkvar_pv.set('1')
tkvar_wind.set('1')

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count = [count1, count2, count3, count4]
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0

root.configure(bg="white")
root.title(string="FlAixEnergy Simulator")
root.iconbitmap(default="FEN_logo.ico")
root.resizable(width=FALSE, height=FALSE)
app = WindowController()
app.mainloop()
