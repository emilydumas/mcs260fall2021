# MCS 260 Fall 2021 Lecture 9

def f(x):  # receive whatever program sent, in variable named x
    if x % 2 == 0:
        return x//2
    else:
        return 3*x+1

n = int(input("Give me an integer: "))
for k in range(50):
    print(n)
    n = f(n)  # send n to function f