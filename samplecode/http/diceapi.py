"""Roll one six-sided die using the dice API at diceapi.com"""
# MCS 260 Fall 2021 Lecture 34
import urllib.request
import json

url = "http://roll.diceapi.com/json/d6"

print("Rolling a 6-sided die by loading JSON data from")
print(url)

res = urllib.request.urlopen("http://roll.diceapi.com/json/d6")
data = json.load(res)  # result object behaves like a file
                       # (so can pass to json.load!)
res.close()

# diceapi.com returns JSON like this:
#  {"success":true,"dice":[{"value":2,"type":"d6"}]}

# Format dissection:
# {
#   "success":true,   <--- Did the request succeed?
#   "dice": [         <--- Start of list of dice rolls
#       {       <--- Start of info about first die
#         "value":2,  <--- Number rolled
#         "type":"d6" <--- What kind of die was this?
#       }       <--- End of the info about first die
#   ]                 <--- End of the list of dice rolls
# }

# So:
# data["dice"] is a list
# data["dice"][0] is a dict with info about the first die roll
# data["dice"]["value"] is an integer, the actual roll value

print("\nGot: {}".format(
    data["dice"][0]["value"]
))
