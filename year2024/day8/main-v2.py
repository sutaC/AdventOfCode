#!/bin/python

def getInput(path: str) -> list[list[str]]:
    with open(path) as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if len(line) == 0:
                lines.pop(i)
            lines[i] = list(line.strip())
        return lines

    

# Start
data = getInput("input.txt")
# Get all antenas
antenas: dict[str, list[tuple[int, int]]] = dict()
for y, list in enumerate(data):
    for x, value in enumerate(list):
        if not value.isalnum():
            continue
        if antenas.get(value) is None:
            antenas[value] = []
        antenas[value].append(tuple([x, y]))
# Count positions
positions: set[str] = set()
for frequencies in antenas.values():
    if len(frequencies) < 2:
        continue
    for i, curr in enumerate(frequencies):
        for j, next in enumerate(frequencies, i+1):
            # Positioning
            sml, big = None, None
            if curr[0] <= next[0] and curr[1] <= next[1]:
                sml, big = curr, next
            else:
                sml, big = next, curr
            # Diffrence
            xdiff = big[0] - sml[0]
            ydiff = big[1] - sml[1]
            if xdiff == 0 and ydiff == 0:
                continue
            # Bound check
            while sml[0] >= 0 and sml[1] >= 0 and sml[0] < len(data[0]) and sml[1] < len(data):
                positions.add(f"{sml[0]}:{sml[1]}")
                sml = [sml[0] - xdiff, sml[1] - ydiff]
            while big[0] >= 0 and big[1] >= 0 and big[0] < len(data[0]) and big[1] < len(data):
                positions.add(f"{big[0]}:{big[1]}")
                big = [big[0] + xdiff, big[1] + ydiff]
# Sumup
print(len(positions))
