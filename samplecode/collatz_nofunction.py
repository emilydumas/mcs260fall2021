# MCS 260 Fall 2021 Lecture 9

n = int(input("Give me an integer: "))
for k in range(50):
    print(n)
    if n % 2 == 0:
        n = n//2
    else:
        n = 3*n+1

