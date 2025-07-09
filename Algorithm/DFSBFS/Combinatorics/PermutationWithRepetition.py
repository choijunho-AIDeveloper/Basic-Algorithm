# Input
'''
What to print all or seperate element, which divided by permutation with repetition
'''
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
# Expected Output : 3 + 9 + 27 = 39
# print(len(results))