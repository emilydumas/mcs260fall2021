"""
Tuesdays between two dates
"""

import datetime
import sys

def usage():
    "Show usage message and quit"
    print("USAGE: {} DATE1 DATE2".format(sys.argv[0]))
    exit(1)

if __name__=="__main__":
    if len(sys.argv) < 3:
        usage()
    dt1 = datetime.datetime.strptime(sys.argv[1],"%Y-%m-%d")
    dt2 = datetime.datetime.strptime(sys.argv[2],"%Y-%m-%d")

    date1 = dt1.date()
    date2 = dt2.date()

    day = datetime.timedelta(days=1)

    while date1 <= date2:
        if date1.weekday() == 1:
            print(date1.strftime("%Y-%m-%d"))
        date1 += day

