#!/bin/python

def getInput(path: str) -> list[int]:
    with open(path) as file:
        out = file.read().strip().split()
        for i, val in enumerate(out):
            out[i] = int(val)
        return out

def blink(stones: list[int], blinks: int) -> None:
    for bl in range(blinks):
        for i in range(len(stones)):
            stone = stones[i]
            sStone = str(stone)
            # Is 0
            if stone == 0:
                stones[i] = 1
            # Is digit num even
            elif len(sStone) % 2 == 0:
                pivot = len(sStone) // 2
                stones[i] = int(sStone[:pivot])
                stones.append(int(sStone[pivot:]))
            # No rules applied
            else:
                stones[i] = stone * 2024
        print(f"Blink {bl+1}")
        
# Start
stones = getInput("input.txt")
blink(stones, 25)
count = len(stones)
print(f"+===+\n{count}\n+===+")