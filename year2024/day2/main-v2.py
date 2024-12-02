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

def getRepDiff(rep: list[int]) -> list[int]:
    diffs: list[int] = []
    for i in range(1, len(rep)):
        diffs.append(rep[i] - rep[i-1])
    return diffs

def isNumPositive(num: int) -> bool:
    return num >= 0

def getInvalidDiff(diffs: list[int]) -> int:
    for i, diff in enumerate(diffs):
        if abs(diff) > 3 or abs(diff) < 1:
            return i
    for i in range(1, len(diffs)):
        if isNumPositive(diffs[i-1]) != isNumPositive(diffs[i]): 
            return i
    return -1

def isReportSafe(rep: list[int]) -> bool:
    diffs = getRepDiff(rep)
    # All valid
    inv = getInvalidDiff(diffs)
    if  inv == -1:
        return True
    # Invalid
    repL = rep.copy()
    repC = rep.copy()
    repR = rep.copy()
    repL.pop(inv-1)
    repC.pop(inv)
    repR.pop(inv+1)
    return getInvalidDiff(getRepDiff(repL)) == -1 or getInvalidDiff(getRepDiff(repC)) == -1 or getInvalidDiff(getRepDiff(repR)) == -1

# Start
reports = getInput("input.txt")
result = 0
for rep in reports:
    if isReportSafe(rep):
        result += 1
print(result)