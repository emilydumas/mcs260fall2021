"""Text adventure game engine"""
# MCS 260 Fall 2021 Project 2 Solution
# David Dumas
import sys
import json


def load_world_map(fn):
    """Load the world map from a JSON file"""
    mapfile = open(sys.argv[1], "r")
    data = json.load(mapfile)
    mapfile.close()
    return data


# -- next bit not required, but is a convenience --
if len(sys.argv) != 2:
    print("Usage: {} MAPFILE.json".format(sys.argv[0]))
    exit(1)
# -------------------------------------------------


# Load map specified by first command line argument
worldmap = load_world_map(sys.argv[1])

# Tracks player location
location = "start"

# A "checklist" of rooms they still need to visit
# (we remove names as they are visited)
missing = [x for x in worldmap if worldmap[x]["mustvisit"]]

# Main game loop
while True:
    print(worldmap[location]["description"])
    if worldmap[location]["mustvisit"] and location in missing:
        # First visit to a required room; check it off
        missing.remove(location)

    if worldmap[location]["roomtype"] in ["win", "lose"]:
        # win and lose rooms trigger exit
        # (see below for code to stop us from getting
        #  here if required rooms not yet visited!)
        exit()

    # Get command
    s = input("> ")

    # Act on command
    if s not in worldmap[location]["exits"]:
        print("You can't go that way.\n")
    else:
        # Where they are asking to go
        nextroom = worldmap[location]["exits"][s]
        # Can they go there?
        if worldmap[nextroom]["roomtype"] == "win" and missing:
            # It's a win room and they haven't visited
            # all required rooms
            print("You aren't ready to go there yet.\n")
        else:
            # Either not a win room or winning is allowed
            # so update location accordingly
            location = nextroom
