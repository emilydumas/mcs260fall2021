"""Hello world API example"""
# MCS 2560 Fall 2021 Lecture 35

import flask

app = flask.Flask("HelloAPI")

@app.route("/")
def hello():
    """Return a simple greeting"""
    return "Nice to meet you."

@app.route("/farewell/")
def goodbye():
    return "Have a good day."

app.run(port=3000)
