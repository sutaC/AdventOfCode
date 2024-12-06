#!/bin/python

def getInput(path: str) -> list[list[str]]:
    with open(path) as file:
        return list(map(list, file.read().strip().split("\n")))

def getStartingPosition(board: list[list[str]]) -> tuple[int, int] | None:
    for y, ls in enumerate(board):
        for x, val in enumerate(ls):
            if val == '^':
                return [x, y]            
    return None

def walk(board: list[list[str]], x: int, y: int, direction: str) -> None:
    while True:
        board[y][x] = "X"
        nx, ny = x, y
        ndir = direction
        match direction:
            case "^":
                ny -= 1 
                ndir = ">"           
            case ">":
                nx += 1   
                ndir = "v"           
            case "v":
                ny += 1   
                ndir = "<"           
            case "<":
                nx -= 1
                ndir = "^"
        if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[y]):
            break           
        if board[ny][nx] == "#":
            direction = ndir
        else:
            x, y = nx, ny

def countPath(board: list[list[str]]) -> int:       
    start = getStartingPosition(board)
    assert start is not None, "Guard not present"
    ox, oy = start
    countBoard = board.copy()
    walk(countBoard, ox, oy, countBoard[oy][ox])
    count = 0
    for ls in countBoard:
        count += ls.count("X")
    return count

# Start
board = getInput("input.txt")
count = countPath(board)
print(count)