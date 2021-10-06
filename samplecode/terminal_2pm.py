"""Mini terminal application for demonstration purposes"""
# MCS 260 Fall 2021 Lecture 18 (2pm)

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
        if name == "listdir":
            # Show the list of files in the directory arg
            for fn in os.listdir(arg):
                print(fn)
        elif name == "create":
            # Make a new empty file with name arg
            if os.path.exists(arg):
                print("ERROR: {} already exists".format(arg))
            else:
                # File does not exist; ok to create
                open(arg,"w").close()
        elif name == "whereami":
            # print the CWD
            print(os.getcwd())
        elif name == "move":
            # change the CWD to arg
            os.chdir(arg)
    elif len(cmdparts) == 3:
        name = cmdparts[0]
        arg1 = cmdparts[1]
        arg2 = cmdparts[2]
        if name == "copy":
            # copy the file named arg1 to a new file named arg2
            if os.path.exists(arg2):
                print("ERROR: Refusing to overwrite existing file")
            else:
                infile=open(arg1,"rb")
                data=infile.read()
                infile.close()
                outfile=open(arg2,"wb")
                outfile.write(data)
                outfile.close()
    else:
        print("Invalid command:",s)
        print("Commands consists of at most 2 words")
