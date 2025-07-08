# 2606
from collections import defaultdict
# 재귀를 쓸거면 sys.setrecusionlimit()를 해제

comps, nets = int(input()), int(input())

graph = defaultdict(list)

# 그래프가 양방향인지 단방향인지
for _ in range(nets):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node, graph, visited):
    visited[node] = 1
    for ele in graph[node]:
        if not visited[ele]:
            dfs(ele, graph, visited)

visited = [0] * (comps + 1)
dfs(1, graph, visited)
print(sum(visited) - 1)