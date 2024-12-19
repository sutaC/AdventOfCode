#!/bin/python

def getInput(path: str) -> dict[int, int]:
    with open(path) as file:
        values = file.read().strip().split()
        stones = dict()
        for val in values:
            key = int(val)
            if stones.get(key) is None:
                stones[key] = 0
            stones[key] += 1
        return stones

def blink(stones: dict[int, int], blinks: int) -> dict[int, int]:
    for bl in range(blinks):
        next: dict[int, int] = dict()
        for stone in stones:
            sStone = str(stone)
            # Is 0
            if stone == 0:
                if next.get(1) is None:
                    next[1] = 0
                next[1] += stones[stone]
            # Is digit num even
            elif len(sStone) % 2 == 0:
                pivot = len(sStone) // 2
                # Left
                key = int(sStone[:pivot])
                if next.get(key) is None:
                    next[key] = 0
                next[key] += stones[stone]
                # Right
                key = int(sStone[pivot:])
                if next.get(key) is None:
                    next[key] = 0
                next[key] += stones[stone]
            # No rules applied
            else:
                key = stone * 2024 
                if next.get(key) is None:
                    next[key] = 0
                next[key] = stones[stone]
        stones = next
        print(f"Blink {bl+1}")
    return stones

def countStones(stones: dict[int, int]) -> int:
    count = 0
    for stone in stones:       
        count += stones[stone]
    return count

# Start
stones = getInput("input.txt")
stones = blink(stones, 75)
count = countStones(stones)
print(f"+===+\n{count}\n+===+")