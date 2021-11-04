"""Locate phone numbers in a text file"""
# Regex example from MCS 260 Fall 2021

import re
import sys

if len(sys.argv) < 2:
    print("Usage: {} INPUTFILE".format(sys.argv[0]))
    exit(1)

f = open(sys.argv[1],"r",encoding="UTF-8")
for line in f:
    for m in re.finditer(r"(\d{3})-(\d{3})-(\d{4})",line):
        print("Possible phone number {} - Area code {}, exchange {}, line {}".format(
            m.group(),
            m.group(1),
            m.group(2),
            m.group(3)
        ))
f.close()
