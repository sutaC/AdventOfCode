#!/bin/python

def getInput(path: str) -> list[tuple[int, list[int]]]:
    with open(path) as file:
        lines = file.read().split("\n")
        for i, line in enumerate(lines):
            if len(line) == 0:
                lines.pop(i)
                continue
            line = line.strip()
            result, factors = line.split(":")
            result = int(result)
            factors = factors.strip().split(" ")
            for j, factor in enumerate(factors):
                factors[j] = int(factor)
            lines[i] = [result, factors]
        return lines
            
def isValidTest(result: int, factors: list[int]) -> bool:
    if len(factors) == 1:
        return result == factors[0]
    curr = factors[0]
    next = factors[1]
    mul = [curr * next]
    mul.extend(factors[2:])
    add = [curr + next]
    add.extend(factors[2:])
    con = [int(str(curr) + str(next))]
    con.extend(factors[2:])
    return isValidTest(result, mul) or isValidTest(result, add) or isValidTest(result, con)

# Start
tests = getInput("input.txt")
count = 0
for result, factors in tests:
    valid = isValidTest(result, factors)
    print(f"{valid} :: {result} - {factors}")
    if valid:
        count += result
print('\n', count, sep="")
