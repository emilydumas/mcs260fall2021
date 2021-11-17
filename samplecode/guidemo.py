"""GUI demo using tkinter"""
# MCS 260 Fall 2021 Lecture 36

import tkinter      # contains window classes and constants
import tkinter.ttk  # contains all the widgets (e.g. buttons, sliders, ...)

# The next three functions are called by certain buttons in the GUI.
# tkinter always calls such functions with a few arguments, often
# not useful to the function.  But we need the function to *allow*
# arguments to be passed.

def quitfn(*args):
    """Exit the program (but be tolerant of 
    being called with any number of arguments)"""
    exit()

def display_message(*args):
    lbl.config(text="Great project proposal!!!")

def clear_message(*args):
    lbl.config(text="")

app = tkinter.Tk()  # make an object representing our program (or its GUI)
# Set the window title (also shown in taskbar in some OS)
app.title("MCS 260 GUI demo")


# Now, we make the widgets.  Each widget has a "parent", which in this
# case is the object `app`.

# Each widget also has a .grid method to specify where it should go within
# the parent window.  Placement is specified using a rectangular grid:
#
#   column 0 row 0       column 1 row 0       column 2 row 0
#   column 0 row 1       column 1 row 1       column 2 row 1


# Button labeled "show" in the top left
btn = tkinter.ttk.Button(app,text="Show",command=display_message)
btn.grid(column=0,row=0)

# Button labeled "hide" in the top middle
btn2 = tkinter.ttk.Button(app,text="Hide",command=clear_message)
btn2.grid(column=1,row=0)

# Button labeled "exit" in the top right
btn3 = tkinter.ttk.Button(app,text="Exit",command=quitfn)
btn3.grid(column=2,row=0)

# Area for non-editable text (a "label") in the bottom left
lbl = tkinter.ttk.Label(app,
    text="",
    width=35 # number of characters
    )
lbl.grid(column=0,row=1)

# A checkbox (doesn't do anything right now)
cb = tkinter.ttk.Checkbutton(
    app,
    text="Awesome"
)
cb.grid(column=1,row=1)

# Start the GUI.  This function won't return until the window is
# closed, typically when the program exits.  That means we lose 
# control from here on; the program just *responds* to things the
# user does.
app.mainloop()