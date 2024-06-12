"""GUI demo: whack-a-mole"""
# MCS 260 Fall 2021
# Emily Dumas
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

        self.b0 = tkinter.ttk.Button(self,text="Mole",command=self.click0)
        self.b0.grid(row=0,column=0,padx=5,pady=5,ipadx=10,ipady=10,sticky="nsew")

        self.b1 = tkinter.ttk.Button(self,text="Mole",command=self.click1)
        self.b1.grid(row=0,column=1,padx=5,pady=5,ipadx=10,ipady=10,sticky="nsew")

        self.b2 = tkinter.ttk.Button(self,text="Mole",command=self.click2)
        self.b2.grid(row=0,column=2,padx=5,pady=5,ipadx=10,ipady=10,sticky="nsew")

        self.b3 = tkinter.ttk.Button(self,text="Mole",command=self.click3)
        self.b3.grid(row=0,column=3,padx=5,pady=5,ipadx=10,ipady=10,sticky="nsew")

        self.buttons = [self.b0, self.b1, self.b2, self.b3]

        self.n = 0
        self.molepos = 0
        self.move_mole()

    def click0(self):
        if self.molepos == 0:
            self.move_mole()
        else:
            self.fail()

    def click1(self):
        if self.molepos == 1:
            self.move_mole()
        else:
            self.fail()

    def click2(self):
        if self.molepos == 2:
            self.move_mole()
        else:
            self.fail()

    def click3(self):
        if self.molepos == 3:
            self.move_mole()
        else:
            self.fail()

    def move_mole(self):
        if self.n == 0:
            self.t0 = time.time()
        elif self.n == 10:
            print("YOU WIN!  Time={:.1f}".format(time.time()-self.t0))
            self.quit()
        self.n += 1
        self.molepos = (self.molepos + random.randrange(1,3)) % 4
        for i,b in enumerate(self.buttons):
            if i == self.molepos:
                btn_text = "Mole"
            else:
                btn_text = ""
            b.config(text=btn_text)

    def fail(self):
        print("Sorry, better luck next time.")
        self.quit()

g = MoleGame()
g.mainloop()