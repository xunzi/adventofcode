#!/usr/bin/env python3

import sys

def split_input(input):
    crates, instructions = input.splt("\n\n")
    return crates, instructions

def parse_crates(crates):
    for l in crates.split("\n"):
        fields = [x for y in l[y:y+2]]



if __name__ == "__main__":
    infile = sys.argv[1]
