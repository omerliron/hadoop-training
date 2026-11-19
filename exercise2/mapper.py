#!/usr/bin/env python
# Exercise 2 - mapper

import sys

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            # strip trailing commas/dots and ignore case
            word = word.rstrip(',.').lower()
            if word:
                print ('%s%s%d' % (word, separator, 1))

if __name__ == "__main__":
    main()
