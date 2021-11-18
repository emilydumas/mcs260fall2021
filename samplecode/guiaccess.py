"""
GUI demo using tkinter
Number pad accepting code 260 and rejecting anything else
"""
# MCS 260 Fall 2021 Lecture 38

import time
import tkinter      # contains window classes and constants
import tkinter.ttk  # contains all the widgets (e.g. buttons, sliders, ...)

print("FYI: The code is 2 6 0")

# Digits the user must enter to get a success message
passcode = [ 2, 6, 0 ]
# list storing digits entered so far
entered = []
# We want to change this variable inside functions.  To avoid
# the need for things we haven't covered (e.g. `global`) we
# do it by making a mutable global object, `statedata` and just
# changing the value associated with a key.  That can be done
# within a function without making `statedata` become a local
# variable.
statedata = {
    "state": "in progress"  # means we allow button presses
                            # while "failed" or "succeeded" mean
                            # we ignore button presses
}

#----------------------------------------------------------------------
# Functions that handle the state of:
# * recorded button presses so far
# * whether the user has failed or succeeded

def fail():
    lbl.config(text="ACCESS DENIED!")
    statedata["state"] = "failed"

def succeed():
    lbl.config(text="Access granted.")
    statedata["state"] = "succeeded"

def press(n):
    if statedata["state"] == "in progress":
        k = len(entered)
        if k >= len(passcode):
            fail()
        elif passcode[k] != n:
            fail()
        else:
            entered.append(n)
            lbl.config(text = "".join([ str(x) for x in entered ]))
            if entered == passcode:
                succeed()

#----------------------------------------------------------------------
# Functions that are called by buttons as the `command`

# TODO: Learn about the arguments that Tk passes well enough
# to replace all these similar functions with one function 
# that can determine which button called it.
def press0(*args):
    press(0)

def press1(*args):
    press(1)

def press2(*args):
    press(2)

def press3(*args):
    press(3)

def press4(*args):
    press(4)

def press5(*args):
    press(5)

def press6(*args):
    press(6)

def press7(*args):
    press(7)

def press8(*args):
    press(8)

def press9(*args):
    press(9)

def clear(*args):
    lbl.config(text="Code?")
    statedata["state"] = "in progress"
    while entered:
        entered.pop()

def exitarg(*args):
    """Wrapped around exit() that allows arguments"""
    exit()

#----------------------------------------------------------------------
# GUI setup
app = tkinter.Tk()  # make an object representing our program (or its GUI)
# Set the window title (also shown in taskbar in some OS)
app.title("Faculty club entry door")

lbl = tkinter.ttk.Label(app,width=16,font=("Arial",30))
lbl.grid(column=0,row=0,columnspan=3,sticky="ew")
lbl.config(anchor="center")
clear() # sets `lbl` to display the starting message

# TODO: Like the functions above, should figure out a way
# to make these buttons in a loop to avoid duplication.
b = tkinter.ttk.Button(app,text="1",command=press1)
b.grid(column=0,row=1,ipadx=20,ipady=20,sticky="nsew")
b = tkinter.ttk.Button(app,text="2",command=press2)
b.grid(column=1,row=1,ipadx=20,ipady=20,sticky="nsew")
b = tkinter.ttk.Button(app,text="3",command=press3)
b.grid(column=2,row=1,ipadx=20,ipady=20,sticky="nsew")
b = tkinter.ttk.Button(app,text="4",command=press4)
b.grid(column=0,row=2,ipadx=20,ipady=20,sticky="nsew")
b = tkinter.ttk.Button(app,text="5",command=press5)
b.grid(column=1,row=2,ipadx=20,ipady=20,sticky="nsew")
b = tkinter.ttk.Button(app,text="6",command=press6)
b.grid(column=2,row=2,ipadx=20,ipady=20,sticky="nsew")
b = tkinter.ttk.Button(app,text="7",command=press7)
b.grid(column=0,row=3,ipadx=20,ipady=20,sticky="nsew")
b = tkinter.ttk.Button(app,text="8",command=press8)
b.grid(column=1,row=3,ipadx=20,ipady=20,sticky="nsew")
b = tkinter.ttk.Button(app,text="9",command=press9)
b.grid(column=2,row=3,ipadx=20,ipady=20,sticky="nsew")
b = tkinter.ttk.Button(app,text="Clr",command=clear)
b.grid(column=0,row=4,ipadx=20,ipady=20,sticky="nsew")
b = tkinter.ttk.Button(app,text="0",command=press0)
b.grid(column=1,row=4,ipadx=20,ipady=20,sticky="nsew")
b = tkinter.ttk.Button(app,text="Exit",command=exitarg)
b.grid(column=2,row=4,ipadx=20,ipady=20,sticky="nsew")

# Start the GUI.  This function won't return until the window is
# closed, typically when the program exits.  That means we lose 
# control from here on; the program just *responds* to things the
# user does.
app.mainloop()