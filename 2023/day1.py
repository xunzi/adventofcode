#!/usr/bin/env python3


import string
import aoclib
import re
sum = 0

args = aoclib.handle_args(description="AOC 2023 day 1")
if args.debug:
    aoclib.debug = True


def find_first_digit(line_array):
    aoclib.debugprint(line_array)
    for letter in line_array:
        if string.digits.count(letter) == 1:
            aoclib.debugprint(letter)
            return letter
if args.test:
    infilename = f"input/day{args.day}.{args.part}test"
else:
    infilename = f"input/day{args.day}"


match args.part:
    case "1":
        with open(infilename) as infile:
            for line in infile.readlines():
                #convert to array
                line_array = [x for x in line]
                first = find_first_digit(line_array)
                line_array.reverse()
                last = find_first_digit(line_array)
                result = f"{first}{last}"
                sum += int(result)
        print("Part1: ", sum)

    case "2":
        with open(infilename) as infile:
            for line in infile.readlines():
                aoclib.debugprint(line.strip())
                aoclib.debugprint(convert_words_to_digits(line.strip())) 
