"""API that provides startup ideas"""
# MCS 260 Fall 2021 Worksheet 13 solution
import flask
import random

product_ideas = [
    "a juice machine",
    "a carpet",
    "an office chair",
    "a coffee maker",
    "a haircut robot",
    "a Python course",
    "a toothbrush",
    "a pair of noise-cancelling headphones",
    "an oversized raccoon plush doll",
    "a detailed model of Boise, Idaho",
    "a university building"
]
special_features = [
    "that is controlled by a smartphone app",
    "that plays polka music",
    "made of polished titanium",
    "that also mines bitcoin",
    "scented with sandalwood and lime oil",
    "with a pleasant strawberry flavor",
    "run by an elite squad of monks trained in martial arts", 
    "without spiders",
    "with an integrated soap dispenser",
    "that is vegetarian and gluten-free",
    "enriched with vitamin D",
    "that fires plastic darts",
    "made of hexagons and confusion"
]

app = flask.Flask("Startup Idea API")

@app.route("/startup/random/")
def startup_idea():
    """Produce a random startup idea from a product and special feature"""
    return flask.jsonify(
        random.choice(product_ideas) + " " + random.choice(special_features)
    )

@app.route("/startup/random/product/")
def product_idea():
    """Produce a random product idea"""
    return flask.jsonify(
        random.choice(product_ideas)
    )

@app.route("/startup/random/feture/")
def feature_idea():
    """Produce a random feature idea"""
    return flask.jsonify(
        random.choice(special_features)
    )

app.run(port=3000)