# MCS 260 Fall 2021 Lecture 16 (offline example)
import sys
import csv
import os

if len(sys.argv) < 2:
    print("Usage: {} INPUTFILE.csv".format(sys.argv[0]))
    exit(1)

fn = sys.argv[1]
try:
    fobj = open(fn,"r",encoding="UTF-8")
except OSError as e:
    print("Failed to open input file:",e)
    exit(1)
rdr = csv.reader(fobj)

print("Report on:",fn)
print("Columns in this CSV file:")
firstrow = True
numrows = 0
for row in rdr:
    if firstrow:
        firstrow = False
        cols = []
        for i,k in enumerate(row):
            if k in cols:
                print("  * {} (index {}) DUPLICATE COLUMN NAME!!".format(k,i))
            else:
                print("  * {} (index {})".format(k,i))
                cols.append(k)
    else:
        numrows = numrows + 1

print("Total rows (excluding header):",numrows)

fobj.close()