"""
GUI counter
"""
# MCS 260 Fall 2021
# David Dumas
import tkinter
import tkinter.ttk

class CounterApp(tkinter.Tk):
    "Counter application main window"
    def __init__(self):
        "Set up the GUI"
        # Call the tkinter.Tk constructor
        super().__init__()
        # Now add the GUI elements we want
        self.title("Counter")

        self.b = tkinter.ttk.Button(self,text="Increment",command=self.click)
        self.b.grid(row=0,column=0,padx=5,pady=5,ipadx=10,ipady=10,sticky="nsew")

        self.lbl = tkinter.ttk.Label(self,text="0",width=3,anchor="center")
        self.lbl.grid(row=0,column=1,padx=5,pady=5,ipadx=10,ipady=10,sticky="nsew")

        self.n = 0

    def click(self):
        self.n += 1
        self.lbl.config(text=str(self.n))

g = CounterApp()
g.mainloop()