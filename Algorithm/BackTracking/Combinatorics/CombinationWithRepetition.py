# Input
'''
What to print all or seperate element, which divided by combination with repetition
'''
inp = ["a", "b", "c"]
results = []

def dfs(result):
    global results
    if len(result) == len(inp):
        return
    for i in range(len(inp)):
        result.append(inp[i])
        results.append(result[:])
        dfs(result)
        result.pop()

dfs([])
print(results)