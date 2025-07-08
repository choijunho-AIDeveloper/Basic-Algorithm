# 2178
from collections import defaultdict, deque

n, m = map(int, input().split())
map = []

for _ in range(n):
    inp = input()
    list = [i for i in inp]
    map.append(list)

def check(y, x):
    possible = []
    if x > 0 and map[y][x - 1] == "1":
        possible.append([y, x - 1])
    if x < m - 1 and map[y][x + 1] == "1":
        possible.append([y, x + 1])
    if y > 0 and map[y - 1][x] == "1":
        possible.append([y - 1, x])
    if y < n - 1 and map[y + 1][x] == "1":
        possible.append([y + 1, x])
    return possible

graph = defaultdict()


for i in range(n):
    for j in range(m):
        possible = check(i, j)
        graph[i, j] = possible[:]

def bfs(node, graph, visited, end):
    queue = deque()
    queue.append(node)
    visited[node[0]][node[1]] = True
    distance = [[-1] * m for _ in range(n)]
    distance[node[0]][node[1]] = 1
    while queue:
        node = queue.popleft()
        for ele in graph[node[0], node[1]]:
            if not visited[ele[0]][ele[1]]:
                visited[ele[0]][ele[1]] = True
                distance[ele[0]][ele[1]] = distance[node[0]][node[1]] + 1
                queue.append(ele)
    return distance[end[0]][end[1]]

visited = [[False] * m for _ in range(n)]
print(bfs([0, 0], graph, visited, [n - 1, m - 1]))