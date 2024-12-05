#!/bin/python

def getInput(path: str) -> list[list[chr]]:
    out = []
    with open(path) as file:
        for line in file:
            out.append(list(line.strip()))
    return out

def search(grp: list[list[chr]], ox: int, oy: int) -> int:
    if ox <= 0 or oy <= 0 or oy >= len(graph)-1 or ox >= len(graph[y])-1:
        # Invalid
        return 0
    # ===
    CHARS = ["MS", "SM"]
    left = grp[y-1][x-1] + grp[y+1][x+1] in CHARS
    right = grp[y-1][x+1] + grp[y+1][x-1] in CHARS
    if left and right:
        # SUCCESS
        return 1
    return 0

# Start
graph = getInput("input.txt")
count = 0
for y, list in enumerate(graph):
    for x, val in enumerate(list):
        if val == 'A':
            count += search(graph, x, y)
print(count)