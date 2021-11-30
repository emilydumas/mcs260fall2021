"""GUI demo: Using a frame widget"""
# Not used in lectures, provided for reference
import tkinter
import tkinter.ttk

class DemoApp(tkinter.Tk):
    """Frame demo: One grid cell contains a frame,
    in which we make another grid of widgets"""
    def __init__(self):
        # Call the tkinter.Tk constructor
        super().__init__()

        # The main window's grid has one column and three rows:
        #    BUTTON  row=0
        #    FRAME   row=1
        #    BUTTON  row=2
        self.top_btn = tkinter.ttk.Button(self,text="Exit",command=self.quit)
        self.top_btn.grid(row=0,column=0,sticky="ew")

        self.bot_btn = tkinter.ttk.Button(self,text="Add column",command=self.addcol)
        self.bot_btn.grid(row=2,column=0,sticky="ew")

        self.inner_fr = tkinter.ttk.Frame()
        self.inner_fr.grid(row=1,column=0)

        # The Frame will have its own grid, with one row and 3 columns
        # and we can add more columns to it later (without messing up
        # the grid of the main window!)
        #    BUTTON BUTTON BUTTON
        #    col=0  col=1  col=2
        
        self.colcount = 3
        for i in range(self.colcount):
            # !! KEY POINT !!
            # NOTE the `self.inner_fr` in the next constructor, instead of the usual
            # parent, `self`.  That means the parent of this button is not the main
            # window, but is the frame widget we already put into the main window.
            newbtn = tkinter.ttk.Button(self.inner_fr,text="Btn{}".format(i+1))
            newbtn.grid(row=0,column=i) # this grid is within the frame,
                                        # separate from the outer grid!
        
        # Note: If we had any need to hold on to the buttons we made above, 
        # we could have created a list like
        #   self.inner_buttons = []
        # above the loop and then called
        #   self.inner_buttons.append(newbtn)
        # inside the loop.

    def addcol(self):
        "Add another column of buttons to the inner frame"
        newbtn = tkinter.ttk.Button(self.inner_fr,text="Btn{}".format(self.colcount+1))
        newbtn.grid(row=0,column=self.colcount)
        self.colcount += 1

app = DemoApp()
app.mainloop()
