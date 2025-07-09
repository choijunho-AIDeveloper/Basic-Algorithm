# Input
'''
What to print all or seperate element, which divided by permutation with repetition
'''
inp = ["a", "b", "c"]
results = []

def dfs(result):
    global results
    for ele in inp:
        result.append(ele)
        results.append(result[:])
        dfs(result)
        result.pop()

dfs([])
print(results)e