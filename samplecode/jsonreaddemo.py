"""Show info about episode lengths of a TV show by
reading from JSON data file"""
# MCS 260 Fall 2021 Lecture 15 (offline example)
import json
import os

# To be discussed in lecture 17: This is the way to
# join a directory and filename that uses "\\" or "/"
# depending on the operating system preference.
fn = os.path.join("data","episodes.json")
# This is a dataset from TVmaze
# https://api.tvmaze.com/shows/2993/episodes

fobj = open(fn,"r",encoding="UTF-8")
data = json.load(fobj)
fobj.close()

# Now data is a list of dictionaries
# Each dictionary represents one episode
# The episodes appear in chronological order
# Keys include "name" (title), "runtime", ...

print("Episode lengths:")
print("ep  |   5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85")
for n,episode in enumerate(data):
    if episode["runtime"] != None:
        # In the scale printed above, each 5-minute increment takes up
        # 3 spaces, so to make a bar chart we use 3/5 of the runtime
        # as the number of stars to print
        numstars = 3*episode["runtime"] // 5
        print("#{:02d} | {}".format(n+1,numstars*"*"))
# Comment about the last episode being so long
print("(Looks like they had a lot of plot to wrap up in the season 3 finale!)")