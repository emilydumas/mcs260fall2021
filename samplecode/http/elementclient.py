"""Contact the Flask example `apielement.py` to get a random chemical
element and print the result as a sentence."""
# MCS 260 Fall 2021 Lecture 35
import urllib.request
import json

res = urllib.request.urlopen("http://localhost:3000/element/random")
data = json.load(res)
res.close()

print("Did you know that chemical element {} is called {} and has an atomic mass of {}?".format(
    data["number"],
    data["name"],
    data["atomic_mass"]
))