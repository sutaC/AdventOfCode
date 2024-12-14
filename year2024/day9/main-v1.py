#!/bin/python

def getInput(path: str) -> str:
    with open(path) as file:
        return file.read().strip()

def extendDisk(disk: str) -> list[int | None]:
    diskmap: list[int | None] = list()
    for i, ch in enumerate(disk):
        if ch == "":
            break
        if i % 2 == 0:
            for j in range(int(ch)):
                diskmap.append(i // 2)
        else:
            for j in range(int(ch)):
                diskmap.append(None)
    return diskmap

def find(arr: list, search, start: int = 0):
    if start >= len(arr) or start < 0:
        return -1
    for i, val in enumerate(arr, start):
        if val == search:
            return i
    return -1

def defragmentDisk(diskmap: list[int | None]) -> list[int]:
    emptyIdx = diskmap.index(None)
    i = len(diskmap) - 1
    while i > emptyIdx:
        if diskmap[i] is None:
            i -= 1
            continue
        # Swap
        diskmap[emptyIdx] = diskmap[i]
        diskmap[i] = None
        # Next step
        emptyIdx = diskmap.index(None, emptyIdx + 1)
        i -= 1
    return diskmap

def calculateChecksum(disk: list[str]) -> int:
    checksum: int = 0
    for i, val in enumerate(disk):
        if val is None:
            continue
        checksum += i * val
    return checksum
 
# Start
disk = getInput("input.txt")
diskmap = extendDisk(disk)
diskmap = defragmentDisk(diskmap)
checksum = calculateChecksum(diskmap)
print(checksum)
