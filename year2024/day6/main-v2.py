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

def nextStep(x: int, y: int, direction: str) -> tuple[int, int, str]:
    match direction:
        case "^":
            return [x, y-1,">"]           
        case ">":
            return [x+1,y,"v"]           
        case "v":
            return [x,y+1,"<"]           
        case "<":
            return [x-1,y,"^"]

def isLoop(board: list[list[str]], saw: set, x: int, y: int, direction: str) -> bool:
    visited = saw.copy()
    visited.add(str([x, y, direction]))

    ox, oy, direction = nextStep(x,y,direction) # Simulates new obstacle
    if board[oy][ox] == "^":
        # Cannot obstacle on initial guard spot
        return False
    board[oy][ox] = "#"

    while True:
        nx, ny, ndir = nextStep(x, y, direction)
        # Out of bounds
        if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[y]):
            break           
        # Next step
        if board[ny][nx] == "#" :
            direction = ndir
        else:
            x, y = nx, ny
        # Check path
        if str([x, y, direction]) in visited:
            # Reset on success
            board[oy][ox] = "."
            return True
        visited.add(str([x, y, direction]))
    # Reset on failure
    board[oy][ox] = "."
    return False

def walk(board: list[list[str]], x: int, y: int, direction: str) -> int:
    newObstacles = set()
    saw = set()
    while True:
        saw.add(str([x,y,direction]))
        nx, ny, ndir = nextStep(x, y, direction)
        # Out of bounds
        if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[y]):
            break         
        # Next step
        if board[ny][nx] == "#" :
            direction = ndir
        else:
            if isLoop(board, saw, x, y, direction):
                newObstacles.add(str([nx,ny]))
                print(len(newObstacles))
            x, y = nx, ny
    return len(newObstacles)

def countPath(board: list[list[str]]) -> int:       
    start = getStartingPosition(board)
    assert start is not None, "Guard not present"
    ox, oy = start
    countBoard = board.copy()
    cnt = walk(countBoard, ox, oy, countBoard[oy][ox])
    return cnt

# Start
board = getInput("input.txt")
count = countPath(board)
print("=== count ===", count, sep='\n')