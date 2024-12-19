#!/bin/python

def getInput(path: str) -> list[list[int]]:
    with open(path) as file:
        out = file.readlines()
        for i, line in enumerate(out):
            line = list(line.strip())
            for j, ch in enumerate(line):
                line[j] = int(ch)
            out[i] = line
    return out

def getStartPoints(tmap: list[list[int]]) -> list[tuple[int, int]]:
    startPoints: list[tuple[int, int]] = list()
    for y, row in enumerate(tmap):
        for x, val in enumerate(row):
            if val == 0:
                startPoints.append(tuple([x, y]))
    return startPoints

def walkTrails(position: tuple[int, int], tmap: list[list[int]], trailheads: set[tuple[int, int]]) -> None:
    x, y = position
    curr = tmap[y][x]
    if curr == 9:
        trailheads.add(position)
        return 
    # Down
    if y+1 < len(tmap) and tmap[y+1][x] == curr + 1:
        walkTrails(tuple([x, y+1]), tmap, trailheads)
    # Up
    if y-1 >= 0 and tmap[y-1][x] == curr + 1:
        walkTrails(tuple([x, y-1]), tmap, trailheads)
    # Right
    if x+1 < len(tmap[y]) and tmap[y][x+1] == curr + 1:
        walkTrails(tuple([x+1, y]), tmap, trailheads)
    # Left
    if x-1 >= 0 and tmap[y][x-1] == curr + 1:
        walkTrails(tuple([x-1, y]), tmap, trailheads)

def countTrails(position: tuple[int, int], tmap: list[list[int]]) -> int:
    trailheads: set[tuple[int, int]] = set()
    walkTrails(position, tmap, trailheads)
    return len(trailheads)

# Start
tmap = getInput("input.txt")
startPoints = getStartPoints(tmap)
trails = 0
for sp in startPoints:
    trails += countTrails(sp, tmap)
print(trails)
