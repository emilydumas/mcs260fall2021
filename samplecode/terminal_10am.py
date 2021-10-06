"""Mini terminal application for demonstration purposes"""
# MCS 260 Fall 2021 Lecture 18 (10am)

import os

while True:
    # Prompt for input
    s=input("? ")
    cmdparts = s.split()
    if len(cmdparts) == 0:
        print("No command given.")
    elif len(cmdparts) == 1:
        if cmdparts[0] == "exit":
            exit()
        else:
            print("Invalid command:",s)
            print("Valid 1-word commands: exit")
    elif len(cmdparts) == 2:
        name = cmdparts[0]
        arg = cmdparts[1]
        if name == "list":
            # list files in the directory arg
            for fn in os.listdir(arg):
                print(fn)
        elif name == "numfiles":
            # print the number of files in directory arg
            numfiles = 0
            numdirs = 0   # arg might be "C:\Users\ddumas\Dropbox\teaching\mcs260\public\samplecode"
            for fn in os.listdir(arg):
                if os.path.isfile(os.path.join(arg,fn)):  # fn might be "map1.json"
                    numfiles = numfiles + 1
                elif os.path.isdir(os.path.join(arg,fn)):
                    numdirs = numdirs + 1
            print("{} files\n{} dirs".format(numfiles,numdirs))
    else:
        print("Invalid command:",s)
        print("Commands consists of at most 2 words")
