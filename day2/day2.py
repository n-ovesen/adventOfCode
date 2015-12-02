#!/usr/bin/env python

import sys
import csv

def wrappingpaper(list):

    total = 0

    for row in list:

        if len(row) == 0:
            return total

        else:

            w = int(row[0])
            h = int(row[1])
            l = int(row[2])
            areas = [l * w, w * h, h * l]
            m = min(s for s in areas)
            total += sum(a for a in areas * 2) + m

def ribbon(list):

    total = 0

    for row in list:

        if len(row) == 0:

            return total

        else:

            w = int(row[0])
            h = int(row[1])
            l = int(row[2])

            lengths = [l + w, w + h, h + l]
            ribbon = 2 * min(s for s in lengths)
            bow = w * h * l
            total = total + bow + ribbon


if __name__ == '__main__':

    #something is really derpy here, don't know why I can run one or the other function but not both

    with open(sys.argv[1]) as file:
        reader = csv.reader(file.read().split('\n'), delimiter='x')
        print "the elves need:", wrappingpaper(reader), "square feet of wrapping paper"
        print "the elves need:", ribbon(reader), "feet of ribbon"
