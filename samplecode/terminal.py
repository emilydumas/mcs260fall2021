"""Mini terminal application for demonstration purposes"""
# MCS 260 Fall 2021 Lecture 18 (unified version)

import os

MSG_UNKNOWN = "Unknown or malformed command.  (The 'help' command will list known commands.)"
MSG_HELP = """Known commands:
help - get help
exit - quit the program
listdir PATH - list the contents of a directory
numfiles PATH - show number of files and subdirs in a directory
create PATH - make a new empty file
moveto PATH - change current working directory
whereami - show current working directory
copy SOURCE DEST - copy contents of SOURCE to new file DEST
"""

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
            # print the CWD
            print(os.getcwd())
        elif name == "help":
            print(MSG_HELP)
        else:
            print(MSG_UNKNOWN)
    elif len(cmdparts) == 2:
        # Commands that take one argument
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
        elif name == "moveto":
            # change the CWD to arg
            os.chdir(arg)
        else:
            print(MSG_UNKNOWN)
    elif len(cmdparts) == 3:
        # Commands that take two arguments
        name = cmdparts[0]
        arg1 = cmdparts[1]
        arg2 = cmdparts[2]
        if name == "copy":
            # copy the file named arg1 to a new file named arg2
            if os.path.exists(arg2):
                print("ERROR: Refusing to overwrite existing file")
            else:
                # NOTE: This way of copying requires enough memory to
                # store the entire file contents.  It is possible to copy
                # a file incrementally, but we don't do that because we
                # haven't covered the way to read data in limited-size
                # blocks other than lines
                infile=open(arg1,"rb")  # "b" means "even if it's not a text file"
                data=infile.read()
                infile.close()
                outfile=open(arg2,"wb")
                outfile.write(data)
                outfile.close()
        else:
            print(MSG_UNKNOWN)
    else:
        # 3 or more arguments
        print(MSG_UNKNOWN)
