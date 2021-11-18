"""
Show the amount of time between two datetimes
"""

import datetime
import sys


def arg_to_dt(s):
    """
    Convert a string to datetime, accepting formats:
    YYYY-MM-DD hh:mm:ss
    YYYY-MM-DD hh:mm
    YYYY-MM-DD
    """
    try:
        dt = datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
        return dt
    except ValueError:
        pass  # A statement that does nothing

    try:
        dt = datetime.datetime.strptime(s,"%Y-%m-%d %H:%M")
        return dt
    except ValueError:
        pass

    try:
        dt = datetime.datetime.strptime(s,"%Y-%m-%d")
        dt += datetime.timedelta(hours=12) # To make default time Noon
        return dt
    except ValueError:
        pass

    raise ValueError("time data '{}' did not match any of the allowed formats".format(s))


def usage():
    "Show usage message and quit"
    print("USAGE: {} DT1 DT2".format(sys.argv[0]))
    print("""
Display the duration between two datetimes in a convenient 
unit (seconds, hours, years, etc.).

Arguments DT1 and DT2 are datetimes in the format
    YYYY-MM-DD hh:mm:ss
or  YYYY-MM-DD hh:mm (assumes seconds=0)
or  YYYY-MM-DD (assumes time=Noon)

Since datetimes often contain spaces, you may need to
enclose them in quotation marks to avoid them being seen
as multiple arguments.

Example: {} \"2021-08-23 10:00:00\" \"2021-12-03 10:50:00\"""".format(sys.argv[0]))
    exit(1)

if __name__=="__main__":
    if len(sys.argv) < 3:
        usage()
    dt1 = arg_to_dt(sys.argv[1])
    dt2 = arg_to_dt(sys.argv[2])
    delta = dt2 - dt1 # difference of datetime objects is a timedelta

    # Now we seek an appropriate unit in which to report the time
    # difference delta.  We consider years, months, days, hours,
    # minutes, and seconds.  The first one we find where the answer
    # is at least 1.0 is reported.
    # TODO: Replace this repetitive code with a loop

    num_years = delta / datetime.timedelta(days=365.25)
    if num_years >= 1:
        print("{:.1f} years".format(num_years))
        exit()

    num_months = delta / datetime.timedelta(days=30.44)
    if num_months >= 1:
        print("{:.1f} months".format(num_months))
        exit()

    num_days = delta / datetime.timedelta(days=1)
    if num_days >= 1:
        print("{:.1f} days".format(num_days))
        exit()

    num_hours = delta / datetime.timedelta(hours=1)
    if num_hours >= 1:
        print("{:.1f} hours".format(num_hours))
        exit()

    num_minutes = delta / datetime.timedelta(minutes=1)
    if num_minutes >= 1:
        print("{:.1f} minutes".format(num_minutes))
        exit()

    num_seconds = delta / datetime.timedelta(seconds=1)
    print("{:.1f} seconds".format(num_seconds))


