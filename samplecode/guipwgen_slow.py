"""GUI demo: password generator with slow generator function"""
# MCS 260 Fall 2021 Lecture 38, 40, and 43
import tkinter
import tkinter.ttk
import pwgen
import threading

class PwGenWorker(threading.Thread):
    """
    An object storing password settings (length, requirements, ...)
    and automatically generates a password meeting those requirements
    in a separate thread (any time the requirements change).
    """
    def __init__(self):
        super().__init__(daemon=True)  # Make it so the worker thread exits when the GUI does
        # Event used to indicate a new password is needed
        self.new_pw_needed = threading.Event()
        self.new_pw_needed.set()  # Make sure a pw is generated as soon as we start
        # Build the variables
        #   Output variable: The current password
        self.password = tkinter.StringVar()
        #   Password requirements
        self.digit_required = tkinter.IntVar()
        self.capital_required = tkinter.IntVar()
        self.symbol_required = tkinter.IntVar()
        #   Password length
        self.length = tkinter.IntVar()
        self.length.set(3)
        #   Non-lowercase fraction
        self.nlfrac = tkinter.DoubleVar()
        self.nlfrac.set(0.0)
        # Setup automatic regeneration of a new password if 
        # any variable changes
        self.symbol_required.trace_add("write",self.request_new)
        self.capital_required.trace_add("write",self.request_new)
        self.digit_required.trace_add("write",self.request_new)
        self.length.trace_add("write",self.request_new)
        self.nlfrac.trace_add("write",self.request_new)

    def request_new(self,*args):
        "Signal to the worker thread that a new password is needed"
        # CALLED FROM THE GUI THREAD
        self.new_pw_needed.set()
    
    def run(self):
        """Body of the worker thread: Wait until a new password is needed
        and then generate it."""
        # CALLED FROM THE WORKER THREAD
        while True:
            self.new_pw_needed.wait()  # pause until the new_pw_needed event is set
            self.new_pw_needed.clear() # cancel the new_pw_needed signal
            print("Generating a new password")
            s = pwgen.random_password(
                length=self.length.get(),
                special_frac=self.nlfrac.get(),
                require_capital=self.capital_required.get(),
                require_digit=self.digit_required.get(),
                require_symbol=self.symbol_required.get(),
                delay=3
            )
            self.password.set(s)
            print("Finished generating a new password")

class PwGenApp(tkinter.Tk):
    "Password generator application main window"
    def __init__(self):
        # Call the tkinter.Tk constructor
        super().__init__()
        # Now add the GUI elements we want
        self.title("UltraPassword XL 5000+")

        self.worker = PwGenWorker() # Make, but don't start the worker thread

        self.pwdisp = tkinter.ttk.Entry(self,width=25,textvariable=self.worker.password)
        self.pwdisp.grid(row=0,column=0,columnspan=4,padx=15,pady=15,sticky="ew")

        self.cbdigit = tkinter.ttk.Checkbutton(self,text="Digit",variable=self.worker.digit_required)
        self.cbdigit.grid(row=1,column=0,columnspan=4,sticky="w",padx=15)

        self.cbcapital = tkinter.ttk.Checkbutton(self,text="Capital",variable=self.worker.capital_required)
        self.cbcapital.grid(row=2,column=0,columnspan=4,sticky="w",padx=15)

        self.cbsymbol = tkinter.ttk.Checkbutton(self,text="Symbol",variable=self.worker.symbol_required)
        self.cbsymbol.grid(row=3,column=0,columnspan=4,sticky="w",padx=15)

        # Length control:  Name label, slider, value display
        
        self.worker.length.trace_add("write",self.update_lensliderdisp)

        self.lenlabel = tkinter.ttk.Label(self,text="Length")
        self.lenlabel.grid(row=4,column=0,columnspan=4,sticky="w",padx=15,pady=(15,0))

        self.lenslider = tkinter.ttk.Scale(self,from_=3,to=16,variable=self.worker.length)
        self.lenslider.grid(row=5,column=0,columnspan=3,sticky="ew",padx=15)

        self.lensliderdisp = tkinter.ttk.Label(self,text="8",width=5)
        self.lensliderdisp.grid(row=5,column=3,sticky="ew",padx=5)

        # Non-letter fraction control:  Name label, slider, value display
        self.worker.nlfrac.trace_add("write",self.update_nlsliderdisp)

        self.nllabel = tkinter.ttk.Label(self,text="Non-letter fraction")
        self.nllabel.grid(row=6,column=0,columnspan=4,sticky="w",padx=15,pady=(15,0))

        self.nlslider = tkinter.ttk.Scale(self,from_=0.0,to=0.5,variable=self.worker.nlfrac)
        self.nlslider.grid(row=7,column=0,columnspan=3,sticky="ew",padx=15)

        self.nlsliderdisp = tkinter.ttk.Label(self,text="100%",width=5)
        self.nlsliderdisp.grid(row=7,column=3,sticky="ew",padx=5)

        self.genbutton = tkinter.ttk.Button(self,text="Generate",width=15,command=self.worker.request_new)
        self.genbutton.grid(row=8,column=0,columnspan=2,sticky="ew",padx=15,pady=15)

        self.exitbutton = tkinter.ttk.Button(self,text="Exit",width=15,command=self.quit)
        self.exitbutton.grid(row=8,column=2,columnspan=2,sticky="ew",padx=15,pady=15)

        # Make a first call to each update function
        self.update_lensliderdisp()
        self.update_nlsliderdisp()

        # Start the worker thread
        self.worker.start()

    def update_lensliderdisp(self,*args):
        "Change the text displayed next to the length slider to reflect its current value"
        s = str(self.worker.length.get())
        self.lensliderdisp.config(text=s)

    def update_nlsliderdisp(self,*args):
        "Change the text displayed next to the nl fraction slider to reflect its current value"
        s = str(int(self.worker.nlfrac.get()*100))+"%"
        self.nlsliderdisp.config(text=s)

app = PwGenApp()
app.mainloop()
