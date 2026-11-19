#!/usr/bin/env python
# Exercise 3 - reducer

import heapq
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    totals = []
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            totals.append((current_word, total_count))
        except ValueError:
            # count was not a number, so silently discard this item
            pass
    # Exercise 3: keep only the 3 highest counts, highest first
    for word, count in heapq.nlargest(3, totals, key=itemgetter(1)):
        print ("%s%s%d" % (word, separator, count))

if __name__ == "__main__":
    main()
