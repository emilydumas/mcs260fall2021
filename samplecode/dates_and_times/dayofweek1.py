"""
Show the day of week of a YYYY-MM-DD date
"""

import datetime
import sys

if len(sys.argv) < 2:
    print("YYYY-MM-DD date must be given as command line argument")
    exit(1)

dt = datetime.datetime.strptime(sys.argv[1],"%Y-%m-%d")
print(dt.strftime("%A"))
