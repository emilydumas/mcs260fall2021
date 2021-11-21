"""GUI demo: password generator"""
# MCS 260 Fall 2021 Lecture 38
import tkinter
import tkinter.ttk

class PwGenApp(tkinter.Tk):
    "Password generator application main window"
    def __init__(self):
        # Call the tkinter.Tk constructor
        super().__init__()
        # Now add the GUI elements we want
        self.title("UltraPassword XL 5000+")

        self.pwdisp = tkinter.ttk.Entry(self,width=25)
        self.pwdisp.grid(row=0,column=0,columnspan=4,padx=15,pady=15,sticky="ew")

        self.cbdigit = tkinter.ttk.Checkbutton(self,text="Digit")
        self.cbdigit.grid(row=1,column=0,columnspan=4,sticky="w",padx=15)

        self.cbcapital = tkinter.ttk.Checkbutton(self,text="Capital")
        self.cbcapital.grid(row=2,column=0,columnspan=4,sticky="w",padx=15)

        self.cbsymbol = tkinter.ttk.Checkbutton(self,text="Symbol")
        self.cbsymbol.grid(row=3,column=0,columnspan=4,sticky="w",padx=15)

        self.lenlabel = tkinter.ttk.Label(self,text="Length")
        self.lenlabel.grid(row=4,column=0,columnspan=4,sticky="w",padx=15,pady=(15,0))

        self.lenslider = tkinter.ttk.Scale(self)
        self.lenslider.grid(row=5,column=0,columnspan=3,sticky="ew",padx=15)

        self.lensliderdisp = tkinter.ttk.Label(self,text="8",width=5)
        self.lensliderdisp.grid(row=5,column=3,sticky="ew",padx=5)

        self.nllabel = tkinter.ttk.Label(self,text="Non-letter probability")
        self.nllabel.grid(row=6,column=0,columnspan=4,sticky="w",padx=15,pady=(15,0))

        self.nlslider = tkinter.ttk.Scale(self)
        self.nlslider.grid(row=7,column=0,columnspan=3,sticky="ew",padx=15)

        self.nlsliderdisp = tkinter.ttk.Label(self,text="100%",width=5)
        self.nlsliderdisp.grid(row=7,column=3,sticky="ew",padx=5)

        self.genbutton = tkinter.ttk.Button(self,text="Generate",width=15)
        self.genbutton.grid(row=8,column=0,columnspan=2,sticky="ew",padx=15,pady=15)

        self.exitbutton = tkinter.ttk.Button(self,text="Exit",width=15)
        self.exitbutton.grid(row=8,column=2,columnspan=2,sticky="ew",padx=15,pady=15)

app = PwGenApp()
app.mainloop()
