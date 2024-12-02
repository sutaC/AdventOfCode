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

def count(arr: list[int]) -> dict[int, int]:
    counter = {}
    for val in arr:
        if counter.get(val) is None:
            counter[val] = 0
        counter[val] += 1
    return counter

# Start
[left, right] = getInput("input.txt")
counter = count(right)
result = 0
for val in left:
    mult = counter.get(val) or 0
    result += mult * val
print(result)