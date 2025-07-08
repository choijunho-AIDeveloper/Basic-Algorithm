# 2644
from collections import defaultdict, deque

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(node, graph, visited, n, end):
    queue = deque()
    visited[node] = True
    queue.append(node)
    # 최단 경로를 구할 경우 distance를 사용
    distance = [-1] * (n + 1)
    distance[node] = 0
    while queue:
        node = queue.popleft()
        for ele in graph[node]:
            if not visited[ele]:
                visited[ele] = True
                distance[ele] = distance[node] + 1
                queue.append(ele)
    return distance[end]

visited = [False] * (n + 1)
print(bfs(start, graph, visited, n, end))