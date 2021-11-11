"""Chemical element API example"""
# MCS 2560 Fall 2021 Lecture 35

import flask
import random

app = flask.Flask("ElementAPI")

# Excerpt of https://github.com/Bowserinator/Periodic-Table-JSON
elementdata = [
    {   "name": "Hydrogen",
        "atomic_mass": 1.008,
        "number": 1,
        "symbol": "H" },
    {   "name": "Helium",
        "atomic_mass": 4.0026022,
        "number": 2,
        "symbol": "He" },
    {   "name": "Lithium",
        "atomic_mass": 6.94,
        "number": 3,
        "symbol": "Li" },
    {   "name": "Beryllium",
        "atomic_mass": 9.01218315,
        "number": 4,
        "symbol": "Be" },
    {   "name": "Boron",
        "atomic_mass": 10.81,
        "number": 5,
        "symbol": "B" },
    {   "name": "Carbon",
        "atomic_mass": 12.011,
        "number": 6,
        "symbol": "C" }
]

@app.route("/element/random")
def random_element():
    """Return data about a random element as JSON object"""
    return flask.jsonify( random.choice(elementdata) )
    # flask.jsonify converts a Python object into a 
    # HTTP response (setting headers, charset, ...)

app.run(port=3000)
