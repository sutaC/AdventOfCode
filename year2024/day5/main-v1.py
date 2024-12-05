#!/bin/python

def getInput(path: str) -> tuple[list[tuple[int, int], list[list[int]]]]:
    with open(path) as file:
        lines = file.read().strip().split("\n")
        idx = lines.index('')
        # Rules
        rules = lines[:idx]
        for i, rule in enumerate(rules):
            rules[i] = list(map(int, rule.split("|")))
        # Prints
        prints = lines[idx+1:]
        for i, pri in enumerate(prints):
            prints[i] = list(map(int, pri.split(",")))
        return (rules, prints)
        


# Start
rules, prints = getInput("input.txt")

# val => (sml: [...], big: [...])
rulebook: dict[int, tuple[set[int], set[int]]] = dict()
for sml, big in rules:
    # Smaller one
    if rulebook.get(sml) is None:
        rulebook[sml] = (set(), set())
    rulebook[sml][1].add(big)
    # Bigger one
    if rulebook.get(big) is None:
        rulebook[big] = (set(), set())
    rulebook[big][0].add(sml)
# Countup
count = 0
for pri in prints:
    valid = True
    # Check
    for i, val in enumerate(pri):
        rlb = rulebook.get(val)
        if rlb is None:
            continue
        if (len(rlb[0]) > 0 and len(pri[i+1:]) > 0 and rlb[0].issubset(pri[i+1:])) or (len(rlb[1]) > 0 and len(pri[:i]) > 0 and rlb[1].issubset(pri[:i])):
            valid = False
            break
    # Sumup
    if valid:
        count += pri[len(pri)//2+1]
        # print(pri[len(pri)//2+1])
# End
# print("===")
print(count)