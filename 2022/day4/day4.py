#!/usr/bin/env python3

def pair2list(pair):
    _pl  = [int(x) for x in pair.split('-')]
    return _pl

def pairinpair(l1, l2):
    if (l1[0] >= l2[0] and l1[1] <= l2[1]) or (l2[0] >= l1[0] and l2[1] <= l1[1]):
        return True
    else:
        return False

def overlap(l1, l2):
    if (l2[0] <= l1[0] <= l2[1]) or (l1[0] <= l2[0] <= l1[1]):
        #print(l1, l2)
        return True
    
with open("day4-input.txt" ) as input:
    lines = input.readlines()

if __name__ == "__main__":
    sum_first = 0
    sum_overlap = 0
    sum_nonoverlap = 0
    for l in lines:
        l = l.strip()
        pair1, pair2 = l.split(',')
        plist1 = pair2list(pair1)
        plist2 = pair2list(pair2)
        #print(pair1, plist1, pair2, plist2)
        # if pairinpair(plist1, plist2):
        #     #print(pair1, plist1, pair2, plist2)
        #     sum_first += 1
        if overlap(plist1, plist2):
            sum_overlap += 1
        else:
            sum_nonoverlap += 1
            print(plist1,plist2)
    print("First part: ", sum_first)
    print("Second part: ", sum_overlap)
    print("Non overlap: ", sum_nonoverlap)
