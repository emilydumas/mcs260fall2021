"""
Show the day of week of a date in the Gregorian calendar
(and be flexible about what format is used)
"""

import datetime
import sys

def arg_to_dt(s):
    """
    Convert a string to date, accepting formats:
    2021-08-23
    23 August 2021
    23 Aug 2021
    August 23 2021
    August 23, 2021
    Aug 23 2021
    Aug 23, 2021
    """
    formats_accepted = [
        "%Y-%m-%d",  # 2021-08-23
        "%d %b %Y",  # 23 Aug 2021
        "%d %B %Y",  # 23 August 2021
        "%B %d, %Y", # August 23, 2021
        "%B %d %Y",  # August 23 2021
        "%b %d, %Y", # Aug 23, 2021
        "%b %d %Y",  # Aug 23 2021
    ]
    for fmt in formats_accepted:
        try:
            dt = datetime.datetime.strptime(s,fmt)
            return dt
        except ValueError:
           pass  # A statement that does nothing

    raise ValueError("string '{}' did not match any of the allowed date formats".format(s))


def usage():
    "Show usage message and quit"
    print("USAGE: {} DATE".format(sys.argv[0]))
    print("""
Show the day of week for a date in the Gregorian calendar.
Date can be in a number of formats, including
2021-08-23
23 Aug 2021
Aug 23, 2021
with abbreviated or full month name.

For dates containing spaces, you will need to enclose the
date in quotes to avoid it being seen as multiple arguments.

Example: {} 2021-08-23""".format(sys.argv[0]))
    exit(1)

if __name__=="__main__":
    if len(sys.argv) < 2:
        usage()
    dt = arg_to_dt(sys.argv[1])
    print(dt.strftime("%A"))
