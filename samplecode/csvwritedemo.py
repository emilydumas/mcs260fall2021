"""Print a table of values to a CSV file"""
# MCS 260 Fall 2021 Lecture 16 (offline example)
import csv
import os

# To be discussed in lecture 17: This is the way to
# join a directory and filename that uses "\\" or "/"
# depending on the operating system preference.
fn = os.path.join("data","sample.csv")

# To be discussed in lecture 17: This function checks
# whether a given filename exists
if os.path.exists(fn):
    print("The file {} already exists. Exiting rather than overwriting it.".format(fn))
    exit(1)

fobj = open(fn,"w",encoding="UTF-8",newline="")
writer = csv.writer(fobj)

writer.writerow(["n","square of n plus one"])
for x in range(1,1001):
    writer.writerow([x,x*x+1])

fobj.close()