inp = ["a", "b", "c"]
results = []

def dfs(idx, result):
    global results
    if len(result) == len(inp):
        return
    for i in range(idx, len(inp)):
        result.append(inp[i])
        results.append(result[:])
        dfs(i, result)
        result.pop()

dfs(0, [])
print(results)
