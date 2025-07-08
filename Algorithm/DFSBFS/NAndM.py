# 15649
n, m = map(int, input().split())

def dfs(level, visited):
    if level == m:
        print(*frame)
        return
    
    for i in range(1, n + 1):
        if not visited[i]:
            frame[level] = i
            visited[i] = True
            dfs(level + 1, visited)
            visited[i] = False

frame = [0] * m
visited = [False] * (n + 1)
dfs(0, visited)
