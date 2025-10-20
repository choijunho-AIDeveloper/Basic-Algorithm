import sys
# sys.setrecursionlimit(10000)

n = int(input())

maps = []
for _ in range(n):
    temp = list(map(str, input().split()))
    maps.append(temp)

def backtracking(cur, move):
    global possibleMap
    y, x = cur
    y_move, x_move = move
    if y_move + y <= len(maps) - 1 and y_move + y >= 0 and x_move + x <= len(maps[0]) - 1 and x_move + x >= 0:
        if possibleMap[y][x] == True:
            return
        if maps[y + y_move][x + x_move] == "S":
            if maps[y][x] == "T":
                return
            possibleMap[y][x] = True
            return
        backtracking([y + y_move, x + x_move], move)

def backtracking_check(cur, move):
    global isTrue
    y, x = cur
    y_move, x_move = move
    if y_move + y <= len(maps) - 1 and y_move + y >= 0 and x_move + x <= len(maps[0]) - 1 and x_move + x >= 0:
        if possibleMap[y + y_move][x + x_move] == True:
            return 
        if maps[y + y_move][x + x_move] == "S":
            isTrue = True
            return
        backtracking([y + y_move, x + x_move], move)

possibleMap = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if maps[i][j] == "T":
            for move in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                backtracking([i, j], move)

count = 0
for i in range(len(possibleMap)):
    for j in range(len(possibleMap[0])):
        if possibleMap[i][j] == True:
            count += 1

if count > 3:
    print("NO")
else:
    isTrue = False
    for i in range(n):
        for j in range(n):
            if maps[i][j] == "T":
                for move in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    backtracking_check([i, j], move)
                    if isTrue: break
            if isTrue: break
        if isTrue: break
    if isTrue:
        print("NO")
    else:
        print("YES")