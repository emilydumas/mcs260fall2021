# MCS 260 Fall 2021 Lecture 16
import csv
import os

# To be discussed in lecture 17: This is the way to
# join a directory and filename that uses "\\" or "/"
# depending on the operating system preference.
fn = os.path.join("data","grades.csv")

fobj = open(fn,"r",encoding="UTF-8")
rdr = csv.reader(fobj)

print("Reading from {}:".format(fn))

# work with rdr to read rows from the file
# need to skip the first row which contains headers, however
firstrow = True
for row in rdr:
    if firstrow:
        firstrow = False
    else:
        # Not the first row
        name = row[0]
        midterm = float(row[1])
        final = float(row[2])
        print("{} has midterm + final average {:.2f}".format(
            name,
            (midterm+final)/2
        ))

fobj.close()