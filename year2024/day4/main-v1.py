#!/bin/python

def getInput(path: str) -> list[list[chr]]:
    out = []
    with open(path) as file:
        for line in file:
            out.append(list(line.strip()))
    return out

TRAVERSE = [
    lambda x, y: (x+1, y+1),
    lambda x, y: (x+1, y),
    lambda x, y: (x+1, y-1),
    lambda x, y: (x, y+1),
    lambda x, y: (x, y-1),
    lambda x, y: (x-1, y+1),
    lambda x, y: (x-1, y),
    lambda x, y: (x-1, y-1),
]

def search(grp: list[list[chr]], ox: int, oy: int) -> int:
    WORD = "XMAS"
    count = 0
    for trav in TRAVERSE:
        x = ox
        y = oy
        for ch in WORD:
            if ch == "X":
                continue
            # Step
            x,y = trav(x,y)
            if y < 0 or x < 0 or y >= len(grp) or x >= len(grp[y]):
                # Out of bounds
                break
            if graph[y][x] != ch:
                # Failure
                break
            if ch == WORD[-1]:
                # Success
                count += 1
    return count

# Start
graph = getInput("input.txt")
count = 0
for y, list in enumerate(graph):
    for x, val in enumerate(list):
        if val == 'X':
            count += search(graph, x, y)
print(count)