#!/bin/python

def getInput(path: str) -> tuple[list[int], list[int]]:
    left = []
    right = []
    with open(path) as file:
        for line in file:
            segm = line.split()
            left.append(int(segm[0]))
            right.append(int(segm[1]))
    return tuple([left, right])

def getSmallest(arr: list[int | None]) -> int:
    sml = None
    for i, val in enumerate(arr):
        if val is None:
            continue
        if sml is None and val is not None:
            sml = i
            continue
        if arr[sml] > val:
            sml = i
    return sml

def reduceArrIdx(arr: list[int]) -> list[int]:
    arrcp = arr.copy()
    out = []
    while True:
        sml = getSmallest(arrcp)
        if sml is None or arrcp[sml] is None:
            break
        out.append(arrcp[sml])
        arrcp[sml] = None
    return out

# Start
values = getInput("input.txt")
rLeft = reduceArrIdx(values[0])
rRight = reduceArrIdx(values[1])

result = 0
for i in range(len(rLeft)):
    result += abs(rLeft[i] - rRight[i])
print(result)