#!/bin/python

def getInput(path: str) -> str:
    with open(path) as file:
        return file.read()
    
def getNextMul(text: str, start: int = 0) -> tuple[int, int] | None:
    i = start-1
    while True:
        i = text.find("mul(", i+1)
        if i < 0 or i > len(text):
            return None
        # Next iteration
        end = text.find(")", i+4)
        if end < 0 or end > i+11:
            continue
        vals = text[i+4:end].split(",")
        if len(vals) != 2:
            continue
        if not vals[0].isnumeric() or not vals[1].isnumeric():
            continue
        return [i, int(vals[0]) * int(vals[1])]
# Start
txt = getInput("input.txt")
result = 0
i = 0
dont = txt.find("don't()", 0)
while True:
    next = getNextMul(txt, i+1)
    if next is None:
        break
    i = next[0]
    if -1 < dont <= i:
        i = txt.find("do()", i+1)
        if i < 0:
            break
        dont = txt.find("don't()", i+1)
        continue
    result += next[1] 
    
print(result)
