#!/bin/python

def getInput(path: str) -> str:
    with open(path) as file:
        return file.read()
    
# Start
txt = getInput("input.txt")
result = 0
i = -1
while True:
    i = txt.find("mul(", i+1)
    if i < 0 or i > len(txt):
        break
    # Next iteration
    end = txt.find(")", i+4)
    if end < 0 or end > i+12:
        continue
    vals = txt[i+4:end].split(",")
    if len(vals) != 2:
        continue
    if not vals[0].isnumeric() or not vals[1].isnumeric():
        continue
    result += int(vals[0]) * int(vals[1])
print(result)
