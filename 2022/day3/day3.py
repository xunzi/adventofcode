#!/usr/bin/env python3

import string

def find_common_char2(a, b):
    for c in a:
        if c in b:
            return c

def find_common_char3(a,b,c):
    for d in a:
        if d in b and d in c:
            print(f"{d} is common between {a}, {b}, {c}")
            return d

def find_prio(c):
    return string.ascii_letters.index(c) + 1

with open("day3-input.txt") as input:
    sum_first = 0
    for l in input.readlines():
        #split l by half
        l = l.strip()
        a, b = l[:len(l)//2], l[len(l)//2:]
        assert f"{a}{b}" == l
        common = find_common_char2(a, b)
        print(f"{common} is common in {a}, {b}")
        if common:
            prio = find_prio(common)
            sum_first += prio
            print(common, prio)
print("first part: ", sum_first)

with open("day3-input.txt") as input:
    sum_second = 0
    l = input.readlines()
    for i in range(0,len(l), 3):
        print(i)
        lines = l[i:i+3]
        common = find_common_char3(lines[0].strip(), lines[1].strip(), lines[2].strip())
        prio = find_prio(common)
        sum_second += prio
print("second part: ", sum_second)
        
        
        
