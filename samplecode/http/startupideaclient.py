"""
Produce startup ideas until user indicates one is acceptable
Fetch the ideas from the API in apistartupidea.py
"""
# MCS 260 Fall 2021 Worksheet 13 solution
import urllib.request
import json

url = "http://localhost:3000/startup/random/"

def startup_idea():
    """Get a random startup idea"""
    res = urllib.request.urlopen(url)
    data = json.load(res)
    res.close()
    return data # should be a string

acceptable = "n"
while acceptable != "y":
    print("Startup idea:",startup_idea())
    acceptable = input("Acceptable? (Y/N): ").lower()
