"""Mini terminal application for demonstration purposes"""
# MCS 260 Fall 2021 Lecture 18

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
        # STUB: add actual implementation here
        print("Received request:")
        print("    Command:",name)
        print("   Argument:",arg)
    else:
        print("Invalid command:",s)
        print("Commands consists of at most 2 words")
