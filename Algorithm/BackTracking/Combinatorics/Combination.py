inp = ["a", "b", "c"]
results = []

def dfs(result, visited):
    global results
    if len(result) == len(inp):
        return
    for i in range(len(inp)):
        if not visited[i]:
            result.append(inp[i])
            visited[i] = True
            results.append(result[:])
            dfs(result, visited)
            result.pop()
            visited[i] = False

visited = [False] * len(inp)
dfs([], visited)
print(results)