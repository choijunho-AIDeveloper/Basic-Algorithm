# 1389
from collections import defaultdict, deque

n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    kavin = [0] * (n + 1)
    while queue:
        node = queue.popleft()
        for ele in graph[node]:
            if not visited[ele]:
                visited[ele] = True
                kavin[ele] = kavin[node] + 1
                queue.append(ele)
    return sum(kavin)

result = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    result.append(bfs(i, visited))
print(result.index(min(result)) + 1)