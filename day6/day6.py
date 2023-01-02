#!/usr/bin/env python3

from icecream import ic

testinput="bvwbjplbgvbhsrlpgdmjqwftvncz"
testinput2 = "nppdvjthqldpwncqszvftbrmjlhg"
stride_packet = 4
stride_msg = 14

def find_startmarker(intext, stride):
    ic(intext)
    seen = []
    assert len(intext) == stride
    for i in range(0,len(intext)):
        if seen.count(intext[i]) == 1:
            return False
        else:
            seen.append(intext[i])
    #ic(seen)
    return True

def iterate_input(intext, stride):
    for i in range(len(intext)):
        chunk = intext[i:i+stride]
        if find_startmarker(chunk, stride):
            return i + stride
    return 0

if __name__ == "__main__":
    ic(iterate_input(testinput, stride_packet))
    ic(iterate_input(testinput2, stride_packet))
    with open("day6-input.txt") as infile:
        datastream = infile.read()
        #ic(iterate_input(infile.read()))
        print(f"Part1: {iterate_input(datastream, stride_packet)}")
        print(f"Part2: {iterate_input(datastream, stride_msg)}") 
