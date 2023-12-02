#!/usr/bin/env python3

import sys
import copy
from icecream import ic

indict = {}

def split_input(input):
    crates, instructions = input.split("\n\n")
    return crates, instructions

def parse_crates(crate_line):
    """split crate_line into chunks of 4 chars and return the resulting list with all whitespace removed"""
    stride = 4
    vals = [crate_line[i:i+stride].strip() for i in range(0, len(crate_line), stride)]
    return vals

def apply_instruction(instr):
    i_split = instr.split()
    amount = int(i_split[1])
    source = i_split[3]
    dest = i_split[5]
    ic(amount, source, dest)
    print("Before:", len(indict[source]), len(indict[dest]))
    #ic(source, indict[source])
    for i in range(1, amount+1):
        #ic(indict[source])
        crate = indict[source].pop()
        indict[dest].append(crate)
    print("After:", len(indict[source]), len(indict[dest]))
    #ic(source, indict[source])

def apply_instruction2(instr):
    i_split = instr.split()
    amount = int(i_split[1])
    source = i_split[3]
    dest = i_split[5]
    ic(amount, source, dest)
    print("Before:", len(indict2[source]), len(indict2[dest]))
    #ic(source, indict[source])
    crates = indict2[source][-amount:]
    indict2[dest].extend(crates)
    for i in range(1, amount+1):
        indict2[source].pop()
    print("After:", len(indict2[source]), len(indict2[dest]))

if __name__ == "__main__":
    infile = sys.argv[1]
    with open(infile) as input:
        crates, instructions = split_input(input.read())
        c_lines = crates.split("\n")
        last_line = c_lines.pop()
        keys = parse_crates(last_line)
        for k in keys:
            indict[k] = []
        for l in c_lines:
            crates = parse_crates(l)
            for i in range(0, len(crates)):
                if crates[i] != "":
                    indict[str(i+1)].append(crates[i])
        for k in indict.keys():
            indict[k].reverse()
        indict2 = copy.deepcopy(indict)
        for inst in instructions.split("\n"):
            if inst == '':
                break
            ic(inst)
            #apply_instruction(inst)
            apply_instruction2(inst)
        #ic(indict)
        print(indict2)
        res2 = ""
        #for k in indict.keys():
        #    print(indict[k][-1])
        for k in indict2.keys():
            print(indict2[k][-1])
            res2 += indict2[k][-1]
        print(res2)
