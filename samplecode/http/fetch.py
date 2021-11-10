"""Make a single HTTP GET request and print the result"""
# MCS 260 Fall 2021 Lecture 34
import urllib.request
import sys

if len(sys.argv) < 2:
    print("Usage: {} URL".format(sys.argv[0]))
    exit(1)

res = urllib.request.urlopen(sys.argv[1])
data = res.read()
res.close()

print("Status was: {}".format(res.status))
print("Received the following headers:")

for k in res.headers:
    print("  {}: {}".format(k,res.headers[k]))

print("Received the following payload:")
enc = res.headers.get_content_charset()
if not enc:
    # encoding wasn't specified in the headers; try UTF-8
    enc = "UTF-8"

try:
    s = data.decode(enc)
    print(s)
except UnicodeDecodeError:
    print("ERROR: Couldn't show as a string because decode failed.  Here are the raw bytes (16 per line, as hex digits):")
    for i,b in enumerate(data):
        if i%16==0:
            print()
        print("{:02x} ".format(b),end="")
    print()
