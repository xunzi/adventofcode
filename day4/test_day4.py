#!/usr/bin/env python3

import day4

testpairs_input="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

testpairs = []

for pairs in testpairs_input.split("\n"):
    print(pairs)
    pairs = pairs.strip()
    p1, p2 = pairs.split(',')
    testpairs.append([day4.pair2list(p1), day4.pair2list(p2)])


def test_overlap():
    sum_overlap = 0
    for p in testpairs:
        #print(p)
        if day4.overlap(p[0], p[1]):
            print(p)
            sum_overlap += 1
    assert sum_overlap == 4
