"""GUI demo: whack-a-mole starter"""
# MCS 260 Fall 2021
# David Dumas
import random
import time
import tkinter
import tkinter.ttk

class MoleGame(tkinter.Tk):
    "Whack-a-mole game"
    def __init__(self):
        "Create main window and buttons"
        # Call the tkinter.Tk constructor
        super().__init__()
        # Now add the GUI elements we want
        self.title("Hit the mole")

        # Build buttons that initially all say "Mole" on them
        self.b0 = tkinter.ttk.Button(self,text="Mole",command=self.click0)
        self.b0.grid(row=0,column=0,padx=5,pady=5,ipadx=10,ipady=10,sticky="nsew")

        self.b1 = tkinter.ttk.Button(self,text="Mole",command=self.click1)
        self.b1.grid(row=0,column=1,padx=5,pady=5,ipadx=10,ipady=10,sticky="nsew")

        self.b2 = tkinter.ttk.Button(self,text="Mole",command=self.click2)
        self.b2.grid(row=0,column=2,padx=5,pady=5,ipadx=10,ipady=10,sticky="nsew")

        self.b3 = tkinter.ttk.Button(self,text="Mole",command=self.click3)
        self.b3.grid(row=0,column=3,padx=5,pady=5,ipadx=10,ipady=10,sticky="nsew")

        self.buttons = [self.b0, self.b1, self.b2, self.b3]

        #----------------------------------------------------------
        # Let's just show how you might change every button's text
        # (you might adapt this part and use it elsewhere, but
        #  you should definitely delete it from the constructor)
        for i,b in enumerate(self.buttons):
            b.config(text="Btn"+str(i))

    def click0(self):
        print("Button 0 was pressed")
        self.quit()  # Tk.quit() exits the application

    def click1(self):
        print("Button 1 was pressed")
        self.quit()

    def click2(self):
        print("Button 2 was pressed")
        self.quit()

    def click3(self):
        print("Button 3 was pressed")
        self.quit()

g = MoleGame()
g.mainloop()