# 10451
from collections import defaultdict

T = int(input())

def dfs(node, graph, visited):
    if visited[node]:
        return False
    visited[node] = True
    for ele in graph[node]:
        if not visited[ele]:
            dfs(ele, graph, visited)
    return True

for _ in range(T):
    n = int(input())
    sequence = list(map(int, input().split()))

    graph = defaultdict(list)
    for i in range(n):
        graph[i + 1].append(sequence[i])

    visited = [False] * (n + 1)
    num = 0
    for i in range(1, n + 1):
        if dfs(i, graph, visited):
            num += 1
    print(num)