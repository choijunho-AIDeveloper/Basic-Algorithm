# 7576
from collections import deque
import sys

input = sys.stdin.readline
m, n = map(int, input().split())

graph = [[0] * m for _ in range(n)]
start = []
for i in range(n):
    inp = list(map(int, input().split()))
    for j in range(m):
        if inp[j] == 1:
            # x, y
            start.append([j, i])
        graph[i][j] = inp[j]
def possibleMove(x, y):
    possible = []
    if x > 0 and graph[y][x - 1] == 0:
        possible.append([x - 1, y])
    if x < m - 1 and graph[y][x + 1] == 0:
        possible.append([x + 1, y])
    if y > 0 and graph[y - 1][x] == 0:
        possible.append([x, y - 1])
    if y < n - 1 and graph[y + 1][x] == 0:
        possible.append([x, y + 1])
    return possible


def bfs(start, visited):
    queue = deque()
    time = [[-1] * m for _ in range(n)]
    for ele in start:
        # append(x, y)
        queue.append(ele)
        # append visited[y][x]
        visited[ele[1]][ele[0]] = True
        time[ele[1]][ele[0]] = 0
    while queue:
        # node format (x, y)
        node = queue.popleft()
        if possibleMove(node[0], node[1]):
            for ele in possibleMove(node[0], node[1]):
                if not visited[ele[1]][ele[0]]:
                    queue.append(ele)
                    time[ele[1]][ele[0]] = time[node[1]][node[0]] + 1
                    visited[ele[1]][ele[0]] = True
    return time    

visited = [[False] * m for _ in range(n)]
time = bfs(start, visited)

maxNum = 0
isNotAll = False
for i in range(m):
    for j in range(n):
        if graph[j][i] == 0 and time[j][i] == -1:
            isNotAll = True
        maxNum = max(maxNum, time[j][i])

if isNotAll:
    print(-1)
else:
    print(maxNum)