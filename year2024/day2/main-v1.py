#!/bin/python

def getInput(path: str) -> list[list[int]]:
    out = []
    with open(path) as file:
        for line in file:
            seg = line.split()
            for i, s in enumerate(seg):
                seg[i] = int(s)
            out.append(seg)
    return out

def isReportSafe(rep: list[int]) -> bool:
    decr = rep[0] > rep[1] 
    for i in range(1, len(rep)):
        first = rep[i-1]
        second = rep[i]
        # Test
        if 1 > abs(first - second) or 3 < abs(first - second):
            return False
        if decr and first < second:
            return False
        if not decr and first > second:
            return False
    return True

# Start

reports = getInput("input.txt")
result = 0
for rep in reports:
    if isReportSafe(rep):
        result += 1
print(result)