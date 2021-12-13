"tkinter GUI to convert integer between bases"
# MCS 260 Fall 2021 David Dumas
import tkinter
import tkinter.ttk

def decimal_to_base(n,b):
    """
    Convert integer `n` to string in base `b`, where base-`b` digits
    beyond the first 10 are given by uppercase letters a-z.
    """
    DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # If n is a string or float, convert to int first.
    if not isinstance(n,int):
        n = int(n)
    if n < 0:
        raise ValueError("n must be greater than or equal to 0")
    if b < 2 or b > 36:
        raise ValueError("b must be between 2 and 36")
    L = []
    while (not L) or n > 0:
        L.append(DIGITS[n%b])
        n = n//b
    return "".join(L[::-1])


class BaseConverterApp(tkinter.Tk):
    def __init__(self):
        "Create new Tk and add GUI elements and callbacks"
        super().__init__()
        
        self.title("Base conversion")
        
        lbl = tkinter.ttk.Label(self,text="Decimal:")
        lbl.grid(row=0,column=0,sticky="e",padx=10,pady=10)

        self.decimalvalue = tkinter.StringVar()
        self.decimalvalue.trace_add("write",self.update)
        self.decimalentry = tkinter.ttk.Entry(self,textvariable=self.decimalvalue,width=30)
        self.decimalentry.grid(row=0,column=1,columnspan=2,padx=10,pady=10)

        lbl = tkinter.ttk.Label(self,text="Converted:")
        lbl.grid(row=1,column=0,sticky="e",padx=10,pady=10)

        self.convertedvalue = tkinter.StringVar()
        self.convertedentry = tkinter.ttk.Entry(self,textvariable=self.convertedvalue,width=30)
        self.convertedentry.config(state="readonly") # Makes text read-only
        self.convertedentry.grid(row=1,column=1,columnspan=2,padx=10,pady=10)

        lbl = tkinter.ttk.Label(self,text="Base:")
        lbl.grid(row=2,column=0,sticky="e",padx=10,pady=10)

        self.basevalue = tkinter.IntVar()
        self.basevalue.set(2)
        self.slider = tkinter.ttk.Scale(self,from_=2,to=36,variable=self.basevalue)
        self.slider.grid(row=2,column=1,sticky="ew",padx=10,pady=10)

        self.basedisp = tkinter.ttk.Label(self,text="")
        self.basedisp.grid(row=2,column=2,padx=10,pady=10)

        self.basevalue.trace_add("write",self.update)
        self.basevalue.trace_add("write",self.show_new_base)

        self.show_new_base()
    
    def show_new_base(self,*args):
        "Update display label to reflect new base slider value"
        self.basedisp.config(text=str(self.basevalue.get()))

    def update(self,*args):
        "Update base conversion output display"
        try:
            n = int(self.decimalvalue.get())
        except ValueError:
            # If something goes wrong, we show nothing
            # in the output area
            self.convertedvalue.set("")
            return

        s = decimal_to_base(n,self.basevalue.get())
        self.convertedvalue.set(s)

app = BaseConverterApp()
app.mainloop()