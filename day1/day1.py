#!/usr/bin/env python3

infile = "day1-input.txt"

calorieslist = []

with open(infile) as input:
    calories = 0
    for line in input.readlines():
        if line != '\n':
            calories += int(line.strip())
        else:
            calorieslist.append(calories)
            calories = 0
            continue
print(sorted(calorieslist)[-1])
print(sum(sorted(calorieslist)[-3:]))
        
