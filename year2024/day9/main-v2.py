#!/bin/python

def getInput(path: str) -> str:
    with open(path) as file:
        return file.read().strip()

# (idx, length)
def segmentDisk(disk: str) -> list[list[int]]:
    diskseg: list[tuple[int, int]] = list()
    for i, ch in enumerate(disk):
        if ch == "":
            break
        if int(ch) == 0:
            continue
        if i % 2 == 0:
            diskseg.append([i // 2, int(ch)])
        else:
            diskseg.append([-1, int(ch)])
    return diskseg

def defragmentDisk(diskseg: list[list[int]]) -> list[tuple[int, int]]:
    i = len(diskseg) - 1
    while i >= 0:
        # If empty segment
        if diskseg[i][0] == -1:
            i -= 1
            continue
        # Search for empty space
        for j in range(i):
            # Occupied
            if diskseg[j][0] >= 0:
                continue
            # Too small
            if diskseg[j][1] < diskseg[i][1]:
                continue
            # Equal space
            if diskseg[j][1] == diskseg[i][1]:
                diskseg[j][0] = diskseg[i][0]
                diskseg[i][0] = -1
                break
            # Bigger space
            seg = diskseg[i].copy()
            diskseg[j][1] -= diskseg[i][1]
            diskseg[i][0] = -1
            diskseg.insert(j, seg)
            break
        # Space junction
        if diskseg[i][0] == -1:
            while i+1 < len(diskseg) and diskseg[i+1][0] == -1:
                diskseg[i][1] += diskseg[i+1][1]
                diskseg.pop(i+1)
            while i-1 >= 0 and diskseg[i-1][0] == -1:
                diskseg[i-1][1] += diskseg[i][1]
                diskseg.pop(i)
                i -= 1
        # Next step
        i -= 1
    return diskseg

def extendDisk(diskseg: list[tuple[int, int]]) -> list[int | None]:
    diskmap: list[int | None] = list()
    for i, seg in enumerate(diskseg):
        if seg[0] >= 0:
            for j in range(seg[1]):
                diskmap.append(seg[0])
        else:
            for j in range(seg[1]):
                diskmap.append(None)
    return diskmap

def calculateChecksum(disk: list[int | None]) -> int:
    checksum: int = 0
    for i, val in enumerate(disk):
        if val is None:
            continue
        checksum += i * val
    return checksum
 
# Start
disk = getInput("input.txt")
diskseg = segmentDisk(disk)
diskseg = defragmentDisk(diskseg)
print(diskseg)
diskmap = extendDisk(diskseg)
checksum = calculateChecksum(diskmap)
print(checksum)
