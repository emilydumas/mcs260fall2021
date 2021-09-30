"""Find hazardous material spill reports involving UIC"""
# MCS 260 Fall 2021 Lecture 16 (offline example)
import sys
import os
import csv

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = os.path.join("data","iema_hazardous_material_spills.csv")
    print("No input filename was specified, so I'm going to try \"{}\".".format(fn))

# ---
# check if the file exists.  We haven't talked about how this works yet, but
# it's here to make the program easier to use.
if not os.path.exists(fn):
    print("The file \"{}\" was not found.".format(fn))
    print("This program expects to read a specific CSV dataset from IEMA")
    print("containing information about hazardous material spills.")
    print("You can specify the CSV file to use as a command line argument.")
    print("The CSV dataset is available from:")
    print(" * Original source: https://data.illinois.gov/dataset/469iema_hazardous_material_spills")
    print(" * Course sample code repo: https://raw.githubusercontent.com/daviddumas/mcs260fall2021/main/samplecode/data/iema_hazardous_material_spills.csv")
    exit(1)
# ---

searchterm = "University of Illinois at Chicago"

# We convert the search term to lower case since we'll
# also do that to each value from the CSV file, accomplishing
# a case-insensitive search.
searchterm = searchterm.lower()

# Open the CSV
fobj = open(fn,"r",encoding="UTF-8",newline="")
print("File opened.")

# Create a reader that will give us rows as dictionaries
# (keys taken from the first row of the file)
rdr = csv.DictReader(fobj)

matches = 0
for row in rdr:
    # This dataset has two similarly-named columns:
    # "Name " stores the name of the reporting organization
    # "Name" stores the name of the hazardous material that was released
    if searchterm in row["Name "].lower():
        # UIC is the reporting organization; print info about this report.
        print("-"*70)
        print("Incident Number:",row["Incident Number"])
        print("Incident Report Date:",row["Incident Report Date"])
        # The address often has newlines in it; convert to spaces for a nice
        # one-line report of the location.
        print("Address:",row["Street Address of Incident Location"].replace("\n"," "))
        print("Material:",row["Name"])
        print("Amount:",row["Amount Released"])
        matches = matches + 1
print("-"*70)
print("Total matches:",matches)

fobj.close()