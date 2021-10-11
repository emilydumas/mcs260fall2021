"""Mini terminal application for demonstration purposes"""
# MCS 260 Fall 2021 Lecture 21
# Function-based version of terminal.py

import os

#----------------------------------------------------------------------
#                    Functions that provide commands

def do_exit():
    """exit the program"""
    exit()

def do_unknown():
    print("Unknown or malformed command.  (The 'help' command will list known commands.)")

def do_help():
    """print a help message"""
    print("Known commands:")
    for name in handlers:
        print(name,"-",handlers[name].__doc__)

def do_whereami():
    """show current working directory"""
    print(os.getcwd())

def do_moveto(a):
    """change current working directory"""
    os.chdir(a)

def do_listdir(*args):
    """list the contents of a directory"""
    if len(args) > 1:
        raise TypeError("listdir accepts at most one argument")
    if len(args) == 1:
        a = args[0]
    else:
        a = os.getcwd()
    for fn in os.listdir(a):
        print(fn)

def do_numfiles(a):
    """show number of files and subdirs in a directory"""
    numfiles = 0
    numdirs = 0   # a might be "C:\Users\ddumas\Dropbox\teaching\mcs260\public\samplecode"
    for fn in os.listdir(a):
        if os.path.isfile(os.path.join(a,fn)):  # fn might be "map1.json"
            numfiles = numfiles + 1
        elif os.path.isdir(os.path.join(a,fn)):
            numdirs = numdirs + 1
    print("{} files\n{} dirs".format(numfiles,numdirs))

def do_create(a):
    """make a new empty file"""
    if os.path.exists(a):
        print("ERROR: {} already exists".format(a))
    else:
        # File does not exist; ok to create
        open(arg,"w").close()

def do_copy(src,dst):
    """copy contents of SRC to new file DST"""
    # copy the file named arg1 to a new file named arg2
    if os.path.exists(dst):
        print("ERROR: Refusing to overwrite existing file")
    else:
        # TODO: Replace with memory-efficient incremental copy
        infile=open(src,"rb")  # "b" means "even if it's not a text file"
        data=infile.read()
        infile.close()
        outfile=open(dst,"wb")
        outfile.write(data)
        outfile.close()
#----------------------------------------------------------------------

# Dispatch table
handlers = {
    "help": do_help,
    "exit": do_exit,
    "listdir": do_listdir,
    "numfiles": do_numfiles,
    "create": do_create,
    "moveto": do_moveto,
    "whereami": do_whereami,
    "copy": do_copy
}


# Main loop

while True:
    # Prompt for input
    s=input("? ")
    cmdparts = s.split()
    if len(cmdparts) == 0:
        print("No command given.")
    else:
        name = cmdparts[0]
        args = cmdparts[1:]
        if name in handlers:
            try:
                handlers[name](*args)
            except TypeError:
                print("Malformed command (wrong number of args?)")
        else:
            do_unknown()
