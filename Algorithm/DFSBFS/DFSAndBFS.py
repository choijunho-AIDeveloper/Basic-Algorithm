from collections import defaultdict, deque

n, m, v = map(int, input().split())

# Undirected Graph
graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# DFS(Stack)
def dfs_stack(node, visited, result):
    stack = [node]
    while stack:
        node = stack.pop()
        if not visited[node]:
            result.append(str(node))
            visited[node] = True
            # If vertex are two or more, select lowest value first
            for ele in sorted(graph[node], reverse = True):
                if not visited[ele]:
                    stack.append(ele)
    return result
# DFS(Recursive)
def dfs_rec(node, visited, result):
    result.append(str(node))
    visited[node] = True
    for ele in sorted(graph[node]):
        if not visited[ele]:
            dfs_rec(ele, visited, result)
# BFS
def bfs(node, visited, result):
    queue = deque()
    visited[node] = True
    queue.append(node)
    while queue:
        node = queue.popleft()
        result.append(str(node))
        for ele in sorted(graph[node]):
            if not visited[ele]:
                queue.append(ele)
                visited[ele] = True
    return result

rec_result = []
dfs_rec(v, [False] * (n + 1), rec_result)

print(" ".join(dfs_stack(v, [False] * (n + 1), [])))
# print(" ".join(rec_result))
print(" ".join(bfs(v, [False] * (n + 1), [])))