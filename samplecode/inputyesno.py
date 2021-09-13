# MCS 260 Fall 2021 Lecture 9
# Function example: read yes/no answer
# from keyboard.
# David Dumas

def input_yes_no():  # no parameters
    while True:
        s = input("Enter yes/y or no/n: ")
        s = s.lower()  # convert s to lowercase
        if s in ["yes", "y"]:
            # handle yes
            s = "yes"
            break
        elif s in ["no","n"]:
            # handle no
            s = "no"
            break
        else:
            print("Answer not recognized.")
    # If we get here, they've given an acceptable
    # answer, and it is stored in s as either "yes"
    # or "no"
    return s


print("Are you enjoying MCS 260 so far?")
answer = input_yes_no()
print("Thank you for your response, which was:",answer)