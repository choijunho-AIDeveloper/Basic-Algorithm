# 2583
from collections import deque

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

for _ in range(k):
    inp = list(map(int, input().split()))
    for i in range(inp[1], inp[3]):
        graph[i][inp[0]:inp[2]] = [1] * (inp[2] - inp[0])
        visited[i][inp[0]:inp[2]] = [True] * (inp[2] - inp[0])

def possibleMove(x, y):
    possible = []
    if x > 0 and graph[y][x - 1] == 0:
        possible.append([x - 1, y])
    if x < n - 1 and graph[y][x + 1] == 0:
        possible.append([x + 1, y])
    if y > 0 and graph[y - 1][x] == 0:
        possible.append([x, y - 1])
    if y < m - 1 and graph[y + 1][x] == 0:
        possible.append([x, y + 1])
    return possible

def bfs(start, visited):
    queue = deque()
    queue.append(start)
    visited[start[1]][start[0]] = True
    num = 0
    while queue:
        node = queue.popleft()
        num += 1
        for ele in possibleMove(node[0], node[1]):
            if not visited[ele[1]][ele[0]]:
                visited[ele[1]][ele[0]] = True
                queue.append(ele)
    return num

result = []
num = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] == False:
            # input x, y
            num += 1
            result.append(bfs([j, i], visited))
print(num)
print(*list(sorted(result)))