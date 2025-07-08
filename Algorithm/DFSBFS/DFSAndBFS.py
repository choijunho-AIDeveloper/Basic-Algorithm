# 1260
from collections import defaultdict, deque

n, m, v = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node, graph, visited, result):
    result.append(str(node))
    visited[node] = True
    for ele in list(sorted(graph[node])):
        if not visited[ele]:
            dfs(ele, graph, visited, result)

def bfs(node, graph, visited, result):
    queue = deque()
    visited[node] = True
    queue.append(node)
    while queue:
        node = queue.popleft()
        result.append(str(node))
        for ele in list(sorted(graph[node])):
            if not visited[ele]:
                queue.append(ele)
                visited[ele] = True


dfsResult = []
dfsVisited = [False] * (n + 1)
bfsResult = []
bfsVisited = [False] * (n + 1)
dfs(v, graph, dfsVisited, dfsResult)
bfs(v, graph, bfsVisited, bfsResult)
print(" ".join(dfsResult))
print(" ".join(bfsResult))