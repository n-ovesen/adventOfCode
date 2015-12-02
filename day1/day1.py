#!/usr/bin/env python
import sys

str = ""
flr = 0
bmt = 0

with open(sys.argv[1], 'r') as file:
    str = file.read()


for i, c in enumerate(str):

    #part 1

    if c == "(":
        flr = flr+1

    if c == ")":
        flr = flr-1

        #part 2

    if flr < 0 and bmt == 0:
        bmt = i + 1

print "Santa needs to go to floor:", flr
print "He enters the basement the first time at character:", bmt
