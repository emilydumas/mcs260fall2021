"""Display a file with line numbers"""
import sys
fin = open(sys.argv[1],"r")  # filename is first command line arg
n = 0
for line in fin:
    n = n+1
    print(n,line,end="") # lines provided by iterating over a file
                         # usually have \n at the end, so we won't
                         # have print() add another one.
fin.close()
