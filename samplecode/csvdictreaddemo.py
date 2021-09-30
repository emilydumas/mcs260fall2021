# MCS 260 Fall 2021 Lecture 16 (offline example_
import csv
import os

# To be discussed in lecture 17: This is the way to
# join a directory and filename that uses "\\" or "/"
# depending on the operating system preference.
fn = os.path.join("data","grades.csv")

fobj = open(fn,"r",encoding="UTF-8")
rdr = csv.DictReader(fobj)

print("Reading from {}:".format(fn))

# work with rdr to read rows from the file
for row in rdr:
    # Not the first row
    print("{} has midterm + final average {:.2f}".format(
        row["fullname"],
        (float(row["midterm"]) + float(row["final"])) / 2
    ))

fobj.close()