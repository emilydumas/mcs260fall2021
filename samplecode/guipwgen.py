"""GUI demo: password generator"""
# MCS 260 Fall 2021 Lecture 38 and 40
import tkinter
import tkinter.ttk
import pwgen

class PwGenApp(tkinter.Tk):
    "Password generator application main window"
    def __init__(self):
        # Call the tkinter.Tk constructor
        super().__init__()
        # Now add the GUI elements we want
        self.title("UltraPassword XL 5000+")

        self.pwvalue = tkinter.StringVar()

        self.pwdisp = tkinter.ttk.Entry(self,width=25,textvariable=self.pwvalue)
        self.pwdisp.grid(row=0,column=0,columnspan=4,padx=15,pady=15,sticky="ew")

        self.digit_required = tkinter.IntVar()
        self.digit_required.trace_add("write",self.regenerate)
        self.capital_required = tkinter.IntVar()
        self.capital_required.trace_add("write",self.regenerate)
        self.symbol_required = tkinter.IntVar()
        self.symbol_required.trace_add("write",self.regenerate)

        self.cbdigit = tkinter.ttk.Checkbutton(self,text="Digit",variable=self.digit_required)
        self.cbdigit.grid(row=1,column=0,columnspan=4,sticky="w",padx=15)

        self.cbcapital = tkinter.ttk.Checkbutton(self,text="Capital",variable=self.capital_required)
        self.cbcapital.grid(row=2,column=0,columnspan=4,sticky="w",padx=15)

        self.cbsymbol = tkinter.ttk.Checkbutton(self,text="Symbol",variable=self.symbol_required)
        self.cbsymbol.grid(row=3,column=0,columnspan=4,sticky="w",padx=15)

        # Length control:  Name label, slider, value display
        
        self.lenvalue = tkinter.IntVar()
        self.lenvalue.set(3)
        self.lenvalue.trace_add("write",self.update_lensliderdisp)

        self.lenlabel = tkinter.ttk.Label(self,text="Length")
        self.lenlabel.grid(row=4,column=0,columnspan=4,sticky="w",padx=15,pady=(15,0))

        self.lenslider = tkinter.ttk.Scale(self,from_=3,to=16,variable=self.lenvalue)
        self.lenslider.grid(row=5,column=0,columnspan=3,sticky="ew",padx=15)

        self.lensliderdisp = tkinter.ttk.Label(self,text="8",width=5)
        self.lensliderdisp.grid(row=5,column=3,sticky="ew",padx=5)

        # Non-letter fraction control:  Name label, slider, value display

        self.nlvalue = tkinter.DoubleVar()
        self.nlvalue.set(0.0)
        self.nlvalue.trace_add("write",self.update_nlsliderdisp)

        self.nllabel = tkinter.ttk.Label(self,text="Non-letter fraction")
        self.nllabel.grid(row=6,column=0,columnspan=4,sticky="w",padx=15,pady=(15,0))

        self.nlslider = tkinter.ttk.Scale(self,from_=0.0,to=0.5,variable=self.nlvalue)
        self.nlslider.grid(row=7,column=0,columnspan=3,sticky="ew",padx=15)

        self.nlsliderdisp = tkinter.ttk.Label(self,text="100%",width=5)
        self.nlsliderdisp.grid(row=7,column=3,sticky="ew",padx=5)

        self.genbutton = tkinter.ttk.Button(self,text="Generate",width=15,command=self.regenerate)
        self.genbutton.grid(row=8,column=0,columnspan=2,sticky="ew",padx=15,pady=15)

        self.exitbutton = tkinter.ttk.Button(self,text="Exit",width=15,command=self.quit)
        self.exitbutton.grid(row=8,column=2,columnspan=2,sticky="ew",padx=15,pady=15)

        # Make a first call to each update function
        self.update_lensliderdisp()
        self.update_nlsliderdisp()

    def update_lensliderdisp(self,*args):
        "Change the text displayed next to the length slider to reflect its current value"
        s = str(self.lenvalue.get())
        self.lensliderdisp.config(text=s)
        self.regenerate()

    def update_nlsliderdisp(self,*args):
        "Change the text displayed next to the nl fraction slider to reflect its current value"
        s = str(int(self.nlvalue.get()*100))+"%"
        # s = "{:.0f}%".format(self.nlvalue.get())
        self.nlsliderdisp.config(text=s)
        self.regenerate()

    def regenerate(self,*args):
        "Generate a new random password and update the display"
        s = pwgen.random_password(
            length=self.lenvalue.get(),
            special_frac=self.nlvalue.get(),
            require_capital=self.capital_required.get(),
            require_digit=self.digit_required.get(),
            require_symbol=self.symbol_required.get()
        )
        self.pwvalue.set(s)

app = PwGenApp()
app.mainloop()
