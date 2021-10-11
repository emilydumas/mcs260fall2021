"""Mini terminal application for demonstration purposes"""
# MCS 260 Fall 2021 Lecture 21
# Function-based version of terminal.py

import os

#----------------------------------------------------------------------
#                    Functions that provide commands

def do_unknown():
    print("Unknown or malformed command.  (The 'help' command will list known commands.)")

def do_help():
    print("""Known commands:
help - get help
exit - quit the program
listdir PATH - list the contents of a directory
numfiles PATH - show number of files and subdirs in a directory
create PATH - make a new empty file
moveto PATH - change current working directory
whereami - show current working directory
copy SOURCE DEST - copy contents of SOURCE to new file DEST
""")

def do_whereami():
    """show current working directory"""
    print(os.getcwd())

def do_moveto(a):
    """change current working directory"""
    os.chdir(a)

def do_listdir(a):
    """list the contents of a directory"""
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


# Main loop

while True:
    # Prompt for input
    s=input("? ")
    cmdparts = s.split()
    if len(cmdparts) == 0:
        print("No command given.")
    elif len(cmdparts) == 1:
        # Commands that take no arguments
        name = cmdparts[0]
        if name == "exit":
            exit()
        elif name == "whereami":
            do_whereami()
        elif name == "help":
            do_help()
        else:
            do_unknown()
    elif len(cmdparts) == 2:
        # Commands that take one argument
        name = cmdparts[0]
        arg = cmdparts[1]
        if name == "listdir":
            do_listdir(arg)
        elif name == "create":
            do_create(arg)
        elif name == "numfiles":
            do_numfiles(arg)
        elif name == "moveto":
            do_moveto(arg)
        else:
            do_unknown()
    elif len(cmdparts) == 3:
        # Commands that take two arguments
        name = cmdparts[0]
        arg1 = cmdparts[1]
        arg2 = cmdparts[2]
        if name == "copy":
            do_copy(arg1,arg2)
        else:
            do_unknown()
    else:
        # 3 or more arguments = invalid
        do_unknown()
